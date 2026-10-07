# Registry Explorer: inspect the key behind a parsed lead

**Question:** What does a copied Registry hive actually contain at the location reported by an automated parser?

Use the [shared setup](../setup.md). Begin with a copied lab hive, such as `C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE`, and its matching transaction logs if available. Preserve the acquired originals. Note the host, source path, hash, tool version, and display timezone before examining data.

## Load and inspect an offline hive

These steps follow the official manual; labels can vary with the installed release.

1. Start Registry Explorer. Choose **File → Load offline hive**, then select the copied SOFTWARE hive. The documented alternate method is dragging an offline hive onto the interface.
2. Wait for loading to finish. Check the displayed source path and messages. If the hive is dirty, record the log-replay decision. If saving an updated hive is offered, choose a new derived-output location outside evidence.
3. Expand the hive tree and navigate to `Microsoft\Windows\CurrentVersion\Run`. Select the key and inspect the value names, types, data, and key last-write time.
4. For a wider check, open **Tools → Find**. Enter a lab filename or path fragment, choose the relevant search areas, and run the search. Treat results in value slack or recovered records separately from active values.
5. Record the full hive and key paths before exporting. The manual documents value-data export from a value's context menu and values-table export from a key's context menu. Save under `C:\Cases\LAB-001\outputs\registry-explorer`, noting any visible-column or filter choices.

## Interpret the setting in context

A Run value is evidence of configured startup behavior in that hive. It does not, by itself, show that the program executed successfully, which person set it, or whether its target bytes were malicious. Follow the referenced executable into file hashes, signature information, process telemetry, and event logs.

The key's last-write time belongs to the key, not to each value individually. A search hit can be an unrelated path fragment; read the value type and surrounding keys before assigning meaning.

## Troubleshooting and next pivots

Check that you loaded the intended hive type and user or machine context. Dirty hives without matching logs can omit recent changes. Search filters, hidden columns, and recovery settings can alter what is visible; include those settings in the notes.

Do not import an exported REG file into your analysis machine. It is a representation for examination, not an installation step. For repeatable processing across copied hives, continue with [RECmd](recmd.md). Where replay is required for another parser, use [RLA](rla.md) and identify the resulting hive as derived evidence.

**Validation status:** Official GUI documentation checked on 2026-10-07. The GUI was **not opened or tested** for this walkthrough; no screenshots or observed findings are supplied.

## Sources

- [Author tool catalog](https://ericzimmerman.github.io/)
- [Official Registry Explorer manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/registryexplorer.txt)
