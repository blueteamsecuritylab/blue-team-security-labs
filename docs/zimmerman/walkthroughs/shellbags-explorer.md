# ShellBags Explorer: examine one folder-navigation lead

**Question:** What underlying shell item supports a path reported in an offline user's ShellBags?

Complete the [shared setup](../setup.md). Use a copied lab user hive such as `C:\Cases\LAB-001\evidence\registry\user-lab\UsrClass.dat`, together with matching transaction logs when acquired. Record the profile relationship, hash, acquisition time, and tool version. Keep the acquired originals outside output locations.

## Load the hive and inspect the item

The following workflow is documented in the official manual. Check the installed release's labels before following it.

1. Start ShellBags Explorer. Use the **Tools** menu's timezone option to confirm the display zone before loading a source. The manual documents UTC as the default.
2. Use the **File** menu to load an **offline hive**, then choose the copied UsrClass hive. Avoid choosing the live Registry when your question concerns an acquired system.
3. Check the parsing summary and Messages window. Retain errors and informational warnings with the review notes.
4. Select a folder branch in the tree, then inspect the corresponding grid row. Record its absolute path, bag path, item type, and source hive.
5. Examine the **Details** and **Hex** views for that selected item. Separate fields decoded from the shell item from the key's last-write timestamp.
6. Export through **File → Export → CSV** to `C:\Cases\LAB-001\outputs\shellbags-explorer`. The manual documents CSV export of available columns; Excel export follows the visible-column selection. Note any filters and timezone choices alongside the export.

## Keep the inference narrow

A reconstructed path is a lead about folder-navigation artifacts in that profile. It is not an inventory of all files the user saw. It also does not establish file execution, copying, or exfiltration.

First/last explored values, embedded created/modified/accessed values, and Registry key last-write times have different meanings. Inspect the selected item and surrounding hierarchy before making a time claim. A recent key timestamp can reflect a change to ShellBag state; it should not be assigned indiscriminately to all children.

## Troubleshooting and next pivots

Unknown GUIDs or extension-block messages can indicate limitations in interpretation. Save those messages and inspect the raw item rather than silently accepting a partial path. Blank timestamp fields may be expected for an item type.

A missing branch can also reflect an incomplete acquisition or the wrong user hive. Check NTUSER and UsrClass coverage and transaction-log availability. For repeatable export across several copied profiles, use [SBECmd](sbecmd.md). Correlate a path with LNK/Jump List records, removable-device evidence, and file-system records before describing a file-access event.

**Validation status:** Official GUI documentation checked on 2026-10-07. ShellBags Explorer was **not opened or tested**; no screenshots or observed findings are supplied.

## Sources

- [Author tool catalog](https://ericzimmerman.github.io/)
- [Official ShellBags Explorer manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/shellbagsexplorer.txt)
