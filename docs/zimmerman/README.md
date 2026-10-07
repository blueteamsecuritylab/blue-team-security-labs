# Zimmerman tool walkthroughs

Practical walkthroughs for all **31 programs** listed in [Eric Zimmerman's official catalog](https://ericzimmerman.github.io/) when checked on October 7, 2026. This scope covers the download catalog, including collection and supporting programs; it does not claim to cover every library or repository under the author's account.

Start with [lab setup and evidence handling](setup.md), then choose a tool for the artifact and question. Each guide includes copied-input paths, a documented command or GUI workflow, output review, limitations, and follow-up checks.

**Validation:** the official catalog, manuals, and relevant source help were reviewed. Zimmerman parser and GUI runs were not performed in this session. Example paths and commands are lab templates; no example result is presented as an observed case finding. Capture the installed tool's help and version before using a template.

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

## Original companion tools

- [EZ CSV Summary](../tools/ez-csv-summary.md): summarize one chosen timestamp column with explicit timezone rules, input hashes, counts, and observed time bounds.
- [Static file triage](../../malware-analysis/README.md): inspect a local file's bytes and hashes without running it.

These tools do not replace artifact acquisition or a parser. They do not establish user attribution, malware behavior, or complete event coverage.

## Source record

[catalog.json](catalog.json) records the checked catalog rows, official manual links, observed source commits, runtime discrepancies, and validation status. Program versions and terms can change. The [official manual repository](https://github.com/EZToolsManuals/EZToolsManuals) and [KAPE documentation](https://github.com/EricZimmerman/KapeDocs) remain the upstream references.

The tutorials and Python utilities are maintained by Blue Team Security. They are independent of Eric Zimmerman and the upstream publishers. No third-party tool binaries or real incident datasets are distributed here.
