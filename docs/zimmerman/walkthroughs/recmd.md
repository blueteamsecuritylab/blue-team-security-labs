# RECmd: batch Registry extraction and key inspection

RECmd extracts selected Registry artifacts from offline hives and supports direct key queries. Use the [lab setup](../setup.md) with copied hives under `C:\Cases\LAB-001\evidence\registry`. Preserve host and profile directories, matching transaction logs, and the list of collected hives. Machine and user hives cover different settings and activity.

## Export with DFIRBatch

Batch CSV export requires both `--bn` and an output directory. The author repository identifies DFIRBatch as the maintained successor to the Kroll batch. Confirm the file exists in the installed package and retain its hash and the tool version.

```powershell
& "C:\Tools\EZTools\RECmd\RECmd.exe" -d "C:\Cases\LAB-001\evidence\registry" --bn "C:\Tools\EZTools\RECmd\BatchExamples\DFIRBatch.reb" --csv "C:\Cases\LAB-001\outputs\recmd"
```

Save the console transcript. Read the relevant batch entries: each specifies a hive type, key path, value selection, recursion, and any plugin interpretation. The batch does not examine every Registry location.

To inspect startup configuration in one copied SOFTWARE hive:

```powershell
& "C:\Tools\EZTools\RECmd\RECmd.exe" -f "C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE" --kn "Microsoft\Windows\CurrentVersion\Run"
```

This prints key details separately from the batch CSV export.

## Interpret values and last-write times

Record the source hive, key path, value name, data, and parsing notes. Attribute user hives through acquired profile paths and SID evidence rather than output filenames.

For an autorun value, examine the referenced file, account context, and independent execution telemetry. Configured startup behavior does not establish successful execution. A key's last-write timestamp records a key change, not an execution time for each value. Keep recovered or deleted records labeled.

## Resolve dirty hives and missing output

Review dirty-hive warnings against matching transaction logs and replay behavior; discarding logs can omit recent data. If another parser requires a derived hive, use [RLA](rla.md) and retain the derivation separately.

Missing output may reflect an absent hive, batch mismatch, missing plugin, or no matching keys. Check the transcript and batch definition. Inspect disputed keys in [Registry Explorer](registry-explorer.md). It shares RECmd's parsing foundation, so agreement is not independent engine validation.

Author documentation and examples checked 2026-10-07. RECmd not run; no lab results supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/RECmd)
- [Current DFIRBatch definition](https://github.com/EricZimmerman/RECmd/blob/master/BatchExamples/DFIRBatch.reb)
- [Official RECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/recmd.txt)
