# RLA: replay Registry logs into a derived hive

RLA applies Registry transactions and writes a derived hive for parsers that cannot replay logs themselves. Follow the [lab setup](../setup.md), retaining hashed acquisition originals unchanged. Use offline copies and an output directory outside evidence; do not point RLA at the active Windows Registry.

## Supply a matched hive and log set

Place `C:\Cases\LAB-001\evidence\registry\user-lab\NTUSER.DAT` with its acquired `NTUSER.DAT.LOG1` and `NTUSER.DAT.LOG2`. Preserve filenames and confirm the files belong to the same acquisition. Logs from another host or snapshot cannot substitute for missing inputs.

Record input hashes, acquisition relationships, starting hive state, and tool version. Select a fresh output directory:

```powershell
& "C:\Tools\EZTools\RLA\rla.exe" -f "C:\Cases\LAB-001\evidence\registry\user-lab\NTUSER.DAT" --out "C:\Cases\LAB-001\outputs\rla"
```

The current author source uses `-f`; older README examples sometimes show `--f`. Retain the transcript, including discovered logs, replay messages, warnings, and actual output paths.

The documented `--ca` default is true, so even a clean hive can be copied to output. An output file alone does not establish that replay occurred.

## Record what changed

Hash the result and retain an input-to-output manifest. Record which logs were selected and applied, along with errors or missing inputs. Label the result as a derived hive after replay and retain its hash separately from the original.

Compare relevant keys before and after replay when the difference affects a finding. Replay exposes the available transaction state; it does not recover every historical state or establish when a human performed an action.

## Investigate absent replay

No applied logs can mean the hive was already clean, logs were absent, filenames changed, or the acquisition set was inconsistent. Do not combine acquisitions to force a result. A copied hive is not proof of successful repair.

RLA may preserve paths or adjust profile-based names. Use the reported output location rather than assuming a filename. Pass the documented derivative to [Registry Explorer](registry-explorer.md) or [RECmd](recmd.md), retaining both replay and parser transcripts.

Manual, author README, and current input-switch source checked 2026-10-07. RLA not executed; no repaired hive supplied.

## Sources

- [Author README: RLA](https://github.com/EricZimmerman/RECmd#rla)
- [Author RLA source and option definitions](https://github.com/EricZimmerman/RECmd/blob/master/rla/Program.cs)
- [Official RLA manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/rla.txt)
