# Blue Team Security Labs

Defensive hunting queries, investigation notes, and small analysis tools from [Blue Team Security](https://blueteamsecurity.org/).

Start with an investigation question, inspect the matching event, and follow the evidence. A query match is a lead; the surrounding process, file, identity, and network activity determines what it means.

## Explore

| Example | Platform | Question |
| --- | --- | --- |
| [Browser to script](hunts/browser-to-script.md) | SentinelOne Deep Visibility | Did a browser parent appear with a script interpreter? |
| [Encoded PowerShell](hunts/encoded-powershell.md) | SentinelOne Deep Visibility | Which PowerShell command lines include encoded-command fragments? |
| [Device process timeline](hunts/device-process-timeline.md) | Microsoft Defender XDR | What process activity was recorded for one device and time window? |
| [File hash scope](hunts/file-hash-scope.md) | Microsoft Defender XDR | How widely did the searched file hash appear? |
| [Static file triage](malware-analysis/README.md) | Python, local files | What bytes and hashes are in the file being reviewed? |

Each hunt includes prerequisites, expected matches, false positives, next pivots, and a link to its published article. Copyable queries live in [queries/](queries/). [PROVENANCE.json](PROVENANCE.json) records their source sections and SHA-256 digests.

## Validation status

The query files are excerpts of published educational articles. Their text and referenced fields were reviewed on October 7, 2026. They have **not been executed in a SentinelOne or Defender tenant for this repository**, and no query results or detection-performance claims are supplied. Console operators, event coverage, and populated values still need an authorized environment check.

The local static triage tool has automated tests against benign temporary fixtures. Run them with Python 3.10 or newer:

```bash
python -m unittest discover -s tests -v
```

## Use and contribute

Choose a small endpoint and time scope before running a hunt. Save the exact query and scope, inspect raw rows, and note missing evidence in the [hunt record](templates/hunt-record.md). The examples contain no response automation.

This repository contains no malware samples, workplace telemetry, incident exports, or deployment credentials. Keep contributions generic or use clearly labeled synthetic data; publish only material you have permission to share.

[Blog](https://blueteamsecurity.org/) · [LinkedIn](https://www.linkedin.com/in/stephentafe/)
