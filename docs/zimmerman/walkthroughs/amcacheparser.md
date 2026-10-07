# AmcacheParser: file references and program associations

Use Amcache to locate a lab program's recorded path and determine whether the file entry is associated with an installed application.

## Acquire the hive and transaction logs

Use [setup and evidence handling](../setup.md) before acquisition. Preserve the source host's `C:\Windows\appcompat\Programs\Amcache.hve`, original path, collection time, hash, Windows build, and matching transaction logs. Keep the hive and logs together under `C:\Cases\LAB-001\evidence\amcache`. The input must come from the source host, not the analysis workstation.

Install the approved tool outside the case directory. The catalog and README show different version banners; record the installed version and help output.

## Export associated and unassociated entries

```powershell
& 'C:\Tools\EZTools\AmcacheParser.exe' --version
& 'C:\Tools\EZTools\AmcacheParser.exe' --help
& 'C:\Tools\EZTools\AmcacheParser.exe' -f 'C:\Cases\LAB-001\evidence\amcache\Amcache.hve' -i --csv 'C:\Cases\LAB-001\output\amcache'
```

`-i` includes associated program/file entries alongside unassociated entries. Leave hash inclusion and exclusion filters off for the initial export. Save console messages: dirty-hive and log-replay warnings affect the recovered coverage.

## Read paths, associations, and hashes

Inspect the generated CSV headers and locate program entries, associated files, and unassociated files where present. Retain each candidate's full path, named timestamp fields, program association, and recorded hash. Distinguish hashes recorded in Amcache from those calculated from an acquired binary.

In a fictional drawing lab, `SketchHelper.exe` might be a portable utility with no installer association. An unassociated entry is a lead, not a malware classification. Amcache's format varies by Windows version; a timestamp is not automatically a launch time, and its recorded SHA-1 may not be interchangeable with a whole-file hash.

## Corroborate execution

Report the path reference with its supporting row. Use [Prefetch](pecmd.md), process telemetry, or other records to establish execution. Hash and inspect an acquired binary without launching it, and record missing artifacts.

For absent rows, check the input's identity, Windows build, output inventory, and parser warnings. Retain failed commands and use the shared setup to resolve runtime errors. Silencing transaction-log warnings does not restore missing data.

## Sources

Checked 2026-10-07:

- [Author's AmcacheParser README](https://github.com/EricZimmerman/AmcacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/amcacheparser.txt)
- [Author's current tool catalog](https://ericzimmerman.github.io/)

Validation: Documentation review only; parser and GUI examples have not been run.
