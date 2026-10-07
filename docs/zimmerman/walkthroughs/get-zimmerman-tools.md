# Get-ZimmermanTools: prepare a reproducible tool set

Which tool builds and supporting definitions will be used for the analysis?

Get-ZimmermanTools downloads and extracts archives from external services and records download details. Prepare the tools before examining evidence, then retain the selected builds and definitions for comparison between runs.

## Choose the destination and runtime

Follow the [shared setup](../setup.md). Obtain and retain the reviewed `Get-ZimmermanTools.ps1` from the author catalog. Use `C:\Tools\Zimmerman`, separate from `C:\Cases\LAB-001\evidence`.

`-NetVersion` accepts `4`, `9`, or `0`; the current default is `9`. Some tools appear in only one catalog column, so one setting does not necessarily download every application.

## Download and record the selected builds

Run the reviewed script in the prepared analysis environment:

```powershell
.\Get-ZimmermanTools.ps1 -Dest 'C:\Tools\Zimmerman' -NetVersion 9
```

Review network and extraction messages. Preserve `!!!RemoteFileDetails.csv`, which records downloads and supports later change checks, with the script. Record the versions actually used and verify executables through the shared setup.

Inspect downloaded folders before processing evidence. Prepare required maps or batch definitions separately. Optional `-Sync` invokes synchronization for EvtxECmd, SQLECmd, and RECmd: it changes supporting definitions and adds network activity. Record that update before a case run rather than changing definitions midway to alter results.

## Handle partial downloads without changing case tools

Retain failed-download messages and compare the completed-file record with required tools. A partial directory is not a complete installation. Use approved proxy configuration where needed and keep credentials out of published records. Resolve policy or endpoint-protection blocks through the approved setup instead of globally weakening controls.

Downloading does not test parser behavior. Keep a recorded case tool set unchanged when comparing runs. The script excludes KAPE, which has separate acquisition and licensing requirements; see the [KAPE guide](kape.md).

## References

- [Author catalog and downloader link](https://ericzimmerman.github.io/)
- [Author's Get-ZimmermanTools script](https://github.com/EricZimmerman/Get-ZimmermanTools/blob/master/Get-ZimmermanTools.ps1)

Sources checked October 7, 2026. Script parameters and source reviewed; no download, update, or synchronization run.
