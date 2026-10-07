# EvtxECmd: start an event-log investigation

**Question:** What did the acquired Windows logs record around a lab event, and which records need a closer look?

Follow the [shared setup](../setup.md) first. Use copied or acquired lab EVTX files under `C:\Cases\LAB-001\evidence\event-logs`. Keep the original collection intact and retain filenames, hashes, acquisition time, host identity, and log-channel coverage. This walkthrough processes a copied Security log; it does not collect a live host.

## Parse one log before expanding scope

Run these commands in PowerShell after adjusting the installed tool path:

```powershell
& "C:\Tools\EZTools\EvtxECmd\EvtxECmd.exe" -f "C:\Cases\LAB-001\evidence\event-logs\Security.evtx" --csv "C:\Cases\LAB-001\outputs\evtxecmd" --csvf "security.csv"
& "C:\Tools\EZTools\EvtxECmd\EvtxECmd.exe" -f "C:\Cases\LAB-001\evidence\event-logs\Security.evtx" --xml "C:\Cases\LAB-001\outputs\evtxecmd\xml"
```

Save the console transcript with the command, tool version, warnings, and hashes of the maps used. The first command gives a sortable table. The second preserves an XML representation for examining the original event fields behind a mapped column. A directory run uses `-d` instead of `-f`; expand only after checking the first file.

## Read a record in its channel

Start with source file, computer, channel, provider, event ID, record ID, and creation time. Then inspect the payload. Event IDs need provider and channel context: a number alone does not describe an action. Mapped payload columns are selected fields, not the entire event.

Filter the exported table to your lab time window and return to the corresponding XML for each lead. Record the timezone used for display. If you later use `--sd` or `--ed`, the documented bounds are UTC; keep an unfiltered baseline.

## Limits, troubleshooting, and next pivots

No rows can mean absent auditing, retention loss, incomplete collection, a filter mistake, or a parser problem. It does not establish that the activity never happened. EvtxECmd processes EVTX, not legacy EVT files. Review parse errors and map availability before treating blank mapped fields as missing raw data.

A time-discrepancy warning is a lead to investigate, not proof of tampering. Check raw timestamps and host-clock evidence. Follow an account or process lead into adjacent event channels, endpoint telemetry, and the [RECmd walkthrough](recmd.md), keeping identifiers and time windows explicit.

**Validation status:** Documentation and command syntax checked on 2026-10-07. The parser was **not run** for this walkthrough; no observed output or detection result is claimed.

## Sources

- [Author repository and CLI](https://github.com/EricZimmerman/evtx)
- [Official EvtxECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/evtxecmd.txt)
- [Author map definitions](https://github.com/EricZimmerman/evtx/tree/master/evtx/Maps)
