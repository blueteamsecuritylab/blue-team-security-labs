"""Tests use benign temporary bytes only; no malware fixtures are distributed."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "static_triage.py"
SPEC = importlib.util.spec_from_file_location("static_triage", SCRIPT)
TRIAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TRIAGE)


class StaticTriageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def fixture(self, content, name="benign.bin"):
        path = self.root / name
        path.write_bytes(content)
        return path

    def test_known_hash_vector_and_source_unchanged(self):
        path = self.fixture(b"abc")
        report = TRIAGE.inspect_file(path)
        self.assertEqual(report["size_bytes"], 3)
        self.assertEqual(report["sha256"], "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
        self.assertEqual(report["sha1"], "a9993e364706816aba3e25717850c26c9cd0d89d")
        self.assertEqual(report["header_hex"], "616263")
        self.assertEqual(path.read_bytes(), b"abc")
        self.assertNotIn(str(self.root), json.dumps(report))

    def test_empty_file(self):
        report = TRIAGE.inspect_file(self.fixture(b""))
        self.assertEqual(report["size_bytes"], 0)
        self.assertEqual(report["header_hex"], "")
        self.assertEqual(report["sha256"], hashlib.sha256(b"").hexdigest())

    def test_binary_header_and_chunked_hash(self):
        data = bytes(range(256)) * 5000
        report = TRIAGE.inspect_file(self.fixture(data))
        self.assertEqual(report["header_hex"], bytes(range(16)).hex())
        self.assertEqual(report["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(report["size_bytes"], len(data))

    def test_size_limit(self):
        with self.assertRaisesRegex(ValueError, "size limit"):
            TRIAGE.inspect_file(self.fixture(b"abcd"), max_bytes=3)

    def test_nonpositive_limit(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            TRIAGE.inspect_file(self.fixture(b"abc"), max_bytes=0)

    def test_directory_and_missing_file(self):
        with self.assertRaisesRegex(ValueError, "regular"):
            TRIAGE.inspect_file(self.root)
        with self.assertRaises(FileNotFoundError):
            TRIAGE.inspect_file(self.root / "missing.bin")

    def test_symlink_rejected_if_supported(self):
        source = self.fixture(b"abc")
        link = self.root / "link.bin"
        try:
            link.symlink_to(source)
        except (OSError, NotImplementedError):
            self.skipTest("Symlink creation not available to this account")
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            TRIAGE.inspect_file(link)

    def test_cli_handles_literal_path_and_emits_json(self):
        path = self.fixture(b"abc", "benign fixture (1).bin")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            capture_output=True, text=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["filename"], path.name)
        self.assertEqual(report["size_bytes"], 3)
        self.assertEqual(path.read_bytes(), b"abc")

    def test_cli_failure_does_not_emit_a_report(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root / "missing.bin")],
            capture_output=True, text=True, check=False
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn("Triage failed", result.stderr)


if __name__ == "__main__":
    unittest.main()
