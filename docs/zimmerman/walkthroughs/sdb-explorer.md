# SDB Explorer: inspect application compatibility definitions

What does the copied shim database specify, and is there evidence it was used?

SDB Explorer displays Windows application compatibility databases (`.sdb`). Database contents describe configuration. Installation and execution require separate evidence.

## Load the copied database

Follow the [shared setup](../setup.md). Use `C:\Cases\LAB-001\evidence\compatibility\training.sdb`, recording its acquisition path, hash, and whether acquisition notes identify it as standard or custom. This is a lab filename, not a discovered persistence artifact. The current catalog lists SDB Explorer as a .NET 9 GUI; verify the selected build's requirements.

## Examine definitions and matching information

1. Load the `.sdb` copy using the file-opening control.
2. Inspect the database structure and record the relevant definitions and application matching information with their displayed field labels.
3. Open **Info → Metrics** for a visual overview, then return to the individual entries. Counts help navigation; they do not classify the database as malicious.
4. Note the database hash, relevant entry, and what the definition specifies.
5. If investigating active use, compare with independently acquired installation records, Registry data, or endpoint events. Distinguish those sources from the SDB contents in the notes.

## Establish use before alleging shim abuse

Compatibility definitions can support legitimate applications. Their presence does not prove they were applied, a program executed, or an attacker created them. Suspected shim abuse needs a link between the database, its installation, and observed process activity.

For load failures, confirm the input is a database rather than an archive or a renamed file. Preserve the original bytes and parse errors. Installing the database to troubleshoot would change the analysis host and test its behavior rather than inspect its contents. Unexpected metrics warrant entry-level examination, not a conclusion based on aggregate counts.

## References

- [Official SDB Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sdbexplorer.txt)
- [Microsoft: application compatibility database](https://learn.microsoft.com/en-us/windows/win32/devnotes/application-compatibility-database)

Sources checked October 7, 2026. Documentation reviewed; GUI not run. No installation or persistence result claimed.
