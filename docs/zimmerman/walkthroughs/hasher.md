# Hasher: compare file contents with SHA-256

Do the working copies contain the same bytes, and did the run cover every intended file?

Hasher calculates and exports file digests through a GUI. A digest supports content comparison; it does not establish whether a file is benign or who created it.

## Select the input and algorithm

Follow the [shared setup](../setup.md). Use benign copies under `C:\Cases\LAB-001\evidence\documents` and export to `C:\Cases\LAB-001\output\hashes`. The catalog lists Hasher under .NET 4 despite its general statement about newer GUI builds. Check the actual download and runtime.

1. Open **Tools → Options** and enable **SHA-256**. Review save path, delimiter, and whether previous results are cleared between runs.
2. Select files or a folder through **File**, or drag them onto the main window.
3. When hashing finishes, inspect filenames and the SHA-256 column. Reconcile the intended file inventory with results and record access errors or exclusions.
4. Export through **File** to a run-specific name, preserving headers.
5. Compare the intended files' SHA-256 values. Keep full paths in the case notes so identical filenames in different folders remain distinguishable.

## Check settings and comparison scope

Preferences persist in `Hasher.ini`. Record the algorithms and result-retention settings. The manual's historical settings example does not enable SHA-256, so confirm the output column before exporting. If old and new rows are mixed, separate the runs before attributing results to the current scope.

Matching SHA-256 values support identical contents for the hashed copies. They do not compare access controls, omitted alternate streams, or file history. An integrity comparison also needs a trustworthy reference digest and a recorded acquisition process. A directory export alone does not establish that every file was readable.

## References

- [Current author catalog](https://ericzimmerman.github.io/)
- [Official Hasher manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/hasher.txt)

Sources checked October 7, 2026. Documentation reviewed; GUI not run. No digest comparison result supplied.
