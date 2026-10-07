# SrumECmd: examine application resource and network usage

**Question:** Which applications have recorded resource or network usage in the copied lab SRUM database?

Complete the [shared setup](../setup.md). Use an acquired or copied lab `SRUDB.dat` from the Windows SRU directory, retaining collected ESE companion files and acquisition context. This example places it at `C:\Cases\LAB-001\evidence\srum\SRUDB.dat`. Also retain a copied SOFTWARE hive from the same system and acquisition. Do not query or repair the live database for this exercise.

## Parse with the SOFTWARE hive

The author documents the SOFTWARE hive as optional but recommended for resolving information. Supplying it also makes that dependency explicit:

```powershell
& "C:\Tools\EZTools\SrumECmd\SrumECmd.exe" -f "C:\Cases\LAB-001\evidence\srum\SRUDB.dat" -r "C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE" --csv "C:\Cases\LAB-001\outputs\srumecmd"
```

Record the hashes of both inputs, the tool version, command, transcript, and generated filenames. Check parsing messages before reviewing tables. If the SOFTWARE hive is unavailable, label that gap; do not silently substitute a hive from another host.

## Compare relevant tables

Begin with application resource-use output and then network-usage output, checking the application identity, user-related identifiers, interval timestamp, and reported counts or byte totals. Confirm the column definitions and display timezone for the installed version before combining them with another timeline.

A recorded usage interval is not a packet capture. A byte total does not identify a destination or the contents transferred, and high outbound volume does not by itself establish exfiltration. Resource usage can support an application-activity lead without supplying its command line or proving malicious intent.

Keep records from different intervals separate until you have established what aggregation the table represents. A summed total should include its selected time range and any coverage gaps.

## Dirty databases, gaps, and next pivots

An ESE dirty-state or parsing error requires a separate recovery decision. Preserve the original database and logs, work only on additional copies, and document any recovery transformation and new hashes. This walkthrough intentionally does not supply a destructive repair command or claim recovery succeeded.

Missing rows can reflect collection timing, database retention, incomplete inputs, unsupported structures, or parsing errors. Do not promise a fixed retention window or infer that an application never ran.

Correlate application paths with execution evidence, endpoint network events, DNS/proxy logs, and file hashes. Use [EvtxECmd](evtxecmd.md) for acquired event-log context. If the question concerns destination or file content, obtain evidence that actually records it.

**Validation status:** Author CLI and official manual checked on 2026-10-07. SrumECmd was **not run**; no usage totals or exfiltration finding are claimed.

## Sources

- [Author README, CLI, and ESE notes](https://github.com/EricZimmerman/Srum)
- [Official SrumECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/srumecmd.txt)
