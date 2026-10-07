![Blue Team Security Labs: threat hunts, forensic walkthroughs, and offline analysis tools](assets/repository-banner.svg)

[![Checks](https://github.com/blueteamsecuritylab/blue-team-security-labs/actions/workflows/checks.yml/badge.svg)](https://github.com/blueteamsecuritylab/blue-team-security-labs/actions/workflows/checks.yml)

[Website](https://blueteamsecurity.org/) · [Hunt queries](hunts/README.md) · [DFIR walkthroughs](docs/zimmerman/README.md) · [Local tools](tools/README.md)

SentinelOne and Microsoft Defender hunts, Windows artifact walkthroughs, and Python utilities for local analysis. This is the code and lab companion to [Blue Team Security](https://blueteamsecurity.org/).

## Start here

| Task | Open | What you'll find |
| --- | --- | --- |
| Investigate endpoint activity | [Hunt queries](hunts/README.md) | Four queries with prerequisites, expected matches, false positives, and investigation pivots |
| Examine Windows artifacts | [Zimmerman walkthroughs](docs/zimmerman/README.md) | 31 tool guides, grouped by artifact, with commands or GUI steps and interpretation notes |
| Inspect a file or CSV export | [Local analysis tools](tools/README.md) | File hashes and byte observations; CSV timestamp counts and UTC bounds |
| Record an investigation | [Templates](templates/README.md) | Hunt and parser records for scope, commands, inputs, and findings |

## Try the CSV tool

Python 3.10 or newer. Both utilities use the standard library; no package installation is needed.

```bash
git clone https://github.com/blueteamsecuritylab/blue-team-security-labs.git
cd blue-team-security-labs
python tools/ez_csv_summary.py examples/ez-csv-summary/synthetic-events.csv --timestamp-column EventTime --naive-tz utc --source "Repository synthetic fixture"
```

The example prints JSON for five synthetic records: three valid timestamps, one invalid value, and one missing value. Its time bounds are 08:00–08:45 UTC. The UTC rule is defined for this fixture; choose the correct rule for your own export.

[Example and expected output](examples/ez-csv-summary/README.md) · [CSV tool reference](docs/tools/ez-csv-summary.md) · [Static file triage](malware-analysis/README.md)

## Hunts

| Hunt | Platform | Investigation |
| --- | --- | --- |
| [Browser to script](hunts/browser-to-script.md) | SentinelOne | Review browser parents associated with script interpreters |
| [Encoded PowerShell](hunts/encoded-powershell.md) | SentinelOne | Inspect encoded-command fragments and their process context |
| [Device process timeline](hunts/device-process-timeline.md) | Defender XDR | Reconstruct process activity for a device and time window |
| [File hash scope](hunts/file-hash-scope.md) | Defender XDR | Find file events containing a selected SHA-256 |

Copyable files are in [queries](queries/README.md). Each hunt links to its published article and explains the next evidence to collect.

## Review and checks

| Content | Coverage |
| --- | --- |
| Hunt queries | Article and field-reference review; tenant execution remains unverified |
| Zimmerman walkthroughs | Official documentation reviewed October 7, 2026; parser and GUI steps have not been run for these guides |
| Python utilities | 32 unit tests using benign fixtures; current results appear in [Checks](https://github.com/blueteamsecuritylab/blue-team-security-labs/actions/workflows/checks.yml) |

Run the same checks locally:

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
```

[Query provenance](PROVENANCE.json) records the four excerpts' article sections and SHA-256 hashes. The [Zimmerman catalog](docs/zimmerman/catalog.json) records upstream manuals, versions, and source commits.

## Contribute

For a correction, include the affected file, tool or platform version, and the evidence supporting the change. See [contribution notes](CONTRIBUTING.md). Use synthetic fixtures for examples and keep workplace data, credentials, and malware binaries out of public issues and pull requests.

[Blue Team Security](https://blueteamsecurity.org/) · [Stephen Tafe](https://www.linkedin.com/in/stephentafe/)
