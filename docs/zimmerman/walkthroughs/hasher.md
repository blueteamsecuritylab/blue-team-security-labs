# Hasher: record a file's content digest

**Question:** Do two working copies contain the same bytes, and which files were hashed?

Hasher calculates file digests through a graphical interface. A digest identifies content for comparison; it does not determine whether a file is benign or who created it. This guide explicitly selects SHA-256 rather than assuming the saved settings already enable it.

## Prepare the input

Follow the [shared setup](../setup.md). Use copied benign files under `C:\Cases\LAB-001\evidence\documents`. Keep exported results under `C:\Cases\LAB-001\output\hashes`. The current author catalog lists Hasher in the .NET 4 column, despite its general statement about newer GUI builds. Check the actual download and runtime instead of applying that general statement to Hasher automatically.

## Hash and export

1. Start Hasher. Open **Tools → Options** and select **SHA-256** among the algorithms. Review the default save path, delimiter, and whether previous results are cleared between runs.
2. Use the **File** menu to select the copied files or their folder. The manual also documents dragging files and folders onto the main window.
3. Allow hashing to finish. Inspect the filename and SHA-256 columns, and check whether every intended file appears. Record any access errors or exclusions.
4. Export the results through the **File** menu to the separate output directory. Give the export a run-specific name and preserve its headers.
5. Compare the SHA-256 values of the files you intended to compare. Keep their full paths in the internal case notes so matching names from different folders are not confused.

## Interpret and troubleshoot

A matching SHA-256 digest supports identical content for the hashed copies. It does not compare access controls, alternate streams omitted from scope, or the history of those files. An integrity comparison requires a trustworthy reference digest and an adequately recorded acquisition process.

Hasher saves preferences in `Hasher.ini`. Preserve the relevant algorithm and result-retention settings with the run notes. The manual's historical example does not enable SHA-256, so confirm the visible column before exporting. If the export combines old and new rows, rerun into a clearly separated result set rather than attributing every row to the current scope. When hashing a directory, reconcile the intended file inventory with results; an export alone does not prove all files were readable.

## Sources and validation

- [Current author catalog](https://ericzimmerman.github.io/)
- [Official Hasher manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/hasher.txt)

Sources checked October 7, 2026. The documented settings and workflow were reviewed; the GUI was not executed for this repository. No digest comparison result is supplied.
