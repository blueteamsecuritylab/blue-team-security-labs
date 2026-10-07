# RBCmd: reconstruct a Recycle Bin metadata reference

**Question:** What original path, size, and deletion timestamp does an acquired Recycle Bin metadata file record?

## Prepare the input

Follow [setup and evidence handling](../setup.md). Acquire an authorized copy of the relevant volume's `$Recycle.Bin` tree, retaining user SID directories and matching `$I` metadata and `$R` content files where available. Older sources may instead have INFO2 metadata. Preserve original names, paths, hashes, collection time, and the mapping between source volume and case copy.

Store working files in `C:\Cases\LAB-001\evidence\recycle-bin`. RBCmd parses Recycle Bin metadata; it is not the SUM database parser. One introductory sentence in the official manual incorrectly describes SUM, so this guide follows the author's catalog and RBCmd README for its purpose.

## Parse and export

Run from PowerShell using the approved installation:

```powershell
& 'C:\Tools\EZTools\RBCmd.exe' --version
& 'C:\Tools\EZTools\RBCmd.exe' --help
& 'C:\Tools\EZTools\RBCmd.exe' -d 'C:\Cases\LAB-001\evidence\recycle-bin' --csv 'C:\Cases\LAB-001\output\recycle-bin'
```

Single quotes keep any dollar-prefixed path components literal in PowerShell. The directory option selects the acquired tree; `--csv` sets the separate output location. Save version, exact command, parse messages, and input/output inventories.

## Inspect the output

Review the generated CSV headers, then retain each relevant source metadata filename alongside its original file path, size, format, and deletion timestamp. Keep SID-folder and volume provenance in the notes even if a CSV field does not include all of it.

For a fictional `SketchDraft.txt` record, distinguish three things: the metadata says an original path was recycled, a corresponding content file may or may not survive, and the person responsible remains a separate attribution question. Deleting an obsolete drawing draft during a lab exercise is a benign explanation. A late timestamp alone does not establish evidence destruction.

A SID directory associates the record with an account's Recycle Bin, not conclusively with a particular human. Metadata does not prove recovered content is complete. Some deletion methods bypass the Recycle Bin, so no match cannot establish that no deletion occurred.

## Pivot and troubleshoot

If a matching `$R` file was acquired, hash and inspect its contents without execution, preserving the pair's filename relationship. Correlate filesystem journal/MFT information, process telemetry, and the source account's activity to explain timing and mechanism.

For errors, check that selected files are metadata inputs rather than expecting RBCmd to recover arbitrary deleted data. Verify acquisition completeness and source format. Keep failures visible; do not rename unrelated files to force parsing. Resolve startup/runtime issues through the shared setup.

## Sources and validation

Checked **2026-10-07**:

- [Author's RBCmd README](https://github.com/EricZimmerman/RBCmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/rbcmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
