# ShellBags Explorer: inspect paths and shell items

ShellBags Explorer shows the shell items behind a reconstructed folder path. Use the [lab setup](../setup.md) with a copied user hive such as `C:\Cases\LAB-001\evidence\registry\user-lab\UsrClass.dat` and matching transaction logs when acquired. Record profile attribution, hash, acquisition time, and tool version. Keep acquired originals outside output locations.

## Load an offline hive

Menu names below follow the official manual and may vary by release.

1. Confirm the display timezone through Tools before loading a source. The documented default is UTC.
2. Use File to load an offline hive and select the copied UsrClass hive. The live Registry option examines the analysis machine instead.
3. Review the parsing summary and Messages window; retain errors and informational warnings.
4. Select a folder branch and its grid row. Record the absolute path, bag path, item type, and source hive.
5. Inspect Details and Hex for the selected item. Distinguish decoded item fields from the key's last-write timestamp.
6. Use File → Export → CSV and save under `C:\Cases\LAB-001\outputs\shellbags-explorer`. CSV exports available columns; Excel follows visible-column selections. Record filters and timezone choices.

## Read the item and its hierarchy

A reconstructed path describes folder-navigation artifacts in the profile. It is not an inventory of files the user saw and does not establish execution, copying, or exfiltration.

First/last explored fields, embedded created/modified/accessed fields, and Registry key last-write times have different meanings. Inspect the selected item and surrounding hierarchy before assigning a time to an action. A changed parent key's timestamp does not apply automatically to every child.

## Investigate partial paths and missing branches

Unknown GUIDs and extension-block messages can indicate interpretation limits. Retain the messages and inspect raw bytes when a path is incomplete. Blank timestamps may be expected for the item type.

Missing branches can also reflect the wrong user hive or an incomplete acquisition. Check NTUSER and UsrClass coverage and transaction-log availability. Use [SBECmd](sbecmd.md) for repeatable export across profiles. Correlate paths with LNK/Jump List records, removable-device evidence, and file-system records before reporting file access.

Official GUI documentation checked 2026-10-07. GUI not opened or tested; no screenshots or observed findings supplied.

## Sources

- [Author tool catalog](https://ericzimmerman.github.io/)
- [Official ShellBags Explorer manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/shellbagsexplorer.txt)
