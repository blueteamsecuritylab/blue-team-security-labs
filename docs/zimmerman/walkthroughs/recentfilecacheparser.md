# RecentFileCacheParser: paths recorded in a legacy cache

Extract file paths from an acquired RecentFileCache and find corroborating records for a candidate program.

## Acquire RecentFileCache.bcf

Follow [setup and evidence handling](../setup.md). When present, acquire `C:\Windows\AppCompat\Programs\RecentFileCache.bcf`. Record the Windows build, original path, collection time, hash, and acquisition method. Preserve original filesystem metadata separately if copying changes it. Place the copy at `C:\Cases\LAB-001\evidence\appcompat\RecentFileCache.bcf`.

This legacy artifact is not expected on every contemporary Windows host and is distinct from Amcache despite the similar directory location. A missing cache does not establish that no software ran.

## Export the cached paths

```powershell
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' --version
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' --help
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' -f 'C:\Cases\LAB-001\evidence\appcompat\RecentFileCache.bcf' --csv 'C:\Cases\LAB-001\output\recent-file-cache'
```

`-f` selects the acquired cache; `--csv` selects the export directory. Save the installed version, command, warnings, and output inventory. The README and manual also document JSON output; CSV provides the initial path list.

## Keep cache timestamps separate from executable paths

Inspect the CSV headers and retain the source cache's identity with each finding. The manual's JSON example lists source-file timestamps separately from its file-name array. The cache's creation or modification time cannot be assigned as an execution time to every listed executable.

For fictional `C:\LabApps\SketchHelper.exe`, record the full path and compare its directory and source-host context. A familiar filename does not identify a known-good binary. A routine program update or lab maintenance task can explain a new reference.

The cache does not supply a complete installation inventory, reliable per-file launch times, proof of a file's current presence, or a malware verdict.

## Corroborate a path reference

Hash and inspect an acquired candidate binary without executing it. Compare [Prefetch](pecmd.md), [Amcache](amcacheparser.md), [ShimCache](appcompatcacheparser.md), and available process telemetry to investigate the activity and its timing.

For empty or failed output, verify that the input is the intended cache, not a renamed unrelated file. Check truncation, format support, acquisition completeness, and parser messages. Record missing artifacts and unsuccessful commands; use shared setup guidance for installation or runtime errors. Failures do not establish absent activity.

## Sources

Checked 2026-10-07:

- [Author's RecentFileCacheParser README](https://github.com/EricZimmerman/RecentFileCacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/recentfilecacheparser.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Validation: Documentation review only; parser and GUI examples have not been run.
