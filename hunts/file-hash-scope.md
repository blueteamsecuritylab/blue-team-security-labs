# File hash scope

Scope a known SHA-256 across available file telemetry.

Query: [file-hash-scope.kql](../queries/defender/file-hash-scope.kql)

## Set the hash and lookback

Use Microsoft Defender XDR Advanced Hunting with access to `DeviceFileEvents`. Replace `<sha256_value>` with the observed 64-character hexadecimal hash. Set a lookback within retention that fits the investigation; the excerpt uses 30 days.

Check SHA-256 availability in the relevant events. Microsoft notes that the column is usually unpopulated and recommends SHA-1 when available. To adapt the query, use an observed SHA-1 from the same file and record the changed column and value.

## Interpret the summary

Results group matching events by hash, filename, and action type. The `dcount` device count is approximate; inspect underlying rows to identify devices. Each group's path set is capped at 20. First and last seen describe only returned events within the queried window.

Inspect `ActionType`, the initiating process, and raw rows to distinguish creation, modification, deletion, or another recorded action. A file event alone does not establish process execution.

## Follow up

1. Export representative raw events and the affected device identities.
2. Review the file's paths, names, action types, initiating processes, and timestamps.
3. Search available process telemetry for the same image hash or correlated execution.
4. Compare distribution with approved software packages, deployment jobs, and quarantine handling.

## Account for legitimate distribution

Approved packages can share the hash across devices, and file presence does not establish execution. An empty result applies only to this table, predicate, and window; it does not prove absence.

Validation: published excerpt and Microsoft column-reference review. It has not been run in a tenant; no output evidence is included.

**Provenance:** [Advanced Hunting Queries for Incident Response — Hash Scope Query](https://blueteamsecurity.org/blog/advanced-hunting-queries-for-incident-response/).

**Field reference:** [Microsoft: DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table).