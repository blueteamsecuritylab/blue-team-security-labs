# Local analysis tools

Python 3.10 or newer; standard library only.

| Tool | Input | Output | Reference |
| --- | --- | --- | --- |
| [EZ CSV Summary](ez_csv_summary.py) | UTF-8 CSV export and an explicit timestamp column | JSON counts, UTC bounds, warnings, and input SHA-256 | [Usage and limits](../docs/tools/ez-csv-summary.md) |
| [Static File Triage](static_triage.py) | One regular file | JSON byte observations and file hashes | [Workflow](../malware-analysis/README.md) |

Start with the [synthetic CSV example](../examples/ez-csv-summary/README.md). Both tools inspect local data without network access or sample execution. Neither acquires artifacts or determines whether a file is malicious.

```bash
python tools/ez_csv_summary.py --help
python tools/static_triage.py --help
python -m unittest discover -s tests -v
```

Run these commands from the repository root.

[Repository home](../README.md) · [Documentation](../docs/README.md)
