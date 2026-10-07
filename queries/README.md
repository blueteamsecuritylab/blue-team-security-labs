# Query files

| Platform | File | Investigation notes |
| --- | --- | --- |
| SentinelOne | [Browser to script](sentinelone/browser-to-script.s1ql) | [Scope and interpretation](../hunts/browser-to-script.md) |
| SentinelOne | [Encoded PowerShell](sentinelone/encoded-powershell.s1ql) | [Scope and interpretation](../hunts/encoded-powershell.md) |
| Defender XDR | [Device process timeline](defender/device-process-timeline.kql) | [Scope and interpretation](../hunts/device-process-timeline.md) |
| Defender XDR | [File hash scope](defender/file-hash-scope.kql) | [Scope and interpretation](../hunts/file-hash-scope.md) |

Read the companion hunt before copying a query. Replace sample scope values where shown and keep the time window small enough to inspect the returned events.

These files preserve the published excerpts exactly. The [source record](../PROVENANCE.json) identifies each article section and SHA-256. Their text and field references were reviewed; execution and results still need a tenant check.

[Repository home](../README.md) · [Hunt index](../hunts/README.md)
