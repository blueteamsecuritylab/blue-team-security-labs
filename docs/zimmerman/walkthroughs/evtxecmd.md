# EvtxECmd: export and inspect Windows event logs

EvtxECmd exports acquired Windows event logs to tables and structured records. This example examines a copied Security log; it performs no live collection.

Use the [lab setup](../setup.md) and place copied EVTX files under `C:\Cases\LAB-001\evidence\event-logs`. Retain the original files, hashes, acquisition time, host identity, and collected channels.

## Export CSV and XML

Adjust the installed tool path, then run in PowerShell:

```powershell
& "C:\Tools\EZTools\EvtxECmd\EvtxECmd.exe" -f "C:\Cases\LAB-001\evidence\event-logs\Security.evtx" --csv "C:\Cases\LAB-001\outputs\evtxecmd" --csvf "security.csv"
& "C:\Tools\EZTools\EvtxECmd\EvtxECmd.exe" -f "C:\Cases\LAB-001\evidence\event-logs\Security.evtx" --xml "C:\Cases\LAB-001\outputs\evtxecmd\xml"
```

The CSV provides a sortable table; the XML exposes event fields behind mapped columns. Save the command, tool version, map hashes, and console warnings. A directory run uses `-d` instead of `-f`; check one file's output before expanding.

## Match each row to its event

Read the source file, computer, channel, provider, event ID, record ID, and creation time before interpreting the payload. An event ID needs its provider and channel. Mapped payload columns select fields from the event; they do not replace the full payload.

Filter the table to the lab time window and inspect the corresponding XML for each lead. Record the display timezone. The documented `--sd` and `--ed` filters use UTC bounds; retain an unfiltered export.

## Check missing records and clock warnings

An empty result can reflect absent auditing, retention loss, incomplete collection, filtering, or a parser error. It does not establish that the activity never occurred. EvtxECmd handles EVTX, not legacy EVT. Check parse errors and maps before treating a blank mapped field as absent raw data.

A time-discrepancy warning alone does not establish tampering. Compare raw timestamps with host-clock evidence. Correlate an account or process with adjacent event channels, endpoint telemetry, and [Registry artifacts](recmd.md), retaining the identifiers and time range used.

Documentation and command syntax checked 2026-10-07. Parser not run; no observed output or detection results supplied.

## Sources

- [Author repository and CLI](https://github.com/EricZimmerman/evtx)
- [Official EvtxECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/evtxecmd.txt)
- [Author map definitions](https://github.com/EricZimmerman/evtx/tree/master/evtx/Maps)
