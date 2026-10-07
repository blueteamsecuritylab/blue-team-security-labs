# RBCmd: original paths and deletion times in Recycle Bin metadata

Recover the original path, size, and deletion timestamp recorded by an acquired Recycle Bin metadata file.

## Preserve metadata, content, and SID folders

Use [setup and evidence handling](../setup.md) for an authorized copy of the relevant volume's `$Recycle.Bin` tree. Retain user SID directories and matching `$I` metadata and `$R` content files where available; older systems may have INFO2 metadata. Record original names, paths, hashes, collection time, and source-volume mapping.

Place the copies in `C:\Cases\LAB-001\evidence\recycle-bin`. RBCmd parses Recycle Bin metadata. The official manual's introductory SUM description is an error; the author's catalog and RBCmd README identify the supported artifacts.

## Export metadata records

```powershell
& 'C:\Tools\EZTools\RBCmd.exe' --version
& 'C:\Tools\EZTools\RBCmd.exe' --help
& 'C:\Tools\EZTools\RBCmd.exe' -d 'C:\Cases\LAB-001\evidence\recycle-bin' --csv 'C:\Cases\LAB-001\output\recycle-bin'
```

Single quotes preserve dollar-prefixed path components in PowerShell. `-d` selects the acquired tree and `--csv` sets the separate export directory. Save the version, command, parser messages, and input/output inventories.

## Read the original path and deletion time

Inspect the CSV headers and retain the source metadata filename with the original path, size, format, and deletion timestamp. Keep SID-folder and volume provenance in the notes even when a CSV lacks those fields.

A fictional `SketchDraft.txt` record describes a recycled path. Its corresponding content may not survive, and attribution needs additional evidence. Deleting an obsolete drawing draft is a benign explanation; a late deletion timestamp alone does not establish evidence destruction.

The SID folder associates the record with an account's Recycle Bin, not conclusively with a human. Metadata does not establish complete recovered content. Deletions that bypass the Recycle Bin will not necessarily leave these records, so an absent match cannot rule out deletion.

## Recover context without executing content

Hash and inspect an acquired matching `$R` file without execution, preserving the pair's filename relationship. Compare filesystem journal/MFT information, process telemetry, and source-account activity to investigate timing and mechanism.

For parse errors, verify metadata input type, source format, and acquisition completeness. RBCmd is not an arbitrary deleted-file recovery tool. Retain failures, avoid renaming unrelated files to force parsing, and use shared setup guidance for runtime problems.

## Sources

Checked 2026-10-07:

- [Author's RBCmd README](https://github.com/EricZimmerman/RBCmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/rbcmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Validation: Documentation review only; parser and GUI examples have not been run.
