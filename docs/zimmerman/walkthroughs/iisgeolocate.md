# iisGeoLocate: parse IIS requests for investigation

Which recorded requests and client-address values need closer examination?

iisGeoLocate converts IIS logs to CSV and enriches IP values with geolocation. Location labels are approximate enrichment, not identity or proof of a request's physical origin.

## Preserve log headers and acquisition scope

Follow the [shared setup](../setup.md). Copy lab logs to `C:\Cases\LAB-001\evidence\IIS` and record original paths, hashes, collection time, and logging configuration. IIS logs commonly reside under `C:\inetpub\logs\LogFiles`; the command operates on the copied directory.

Confirm the logged fields and timestamp format, preserving headers and malformed lines. Review the build's geolocation data requirements and network behavior before processing sensitive addresses. This workflow includes no public reputation lookup or telemetry upload.

## Export requests and rejected lines

Run from the iisGeoLocate directory:

```powershell
.\iisGeoLocate.exe -d 'C:\Cases\LAB-001\evidence\IIS' --csv 'C:\Cases\LAB-001\output\iis'
```

`-d` recursively searches for `.log` files; `--csv` sets the output directory. Retain console messages, CSVs, and logged bad-line data. Keep errors visible while checking parsing coverage.

In [Timeline Explorer](timeline-explorer.md), scope the time window, inspect raw request fields, and group address values. Check response status and requested paths where logged. Trace relevant rows to their original file and line before writing findings.

## Account for proxies and incomplete parsing

A logged address can belong to a proxy, gateway, or intermediary. Its meaning depends on the field and server configuration. Geolocation can be incomplete or outdated and does not identify the requester. Correlate authentication, application, and endpoint evidence when investigating compromise.

For skipped lines, inspect bad-line output and headers before interpreting absent requests. Record processed-file counts and whether logs cover the period of interest. Errors or partial acquisition limit any coverage claim.

## References

- [Official iisGeoLocate manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/iisgeolocate.txt)
- [iisGeoLocate repository](https://github.com/EricZimmerman/iisGeolocate)

Sources checked October 7, 2026. Syntax and documented outputs reviewed; parsing and enrichment not run. No request or location findings claimed.
