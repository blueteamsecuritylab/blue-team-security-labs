# WxTCmd: inspect recorded Windows Timeline activity

**Question:** What activity records survive in a source user's acquired Timeline database, and what do they contribute to a lab timeline?

## Prepare the input

Follow [setup and evidence handling](../setup.md). Acquire an authorized copy of the source profile's `ActivitiesCache.db`, commonly beneath `AppData\Local\ConnectedDevicesPlatform\L.<profile>`. Preserve original directory/profile mapping, Windows build, hashes, acquisition time, and any matching SQLite `-wal` and `-shm` files present. Keep the acquired set intact; committed changes may still reside in a WAL.

Keep the acquired database and companions unchanged in `C:\Cases\LAB-001\evidence\timeline`. Before each analysis attempt, copy the complete acquired set into a fresh `C:\Cases\LAB-001\working\timeline` directory, preserving filenames and keeping matching companions beside the database. Record each source-to-working path and SHA-256 comparison before parsing. Record the acquisition's consistency and whether the analysis tool incorporated companion files rather than assuming it did.

Microsoft describes Timeline as a Windows 10 feature; its Windows 11 user experience was retired. Availability and activity-history settings therefore matter. An absent database is a coverage gap.

## Parse and export

Use the verified installation in PowerShell:

```powershell
& 'C:\Tools\EZTools\WxTCmd.exe' --version
& 'C:\Tools\EZTools\WxTCmd.exe' --help
& 'C:\Tools\EZTools\WxTCmd.exe' -f 'C:\Cases\LAB-001\working\timeline\ActivitiesCache.db' --csv 'C:\Cases\LAB-001\output\timeline'
```

Save the installed version, command, messages, and output inventory. The file switch targets the working database; CSV selects the results directory. Record working-set hashes after parsing and any changes, because opening a SQLite database can affect its associated state depending on the reader. This example does not claim a read-only tool mode.

## Inspect the outputs

The official manual describes activity and package-ID CSVs. Inspect actual headers rather than depending on a release-specific filename. Review application identifiers, activity type, start/end fields, and payload context where present. Keep the profile mapping and database source with each selected row.

Filter to the lab window and inspect a fictional activity involving `WorkshopPlan.txt`. Resuming a legitimate editing task is a benign explanation. An application's activity record is not automatically equivalent to a process-creation event, a complete execution interval, or proof that a document's contents were read.

Treat start/end values according to the record's semantics. Do not infer user presence continuously between them or identify a human solely from the profile directory.

## Pivot and troubleshoot

Correlate relevant records with [Jump Lists](jlecmd.md), [shortcuts](lecmd.md), [Prefetch](pecmd.md), and endpoint process telemetry. State which independent record supports each execution or access claim.

For database errors or absent rows, check source build, collection completeness, SQLite companions, supported schema, and parser warnings. Do not alter the original database to make it open. Any reconstruction belongs on a separately documented derivative copy, with the method and limitations recorded. Preserve unsuccessful attempts and resolve startup/runtime issues through the shared setup.

## Sources and validation

Checked **2026-10-07**:

- [Author's WxTCmd README](https://github.com/EricZimmerman/WxTCmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/wxtcmd.txt)
- [Microsoft Timeline support](https://support.microsoft.com/en-us/windows/ai/ai-features/get-help-with-timeline)
- [SQLite WAL documentation](https://sqlite.org/wal.html)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
