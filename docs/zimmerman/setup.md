# Lab setup

[All walkthroughs](README.md) · [Parse record](../../templates/dfir-parse-record.md)

## Tool packages and runtimes

Download from the [author's catalog](https://ericzimmerman.github.io/) and read the [tool documentation](https://ericzimmerman.github.io/documentation/). Check the package's hash and any publisher signature, then record the executable version, hash, runtime, and help output.

The catalog's downloader defaults to .NET 9. Its general runtime note conflicts with some individual rows; use the selected package's requirements. GUI tools may need the Windows Desktop Runtime. Microsoft's [support policy](https://dotnet.microsoft.com/en-us/platform/support/policy) ends .NET 9 support on November 10, 2026. Check the current package and policy after that date: a newer major runtime alone does not establish compatibility.

Guide commands use example directories such as `C:\Tools\EZTools\PECmd`. Substitute your extracted package path; the downloader may arrange directories differently. If Windows blocks a tool, inspect the cause and follow the workstation's approved software process.

## Case directories

Use a consistent acquired copy, with source paths, hashes, and acquisition notes. Preserve relevant Registry transaction logs and SQLite WAL/SHM files. Copying a busy live file can leave an inconsistent set.

| Location | Contents |
| --- | --- |
| `C:\Cases\LAB-001\evidence` | Acquired copies, kept unchanged |
| `C:\Cases\LAB-001\working` | Disposable copies and derivatives, including replayed hives |
| `C:\Cases\LAB-001\outputs` | Separate directories for each tool and run |
| `C:\Cases\LAB-001\logs` | Versions, commands, diagnostics, and analysis decisions |

LAB-001 is an example layout; supply your own authorized lab artifacts. Record the exact command and batch/map hashes in the [parse record](../../templates/dfir-parse-record.md). Keep outputs separate from inputs. RLA produces derived hives; mounting and acquisition tools also have a different operating scope from offline parsers.

## Output review

Retain the original export and source record identifiers. Record timestamp semantics, display zones, and any conversions. A formatting switch may change presentation without converting the timezone.

Check the installed parser with a known benign artifact. Save errors, missing-file warnings, record counts, and coverage gaps. Empty output describes that input and configuration; it does not establish that activity was absent.

[EZ CSV Summary](../tools/ez-csv-summary.md) records a selected column's counts, UTC bounds, and input hash. It summarizes exports; it does not acquire artifacts, replace a parser, or establish execution or attribution.

## Publisher terms

These guides distribute instructions and original utilities, not third-party binaries. Licensing differs across the Zimmerman catalog; it is not an entirely open-source suite.

KAPE's [official FAQ](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/50-Frequently-asked-questions.md) states that commercial use on third-party networks or paid engagements is no longer available from January 1, 2026. Listed free uses include government, education, research, and internal company work. Read the current terms before use.

Documentation checked October 7, 2026. No Zimmerman binary was downloaded or run for these guides.
