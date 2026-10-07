# JumpList Explorer: inspect one destination and its embedded links

**Question:** How does a Jump List's visible entry relate to its source container, application identifier, and embedded shortcut?

## Prepare the input

Complete [setup and evidence handling](../setup.md). Acquire authorized copies of the source profile's AutomaticDestinations and CustomDestinations folders under `AppData\Roaming\Microsoft\Windows\Recent`. Preserve original filenames, profile mapping, hashes, and collection time. Place working files beneath `C:\Cases\LAB-001\evidence\recent` and prepare a separate export directory.

JumpList Explorer is the author's GUI viewer. Its underlying parsing libraries have public repositories, but the GUI itself is not described as open source. Use the current official distribution and record the displayed version.

## Load and inspect

Launch the approved installation from PowerShell; adjust the executable's location to match your verified installation:

```powershell
& 'C:\Tools\EZTools\JumpListExplorer.exe'
```

The official manual's screenshot shows `File -> Load jump lists`. Select that control and choose the acquired destination files, rather than your workstation's live Recent collection. Confirm the displayed sources belong to LAB-001 before interpreting any rows. Menu captions may change; consult the installed help if the current build differs.

Inspect an automatic destination and then a custom destination. Keep their types distinguishable. Select the relevant item and review its source filename, AppID/application description, target path, and available destination/link details. Record the field labels attached to timestamps rather than transcribing an unlabeled date.

For a fictional `WorkshopPlan.txt` target, compare the visible entry with the embedded-link context. A normal editor session or pinned document can explain a match. Do not assume identical metadata is available in both Jump List formats.

## Search, export, and pivot

The manual documents the top-right magnifying glass as the control that reveals the search bar. Search for the document name, then check the complete path and source container. Record the active search so a screenshot does not suggest an unfiltered collection.

Use the documented `File -> Export -> Lnk files` control to export embedded shortcuts into `C:\Cases\LAB-001\output\jumplist-links`. Retain a mapping from each export to its original destination and entry. Inspect exported copies with [LECmd](lecmd.md); use [JLECmd](jlecmd.md) for a reproducible CSV comparison. Never follow a link's target to test it.

A destination reference supports application/file interaction context. It does not prove contents were read or transferred, or identify the person using the account.

## Troubleshoot

For an empty view, verify the selected evidence files, format, source paths, and any load errors. Clear the search before declaring no entries exist. Keep a failed load in the notes. For startup or scaling problems, follow shared setup and current catalog guidance rather than changing evidence.

## Sources and validation

Checked **2026-10-07**:

- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/jumplistexplorer.txt)
- [Official menu screenshot](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/resources/jumplistexplorer/JumpListExplorerExportLnkFiles.jpg)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
