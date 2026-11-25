# Get-ZimmermanTools: prepare a reproducible tool set

Which tool builds and supporting definitions will be used for the analysis?

Get-ZimmermanTools downloads and extracts archives from external services and records download details. Prepare the tools before examining evidence, then retain the selected builds and definitions for comparison between runs.

## Choose the destination and runtime

Follow the [shared setup](../setup.md). Obtain and retain the reviewed `Get-ZimmermanTools.ps1` from the author catalog. Use `C:\Tools\Zimmerman`, separate from `C:\Cases\LAB-001\evidence`.

Use `-NetVersion 10` for .NET 10 (the default), `4` for the available .NET Framework builds, or `0` for both families. Check the catalog for each tool’s available builds. The current script accepts the older value `9`, prints a warning, and downloads the .NET 10 builds. Record the versions from the installed tools.

## Download and record the selected builds

Run the reviewed script in the prepared analysis environment:

```powershell
.\Get-ZimmermanTools.ps1 -Dest 'C:\Tools\Zimmerman' -NetVersion 10
```

Review network and extraction messages. Preserve `!!!RemoteFileDetails.csv`, which records downloads and supports later change checks, with the script. Record the versions actually used and verify executables through the shared setup.

Inspect downloaded folders before processing evidence. Prepare required maps or batch definitions separately. Optional `-Sync` invokes synchronization for EvtxECmd, SQLECmd, and RECmd: it changes supporting definitions and adds network activity. Record that update before a case run rather than changing definitions midway to alter results.

## Handle partial downloads without changing case tools

Retain failed-download messages and compare the completed-file record with required tools. A partial directory is not a complete installation. Use approved proxy configuration where needed and keep credentials out of published records. Resolve policy or endpoint-protection blocks through the approved setup instead of globally weakening controls.

Downloading does not test parser behavior. Keep a recorded case tool set unchanged when comparing runs. The script excludes KAPE, which has separate acquisition and licensing requirements; see the [KAPE guide](kape.md).

## References

- [Author catalog and downloader link](https://ericzimmerman.github.io/)
- [Downloader source used to verify the runtime options](https://github.com/EricZimmerman/Get-ZimmermanTools/blob/c8178ec1a9bc6e59a3e3ff6ba5d24f3c3a3d13c4/Get-ZimmermanTools.ps1)

Sources checked October 7, 2026. Runtime options were rechecked against the script on November 24, 2026. This review examined the source without running the downloader or synchronizing definitions.
