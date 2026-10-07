# AppCompatCacheParser: investigate file knowledge without inventing a launch time

**Question:** Does the fictional lab host's compatibility cache reference an executable of interest, and which control set contains that reference?

## Prepare the input

Complete [setup and evidence handling](../setup.md). Acquire an authorized copy of the SYSTEM Registry hive from the source host, usually `C:\Windows\System32\config\SYSTEM`, with its matching transaction logs. Preserve original paths, hashes, collection time, and Windows build. Store working copies together in `C:\Cases\LAB-001\evidence\registry`.

AppCompatCacheParser reads a live Registry if `-f` is omitted. For this offline workflow, always supply the acquired SYSTEM hive so the analyst workstation cannot accidentally become the subject of the report.

## Parse the working copy

Use PowerShell with an approved installation:

```powershell
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' --version
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' --help
& 'C:\Tools\EZTools\AppCompatCacheParser.exe' -f 'C:\Cases\LAB-001\evidence\registry\SYSTEM' --csv 'C:\Cases\LAB-001\output\shimcache'
```

The first pass leaves control-set selection at its documented default of all control sets. Save the actual version, command, output inventory, and parser warnings. The README includes older syntax/version examples; consult the installed help before adding control-set or other optional switches.

## Inspect the output

Open the generated CSV files and identify the source hive, control set, path, ordering information, and timestamp fields available for that source format. Keep each control set distinguishable rather than combining similar-looking rows into independent executions. Search for the complete path of fictional `CanvasDemo.exe`, then review surrounding entries to understand the collection's context.

A compatibility-cache entry supports file knowledge under the source Windows format. It does not automatically prove that a process launched. In particular, a file's last-modified timestamp is not a last-execution timestamp. An application installation or ordinary file browsing can leave a benign explanation for a path that initially looks unfamiliar.

## Bound the conclusion and pivot

Record the artifact-level finding and the unanswered question separately: a path was recorded, but execution still needs corroboration. Compare with [Prefetch](pecmd.md), [Amcache](amcacheparser.md), UserAssist where available, and process creation telemetry. Identify precisely which record supports any claimed launch time or account attribution.

For empty output, confirm that the acquisition is the intended SYSTEM hive and that the Windows format is supported. Read dirty-hive and transaction-log messages; missing logs can limit recovered data. Do not use a “no-log” option merely to suppress that limitation. Address startup/runtime errors through the shared setup and retain the failed command in the notes.

## Sources and validation

Checked **2026-10-07**:

- [Author's AppCompatCacheParser README](https://github.com/EricZimmerman/AppCompatCacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/appcompatcacheparser.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
