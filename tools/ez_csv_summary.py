"""Summarize an explicitly selected CSV timestamp column without running parsers.

The input is a bounded, stable byte snapshot. JSON output contains counts and
observed time bounds, not raw rows or claims about activity or evidence completeness.
"""
import argparse
import csv
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile


DEFAULT_MAX_BYTES = 64 * 1024 * 1024
MAX_WARNINGS = 10
ISO_TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})?$"
)


class NaiveTimezoneRequired(ValueError):
    pass


def parse_naive_timezone(value):
    """Accept UTC or a fixed numeric offset; never infer local time or DST."""
    if value is None:
        return None
    if value.lower() == "utc":
        return timezone.utc
    match = re.fullmatch(r"([+-])(\d{2}):(\d{2})", value)
    if not match:
        raise ValueError("Naive timezone must be utc or a fixed offset such as +02:00")
    sign, hours, minutes = match.groups()
    hours, minutes = int(hours), int(minutes)
    if hours > 23 or minutes > 59:
        raise ValueError("Fixed timezone offset must be less than 24 hours")
    delta = timedelta(hours=hours, minutes=minutes)
    return timezone(delta if sign == "+" else -delta)


def parse_timestamp(value, naive_timezone):
    if not ISO_TIMESTAMP.fullmatch(value):
        raise ValueError("Timestamp is outside the supported ISO 8601 format")
    offset = re.search(r"([+-])(\d{2}):(\d{2})$", value)
    if offset and (int(offset.group(2)) > 23 or int(offset.group(3)) > 59):
        raise ValueError("Timestamp timezone offset must use hours below 24 and minutes below 60")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        if naive_timezone is None:
            raise NaiveTimezoneRequired(
                "A timezone-free timestamp requires --naive-tz utc or a fixed offset"
            )
        parsed = parsed.replace(tzinfo=naive_timezone)
    return parsed.astimezone(timezone.utc)


def _fingerprint(info):
    # Windows path-stat and handle-stat ctime have different semantics. Compare
    # ctime only between handle-stat calls; identity, size and mtime cross APIs.
    return (
        info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns,
    )


def read_snapshot(path, max_bytes):
    if max_bytes <= 0:
        raise ValueError("Size limit must be positive")
    path = Path(path)
    before = path.lstat()
    if stat.S_ISLNK(before.st_mode):
        raise ValueError("Symlinks are not accepted; select the regular file explicitly")
    if not stat.S_ISREG(before.st_mode):
        raise ValueError("Input must be a regular file")
    if before.st_size > max_bytes:
        raise ValueError("Input exceeds the configured size limit")
    with path.open("rb") as handle:
        opened = os.fstat(handle.fileno())
        if _fingerprint(opened) != _fingerprint(before):
            raise ValueError("Input changed before reading; summary discarded")
        data = handle.read(max_bytes + 1)
        after = os.fstat(handle.fileno())
    final = path.lstat()
    if (
        _fingerprint(after) != _fingerprint(opened)
        or after.st_ctime_ns != opened.st_ctime_ns
        or _fingerprint(final) != _fingerprint(opened)
        or stat.S_ISLNK(final.st_mode)
        or len(data) != opened.st_size
    ):
        raise ValueError("Input changed while reading; summary discarded")
    if len(data) > max_bytes:
        raise ValueError("Input exceeds the configured size limit")
    return data


@contextmanager
def _csv_field_limit(max_bytes):
    """Allow fields within the byte snapshot bound and restore the CSV default."""
    previous = csv.field_size_limit()
    csv.field_size_limit(min(max_bytes, sys.maxsize))
    try:
        yield
    finally:
        csv.field_size_limit(previous)


