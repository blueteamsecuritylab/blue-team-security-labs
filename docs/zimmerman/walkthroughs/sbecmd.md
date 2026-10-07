# SBECmd: export offline ShellBags

SBECmd extracts folder-navigation artifacts from user Registry hives. Follow the [lab setup](../setup.md) with copied `NTUSER.DAT` and `UsrClass.dat` under `C:\Cases\LAB-001\evidence\registry\user-lab`. Retain profile paths, matching transaction logs, hashes, and acquisition time. Collecting only one hive can omit ShellBags present in the other.

## Parse the copied user hives

The directory option processes offline hives:

```powershell
& "C:\Tools\EZTools\SBECmd\SBECmd.exe" -d "C:\Cases\LAB-001\evidence\registry\user-lab" --csv "C:\Cases\LAB-001\outputs\sbecmd"
```

Adjust the executable path if SBECmd is packaged beside ShellBags Explorer. Save the tool version, transcript, and generated file list. Check dirty-hive and incomplete-parsing warnings. `--nl` ignores transaction logs; the command leaves that override unset.

Maintain source attribution for each hive. An output filename alone does not identify the account or host represented by a row.

## Separate navigation from file activity

Review reconstructed paths, source hives, bag paths, and shell-item types. First/last interaction fields, key last-write times, and embedded file-system timestamps describe different structures. Keep their meanings separate rather than labeling all of them “access time.”

A ShellBag path can support folder-navigation analysis. It does not establish that every contained file was opened or copied, that a program executed, or that the account holder performed the action. First and last interaction fields do not list visits between those endpoints.

Retain unusual paths, remote locations, and removable-volume references. Correlate them with the acquired profile and independent activity in the same time window.

## Review gaps and disputed records

Empty output can reflect missing hives, absent ShellBags, parsing errors, or collection gaps; it does not prove the user never visited a folder. Some item types lack particular timestamps or identifiers.

Use [ShellBags Explorer](shellbags-explorer.md) to inspect a disputed item's details and bytes. The tools share a parsing foundation, so agreement is not independent parser validation. Correlate LNK files, Jump Lists, event logs, and file-system records to investigate file access or volume context.

Official manual and author usage example checked 2026-10-07. SBECmd not run; no output rows or account activity supplied.

## Sources

- [Official SBECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sbecmd.txt)
- [Author benchmarks with offline SBECmd example](https://ericzimmerman.github.io/benchmarks/)
- [Author tool catalog](https://ericzimmerman.github.io/)
