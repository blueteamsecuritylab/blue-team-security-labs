# SQLECmd: extract SQLite records with a preserved map set

SQLECmd extracts application records from SQLite databases that match its maps. Follow the [lab setup](../setup.md) and retain the acquired History database with collected WAL/SHM or journal files under `C:\Cases\LAB-001\evidence\sqlite\browser-lab`. Preserve acquisition context, browser/profile identity, hashes, filenames, and relative paths. A main database without relevant journal or WAL data may be incomplete.

Copy the acquired set to `C:\Cases\LAB-001\working\sqlite`, preserving companion-file relationships and recording source-to-working hashes. Both commands use this disposable copy. SQLite opens can create or update companion files; a read-only open by this parser has not been established.

## Preserve the matching maps

A SQLite header alone is insufficient: SQLECmd needs a map matching the application's database schema. Retain the exact map set and hashes. Updating maps between runs can change output and should be recorded as a separate run.

```powershell
& "C:\Tools\EZTools\SQLECmd\SQLECmd.exe" -f "C:\Cases\LAB-001\working\sqlite\browser-lab\History" --maps "C:\Tools\EZTools\SQLECmd\Maps" --csv "C:\Cases\LAB-001\outputs\sqlecmd"
```

Save the version, command, transcript, and generated file list. Confirm the matched map and whether each extraction query completed. This command uses local maps without refreshing them during analysis.

For unknown lab databases, `--hunt` identifies SQLite headers regardless of filenames:

```powershell
& "C:\Tools\EZTools\SQLECmd\SQLECmd.exe" -d "C:\Cases\LAB-001\working\sqlite" --hunt --maps "C:\Tools\EZTools\SQLECmd\Maps" --csv "C:\Cases\LAB-001\outputs\sqlecmd-hunt"
```

Header detection does not establish that a matching map exists.

## Read the map's SQL

Review SQL and descriptions before interpreting timestamps, joins, or row counts. A browser URL record belongs to the acquired database and profile; background activity, synchronization, redirects, and retained history prevent automatic attribution to a deliberate human visit.

Keep source paths for byte-identical inputs. The documented deduplication default can reduce repeated parsing, but separate acquisitions retain distinct evidential context.

## Resolve unmapped or empty results

No CSV may mean a missing map, changed schema, non-SQLite input, damaged copy, or a query returning no rows. Check the transcript and schema before concluding that activity was absent. Do not modify acquired originals to make a query work.

Correlate download and URL records with file-system paths, endpoint telemetry, and adjacent browser artifacts. Record the rows and map queries supporting a finding, and identify unparsed data.

Author CLI and official manual checked 2026-10-07. SQLECmd not run; no parsed database or findings supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/SQLECmd)
- [Author map definitions](https://github.com/EricZimmerman/SQLECmd/tree/master/SQLMap/Maps)
- [Official SQLECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sqlecmd.txt)
- [SQLite documentation: write-ahead logging and companion files](https://sqlite.org/wal.html)
