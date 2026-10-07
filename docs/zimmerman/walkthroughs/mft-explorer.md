# MFT Explorer: inspect an NTFS record visually

**Question:** What is inside an MFT record, and how does it relate to the CSV view?

MFT Explorer is a graphical viewer for `$MFT` files. The official manual limits its intended use to smaller MFTs and education. For routine parsing or large collections, use [MFTECmd](mftecmd.md), then review the exported CSV. This guide uses a small, deliberately prepared lab artifact to learn the structure.

## Prepare the input

Follow the [shared setup](../setup.md). Keep a working copy at `C:\Cases\LAB-001\evidence\NTFS\$MFT`, with its acquisition notes and hash. Choose a small training volume rather than a workstation-wide artifact. Record the MFT Explorer build and runtime used; the current catalog offers its GUI build in the .NET 9 column.

## Explore the record

1. Start MFT Explorer on the analysis workstation and load the copied `$MFT` using its file-opening control. Keep the evidence path in your notes.
2. Inspect the populated record list before searching. Identify which values are record references, filenames, or timestamps so a text match is not mistaken for a different field.
3. Right-click a column header and select **Show Find Panel**, as documented in the manual. Search for a filename created in the training exercise.
4. Select the relevant record and examine its displayed details. Note the record identifier, associated paths, and timestamp values rather than copying only the filename.
5. Parse the same copy with MFTECmd and compare the relevant CSV row. Save your interpretation in the case notes, including both tool versions and the input hash.

## Review the evidence

The useful output here is the viewer state and your documented record comparison. A filename can appear in more than one record; deleted entries and reused references require context. A displayed timestamp is filesystem metadata, not a complete account of user activity. The viewer alone cannot establish execution, a login identity, or malicious intent.

If opening is slow or fails, check artifact size and confirm it is a raw `$MFT`, not the enclosing image. Move larger work to MFTECmd rather than repeatedly forcing the GUI to load it. If a search hides surrounding records, clear the search before concluding that related entries are absent. Do not publish screenshots that expose private paths or account names.

## Sources and validation

- [Author catalog](https://ericzimmerman.github.io/)
- [Official MFT Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/mftexplorer.txt)

Sources checked October 7, 2026. The documented workflow was reviewed; the GUI was not executed for this repository. The example paths describe a proposed lab, not observed evidence.
