# SumECmd: inspect Windows Server User Access Logging

SumECmd parses Windows Server User Access Logging (UAL). Follow the [lab setup](../setup.md) with copied `C:\Windows\System32\LogFiles\SUM` data under `C:\Cases\LAB-001\evidence\sum`. Preserve the whole acquired database set and related files. Record server identity, enabled roles, acquisition time, and input hashes.

## Parse the SUM database set

The directory scan looks for databases such as SystemIdentity and Current. SUM's databases differ from SRUM's SRUDB.dat and require SumECmd rather than SrumECmd.

```powershell
& "C:\Tools\EZTools\SumECmd\SumECmd.exe" -d "C:\Cases\LAB-001\evidence\sum" --csv "C:\Cases\LAB-001\outputs\sumecmd"
```

Retain the version, command, transcript, warnings, and generated file list. Day-level detail is documented as enabled by default; check installed help before changing it. Read summary tables first to establish the database set and represented period.

## Correlate clients, roles, and historical addresses

Inspect client and role-access tables together. Retain account identifiers, client addresses, first/last recorded values, counters, and server or role context. UAL service-usage records do not replace Security logs or enumerate every interactive logon.

Where DNS-information output exists, check the dates before associating a hostname with an address. DHCP reassignment, name changes, and aliases can make present-day resolution misleading.

A configured role does not establish that a particular account accessed it. First and last recorded values bound retained information, not all activity across the environment.

## Check role coverage and database errors

Server roles affect available data. Limited UAL coverage or a missing DNS table does not establish an absence of DNS activity. Review collection coverage, enabled roles, and summary periods before drawing that conclusion.

SUM uses ESE databases. Preserve originals and matching companion files after a dirty-state or parse error. Any recovery must use a separate working copy, with recorded commands and resulting hashes. No successful repair is claimed.

Correlate candidate account/client pairs with [acquired event logs](evtxecmd.md), identity telemetry, and service logs from the same server and time range. Identify the source supporting each timeline entry.

Author CLI and official manual checked 2026-10-07. SumECmd not run; no account activity or name-address mappings supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/Sum)
- [Official SumECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sumecmd.txt)
