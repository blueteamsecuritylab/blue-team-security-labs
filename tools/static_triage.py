"""Read a regular file and report basic byte observations without executing it."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import sys


DEFAULT_MAX_BYTES = 256 * 1024 * 1024


def inspect_file(path, max_bytes=DEFAULT_MAX_BYTES):
    """Return hashes and metadata; reject unsupported inputs or detected changes."""
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

    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    total = 0
    header = b""
    with path.open("rb") as handle:
        opened = os.fstat(handle.fileno())
        if (opened.st_ino, opened.st_dev, opened.st_size, opened.st_mtime_ns) != (
            before.st_ino, before.st_dev, before.st_size, before.st_mtime_ns
        ):
            raise ValueError("Input changed before it could be read")
        while chunk := handle.read(1024 * 1024):
            total += len(chunk)
            if total > max_bytes:
                raise ValueError("Input exceeds the configured size limit")
            if not header:
                header = chunk[:16]
            sha256.update(chunk)
            sha1.update(chunk)
        after = os.fstat(handle.fileno())

    if (after.st_size, after.st_mtime_ns, after.st_ctime_ns) != (
        opened.st_size, opened.st_mtime_ns, opened.st_ctime_ns
    ) or total != opened.st_size:
        raise ValueError("Input changed while it was read; report discarded")

    return {
        "filename": path.name,
        "size_bytes": total,
        "sha256": sha256.hexdigest(),
        "sha1": sha1.hexdigest(),
        "modified_utc": datetime.fromtimestamp(
            opened.st_mtime, timezone.utc
        ).isoformat().replace("+00:00", "Z"),
        "header_hex": header.hex(),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="Regular file to read")
    parser.add_argument("--max-mib", type=int, default=256, help="Positive size limit (default: 256)")
    args = parser.parse_args(argv)
    try:
        report = inspect_file(args.file, args.max_mib * 1024 * 1024)
    except (OSError, ValueError) as exc:
        print(f"Triage failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
