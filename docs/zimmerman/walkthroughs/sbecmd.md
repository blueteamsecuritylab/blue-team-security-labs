# SBECmd: inspect folder-navigation artifacts at scale

**Question:** Which folder paths are represented in the acquired lab user's ShellBags, and what follow-up evidence would test their meaning?

Start with the [shared setup](../setup.md). Use copied `NTUSER.DAT` and `UsrClass.dat` hives under `C:\Cases\LAB-001\evidence\registry\user-lab`. Preserve their profile paths, matching transaction logs, hashes, and acquisition time. Collecting just one hive can leave a different set of ShellBags than collecting both.

## Parse the offline directory

The documented directory option examines offline hives. This example does not use the live-Registry option:

```powershell
& "C:\Tools\EZTools\SBECmd\SBECmd.exe" -d "C:\Cases\LAB-001\evidence\registry\user-lab" --csv "C:\Cases\LAB-001\outputs\sbecmd"
```

Adjust the executable path if SBECmd is packaged beside ShellBags Explorer. Save the console transcript, installed version, and generated file list. Inspect warnings concerning dirty hives or incomplete parsing. The manual describes `--nl` as ignoring transaction logs; this example leaves that override unset.

Keep separate source attribution for each hive. Output filenames are a convenience, not sufficient proof of the account or host to which a row belongs.

## Read paths and times together

Begin with the reconstructed path, source hive, bag path, and shell-item type. Check first/last interaction fields when available, then inspect key last-write times and embedded file-system timestamps separately. They come from different structures and should not be collapsed into one generic “access time.”

A represented folder path can support a lead about folder navigation. It does not establish that every file in the folder was opened or copied, that an executable ran, or that the account holder personally performed the action. First and last interaction fields do not enumerate every visit between them.

Preserve unusual paths, remote locations, and removable-volume references in the notes. Correlate them with the relevant acquired profile and independent activity within the same time window.

## Troubleshooting and next pivots

An empty CSV can reflect missing hives, no relevant ShellBags, parsing errors, or collection gaps. Check the transcript before concluding that the user never visited a folder. Some rows legitimately lack particular timestamps or identifiers.

Review a disputed record in [ShellBags Explorer](shellbags-explorer.md), using its details and hex views to inspect the shell item. Agreement between these tools is not independent parser validation because they share a parsing foundation. Pivot to LNK files, Jump Lists, event logs, and file-system records to test file access or volume context.

**Validation status:** Official manual and author usage example checked on 2026-10-07. SBECmd was **not run**; no output rows or account activity are claimed.

## Sources

- [Official SBECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sbecmd.txt)
- [Author benchmarks with offline SBECmd example](https://ericzimmerman.github.io/benchmarks/)
- [Author tool catalog](https://ericzimmerman.github.io/)
