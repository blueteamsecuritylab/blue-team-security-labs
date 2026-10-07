# Zimmerman tool walkthroughs

[Repository home](../../README.md) · [Lab setup](setup.md) · [Parse record](../../templates/dfir-parse-record.md)

Guides for the 31 programs in [Eric Zimmerman's download catalog](https://ericzimmerman.github.io/), grouped by the artifact they examine. Each guide covers inputs, commands or GUI steps, output fields, common misreadings, and related evidence.

Start with [lab setup](setup.md), then choose an artifact below.

[Caches](#execution-and-compatibility-caches) · [Files](#file-inspection) · [Logs](#event-and-web-logs) · [Viewers](#graphical-viewers) · [User activity](#user-activity) · [NTFS](#ntfs-metadata) · [Registry](#registry-processing) · [Databases](#databases-and-resource-usage) · [Collection](#collection-and-supporting-tools)

## Execution and compatibility caches

| Tool | Interface | Starting point |
| --- | --- | --- |
| [AmcacheParser](walkthroughs/amcacheparser.md) | CLI | Amcache.hve |
| [AppCompatCacheParser](walkthroughs/appcompatcacheparser.md) | CLI | SYSTEM hive / AppCompatCache |
| [PECmd](walkthroughs/pecmd.md) | CLI | Windows Prefetch .pf files |
| [RecentFileCacheParser](walkthroughs/recentfilecacheparser.md) | CLI | RecentFileCache.bcf |

## File inspection

| Tool | Interface | Starting point |
| --- | --- | --- |
| [bstrings](walkthroughs/bstrings.md) | CLI | File bytes; ASCII/code-page and Unicode strings |
| [Hasher](walkthroughs/hasher.md) | GUI | Single files or directories |

## Event and web logs

| Tool | Interface | Starting point |
| --- | --- | --- |
| [EvtxECmd](walkthroughs/evtxecmd.md) | CLI | Windows .evtx files |
| [iisGeoLocate](walkthroughs/iisgeolocate.md) | CLI | IIS .log files |

## Graphical viewers

| Tool | Interface | Starting point |
| --- | --- | --- |
| [EZViewer](walkthroughs/ezviewer.md) | GUI | Supported office/document/text formats; other bytes via hex |
| [JumpList Explorer](walkthroughs/jumplist-explorer.md) | GUI | Automatic and Custom Destinations Jump Lists |
| [MFTExplorer](walkthroughs/mft-explorer.md) | GUI | Small $MFT files |
| [Registry Explorer](walkthroughs/registry-explorer.md) | GUI | Registry hives, transaction logs, plugins/bookmarks |
| [SDB Explorer](walkthroughs/sdb-explorer.md) | GUI | Application compatibility/shim .sdb databases |
| [ShellBags Explorer](walkthroughs/shellbags-explorer.md) | GUI | ShellBag structures in user Registry hives |
| [Timeline Explorer](walkthroughs/timeline-explorer.md) | GUI | CSV, TSV, XLSX, TXT with applicable plugins |

## User activity

| Tool | Interface | Starting point |
| --- | --- | --- |
| [JLECmd](walkthroughs/jlecmd.md) | CLI | *.automaticDestinations-ms and *.customDestinations-ms |
| [LECmd](walkthroughs/lecmd.md) | CLI | .lnk shortcut files |
| [RBCmd](walkthroughs/rbcmd.md) | CLI | Recycle Bin INFO2 and $I metadata |
| [SBECmd](walkthroughs/sbecmd.md) | CLI | NTUSER.DAT and UsrClass.dat user hives |

## NTFS metadata

| Tool | Interface | Starting point |
| --- | --- | --- |
| [MFTECmd](walkthroughs/mftecmd.md) | CLI | $MFT, $J, $Boot, $SDS, $I30 |

## Registry processing

| Tool | Interface | Starting point |
| --- | --- | --- |
| [RECmd](walkthroughs/recmd.md) | CLI | Offline Registry hives and adjacent transaction logs |
| [RLA](walkthroughs/rla.md) | CLI | Registry hives plus transaction logs |

## Databases and resource usage

| Tool | Interface | Starting point |
| --- | --- | --- |
| [SQLECmd](walkthroughs/sqlecmd.md) | CLI | SQLite files with matching maps |
| [SrumECmd](walkthroughs/srumecmd.md) | CLI | SRUDB.dat; optional SOFTWARE hive |
| [SumECmd](walkthroughs/sumecmd.md) | CLI | SUM/User Access Logging .mdb directory |
| [WxTCmd](walkthroughs/wxtcmd.md) | CLI | Windows Timeline ActivitiesCache.db |

## Collection and supporting tools

| Tool | Interface | Starting point |
| --- | --- | --- |
| [VSCMount](walkthroughs/vscmount.md) | CLI | Available Volume Shadow Copies on a drive |
| [Get-ZimmermanTools](walkthroughs/get-zimmerman-tools.md) | PowerShell | Official distribution catalog and local download-state CSV |
| [KAPE](walkthroughs/kape.md) | CLI and GUI (gkape) | Configured Targets; configured Modules and external binaries |
| [TimeApp](walkthroughs/timeapp.md) | GUI | Workstation local/UTC clock; stopwatch/countdown; optional public IP |
| [XWFIM](walkthroughs/xwfim.md) | GUI | Authorized X-Ways installation |

## Companion utilities

- [EZ CSV Summary](../tools/ez-csv-summary.md): input SHA-256, timestamp counts, and UTC bounds for one selected CSV column.
- [Static file triage](../../malware-analysis/README.md): byte observations and hashes for a local file.

Both utilities inspect supplied data. Acquisition, artifact parsing, and attribution require separate evidence and tools.

## References and review

Catalog, manual, and source-help review: October 7, 2026. Parser and GUI runs have not been performed for these guides. Commands use illustrative lab paths; test the installed version against a known benign artifact.

[catalog.json](catalog.json) records tool versions, manual links, source commits, runtime discrepancies, and review status. Check current packages and terms in the [official manuals](https://github.com/EZToolsManuals/EZToolsManuals) and [KAPE documentation](https://github.com/EricZimmerman/KapeDocs).

These are independent Blue Team Security tutorials. Upstream publishers supply and license their binaries.
