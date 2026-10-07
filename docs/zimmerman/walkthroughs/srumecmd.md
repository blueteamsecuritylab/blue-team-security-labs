# SrumECmd: examine application resource and network usage

SrumECmd parses recorded application usage from Windows SRUM. Follow the [lab setup](../setup.md) with a copied `SRUDB.dat` from the Windows SRU directory at `C:\Cases\LAB-001\evidence\srum\SRUDB.dat`. Retain acquired ESE companion files and acquisition context, plus a SOFTWARE hive from the same system and acquisition. Do not query or repair the live database.

## Supply the matching SOFTWARE hive

The SOFTWARE hive is documented as optional but recommended for resolving information:

```powershell
& "C:\Tools\EZTools\SrumECmd\SrumECmd.exe" -f "C:\Cases\LAB-001\evidence\srum\SRUDB.dat" -r "C:\Cases\LAB-001\evidence\registry\machine\SOFTWARE" --csv "C:\Cases\LAB-001\outputs\srumecmd"
```

Record both input hashes, tool version, command, transcript, and generated filenames. Review parsing messages before opening tables. If SOFTWARE is missing, document the gap; another host's hive is not a substitute.

## Compare resource and network intervals

Review application resource-use output alongside network-usage output. Check application identity, user-related identifiers, interval timestamps, and reported counts or byte totals. Confirm column definitions and display timezone before combining records with another timeline.

SRUM intervals do not supply packet-level traffic, destinations, or transferred content. High outbound volume alone does not establish exfiltration. Resource usage can support application-activity analysis without a command line or evidence of malicious intent.

Keep intervals separate until the table's aggregation is understood. Any summed total needs its selected time range and coverage gaps.

## Handle ESE errors and incomplete coverage

A dirty-state or parsing error requires a separate recovery decision. Preserve original databases and logs; recover only additional working copies and record transformations and resulting hashes. No repair procedure or successful recovery is supplied here.

Missing rows can reflect collection timing, retention, incomplete inputs, unsupported structures, or parsing errors. They do not establish that an application never ran, and retention should not be assumed to cover a fixed period.

Correlate application paths with execution evidence, endpoint network events, DNS/proxy logs, and file hashes. [EvtxECmd](evtxecmd.md) provides acquired event-log context. Destination and file-content claims require sources recording those details.

Author CLI and official manual checked 2026-10-07. SrumECmd not run; no usage totals or exfiltration findings supplied.

## Sources

- [Author README, CLI, and ESE notes](https://github.com/EricZimmerman/Srum)
- [Official SrumECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/srumecmd.txt)
