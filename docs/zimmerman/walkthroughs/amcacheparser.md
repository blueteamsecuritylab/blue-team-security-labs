# AmcacheParser: separate an application lead from an execution claim

**Question:** Does the acquired Amcache contain a reference to the fictional lab program being reviewed, and is that reference associated with an installed application?

## Prepare the input

Follow [setup and evidence handling](../setup.md). Obtain an authorized acquisition copy of `C:\Windows\appcompat\Programs\Amcache.hve`, preserving its original location, collection time, hash, and any accompanying transaction logs. Put the working hive and its matching logs together under `C:\Cases\LAB-001\evidence\amcache`. Record the source Windows build. Do not substitute the analyst workstation's hive.

Use an approved tool installation outside the case directory. The catalog and repository README carry different version banners; save the installed version and help before choosing options.

## Parse the working copy

Run in PowerShell:

```powershell
& 'C:\Tools\EZTools\AmcacheParser.exe' --version
& 'C:\Tools\EZTools\AmcacheParser.exe' --help
& 'C:\Tools\EZTools\AmcacheParser.exe' -f 'C:\Cases\LAB-001\evidence\amcache\Amcache.hve' -i --csv 'C:\Cases\LAB-001\output\amcache'
```

The example includes associated program/file entries with `-i` rather than reducing the first pass to unassociated entries. Leave hash inclusion/exclusion filters off during this baseline review. Save console messages with the case notes; a dirty-hive or replay warning changes the coverage you can claim.

## Inspect the outputs

Review the generated CSV files rather than assuming a fixed filename or column layout. Locate program entries, associated files, and unassociated files when present. For a candidate, retain its full path, relevant timestamp names, application association, and recorded hash. State explicitly whether a value came from the artifact or was calculated from a recovered file.

An unassociated entry for fictional `SketchHelper.exe` is a triage lead. A portable legitimate drawing utility can also lack an installer association. Neither its name nor that category decides whether it is malware. Amcache formats differ across Windows versions; do not turn every timestamp into a launch time or assume a recorded SHA-1 is interchangeable with a whole-file hash.

## Bound the conclusion and pivot

Write: “The acquired hive references this path,” followed by the exact supporting row. Confirm execution separately using [Prefetch](pecmd.md), process telemetry, or other available records. If the binary was acquired, calculate its hashes and inspect it without launching it. Document missing artifacts.

For absent rows, verify input identity, Windows build, output files, and warnings before interpreting absence. Preserve a failed parse and troubleshoot the runtime through the shared setup. Do not silence transaction-log warnings merely to obtain a clean-looking report.

## Sources and validation

Checked **2026-10-07**:

- [Author's AmcacheParser README](https://github.com/EricZimmerman/AmcacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/amcacheparser.txt)
- [Author's current tool catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
