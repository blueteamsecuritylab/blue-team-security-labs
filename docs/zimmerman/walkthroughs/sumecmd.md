# SumECmd: examine Windows Server User Access Logging

**Question:** What account, client, role, and historical name-address information does this acquired server's User Access Logging contain?

Read the [shared setup](../setup.md). Use copied lab data from `C:\Windows\System32\LogFiles\SUM`, staged at `C:\Cases\LAB-001\evidence\sum`. Preserve the whole acquired database set and related files, rather than selecting a single convenient MDB. Record the server identity, enabled roles, acquisition time, and input hashes.

## Parse the copied directory

SumECmd looks for databases such as SystemIdentity and Current within the directory. Its name and input are distinct from SrumECmd and SRUDB.dat.

```powershell
& "C:\Tools\EZTools\SumECmd\SumECmd.exe" -d "C:\Cases\LAB-001\evidence\sum" --csv "C:\Cases\LAB-001\outputs\sumecmd"
```

Save the installed version, command, console transcript, warnings, and generated file list. The documented day-detail option is enabled by default; verify the installed help before changing it. Begin by checking summary tables for the database set and period represented.

## Read client activity with server context

Inspect client and role-access tables together. Preserve the account identifiers, client addresses, first/last recorded values, counters, and the role or server context provided by the output. These are service-usage records in the acquired data, not a complete replacement for Security event logs or a precise list of every interactive logon.

If DNS-information output is present, use it as historical context for name-address associations. Check its dates before assigning a hostname to an IP. DHCP reassignment, name changes, and aliases can make a present-day lookup misleading.

Do not treat a role's existence as proof that a particular account accessed it. Likewise, a first or last recorded value bounds the retained information; it does not establish the first or last activity across the whole environment.

## Missing tables and database errors

Role configuration affects what data can appear. A server may have limited UAL data, and a missing DNS table does not prove that no DNS activity occurred. Review collection coverage, enabled roles, and summary periods before drawing a negative conclusion.

SUM uses ESE databases. If a dirty-state or parse error occurs, preserve the originals and matching companion files. Any recovery belongs on a separate working copy with recorded commands and resulting hashes; this walkthrough makes no repair-success claim.

Pivot from a candidate account/client pair into [acquired event logs](evtxecmd.md), identity telemetry, and relevant service logs for the same server and time range. Describe which source supplies each part of the timeline.

**Validation status:** Author CLI and official manual checked on 2026-10-07. SumECmd was **not run**; no account activity or name-address mappings are supplied.

## Sources

- [Author README and CLI](https://github.com/EricZimmerman/Sum)
- [Official SumECmd manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sumecmd.txt)
