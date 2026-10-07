# Registry Explorer: inspect offline Registry keys

Registry Explorer exposes keys and values behind an automated Registry finding. Use the [lab setup](../setup.md) with a copied hive such as `C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE` and matching transaction logs where available. Preserve acquired originals and record the host, source path, hash, tool version, and display timezone.

## Load the hive and inspect startup configuration

Menu names below follow the official manual and may vary by release.

1. Choose File → Load offline hive and select the copied SOFTWARE hive. Dragging an offline hive onto the interface is also documented.
2. Wait for loading to finish and check the source path and messages. For a dirty hive, record the replay decision. Save any updated hive outside the evidence directory as a derivative.
3. Navigate to `Microsoft\Windows\CurrentVersion\Run` and inspect value names, types, data, and the key's last-write time.
4. Use Tools → Find to search a filename or path fragment. Select the relevant search areas. Distinguish active values from recovered records and value-slack hits.
5. Record the full hive and key paths before exporting. A value's context menu exports its data; a key's context menu exports the values table. Save under `C:\Cases\LAB-001\outputs\registry-explorer` and note visible columns and filters.

## Test an autorun interpretation

A Run value records startup configuration in that hive. It does not establish successful execution, who set it, or whether the target file was malicious. Examine the referenced file's hash and signature, then correlate process telemetry and event logs.

Last-write belongs to the key, not each value. A path-fragment search may return unrelated data; inspect the value type and surrounding keys.

## Account for hidden or missing data

Confirm the intended hive type and user or machine context. Dirty hives without matching logs can omit recent changes. Record search filters, hidden columns, and recovery settings because they affect the displayed data.

Keep exported REG files for examination; importing one changes the analysis machine's Registry. Use [RECmd](recmd.md) for repeatable extraction across copied hives or [RLA](rla.md) when another parser needs replayed data. Identify a replayed hive as derived evidence.

Official GUI documentation checked 2026-10-07. GUI not opened or tested; no screenshots or observed findings supplied.

## Sources

- [Author tool catalog](https://ericzimmerman.github.io/)
- [Official Registry Explorer manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/registryexplorer.txt)
