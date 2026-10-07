# SQLECmd: parse a mapped SQLite database reproducibly

**Question:** Which application records are present in a copied lab database, and which map explains the output?

Follow the [shared setup](../setup.md). Keep the acquired lab browser History database and its collected WAL/SHM or journal files under `C:\Cases\LAB-001\evidence\sqlite\browser-lab`, unchanged. Preserve acquisition context, browser/profile identity, hashes, filenames, and relative paths. A main database without its relevant journal or WAL context may not represent the complete acquired state.

Before parsing, duplicate the acquired SQLite set into `C:\Cases\LAB-001\working\sqlite`, preserving companion-file relationships and recording the source-to-working hash mapping. Both commands below use that disposable working copy. Opening a SQLite database can create or update companion files; do not assume this parser opens it read-only.

## Fix the map set for the run

SQLECmd does not decode every SQLite database automatically. A matching map must exist. Review the author map definitions for the application's schema and preserve the exact map set and hashes used. Updating maps between runs can change output; record that as a separate run.

```powershell
& "C:\Tools\EZTools\SQLECmd\SQLECmd.exe" -f "C:\Cases\LAB-001\working\sqlite\browser-lab\History" --maps "C:\Tools\EZTools\SQLECmd\Maps" --csv "C:\Cases\LAB-001\outputs\sqlecmd"
```

Save the tool version, command, transcript, and generated file list. Check which map matched and whether each extraction query completed. The example deliberately uses a preserved local map set rather than refreshing it during analysis.

For a directory of unknown lab databases, the documented `--hunt` option identifies SQLite headers regardless of filenames:

```powershell
& "C:\Tools\EZTools\SQLECmd\SQLECmd.exe" -d "C:\Cases\LAB-001\working\sqlite" --hunt --maps "C:\Tools\EZTools\SQLECmd\Maps" --csv "C:\Cases\LAB-001\outputs\sqlecmd-hunt"
```

Identifying a SQLite file still does not guarantee a map can parse it.

## Interpret the query, not just the column name

Read the matched map's SQL and descriptions before interpreting timestamps, joined fields, or row counts. A browser URL record is evidence in that database and profile; it does not necessarily establish a deliberate visit by a particular human. Background activity, synchronization, redirects, and retained history can affect interpretation.

Retain source paths even where inputs have identical bytes. The documented deduplication default can reduce duplicate processing, but separate acquisitions may still have distinct evidential context.

## Troubleshooting and next pivots

No CSV can mean no matching map, a changed schema, a non-SQLite input, a damaged copy, or no rows returned by the map's query. Inspect the transcript and schema before describing absence of activity. Do not modify the original database to make a query work.

Follow a download or URL lead into its file-system path, endpoint telemetry, and adjacent browser artifacts. Record which rows and map queries support the claim and which data remained unparsed.

**Validation status:** Author CLI and official manual checked on 2026-10-07. SQLECmd was **not run**; no parsed database or findings are supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/SQLECmd)
- [Author map definitions](https://github.com/EricZimmerman/SQLECmd/tree/master/SQLMap/Maps)
- [Official SQLECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sqlecmd.txt)
- [SQLite documentation: write-ahead logging and companion files](https://sqlite.org/wal.html)
