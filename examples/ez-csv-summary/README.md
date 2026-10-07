# CSV timestamp example

[synthetic-events.csv](synthetic-events.csv) contains five authored records. It is a utility fixture, not a Zimmerman parser export or incident dataset.

| CSV line | Value | Expected handling |
| --- | --- | --- |
| 2 | `2026-10-07T08:00:00Z` | Parse as 08:00 UTC |
| 3 | `2026-10-07T10:30:00+02:00` | Normalize to 08:30 UTC |
| 4 | `2026-10-07 08:45:00` | Apply the fixture's explicit UTC rule |
| 5 | `invalid-time` | Count as invalid; report the line number |
| 6 | Empty | Count as missing; report the line number |

## Reproduce the summary

Run from the repository root:

```bash
python tools/ez_csv_summary.py examples/ez-csv-summary/synthetic-events.csv --timestamp-column EventTime --naive-tz utc --source "Repository synthetic fixture"
```

The command prints JSON. It does not overwrite the stored [summary.json](summary.json).

Expected counts: five data records, three parsed timestamps, one invalid timestamp, and one missing timestamp. The minimum and maximum are 08:00 and 08:45 UTC. The source label is caller-supplied and remains marked unverified.

The stored report hashes the exact 329-byte CSV. Changing line endings or any other bytes changes the SHA-256 even if the parsed values stay the same. Choose a timezone from the actual export's semantics when working with another input; this fixture's UTC rule is specific to its authored values.

[CSV tool reference](../../docs/tools/ez-csv-summary.md) · [Repository home](../../README.md)
