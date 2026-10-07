# MFTECmd: follow a file through NTFS metadata

**Question:** What paths and recorded changes relate to a file on the lab volume?

MFTECmd parses `$MFT`, `$J`, `$Boot`, `$SDS`, and `$I30` artifacts. This walkthrough starts with an acquired `$MFT` and its associated USN change journal, `$J`. It does not assume `$LogFile` parsing is available; the current author catalog marks that support as forthcoming.

## Prepare the inputs

Follow the [shared setup](../setup.md). Place working copies from the same volume at `C:\Cases\LAB-001\evidence\NTFS\$MFT` and `C:\Cases\LAB-001\evidence\NTFS\$J`. Record acquisition time, volume identity, and hashes. Use separate output directories so journal rows and MFT rows retain their provenance.

## Parse and inspect

From the directory containing the reviewed MFTECmd build, use PowerShell:

```powershell
.\MFTECmd.exe -f 'C:\Cases\LAB-001\evidence\NTFS\$MFT' --csv 'C:\Cases\LAB-001\output\mft' --csvf 'mft.csv'
.\MFTECmd.exe -f 'C:\Cases\LAB-001\evidence\NTFS\$J' -m 'C:\Cases\LAB-001\evidence\NTFS\$MFT' --csv 'C:\Cases\LAB-001\output\usn' --csvf 'usn.csv'
```

Single quotes keep PowerShell from interpreting the dollar signs. The `-m` input helps resolve journal parent paths using the associated MFT. Preserve console messages alongside both CSVs.

Open the CSVs in [Timeline Explorer](timeline-explorer.md). Search the filename, then inspect parent paths, entry and sequence numbers, timestamps, and journal reasons. Follow the same reference across rename or deletion-related rows rather than treating matching filenames as one object. Record the exact rows used for each interpretation.

## What the results support

An MFT record describes filesystem metadata; it does not prove program execution. A journal change records a filesystem operation, not the identity or intent of the person responsible. Compare both sources with event logs or endpoint process telemetry before describing an execution chain. A missing row can reflect journal rollover, record reuse, acquisition scope, or filtering.

If parsing fails, confirm these are extracted NTFS artifacts rather than a whole disk image. Check that `$MFT` and `$J` came from the same volume. Compare installed `--help` with the documented switches, and retain errors rather than silently discarding a partial export.

## Sources and validation

- [Author catalog](https://ericzimmerman.github.io/)
- [Official MFTECmd manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/mftecmd.txt)
- [MFTECmd repository](https://github.com/EricZimmerman/MFTECmd)

Sources checked October 7, 2026. Documentation and command syntax were reviewed; the parser commands were not executed for this repository. No case results are supplied.
