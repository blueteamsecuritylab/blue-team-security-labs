# Device process timeline

**Question:** What process activity was recorded for one device during the alert window?

**Query:** [device-process-timeline.kql](../queries/defender/device-process-timeline.kql)

## Before running

Use Microsoft Defender XDR Advanced Hunting with Defender for Endpoint process telemetry and access to `DeviceProcessEvents`.

Replace `HOST-042` with the device's reported name and replace both May 24, 2026 timestamps with the actual investigation window in UTC. The fixed dates are illustrative values from the published article; running them unchanged can return nothing simply because the data is outside retention.

## Read the match

The query returns device-scoped process rows in chronological order, including the initiating process, command line, image path, available SHA-256, and report identifier. It does not filter `ActionType`; inspect that field in the raw event before describing the activity.

The Microsoft reference describes `DeviceName` as an FQDN and notes that `ReportId` is a repeating counter. Preserve device identity and time with the report identifier. Missing SHA-256 values do not make a row irrelevant.

## Next pivots

1. Inspect the initiating process and child process paths and command lines.
2. Correlate nearby file and network events on the same device.
3. Use available process identifiers and creation times to distinguish reused process IDs.
4. Follow a specific file hash or destination into a wider scoped search.

## Expected benign matches and limits

This is a timeline, so normal software activity is expected. Sensor coverage, ingestion, retention, and empty columns limit the returned history. A row by itself does not explain intent or prove that all related activity was collected.

**Status:** Published excerpt and Microsoft column-reference review only. No tenant execution or output evidence supplied.

**Provenance:** [Advanced Hunting Queries for Incident Response — Process Execution Query](https://blueteamsecurity.org/blog/advanced-hunting-queries-for-incident-response/).

**Field reference:** [Microsoft: DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table).
