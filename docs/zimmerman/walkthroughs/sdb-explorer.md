# SDB Explorer: inspect an application compatibility database

**Question:** What compatibility definitions are present in this copied shim database?

SDB Explorer is a graphical viewer for Windows application compatibility databases with the `.sdb` extension. Start by understanding the database's definitions, then use other evidence to determine whether the database was installed or used on a system.

## Prepare the input

Follow the [shared setup](../setup.md). Place an acquired working copy at `C:\Cases\LAB-001\evidence\compatibility\training.sdb`. Record where it was acquired, its hash, and whether it was a standard or custom database according to your acquisition notes. The filename here is a lab placeholder; it does not describe a discovered persistence mechanism.

Use the current author download and check its runtime requirements. SDB Explorer is listed as a .NET 9 GUI tool in the catalog. Opening the copied database for examination is distinct from registering or installing it in Windows.

## Inspect the database

1. Start SDB Explorer and load the `.sdb` copy using the application's file-opening control.
2. Examine the displayed database structure. Record the definitions and any application matching information relevant to the question, preserving the field labels as shown.
3. Use **Info → Metrics**, the menu documented in the manual, for a visual overview of the loaded database. Treat it as a navigation aid rather than a verdict about the database.
4. Return to the individual definitions before writing conclusions. Note the database hash, the relevant entry, and what it actually specifies.
5. Compare the definitions with independently acquired installation records, registry data, or endpoint events if the question concerns active use. Keep those sources separate from the SDB contents in your notes.

## Evidence boundaries and troubleshooting

Compatibility databases can support legitimate application behavior. The presence of a definition is not proof that it was applied, that a program executed, or that an attacker created it. Investigating suspected shim abuse requires a link between the database, its installation, and observed process activity.

If loading fails, verify that the file is a database rather than an enclosing archive or a file renamed to `.sdb`. Preserve parse errors and the original bytes. Do not install the database as a troubleshooting step: that would change the analysis host and test a different question. If the viewer's metrics look surprising, inspect the underlying entries instead of treating aggregate counts as case findings.

## Sources and validation

- [Official SDB Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/sdbexplorer.txt)
- [Microsoft: application compatibility database](https://learn.microsoft.com/en-us/windows/win32/devnotes/application-compatibility-database)

Sources checked October 7, 2026. The documented workflow was reviewed; the GUI was not executed for this repository. No installation or persistence result is claimed.
