# Contributing

## Corrections

Open an issue with the affected file, the tool or platform version, and the source or observed behavior supporting the correction. For query issues, include the operator, time scope, and a sanitized example of the mismatch.

## Pull requests

Keep a change focused. For a guide, cite the upstream manual or source help and preserve the distinction between documented steps and a recorded run. For a utility change, include a benign fixture that exercises the behavior.

Run the checks from the repository root:

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
```

Query files are article excerpts: if their text changes, update the companion hunt and its [source record](PROVENANCE.json) together.

## Public examples

Use synthetic records. Keep credentials, workplace or customer telemetry, completed case notes, and malware binaries outside public issues and pull requests. Third-party tools retain their publishers' distribution and use terms.

[Repository home](README.md)
