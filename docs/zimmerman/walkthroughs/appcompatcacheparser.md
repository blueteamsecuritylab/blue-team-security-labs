# AppCompatCacheParser: paths and control sets in ShimCache

Locate an executable's compatibility-cache reference and identify the control set containing it. ShimCache records file knowledge; execution requires separate evidence.

## Acquire SYSTEM and its transaction logs

Follow [setup and evidence handling](../setup.md). Preserve an authorized copy of the source host's SYSTEM hive, usually `C:\Windows\System32\config\SYSTEM`, with matching transaction logs. Record original paths, hashes, collection time, and Windows build. Keep the copies together in `C:\Cases\LAB-001\evidence\registry`.

Always supply `-f` for offline analysis. Without it, AppCompatCacheParser reads the analysis workstation's live Registry.

## Export all control sets

```powershell
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' --version
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' --help
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' -f 'C:\Cases\LAB-001\evidence\registry\SYSTEM' --csv 'C:\Cases\LAB-001\output\shimcache'
```

The default includes all control sets. Save the installed version, command, output inventory, and warnings. The README contains older syntax and version examples; check installed help before adding a control-set selector or other optional switches.

## Interpret the path and timestamp fields

Identify the source hive, control set, path, ordering information, and available timestamp fields in each generated CSV. Keep control sets distinguishable: similar rows from different sets are not separate executions.

Search for the complete path of fictional `CanvasDemo.exe` and inspect surrounding entries. Installation or ordinary file browsing can explain an unfamiliar path. A cache entry does not, by itself, establish a process launch. The file's last-modified timestamp is not its last-execution time; interpret the fields according to the source Windows format.

## Find execution evidence

Record the referenced path and its source row, then compare [Prefetch](pecmd.md), [Amcache](amcacheparser.md), UserAssist where available, and process creation telemetry. Identify the record supporting each launch-time or account-attribution claim.

For empty output, verify that the input is the intended SYSTEM hive and that its format is supported. Read dirty-hive and transaction-log messages; missing logs limit recovery. A no-log option skips log replay without resolving that limitation. Retain unsuccessful commands and use shared setup guidance for startup or runtime errors.

## Sources

Checked 2026-10-07:

- [Author's AppCompatCacheParser README](https://github.com/EricZimmerman/AppCompatCacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/appcompatcacheparser.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Validation: Documentation review only; parser and GUI examples have not been run.
