# Set up a Zimmerman artifact-analysis lab

Checked October 7, 2026. These instructions describe a lab workflow; no Zimmerman binary was downloaded or run for this repository.

## Choose the tool and runtime

Start at the [author's download catalog](https://ericzimmerman.github.io/) and the [official documentation index](https://ericzimmerman.github.io/documentation/). Use the package for your analysis workstation and verify its publisher signature and hash. Record the actual executable version, hash, runtime, and help output before parsing.

The current catalog defaults its downloader to .NET 9. Its general runtime note and several individual download rows disagree, so use the selected package's requirements rather than assuming every program has both builds. GUI packages may require the Windows Desktop Runtime. Microsoft's [support policy](https://dotnet.microsoft.com/en-us/platform/support/policy) currently ends .NET 9 support on **November 10, 2026**. Recheck the vendor package and Microsoft's policy when using this guide after that date; installing a newer major runtime alone does not establish application compatibility.

Each walkthrough uses an example tool directory such as `C:\Tools\EZTools\PECmd`. Replace it with the directory you actually extracted. This is an example layout, not a promise about the downloader's folder structure. If a program is blocked, inspect the reported cause and follow the workstation's approved software process.

## Separate inputs and outputs

Use an acquired copy from an authorized lab or investigation. Copying a busy live file is not automatically a consistent forensic acquisition. Preserve acquisition notes, hashes, source paths, and relevant companion files such as Registry transaction logs or SQLite WAL/SHM files.

| Location | Purpose |
| --- | --- |
| `C:\Cases\LAB-001\evidence` | Acquired input copies, kept unchanged |
| `C:\Cases\LAB-001\working` | Disposable derivatives, including replayed hives |
| `C:\Cases\LAB-001\outputs` | A separate subdirectory for each tool and run |
| `C:\Cases\LAB-001\logs` | Tool versions, commands, diagnostics, and decisions |

The LAB-001 paths are illustrative. This repository does not supply a case image or pretend the example artifacts exist.

Before a run, fill in the [parse record](../../templates/dfir-parse-record.md). Record the precise command and chosen batch/map files. Hash those configurations as well as the input. Keep output apart from input; tools such as RLA create derived evidence, and mounting or acquisition tools have a different operating scope from offline parsers.

## Read results in context

Open the output without rewriting the original export. Keep source record identifiers and distinguish the timestamp's meaning from its display format. A formatting switch is not automatically a timezone conversion. Record any conversion you make, including how naive timestamps were interpreted.

Use a small known benign artifact to check the installed parser version before relying on its output. Document parser errors, missing companion files, record counts, and coverage gaps. An empty output is a result from that input and configuration; it does not prove the underlying activity never occurred.

The [offline CSV summarizer](../tools/ez-csv-summary.md) can record input hashes and normalized time bounds from a selected timestamp column. It does not acquire artifacts, replace the parser, or establish execution or attribution.

## Licensing and distribution

Follow each publisher's terms. This repository contains authored instructions and original Python utilities; it does not redistribute Zimmerman binaries or assume the entire suite is open source.

KAPE's [current official FAQ](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/50-Frequently-asked-questions.md) states that commercial use on third-party networks or paid engagements is no longer available from January 1, 2026. Its listed free uses include government, education, research, and internal company work. Read the current terms before selecting it for a task.
