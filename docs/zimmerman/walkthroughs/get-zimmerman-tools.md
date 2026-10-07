# Get-ZimmermanTools: prepare a recorded tool set

**Question:** Which downloaded tools and supporting definitions will this lab use?

Get-ZimmermanTools is the author's PowerShell downloader and updater. It contacts external download services, extracts tool archives, and records download details. Run it during tool preparation, then freeze the selected build and definitions for a repeatable analysis run.

## Prepare the destination

Follow the [shared setup](../setup.md). Obtain `Get-ZimmermanTools.ps1` through the author catalog, retain a copy of the reviewed script, and choose a tool directory such as `C:\Tools\Zimmerman`. Keep that directory separate from `C:\Cases\LAB-001\evidence`; downloading tools is not evidence collection.

The current script accepts `-NetVersion 4`, `9`, or `0`, with `9` as its default. Some catalog entries are offered only in one column. Review the catalog for the specific tool instead of assuming that one downloader setting supplies every application.

## Download and record

After reviewing the script and choosing the appropriate analysis environment:

```powershell
.\Get-ZimmermanTools.ps1 -Dest 'C:\Tools\Zimmerman' -NetVersion 9
```

Review the run's network and extraction messages. The current script records downloaded details in `!!!RemoteFileDetails.csv` under the destination and uses that information when checking for changes on later runs. Preserve it with the selected script and record the versions of tools actually used. Verify the downloaded executables as described in the shared setup.

Inspect the resulting folders before pointing any parser at evidence. Where ancillary maps or batch definitions are required, prepare and record them separately. The optional `-Sync` switch invokes synchronization for EvtxECmd, SQLECmd, and RECmd; it changes supporting definitions and adds network activity. Do not add it to a running case merely to obtain different results.

## Troubleshoot and preserve repeatability

If a download fails, save the error and review the script's completed-file record; a partial tool directory is not a complete installation. Use approved proxy configuration where required, without publishing proxy credentials. Do not globally weaken PowerShell policy or endpoint protections to make the script run.

The script downloads and updates; it does not test parser behavior against your artifacts. Do not replace a recorded case tool set in place when comparing runs. KAPE has separate acquisition and licensing requirements and is excluded by the current downloader script; follow the [KAPE guide](kape.md) for its scope.

## Sources and validation

- [Author catalog and downloader link](https://ericzimmerman.github.io/)
- [Author's Get-ZimmermanTools script](https://github.com/EricZimmerman/Get-ZimmermanTools/blob/master/Get-ZimmermanTools.ps1)

Sources checked October 7, 2026. The script's documented parameters and current source were reviewed; no download, update, or synchronization was run for this repository.
