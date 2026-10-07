# File hash scope

**Question:** How widely did a known SHA-256 appear in available file telemetry?

**Query:** [file-hash-scope.kql](../queries/defender/file-hash-scope.kql)

## Before running

Use Microsoft Defender XDR Advanced Hunting with access to `DeviceFileEvents`. Replace `<sha256_value>` with the observed 64-character hexadecimal hash. Select a justified lookback within available retention; the excerpt uses 30 days.

Check whether SHA-256 is populated for the relevant event. Microsoft notes that this column is usually not populated and recommends SHA-1 when available. If you adapt the query to SHA-1, use an observed SHA-1 from the same file and record the changed column and value.

## Read the match

The output groups matching file events by hash, filename, and action type. The device count is approximate because it uses `dcount`. This summary does not list device identities; review the underlying matching rows for device-level scoping. The stored path set is capped at 20 per group. First and last seen refer to the returned events in the queried window.

A file event is not process execution evidence. Inspect `ActionType`, the initiating process, and raw rows to distinguish creation, modification, deletion, or another recorded action.

## Next pivots

1. Export representative raw events and the affected device identities.
2. Review the file's paths, names, action types, initiating processes, and timestamps.
3. Search available process telemetry for the same image hash or correlated execution.
4. Compare distribution with approved software packages, deployment jobs, and quarantine handling.

## Expected benign matches and limits

Legitimate packages can share the searched hash across devices. A known hash can appear without execution. An empty result means no matching rows were returned for this table, predicate, and window; it does not prove the file was absent.

**Status:** Published excerpt and Microsoft column-reference review only. No tenant execution or output evidence supplied.

**Provenance:** [Advanced Hunting Queries for Incident Response — Hash Scope Query](https://blueteamsecurity.org/blog/advanced-hunting-queries-for-incident-response/).

**Field reference:** [Microsoft: DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table).
