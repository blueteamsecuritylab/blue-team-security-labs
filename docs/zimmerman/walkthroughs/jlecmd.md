# JLECmd: connect a Jump List entry to its application and source

**Question:** Does an acquired user profile's Jump List reference the fictional lab document, and what application-specific context accompanies the reference?

## Prepare the input

Follow [setup and evidence handling](../setup.md). Acquire the source profile's `AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations` and `CustomDestinations` directories. Preserve both folders, original filenames, user-profile mapping, hashes, and acquisition time. Put working copies under `C:\Cases\LAB-001\evidence\recent`. A profile location provides account context; it does not identify the human operating that account.

Use a verified tool installation and keep outputs separate. Jump List types differ, so do not assume every custom destination has the same DestList metadata as an automatic destination.

## Parse the collection

Run in PowerShell:

```powershell
& 'C:\Tools\EZTools\JLECmd.exe' --version
& 'C:\Tools\EZTools\JLECmd.exe' --help
& 'C:\Tools\EZTools\JLECmd.exe' -d 'C:\Cases\LAB-001\evidence\recent' --csv 'C:\Cases\LAB-001\output\jumplists'
```

The minimal directory command processes recognized Jump List extensions recursively. Record the installed version, command, file counts, and warnings. Do not apply `--all` simply to remove a count discrepancy; first inventory the selected collection and determine which files were skipped.

## Inspect the outputs

Open the generated CSV files and inspect their actual headers. Preserve the source destination filename and AppID with every selected row. Review the resolved application description, target path, available DestList times, MRU position, pin state, and embedded-link information. Treat the AppID description as a mapping to review, not a replacement for the source identifier.

Search for fictional `WorkshopPlan.txt`. Opening that document in a legitimate editor during a lab exercise is a benign explanation. A pinned destination or application-generated task can remain visible without demonstrating a new access at the time you are investigating. Separate DestList activity metadata from target-file timestamps copied into an embedded LNK.

## Bound the conclusion and pivot

A reference can support application/file interaction context; it does not prove file contents were read, copied, or exfiltrated. Note the source account association and corroboration needed before attributing an action.

For detailed follow-up, the author documents `--dumpTo` for exporting embedded LNK files. Check local help before using it, retain the container-to-link mapping, and inspect the exported copies with [LECmd](lecmd.md). Compare ordinary Recent-folder shortcuts, filesystem records, and endpoint telemetry.

If no rows appear, check file extensions, collection identity, supported format, and parser messages. A parser failure or incomplete profile is a coverage gap. Address runtime problems through the shared setup; retain failed commands and their inputs.

## Sources and validation

Checked **2026-10-07**:

- [Author's JLECmd README](https://github.com/EricZimmerman/JLECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/jlecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
