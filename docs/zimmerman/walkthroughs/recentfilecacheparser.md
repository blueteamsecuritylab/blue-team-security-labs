# RecentFileCacheParser: turn a legacy cache path into a scoped lead

**Question:** Which file paths are present in an acquired RecentFileCache, and can another artifact explain those references?

## Prepare the input

Follow [setup and evidence handling](../setup.md). When the source system contains it, acquire an authorized copy of `C:\Windows\AppCompat\Programs\RecentFileCache.bcf`. Record Windows build, original path, collection time, hash, and acquisition method. Preserve filesystem metadata separately if ordinary copying changes it. Place a working file at `C:\Cases\LAB-001\evidence\appcompat\RecentFileCache.bcf`.

This is a legacy artifact workflow. Do not assume a contemporary Windows host must contain this file, or confuse it with Amcache merely because the directories are similar. A missing cache is not a finding that no software ran.

## Parse and export

Use the approved installation in PowerShell:

```powershell
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' --version
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' --help
& 'C:\Tools\EZTools\RecentFileCacheParser.exe' -f 'C:\Cases\LAB-001\evidence\appcompat\RecentFileCache.bcf' --csv 'C:\Cases\LAB-001\output\recent-file-cache'
```

The file option identifies the acquired cache and the CSV option selects the output directory. Capture actual version, command, warnings, and output inventory. The author's README and manual document JSON as another option, but CSV is sufficient for the initial path review.

## Inspect the output

Open the generated CSV and inspect its headers before filtering. Keep the input cache's identity attached to every finding. The manual's JSON example separates source-file timestamps from an array of file names. That structure matters: do not assign the cache's created or modified time as an execution time for each listed executable.

Choose one complete path, such as fictional `C:\LabApps\SketchHelper.exe`, and write down the exact reference. Compare name, directory, and source-host context rather than treating a familiar filename as a known-good identity. A normal program update or lab maintenance task can explain a new path just as readily as suspicious activity.

## Bound the conclusion and pivot

State that the acquired cache contains a path; do not claim that it supplies a complete installation inventory, a reliable per-file launch time, a current file on disk, or a malware verdict. If the underlying binary was acquired, calculate its hashes and inspect it without execution. Compare [Prefetch](pecmd.md), [Amcache](amcacheparser.md), [ShimCache](appcompatcacheparser.md), and available process telemetry to determine what happened and when.

For empty or failed output, check that the file is the intended cache rather than a renamed unrelated artifact. Review truncation, format support, acquisition completeness, and parser messages. Record missing artifacts and unsuccessful commands. Resolve installation/runtime problems through the shared setup instead of masking them as negative evidence.

## Sources and validation

Checked **2026-10-07**:

- [Author's RecentFileCacheParser README](https://github.com/EricZimmerman/RecentFileCacheParser)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/recentfilecacheparser.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
