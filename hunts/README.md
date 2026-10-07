# Hunt queries

Each hunt pairs a copyable query with scope, expected matches, benign explanations, and follow-up evidence.

| Hunt | Platform | Query |
| --- | --- | --- |
| [Browser to script](browser-to-script.md) | SentinelOne Deep Visibility | [browser-to-script.s1ql](../queries/sentinelone/browser-to-script.s1ql) |
| [Encoded PowerShell](encoded-powershell.md) | SentinelOne Deep Visibility | [encoded-powershell.s1ql](../queries/sentinelone/encoded-powershell.s1ql) |
| [Device process timeline](device-process-timeline.md) | Microsoft Defender XDR | [device-process-timeline.kql](../queries/defender/device-process-timeline.kql) |
| [File hash scope](file-hash-scope.md) | Microsoft Defender XDR | [file-hash-scope.kql](../queries/defender/file-hash-scope.kql) |

The queries are published article excerpts reviewed against their source text and field references. Tenant execution remains unverified. Check operators, scope, event coverage, and populated values in the authorized console before using a match in an investigation.

Use the [hunt record](../templates/hunt-record.md) to save the query, endpoint and time scope, supporting rows, and gaps. [PROVENANCE.json](../PROVENANCE.json) records source sections and query hashes.

[Repository home](../README.md) · [Query files](../queries/README.md)
