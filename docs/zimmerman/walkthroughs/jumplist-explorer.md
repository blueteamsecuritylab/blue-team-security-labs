# JumpList Explorer: inspect destinations and embedded shortcuts

Use the GUI to trace a displayed Jump List entry to its source container, application identifier, and embedded shortcut.

## Acquire the user's destination folders

Complete [setup and evidence handling](../setup.md). Acquire authorized copies of the source profile's AutomaticDestinations and CustomDestinations folders under `AppData\Roaming\Microsoft\Windows\Recent`. Preserve original filenames, profile mapping, hashes, and collection time. Keep the acquired copies beneath `C:\Cases\LAB-001\evidence\recent` and prepare a separate export directory.

The viewer's parsing libraries have public repositories; the GUI itself is not described as open source. Use the current official distribution and record the displayed version.

## Load automatic and custom destinations

Launch the verified installation from PowerShell, adjusting the executable's location:

```powershell
& 'C:\Tools\EZTools\JumpListExplorer.exe'
```

Select the documented `File -> Load jump lists` control and choose the acquired destination files. Check that the displayed sources belong to LAB-001, not the workstation's live Recent collection. Consult the installed help if menu captions differ from the official manual's screenshot.

Inspect both automatic and custom destinations, keeping their types distinct. For each relevant item, review the source filename, AppID/application description, target path, and available destination/link details. Record each timestamp with its field label.

For a fictional `WorkshopPlan.txt` target, compare the visible entry with the embedded-link context. A normal editor session or pinned document can explain a match. Do not assume identical metadata is available in both Jump List formats.

## Search entries and export embedded LNK files

The top-right magnifying glass opens the documented search bar. Search for the document name, then check the complete path and source container. Record the active search with screenshots so the filter remains clear.

Use the documented `File -> Export -> Lnk files` control to export embedded shortcuts into `C:\Cases\LAB-001\output\jumplist-links`. Retain a mapping from each export to its original destination and entry. Inspect exported copies with [LECmd](lecmd.md); use [JLECmd](jlecmd.md) for a reproducible CSV comparison. Never follow a link's target to test it.

A destination reference supports application/file interaction context. It does not prove contents were read or transferred, or identify the person using the account.

## Empty views and load errors

For an empty view, check the selected evidence files, format, source paths, and load errors. Clear the search before concluding that no entries exist. Record failed loads. Use the shared setup and current catalog guidance for startup or scaling problems; leave evidence unchanged.

## Sources and validation

Sources checked 2026-10-07:

- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/jumplistexplorer.txt)
- [Official menu screenshot](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/resources/jumplistexplorer/JumpListExplorerExportLnkFiles.jpg)
- [Author's current catalog](https://ericzimmerman.github.io/)

Documentation review only; the GUI steps have not been run.
