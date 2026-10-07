# RLA: create a documented hive after transaction-log replay

**Question:** Can matching Registry transaction logs supply a consistent derived hive for a parser that cannot replay them itself?

Read the [shared setup](../setup.md). RLA is a preparation step, not an artifact report. It applies Registry transactions and writes a new hive. Keep acquisition originals isolated, hashed, and unchanged. Never put the output directory inside the evidence directory or point the input at an active Windows Registry hive.

## Prepare one hive and its logs

Use the copied lab hive `C:\Cases\LAB-001\evidence\registry\user-lab\NTUSER.DAT` with its acquired, matching `NTUSER.DAT.LOG1` and `NTUSER.DAT.LOG2` in the same directory. Preserve those names. Logs from another snapshot or host are not substitutes.

Record the input hashes, acquisition relationship, tool version, and starting hive state. Choose a fresh output directory:

```powershell
& "C:\Tools\EZTools\RLA\rla.exe" -f "C:\Cases\LAB-001\evidence\registry\user-lab\NTUSER.DAT" --out "C:\Cases\LAB-001\outputs\rla"
```

The single-letter input switch is `-f`. The current author source confirms that spelling; some older README examples show `--f`. Save the entire console transcript, including discovered logs, replay messages, warnings, and actual output paths.

The documented default of `--ca` is true: a clean hive can also be copied to output. Therefore, an output file's existence alone does not prove that transactions were applied. Record what the transcript says happened.

## Track the transformation

Hash the resulting hive and retain an input-to-output manifest. Record whether logs were applied, which logs were selected, and any missing inputs or errors. Identify the output as a **derived hive after replay**, not the acquired original. The original and derived hashes should remain distinct entries in your notes.

Compare the relevant keys before and after replay if that difference matters to the investigation question. Replay makes the available transaction state usable; it does not recover every historical Registry state or establish when a human performed an action.

## Troubleshooting and next pivots

If no logs are applied, investigate whether the hive was already clean, logs were absent, filenames were altered, or the collected set was inconsistent. Do not force a positive result by mixing logs from different acquisitions. A successful copy is not a successful repair claim.

The utility may preserve paths or adjust profile-based names; inspect the reported output location rather than inventing a filename. Feed the documented derived hive into [Registry Explorer](registry-explorer.md) or [RECmd](recmd.md), retaining both the replay transcript and parser transcript.

**Validation status:** Manual, author README, and current input-switch source checked on 2026-10-07. RLA was **not executed** and no repaired hive is supplied.

## Sources

- [Author README: RLA](https://github.com/EricZimmerman/RECmd#rla)
- [Author RLA source and option definitions](https://github.com/EricZimmerman/RECmd/blob/master/rla/Program.cs)
- [Official RLA manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/rla.txt)
