# MFT Explorer: inspect an NTFS record visually

How does a displayed MFT record relate to the parser's CSV row?

MFT Explorer is intended for small MFTs and education. Use [MFTECmd](mftecmd.md) for routine parsing and large collections. A small training volume makes record structure easier to inspect without forcing a workstation-wide MFT into the GUI.

## Load a small training MFT

Follow the [shared setup](../setup.md). Keep the copied artifact at `C:\Cases\LAB-001\evidence\NTFS\$MFT`, with its acquisition notes and hash. Record the viewer build and runtime; the current catalog lists its GUI build under .NET 9.

## Compare a record with its CSV row

1. Load the copied `$MFT` using the file-opening control and record its path.
2. Inspect the record list before searching. Distinguish record references, filenames, and timestamps; a text match can occur in any displayed field.
3. Right-click a column header and select **Show Find Panel**. Search for a filename from the training exercise.
4. Select the record and note its identifier, associated paths, and timestamp values.
5. Parse the same copy with MFTECmd and compare the relevant CSV row. Record the input hash, both tool versions, and the comparison in the case notes.

## Account for reused and deleted records

The viewer state and record comparison provide the basis for the notes. A filename can appear in several records, including deleted entries and reused references. Filesystem timestamps do not by themselves establish execution, a login identity, malicious intent, or a complete history of user activity.

If loading is slow or fails, check the artifact size and confirm it is a raw `$MFT`, not the enclosing image. Move large inputs to MFTECmd. Clear the search before concluding that surrounding records are absent. Any shared screenshot needs private paths and account names removed.

## References

- [Author catalog](https://ericzimmerman.github.io/)
- [Official MFT Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/mftexplorer.txt)

Sources checked October 7, 2026. Documentation reviewed; GUI not run. Paths describe a proposed lab, not observed evidence.
