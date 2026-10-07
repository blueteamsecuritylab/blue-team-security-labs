# JLECmd: trace Jump List references to applications and files

Search an acquired user profile's Jump Lists for a fictional lab document, then examine the application and source record behind each reference.

## Acquire AutomaticDestinations and CustomDestinations

Follow [setup and evidence handling](../setup.md). Acquire the source profile's `AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations` and `CustomDestinations` directories. Preserve both folders, original filenames, user-profile mapping, hashes, and acquisition time. Keep the acquired copies under `C:\Cases\LAB-001\evidence\recent`. A profile location provides account context; it does not identify the human operating that account.

Use a verified tool installation and a separate output directory. Automatic and custom destinations differ; do not assume they expose the same DestList metadata.

## Parse the collected Jump Lists

Run in PowerShell:

```powershell
& 'C:\Tools\EZTools\JLECmd.exe' --version
& 'C:\Tools\EZTools\JLECmd.exe' --help
& 'C:\Tools\EZTools\JLECmd.exe' -d 'C:\Cases\LAB-001\evidence\recent' --csv 'C:\Cases\LAB-001\output\jumplists'
```

The directory command recursively processes recognized Jump List extensions. Record the version, command, file counts, and warnings. If counts differ from the collection inventory, identify the skipped files before considering `--all`.

## Review AppID, DestList, and embedded-link fields

Inspect the generated CSV headers. Keep the source destination filename and AppID with each selected row. Review the resolved application description, target path, available DestList times, MRU position, pin state, and embedded-link information. Verify the AppID description while retaining the source identifier.

Search for fictional `WorkshopPlan.txt`. Opening that document in a legitimate editor during a lab exercise is a benign explanation. A pinned destination or application-generated task can remain visible without demonstrating a new access at the time you are investigating. Separate DestList activity metadata from target-file timestamps copied into an embedded LNK.

## Corroborate file interaction

A reference provides application/file interaction context. It does not prove that contents were read, copied, or exfiltrated. Record the source account association and corroborating evidence needed before attributing an action.

For detailed follow-up, the author documents `--dumpTo` for exporting embedded LNK files. Check local help before using it, retain the container-to-link mapping, and inspect the exported copies with [LECmd](lecmd.md). Compare ordinary Recent-folder shortcuts, filesystem records, and endpoint telemetry.

## Missing rows and parser errors

If no rows appear, check file extensions, collection identity, supported format, and parser messages. Parser failures and incomplete profiles leave coverage gaps. Use the shared setup for runtime problems; retain failed commands and their inputs.

## Sources and validation

Sources checked 2026-10-07:

- [Author's JLECmd README](https://github.com/EricZimmerman/JLECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/jlecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Documentation review only; the parser commands have not been run.
