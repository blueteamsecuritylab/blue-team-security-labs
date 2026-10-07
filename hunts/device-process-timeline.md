# Device process timeline

Build a process timeline for one device during the alert window.

Query: [device-process-timeline.kql](../queries/defender/device-process-timeline.kql)

## Set the device and window

Use Microsoft Defender XDR Advanced Hunting with Defender for Endpoint process telemetry and access to `DeviceProcessEvents`.

Replace `HOST-042` with the reported device name and both May 24, 2026 timestamps with the investigation window in UTC. Those article examples may fall outside retention and return no rows if left unchanged.

## Interpret the timeline

Results are ordered by time and include the initiating process, command line, image path, available SHA-256, and report identifier. The query does not filter `ActionType`; inspect it in the raw event before describing the activity.

Microsoft defines `DeviceName` as an FQDN and `ReportId` as a repeating counter. Preserve device identity and time alongside the report identifier. Keep rows with missing SHA-256 values in the review.

## Follow up

1. Inspect the initiating process and child process paths and command lines.
2. Correlate nearby file and network events on the same device.
3. Use available process identifiers and creation times to distinguish reused process IDs.
4. Follow a specific file hash or destination into a wider scoped search.

## Account for gaps

Normal software activity belongs in this timeline. Sensor coverage, ingestion, retention, and empty columns limit its history. A row alone does not explain intent or establish that all related activity was collected.

Validation: published excerpt and Microsoft column-reference review. It has not been run in a tenant; no output evidence is included.

**Provenance:** [Advanced Hunting Queries for Incident Response — Process Execution Query](https://blueteamsecurity.org/blog/advanced-hunting-queries-for-incident-response/).

**Field reference:** [Microsoft: DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table).