def summarize_csv(
    path, timestamp_column, *, naive_tz=None, delimiter=",",
    max_bytes=DEFAULT_MAX_BYTES, parser_name=None, parser_version=None,
    source=None, include_filename=False,
):
    if not timestamp_column:
        raise ValueError("Timestamp column is required")
    if len(delimiter) != 1 or delimiter in "\r\n\x00":
        raise ValueError("Delimiter must be one character other than a line break or NUL")
    naive_timezone = parse_naive_timezone(naive_tz)
    data = read_snapshot(path, max_bytes)
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Input must be UTF-8, with an optional UTF-8 BOM") from exc
    with _csv_field_limit(max_bytes):
        reader = csv.reader(io.StringIO(text, newline=""), delimiter=delimiter, strict=True)
        try:
            headers = next(reader)
        except StopIteration as exc:
            raise ValueError("Input is empty; a CSV header is required") from exc
        except csv.Error as exc:
            raise ValueError("Malformed CSV header") from exc
        if not headers or any(not header.strip() for header in headers):
            raise ValueError("CSV headers must be nonempty")
        if len(set(headers)) != len(headers):
            raise ValueError("Duplicate CSV headers are not accepted")
        if timestamp_column not in headers:
            raise ValueError("Selected timestamp column is not in the CSV header")
        column_index = headers.index(timestamp_column)
        counts = {
            "data_records": 0, "parsed_timestamps": 0, "blank_records": 0,
            "row_width_errors": 0, "missing_timestamps": 0, "invalid_timestamps": 0,
        }
        warnings = []
        warning_count = 0
        first = last = None
        previous_line = reader.line_num

        def warn(kind, start_line, end_line):
            nonlocal warning_count
            warning_count += 1
            if len(warnings) < MAX_WARNINGS:
                warnings.append({
                    "kind": kind, "start_line": start_line, "end_line": end_line,
                })

        try:
            for row in reader:
                start_line = previous_line + 1
                end_line = reader.line_num
                previous_line = end_line
                counts["data_records"] += 1
                if not row or all(not cell.strip() for cell in row):
                    counts["blank_records"] += 1
                    warn("blank_record", start_line, end_line)
                    continue
                if len(row) != len(headers):
                    counts["row_width_errors"] += 1
                    warn("row_width_error", start_line, end_line)
                    continue
                value = row[column_index].strip()
                if not value:
                    counts["missing_timestamps"] += 1
                    warn("missing_timestamp", start_line, end_line)
                    continue
                try:
                    parsed = parse_timestamp(value, naive_timezone)
                except NaiveTimezoneRequired:
                    raise
                except (ValueError, OverflowError):
                    counts["invalid_timestamps"] += 1
                    warn("invalid_timestamp", start_line, end_line)
                    continue
                counts["parsed_timestamps"] += 1
                first = parsed if first is None or parsed < first else first
                last = parsed if last is None or parsed > last else last
        except csv.Error as exc:
            raise ValueError("Malformed CSV record; summary discarded") from exc

    def utc_text(value):
        return value.isoformat().replace("+00:00", "Z") if value else None

    report = {
        "summary_format_version": 1,
        "input": {"size_bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()},
        "timestamp_policy": {
            "column": timestamp_column, "delimiter": delimiter,
            "naive_timezone": naive_tz, "output_timezone": "UTC",
            "format": "ISO 8601 date-time with seconds and up to 6 fractional digits",
        },
        "counts": counts,
        "observed_time_bounds_utc": {"minimum": utc_text(first), "maximum": utc_text(last)},
        "warnings": warnings,
        "warnings_omitted": warning_count - len(warnings),
        "scope": (
            "Counts and bounds describe parsed values in this selected CSV snapshot. "
            "They do not establish execution, causation, coverage or evidence completeness."
        ),
    }
    if include_filename:
        report["input"]["filename"] = Path(path).name
    labels = {
        key: value for key, value in {
            "parser_name": parser_name, "parser_version": parser_version,
            "source": source,
        }.items() if value is not None
    }
    if labels:
        report["reported_provenance"] = {"verification": "unverified_user_labels", **labels}
    return report


def write_report(path, report, input_path, *, overwrite=False):
    """Publish a completed JSON file atomically without replacing input bytes."""
    target, source = Path(path), Path(input_path)
    if target.resolve() == source.resolve():
        raise ValueError("Output must not be the input file")
    if target.exists() or target.is_symlink():
        if target.is_symlink():
            raise ValueError("Output symlinks are not accepted")
        if not target.is_file():
            raise ValueError("Output must be a regular file")
        if os.path.samefile(target, source):
            raise ValueError("Output must not alias the input file")
        if not overwrite:
            raise FileExistsError("Output already exists; use --overwrite explicitly")
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n",
            dir=target.parent, prefix=".ez-summary-", suffix=".tmp", delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            json.dump(report, handle, indent=2, ensure_ascii=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        if overwrite:
            os.replace(temporary_path, target)
            temporary_path = None
        else:
            # An atomic hard-link publication refuses a concurrently created target.
            os.link(temporary_path, target)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="Selected UTF-8 CSV; no collection or parser execution")
    parser.add_argument("--timestamp-column", required=True, help="Exact, unique header to summarize")
    parser.add_argument("--naive-tz", help="Required for timezone-free values: utc or fixed offset, e.g. --naive-tz=-05:00")
    parser.add_argument("--delimiter", default=",", help="One-character CSV delimiter (default: comma)")
    parser.add_argument("--max-mib", type=int, default=64, help="Positive byte snapshot limit in MiB (default: 64)")
    parser.add_argument("--parser-name", help="Unverified label supplied by you; does not run the parser")
    parser.add_argument("--parser-version", help="Unverified parser-version label supplied by you")
    parser.add_argument("--source", help="Unverified source label; omit sensitive names")
    parser.add_argument("--include-filename", action="store_true", help="Include the input basename; omitted by default")
    parser.add_argument("--output", type=Path, help="Write JSON atomically; otherwise print JSON")
    parser.add_argument("--overwrite", action="store_true", help="Explicitly replace an existing output report")
    args = parser.parse_args(argv)
    if args.overwrite and args.output is None:
        parser.error("--overwrite requires --output")
    try:
        report = summarize_csv(
            args.csv_file, args.timestamp_column, naive_tz=args.naive_tz,
            delimiter=args.delimiter, max_bytes=args.max_mib * 1024 * 1024,
            parser_name=args.parser_name, parser_version=args.parser_version,
            source=args.source, include_filename=args.include_filename,
        )
        if args.output:
            write_report(args.output, report, args.csv_file, overwrite=args.overwrite)
        else:
            print(json.dumps(report, indent=2, ensure_ascii=True))
    except (OSError, ValueError) as exc:
        # OSError text may contain full private paths; emit only its class.
        detail = type(exc).__name__ if isinstance(exc, OSError) else str(exc)
        print(f"CSV summary failed: {detail}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
