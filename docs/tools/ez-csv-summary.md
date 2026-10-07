# Offline CSV timestamp summary

[ez_csv_summary.py](../../tools/ez_csv_summary.py) is an original Blue Team Security utility for checking a selected CSV export before a detailed timeline review. It reads one UTF-8 CSV, hashes the exact bytes it parses, counts usable and rejected timestamp records, and reports the observed minimum and maximum in UTC.

This is a summary utility, not an artifact parser or acquisition tool. It does not launch Eric Zimmerman tools, execute an artifact, collect endpoint data, contact a network, or infer that a file was executed. CSV values remain data; spreadsheet formulas are never evaluated. Output is JSON only.

## Try the supplied synthetic fixture

From the repository root, run:

```powershell
python tools/ez_csv_summary.py examples/ez-csv-summary/synthetic-events.csv --timestamp-column EventTime --naive-tz utc --source "Repository synthetic fixture"
```

The [fixture](../../examples/ez-csv-summary/synthetic-events.csv) has five deliberately authored records. The actual [JSON output](../../examples/ez-csv-summary/summary.json) from the October 7, 2026 Windows run contains three parsed timestamps, one invalid timestamp, and one missing timestamp. The observed bounds are 08:00 through 08:45 UTC. These are synthetic utility results, not Zimmerman parser output or an incident finding. The fixture's naive time is deliberately defined as UTC; do not transfer that assumption to a real export.

## Start with the exact export

Use Python 3.10 or newer. Select the CSV and inspect its timestamp header and the parser's time handling before choosing a policy. Header matching is exact and case-sensitive; duplicate or blank headers are rejected.

For timestamps that carry `Z` or a numeric offset:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime"
```

If timestamps omit an offset, explicitly state how they should be interpreted. Use `utc` only when you have established that the values are UTC:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz utc --output "C:\Lab\Reports\synthetic-summary.json"
```

A fixed offset is also accepted:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz=-05:00
```

A fixed offset has no daylight-saving rules. Do not use one across a DST change without establishing the appropriate interpretation. Offset-bearing values keep their own offset regardless of `--naive-tz`.

The input directory examples above are fictional. The utility does not create output directories.

## Format and limits

Supported timestamps contain a date and time with seconds:

- `2026-10-07T08:00:00Z`
- `2026-10-07 08:00:00.123456+02:00`
- `2026-10-07 08:00:00`, with an explicit naive-time policy

Numeric offsets require hours from 00 through 23 and minutes from 00 through 59. Invalid offset minutes are rejected rather than normalized. Fractional seconds may contain up to six digits. Values with higher precision, date-only values, locale-specific dates, impossible dates and other formats are counted as invalid. The utility does not truncate precision or guess a date format. Some parser exports use different timestamp formats; check your selected column before using this utility.

UTF-8 with or without a UTF-8 BOM is accepted. Other encodings require an independently documented conversion; preserve the original export separately. Comma is the default delimiter. For an explicitly selected semicolon-delimited file, add `--delimiter ";"`.

The default input limit is 64 MiB. `--max-mib` sets another positive limit. CSV fields are allowed within that snapshot bound, including long unused payload fields; the process's previous CSV field limit is restored after parsing. The utility reads a bounded byte snapshot once, then hashes and parses that same snapshot. It checks file identity, size and modification metadata before and after reading and rejects detected changes. Metadata checks are a practical stability check, not an acquisition guarantee or protection against an adversarial writer that evades them.

Final-component input symlinks, nonregular inputs, malformed CSV syntax, duplicate headers and missing selected columns cause failure. A CSV containing only a valid header is allowed and produces zero records and null time bounds.

## Read the result

The JSON contains:

| Field | Meaning |
| --- | --- |
| `input.sha256` | SHA-256 of the exact bytes used for this summary, including any BOM |
| `input.size_bytes` | Size of those bytes |
| `timestamp_policy` | Selected header, delimiter and explicit naive-time policy |
| `counts.data_records` | All records after the header, including blank and rejected records |
| `counts.parsed_timestamps` | Records with the expected width and a supported timestamp |
| `counts.row_width_errors` | Records with fewer or more fields than the header |
| `counts.missing_timestamps` | Correct-width, nonblank records with an empty selected timestamp |
| `counts.invalid_timestamps` | Correct-width records with a value outside the supported timestamp format |
| `counts.blank_records` | Empty records or records containing only whitespace |
| `observed_time_bounds_utc` | Minimum and maximum parsed values; null if none were parsed |
| `warnings` | First ten rejected-record notices, with physical start/end line numbers |
| `warnings_omitted` | Additional notices omitted from the sample |

Each nonparsed record belongs to one of the four rejection categories. A multiline quoted CSV record counts as one record; warning line numbers cover its physical lines. A malformed quoted record fails the whole summary rather than silently skipping it.

Counts and time bounds describe only the selected CSV snapshot. They do not establish execution, event ordering across clocks, causation, collection coverage, retention or evidence completeness. A matching hash helps identify a file; it does not authenticate its provenance.

## Provenance and privacy

Optional labels can record what you report about the export:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz utc --parser-name "ExampleParser" --parser-version "reported-version" --source "Synthetic lab fixture"
```

These labels appear under `reported_provenance` with `verification: unverified_user_labels`. The utility does not verify a binary, a parser version, a command line, a source artifact or a chain of custody. Preserve those records separately.

Full input paths, raw CSV rows, unused columns and timestamp values from rejected records are omitted. The input basename is also omitted unless you supply `--include-filename`. User-provided provenance labels and the selected timestamp header are included literally, so keep sensitive names out of them. Timestamps and counts can themselves reveal activity patterns; review the JSON before sharing it.

## Output and exit codes

With no `--output`, JSON is printed to standard output. With `--output`, a completed JSON file is published atomically in the existing destination directory. An existing target is refused unless you explicitly add `--overwrite`. Input/output aliases, output symlinks and output directories are refused. The no-overwrite path requires filesystem hard-link support; if unavailable, writing fails instead of falling back to a partial or unsafe replacement.

| Exit code | Meaning |
| --- | --- |
| `0` | Summary completed; inspect rejection counts even when the command succeeds |
| `1` | Input, parsing, stability or output failure; no successful JSON summary is emitted |
| `2` | Command-line usage error |

A valid CSV can produce a successful summary with zero usable timestamps. A timezone-free supported timestamp without `--naive-tz` fails the command.

## Validation

Run the benign fixture suite:

```powershell
python -B -m unittest discover -s tests -p test_ez_csv_summary.py -v
```

On October 7, 2026, all **23 tests passed** on the connected Windows development machine. Tests cover offset normalization and range validation, explicit naive-time rules, long unused CSV fields, malformed and missing values, row widths and line counts, UTF-8 BOM, headers, format precision, input limits, symlinks, a changed input, output aliases, concurrent target creation, overwrite refusal, privacy defaults and CLI exit codes. Fixtures are generated in temporary directories and contain no real exports.

No Eric Zimmerman parser was run to validate this utility, and no real investigation result is supplied. The tests validate the summary behavior on synthetic CSV inputs.
