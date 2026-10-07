# Offline CSV timestamp summary

[ez_csv_summary.py](../../tools/ez_csv_summary.py) reads one UTF-8 CSV, hashes the bytes it parses, counts usable and rejected timestamps, and reports the observed bounds in UTC. Use it to check an export before reviewing the timeline in detail.

The utility performs no artifact parsing or acquisition, Zimmerman tool launches, artifact execution, endpoint collection, or network access. It evaluates no spreadsheet formulas and writes JSON only. A summary does not establish that a file was executed.

## Try the sample

From the repository root, run:

```powershell
python tools/ez_csv_summary.py examples/ez-csv-summary/synthetic-events.csv --timestamp-column EventTime --naive-tz utc --source "Repository synthetic fixture"
```

The five-record [fixture](../../examples/ez-csv-summary/synthetic-events.csv) produces three parsed timestamps, one invalid timestamp, and one missing timestamp. The [recorded JSON output](../../examples/ez-csv-summary/summary.json) from the October 7, 2026 Windows run spans 08:00–08:45 UTC. This synthetic utility test contains no Zimmerman parser output or incident findings. Its naive time is defined as UTC; establish the timezone independently for a real export.

## Select the column and timezone

Use Python 3.10 or newer. Check the CSV's timestamp header and the parser's time handling before selecting a timezone policy. Headers are matched exactly, including case; duplicate and blank headers are rejected.

For timestamps that carry `Z` or a numeric offset:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime"
```

For values without an offset, specify their timezone. Use `utc` only after establishing that the export records UTC:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz utc --output "C:\Lab\Reports\synthetic-summary.json"
```

A fixed offset is also accepted:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz=-05:00
```

Fixed offsets have no daylight-saving rules. Establish the time interpretation before applying one across a DST change. Values that carry an offset retain it regardless of `--naive-tz`.

The example directories are fictional. Create the output directory before running the command.

## Format and limits

Supported timestamps contain a date and time with seconds:

- `2026-10-07T08:00:00Z`
- `2026-10-07 08:00:00.123456+02:00`
- `2026-10-07 08:00:00`, with an explicit naive-time policy

Offsets accept hours 00–23 and minutes 00–59; invalid minutes are rejected. Fractional seconds are limited to six digits. Higher precision, date-only values, locale-specific dates, impossible dates, and unsupported formats count as invalid. No precision is truncated and no format is guessed. Check the selected column because parser exports can use other formats.

Input must be UTF-8, with an optional UTF-8 BOM. Document any encoding conversion and preserve the original export. The delimiter defaults to comma; use `--delimiter ";"` for a semicolon-delimited file.

The default byte limit is 64 MiB; `--max-mib` accepts another positive limit. Fields, including unused payloads, may occupy that bound. Parsing sets the CSV field limit to the snapshot bound and restores its prior value afterward.

The file is read once; the same snapshot is hashed and parsed. Identity, size, and modification metadata checks reject detected changes during reading. These checks do not guarantee acquisition or detect an adversarial writer that evades them.

Input symlinks at the final path component, nonregular files, malformed CSV, duplicate headers, and missing selected columns fail the command. A valid header-only file produces zero records and null bounds.

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

Every nonparsed record enters one of four rejection categories. A multiline quoted record counts once; warnings identify its physical start and end lines. Malformed quoting fails the entire summary.

The counts and bounds apply only to this CSV snapshot. They do not establish execution, order across clocks, causation, coverage, retention, or evidence completeness. A matching hash identifies bytes without authenticating provenance.

## Record provenance and review disclosure

Optional labels can record what you report about the export:

```powershell
python tools/ez_csv_summary.py "C:\Lab\Exports\synthetic-events.csv" --timestamp-column "EventTime" --naive-tz utc --parser-name "ExampleParser" --parser-version "reported-version" --source "Synthetic lab fixture"
```

Labels appear under `reported_provenance` with `verification: unverified_user_labels`. Preserve binary, parser-version, command-line, source-artifact, and chain-of-custody records separately; the utility verifies none of them.

The JSON omits full input paths, raw rows, unused columns, and rejected timestamp values. The basename is included only with `--include-filename`. Provenance labels and the selected header are copied literally; omit sensitive names. Review timestamps and counts for disclosure before sharing the report.

## Output and exit codes

Without `--output`, JSON goes to standard output. With it, the completed report is published atomically in an existing directory. Replacing an existing report requires `--overwrite`; input/output aliases, output symlinks, and directory targets are refused. Without overwrite, publication requires hard-link support. If the filesystem lacks it, the write fails.

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

On October 7, 2026, **23 tests passed** on Windows. Coverage includes offset normalization and ranges, naive-time rules, long unused fields, malformed and missing values, row widths, physical line counts, BOM, headers, precision, size limits, symlinks, changed input, output aliases, concurrent target creation, overwrite refusal, privacy defaults, and CLI exits. All fixtures are generated in temporary directories using synthetic data.

The tests validate synthetic CSV summaries. No Eric Zimmerman parser was run, and no real investigation results are included.