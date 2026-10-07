"""Benign synthetic CSV fixtures only; no parser binaries or real exports."""
import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "ez_csv_summary.py"
SPEC = importlib.util.spec_from_file_location("ez_csv_summary", SCRIPT)
SUMMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUMMARY)


class EZCSVSummaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def fixture(self, content, name="synthetic.csv"):
        path = self.root / name
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)
        return path

    def test_offsets_normalize_and_hash_exact_input(self):
        data = (
            "Time,Event\r\n"
            "2026-10-07T10:00:00+02:00,synthetic A\r\n"
            "2026-10-07T04:30:00-05:00,synthetic B\r\n"
            "2026-10-07T09:00:00Z,synthetic C\r\n"
        ).encode()
        path = self.fixture(data)
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["counts"]["parsed_timestamps"], 3)
        self.assertEqual(result["observed_time_bounds_utc"], {
            "minimum": "2026-10-07T08:00:00Z", "maximum": "2026-10-07T09:30:00Z",
        })
        self.assertEqual(result["input"]["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(result["input"]["size_bytes"], len(data))
        self.assertEqual(path.read_bytes(), data)

    def test_naive_values_require_explicit_policy(self):
        path = self.fixture("Time\n2026-10-07 08:00:00\n")
        with self.assertRaisesRegex(SUMMARY.NaiveTimezoneRequired, "--naive-tz"):
            SUMMARY.summarize_csv(path, "Time")
        utc = SUMMARY.summarize_csv(path, "Time", naive_tz="utc")
        offset = SUMMARY.summarize_csv(path, "Time", naive_tz="-05:00")
        self.assertEqual(utc["observed_time_bounds_utc"]["minimum"], "2026-10-07T08:00:00Z")
        self.assertEqual(offset["observed_time_bounds_utc"]["minimum"], "2026-10-07T13:00:00Z")

    def test_aware_values_keep_their_own_offset(self):
        path = self.fixture("Time\n2026-10-07T08:00:00.123456+02:00\n")
        result = SUMMARY.summarize_csv(path, "Time", naive_tz="-05:00")
        self.assertEqual(result["observed_time_bounds_utc"]["minimum"], "2026-10-07T06:00:00.123456Z")

    def test_invalid_missing_width_and_blank_records(self):
        path = self.fixture(
            "Time,Event\n"
            "2026-10-07T08:00:00Z,ok\n"
            "invalid,do not disclose this row\n"
            ",missing\n"
            "2026-10-07T09:00:00Z,extra,column\n"
            "\n"
        )
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["counts"], {
            "data_records": 5, "parsed_timestamps": 1, "blank_records": 1,
            "row_width_errors": 1, "missing_timestamps": 1, "invalid_timestamps": 1,
        })
        self.assertEqual([warning["start_line"] for warning in result["warnings"]], [3, 4, 5, 6])
        self.assertNotIn("do not disclose", json.dumps(result))

    def test_large_unused_field_within_snapshot_limit_and_restore_csv_limit(self):
        previous_limit = csv.field_size_limit()
        path = self.fixture("Time,Payload\n2026-10-07T08:00:00Z," + "x" * 140000 + "\n")
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["counts"]["parsed_timestamps"], 1)
        self.assertNotIn("x" * 100, json.dumps(result))
        self.assertEqual(csv.field_size_limit(), previous_limit)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            SUMMARY.summarize_csv(self.fixture("Time,Time\n"), "Time")
        self.assertEqual(csv.field_size_limit(), previous_limit)

    def test_multiline_record_warning_reports_physical_lines(self):
        path = self.fixture('Time,Event\ninvalid,"synthetic\nmultiline"\n')
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["warnings"][0], {
            "kind": "invalid_timestamp", "start_line": 2, "end_line": 3,
        })

    def test_warning_samples_are_bounded(self):
        path = self.fixture("Time\n" + "invalid\n" * 15)
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["counts"]["invalid_timestamps"], 15)
        self.assertEqual(len(result["warnings"]), 10)
        self.assertEqual(result["warnings_omitted"], 5)
        self.assertEqual(result["observed_time_bounds_utc"], {"minimum": None, "maximum": None})

    def test_utf8_bom_and_explicit_semicolon(self):
        data = b"\xef\xbb\xbfTime;Event\n2026-10-07T08:00:00Z;synthetic\n"
        result = SUMMARY.summarize_csv(self.fixture(data), "Time", delimiter=";")
        self.assertEqual(result["counts"]["parsed_timestamps"], 1)
        self.assertEqual(result["input"]["sha256"], hashlib.sha256(data).hexdigest())

    def test_empty_duplicate_blank_and_unknown_headers(self):
        for text, error in (
            ("", "empty"),
            ("Time,Time\n", "Duplicate"),
            ("Time,\n", "nonempty"),
            ("Other\n", "Selected timestamp column"),
        ):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, error):
                    SUMMARY.summarize_csv(self.fixture(text), "Time")
        result = SUMMARY.summarize_csv(self.fixture("Time\n"), "Time")
        self.assertEqual(result["counts"]["data_records"], 0)

    def test_malformed_csv_and_non_utf8_are_fatal(self):
        with self.assertRaisesRegex(ValueError, "Malformed CSV"):
            SUMMARY.summarize_csv(self.fixture('Time,Event\n2026-10-07T08:00:00Z,"unclosed\n'), "Time")
        with self.assertRaisesRegex(ValueError, "UTF-8"):
            SUMMARY.summarize_csv(self.fixture(b"Time\n\xff\n"), "Time")

    def test_timestamp_formats_do_not_infer_dates_or_drop_precision(self):
        path = self.fixture(
            "Time\n2026-10-07\n10/07/2026 08:00:00\n"
            "2026-10-07T08:00:00.1234567Z\n2026-02-30T08:00:00Z\n"
        )
        result = SUMMARY.summarize_csv(path, "Time")
        self.assertEqual(result["counts"]["invalid_timestamps"], 4)

    def test_aware_offset_ranges_reject_normalized_invalid_minutes(self):
        invalid_offsets = ("+00:60", "+00:99", "-01:60", "+24:00", "-23:60")
        rows = ["Time"]
        rows.extend("2026-10-07T08:00:00" + offset for offset in invalid_offsets)
        rows.extend(("2026-10-07T08:00:00+23:59", "2026-10-07T08:00:00+00:59"))
        result = SUMMARY.summarize_csv(self.fixture("\n".join(rows) + "\n"), "Time")
        self.assertEqual(result["counts"]["invalid_timestamps"], len(invalid_offsets))
        self.assertEqual(result["counts"]["parsed_timestamps"], 2)
        self.assertEqual(result["observed_time_bounds_utc"], {
            "minimum": "2026-10-06T08:01:00Z", "maximum": "2026-10-07T07:01:00Z",
        })

    def test_invalid_timezone_delimiter_and_size_limits(self):
        path = self.fixture("Time\n")
        for zone in ("local", "America/New_York", "+24:00", "-05:60"):
            with self.subTest(zone=zone):
                with self.assertRaises(ValueError):
                    SUMMARY.summarize_csv(path, "Time", naive_tz=zone)
        with self.assertRaisesRegex(ValueError, "Delimiter"):
            SUMMARY.summarize_csv(path, "Time", delimiter=",,")
        with self.assertRaisesRegex(ValueError, "positive"):
            SUMMARY.summarize_csv(path, "Time", max_bytes=0)
        with self.assertRaisesRegex(ValueError, "size limit"):
            SUMMARY.summarize_csv(path, "Time", max_bytes=1)

    def test_directory_and_missing_input(self):
        with self.assertRaisesRegex(ValueError, "regular file"):
            SUMMARY.summarize_csv(self.root, "Time")
        with self.assertRaises(FileNotFoundError):
            SUMMARY.summarize_csv(self.root / "absent.csv", "Time")

    def test_input_symlink_rejected_if_supported(self):
        original = self.fixture("Time\n")
        link = self.root / "link.csv"
        try:
            link.symlink_to(original)
        except (OSError, NotImplementedError):
            self.skipTest("Symlink creation is unavailable to this account")
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            SUMMARY.summarize_csv(link, "Time")

    def test_change_during_read_discards_snapshot(self):
        path = self.fixture("Time\n2026-10-07T08:00:00Z\n")
        real_open = Path.open

        class ChangingReader:
            def __enter__(self):
                self.handle = real_open(path, "rb")
                return self

            def __exit__(self, *args):
                self.handle.close()

            def fileno(self):
                return self.handle.fileno()

            def read(self, size):
                data = self.handle.read(size)
                with real_open(path, "ab") as writer:
                    writer.write(b"changed\n")
                return data

        with patch.object(Path, "open", return_value=ChangingReader()):
            with self.assertRaisesRegex(ValueError, "changed"):
                SUMMARY.summarize_csv(path, "Time")

    def test_privacy_defaults_and_unverified_labels(self):
        path = self.fixture("Time,Event\n2026-10-07T08:00:00Z,=HYPERLINK(private-value)\n")
        result = SUMMARY.summarize_csv(
            path, "Time", parser_name="ExampleParser", parser_version="reported version", source="Synthetic fixture",
        )
        output = json.dumps(result)
        self.assertNotIn(str(self.root), output)
        self.assertNotIn(path.name, output)
        self.assertNotIn("HYPERLINK", output)
        self.assertEqual(result["reported_provenance"]["verification"], "unverified_user_labels")
        included = SUMMARY.summarize_csv(path, "Time", include_filename=True)
        self.assertEqual(included["input"]["filename"], path.name)

    def test_formula_string_in_timestamp_is_data(self):
        result = SUMMARY.summarize_csv(self.fixture("Time\n=1+1\n@SUM(A1:A2)\n"), "Time")
        self.assertEqual(result["counts"]["invalid_timestamps"], 2)
        self.assertEqual(result["counts"]["parsed_timestamps"], 0)

    def test_output_refuses_input_and_hardlink_alias(self):
        path = self.fixture("Time\n")
        with self.assertRaisesRegex(ValueError, "input file"):
            SUMMARY.write_report(path, {}, path, overwrite=True)
        alias = self.root / "alias.json"
        try:
            os.link(path, alias)
        except OSError:
            self.skipTest("Hard links are unavailable")
        with self.assertRaisesRegex(ValueError, "alias"):
            SUMMARY.write_report(alias, {}, path, overwrite=True)
        self.assertEqual(path.read_text(), "Time\n")

    def test_output_no_overwrite_and_explicit_replacement(self):
        path = self.fixture("Time\n")
        target = self.root / "summary.json"
        SUMMARY.write_report(target, {"synthetic": 1}, path)
        self.assertEqual(json.loads(target.read_text()), {"synthetic": 1})
        with self.assertRaises(FileExistsError):
            SUMMARY.write_report(target, {"synthetic": 2}, path)
        self.assertEqual(json.loads(target.read_text()), {"synthetic": 1})
        SUMMARY.write_report(target, {"synthetic": 2}, path, overwrite=True)
        self.assertEqual(json.loads(target.read_text()), {"synthetic": 2})
        self.assertEqual(list(self.root.glob(".ez-summary-*.tmp")), [])

    def test_concurrent_target_creation_does_not_clobber(self):
        path = self.fixture("Time\n")
        target = self.root / "summary.json"
        real_link = os.link

        def competing_link(source, destination):
            target.write_text("concurrent data")
            return real_link(source, destination)

        with patch.object(SUMMARY.os, "link", side_effect=competing_link):
            with self.assertRaises(FileExistsError):
                SUMMARY.write_report(target, {"synthetic": 1}, path)
        self.assertEqual(target.read_text(), "concurrent data")
        self.assertEqual(list(self.root.glob(".ez-summary-*.tmp")), [])

    def test_output_symlink_and_directory_rejected(self):
        path = self.fixture("Time\n")
        with self.assertRaisesRegex(ValueError, "regular file"):
            SUMMARY.write_report(self.root, {}, path, overwrite=True)
        target = self.root / "output.json"
        try:
            target.symlink_to(path)
        except (OSError, NotImplementedError):
            self.skipTest("Symlink creation is unavailable to this account")
        with self.assertRaisesRegex(ValueError, "input file|symlinks"):
            SUMMARY.write_report(target, {}, path, overwrite=True)

    def test_cli_json_help_and_failure_exit_codes(self):
        path = self.fixture("Time\n2026-10-07T08:00:00Z\n", "synthetic export (1).csv")
        success = subprocess.run(
            [sys.executable, str(SCRIPT), str(path), "--timestamp-column", "Time"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout)["counts"]["parsed_timestamps"], 1)
        help_result = subprocess.run(
            [sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True, check=False,
        )
        self.assertEqual(help_result.returncode, 0)
        self.assertIn("--naive-tz", help_result.stdout)
        for args, code in (
            ([str(self.root / "missing.csv"), "--timestamp-column", "Time"], 1),
            ([str(path)], 2),
            ([str(path), "--timestamp-column", "Time", "--overwrite"], 2),
        ):
            failure = subprocess.run(
                [sys.executable, str(SCRIPT), *args], capture_output=True, text=True, check=False,
            )
            self.assertEqual(failure.returncode, code, failure.stderr)
            self.assertEqual(failure.stdout, "")
            if code == 1:
                self.assertNotIn(str(self.root), failure.stderr)


if __name__ == "__main__":
    unittest.main()
