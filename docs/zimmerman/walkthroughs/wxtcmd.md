# WxTCmd: activity records in ActivitiesCache.db

Inspect a source user's acquired Timeline database for application and document activity within the investigation window.

## Preserve the database and SQLite companions

Follow [setup and evidence handling](../setup.md). Acquire the source profile's `ActivitiesCache.db`, commonly beneath `AppData\Local\ConnectedDevicesPlatform\L.<profile>`. Preserve original directory/profile mapping, Windows build, hashes, acquisition time, and matching `-wal` and `-shm` files. Committed changes may still reside in the WAL.

Keep this acquired set unchanged in `C:\Cases\LAB-001\evidence\timeline`. For each attempt, copy the complete set into a fresh `C:\Cases\LAB-001\working\timeline` directory, retaining filenames and placing companions beside the database. Record source-to-working paths and SHA-256 comparisons before parsing. Document acquisition consistency and whether the parser incorporated companion files.

Timeline is a Windows 10 feature; its Windows 11 user experience was retired. Availability and activity-history settings affect coverage. A missing database leaves the activity question unresolved.

## Parse the working database

```powershell
& 'C:\Tools\EZTools\WxTCmd.exe' --version
& 'C:\Tools\EZTools\WxTCmd.exe' --help
& 'C:\Tools\EZTools\WxTCmd.exe' -f 'C:\Cases\LAB-001\working\timeline\ActivitiesCache.db' --csv 'C:\Cases\LAB-001\output\timeline'
```

Save the version, command, messages, and export inventory. `-f` targets the working database; `--csv` selects exports. Hash the working set after parsing and record changes: a SQLite reader can affect associated state. No read-only tool mode is assumed.

## Interpret activity types and time fields

Inspect headers in the activity and package-ID CSVs rather than relying on release-specific filenames. Review application identifiers, activity type, start/end fields, and available payload context. Retain source-database and profile mapping with each selected row.

Filter to the lab window. A fictional `WorkshopPlan.txt` activity can reflect resuming an ordinary editing task. An activity record is not automatically a process-creation event, complete execution interval, or proof that document contents were read. Interpret start/end fields according to the record type; they do not establish continuous user presence or identify a human from the profile directory.

## Corroboration and database errors

Compare [Jump Lists](jlecmd.md), [shortcuts](lecmd.md), [Prefetch](pecmd.md), and endpoint process telemetry. Identify the independent record supporting each execution or access claim.

For missing rows or database errors, check the source build, collection completeness, companions, supported schema, and warnings. Preserve the acquired database. Any reconstruction belongs on a separately documented derivative, with its method and limitations recorded. Retain failed attempts and use shared setup guidance for startup or runtime problems.

## Sources

Checked 2026-10-07:

- [Author's WxTCmd README](https://github.com/EricZimmerman/WxTCmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/wxtcmd.txt)
- [Microsoft Timeline support](https://support.microsoft.com/en-us/windows/ai/ai-features/get-help-with-timeline)
- [SQLite WAL documentation](https://sqlite.org/wal.html)

Validation: Documentation review only; parser and GUI examples have not been run.
