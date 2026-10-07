# RECmd: turn copied Registry hives into reviewable leads

**Question:** Which recorded Registry settings or user artifacts help explain the lab activity?

Complete the [shared setup](../setup.md). Place copied lab hives under `C:\Cases\LAB-001\evidence\registry`, preserving the user and host directory structure. Include matching transaction logs when acquired. Record which hives were collected; a user hive and a machine hive answer different questions.

## Use a named batch definition

RECmd batch export requires a batch file and an output directory. The author repository currently identifies DFIRBatch as the maintained successor to the older Kroll batch. Retain the exact batch file used, its hash, and the tool version.

```powershell
& "C:\Tools\EZTools\RECmd\RECmd.exe" -d "C:\Cases\LAB-001\evidence\registry" --bn "C:\Tools\EZTools\RECmd\BatchExamples\DFIRBatch.reb" --csv "C:\Cases\LAB-001\outputs\recmd"
```

Check that the named batch exists in your installed package before running. Save the console transcript. Read the batch definitions relevant to your question: they state the hive type, key path, value selection, recursion, and any plugin interpretation. Do not assume the batch exhaustively examines every Registry location.

For a focused follow-up, use a documented key query against one copied SOFTWARE hive:

```powershell
& "C:\Tools\EZTools\RECmd\RECmd.exe" -f "C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE" --kn "Microsoft\Windows\CurrentVersion\Run"
```

This prints key details; it is a separate operation from the batch CSV export.

## Review the value before naming the behavior

For each lead, retain the source hive, key path, value name, value data, and parsing notes. Associate user hives with their acquired profile path and SID evidence, not just an output filename. Compare an autorun value with the referenced file, account context, and independent execution telemetry. Configuration can exist without successful execution.

Key last-write timestamps describe changes to a key; they are not an execution time for every value beneath it. Recovered or deleted records must remain labeled as such.

## Limits and troubleshooting

A dirty-hive warning requires attention to matching transaction logs and replay behavior. Do not silence it by discarding logs. If an older parser needs a derived hive, use the [RLA workflow](rla.md) and keep the derivation separate.

Missing output can reflect an absent hive, a batch mismatch, missing plugins, or no matching keys. Check the transcript and batch definition before interpreting absence. Inspect a disputed key in [Registry Explorer](registry-explorer.md); both tools share a parsing foundation, so their agreement is useful but not an independent engine validation.

**Validation status:** Author documentation and examples checked on 2026-10-07. RECmd was **not run**; no lab results are supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/RECmd)
- [Current DFIRBatch definition](https://github.com/EricZimmerman/RECmd/blob/master/BatchExamples/DFIRBatch.reb)
- [Official RECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/recmd.txt)
