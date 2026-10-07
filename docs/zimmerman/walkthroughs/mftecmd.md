# MFTECmd: trace file records and USN changes

What paths and filesystem changes relate to a file on the lab volume?

MFTECmd parses `$MFT`, `$J`, `$Boot`, `$SDS`, and `$I30`. The example below pairs an acquired MFT with its USN change journal. `$LogFile` support is still marked forthcoming in the author catalog.

## Pair artifacts from the same volume

Use the [shared setup](../setup.md), then place working copies at `C:\Cases\LAB-001\evidence\NTFS\$MFT` and `C:\Cases\LAB-001\evidence\NTFS\$J`. Record acquisition time, volume identity, and both hashes. Separate output directories keep the MFT and journal rows distinguishable.

## Export the MFT and journal

Run in PowerShell from the MFTECmd directory:

```powershell
.\MFTECmd.exe -f 'C:\Cases\LAB-001\evidence\NTFS\$MFT' --csv 'C:\Cases\LAB-001\output\mft' --csvf 'mft.csv'
.\MFTECmd.exe -f 'C:\Cases\LAB-001\evidence\NTFS\$J' -m 'C:\Cases\LAB-001\evidence\NTFS\$MFT' --csv 'C:\Cases\LAB-001\output\usn' --csvf 'usn.csv'
```

Single quotes preserve the dollar signs in PowerShell. `-m` supplies the associated MFT for journal parent-path resolution. Save console messages with the CSVs.

In [Timeline Explorer](timeline-explorer.md), search the filename and inspect parent paths, entry and sequence numbers, timestamps, and journal reasons. Follow the record reference through rename or deletion-related rows: identical filenames can belong to different objects. Record the rows that support each interpretation.

## Separate filesystem changes from execution

MFT records describe metadata; USN rows describe filesystem operations. Neither establishes program execution or the responsible person's identity or intent. Correlate with event logs or endpoint process telemetry before describing an execution chain. Journal rollover, record reuse, acquisition scope, and filters can all explain missing rows.

For parsing errors, confirm the inputs are extracted NTFS artifacts, not the enclosing disk image, and that both came from the same volume. Check installed `--help` and retain errors with any partial export.

## References

- [Author catalog](https://ericzimmerman.github.io/)
- [Official MFTECmd manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/mftecmd.txt)
- [MFTECmd repository](https://github.com/EricZimmerman/MFTECmd)

Sources checked October 7, 2026. Command syntax reviewed; parser commands not run. No case results supplied.
