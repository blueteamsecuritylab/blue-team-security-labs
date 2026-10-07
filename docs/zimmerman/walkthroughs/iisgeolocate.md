# iisGeoLocate: turn IIS log rows into reviewable leads

**Question:** Which recorded requests and client-address values need closer examination?

iisGeoLocate parses IIS logs, creates CSV data, and enriches IP address values with geolocation information. Start with a bounded log collection. A country or city label is enrichment, not a reliable identity or proof of a request's physical origin.

## Prepare the inputs

Follow the [shared setup](../setup.md). Copy the authorized lab IIS logs into `C:\Cases\LAB-001\evidence\IIS`. Record their original paths, hashes, collection time, and logging configuration. IIS logs commonly reside under `C:\inetpub\logs\LogFiles`; the parser command below operates only on the copied directory.

Confirm which timestamp format and fields the source logs contain. Preserve headers and any malformed lines. Review the selected build's geolocation data requirements and network behavior before processing sensitive addresses; this guide does not request public reputation lookups or telemetry uploads.

## Parse and inspect

Run from the reviewed tool directory:

```powershell
.\iisGeoLocate.exe -d 'C:\Cases\LAB-001\evidence\IIS' --csv 'C:\Cases\LAB-001\output\iis'
```

`-d` recursively searches the selected directory for `.log` files, and `--csv` supplies the output directory. Keep console messages, generated CSVs, and any logged bad-line data. Do not suppress errors while establishing whether the collection parsed cleanly.

Open the CSV in [Timeline Explorer](timeline-explorer.md). Scope the time window, inspect raw request fields, and group relevant address values. Check response status and requested paths where those fields were logged. Trace each notable row back to its original file and line before using it in the investigation notes.

## Interpret and troubleshoot

An address in a web log can represent a proxy, gateway, or intermediary. Its meaning depends on the logging field and server configuration. Geolocation can be incomplete or outdated, and an address's apparent location does not establish who made the request. Correlate with authentication, application, and endpoint evidence when the question concerns compromise.

If parsing skips lines, inspect the bad-line output and log headers. Separate format problems from genuine absence of requests. Record how many source files were processed and whether the period of interest is covered. Avoid making a complete-coverage claim from a CSV produced with errors or a partially collected directory.

## Sources and validation

- [Official iisGeoLocate manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/iisgeolocate.txt)
- [iisGeoLocate repository](https://github.com/EricZimmerman/iisGeolocate)

Sources checked October 7, 2026. The parser syntax and documented outputs were reviewed; parsing and enrichment were not executed for this repository. No request or location findings are claimed.
