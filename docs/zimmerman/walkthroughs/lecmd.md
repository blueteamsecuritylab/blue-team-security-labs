# LECmd: separate shortcut and target-file metadata

Parse an acquired shortcut's target, arguments, and stored metadata, then identify which conclusions require independent evidence.

## Acquire shortcuts without following their targets

Complete [setup and evidence handling](../setup.md). Acquire authorized copies of relevant `.lnk` files, including the source user's Recent directory when applicable. Preserve their original paths and filesystem metadata through the acquisition method; ordinary copying may change timestamps. Keep acquired copies in `C:\Cases\LAB-001\evidence\lnk` and record the source profile, hashes, and acquisition time.

Double-clicking a shortcut can follow its target. Inspect its bytes with the verified parser instead.

## Parse the acquired LNK files

Use PowerShell:

```powershell
& 'C:\Tools\EZTools\LECmd.exe' --version
& 'C:\Tools\EZTools\LECmd.exe' --help
& 'C:\Tools\EZTools\LECmd.exe' -d 'C:\Cases\LAB-001\evidence\lnk' --csv 'C:\Cases\LAB-001\output\lnk'
```

The directory option recursively selects shortcuts by their expected extension. Save the version, command, counts, and parsing warnings. If acquisition renamed extensions, document the changes before considering `--all`; record any expanded scope and exclude unrelated evidence.

## Review source and target fields

Review the generated CSV headers and each candidate's complete record. Retain the source shortcut path, target path, arguments where present, working directory, volume details, and target ID or extra-block context.

The manual separates `SourceCreated`, `SourceModified`, and `SourceAccessed` from `TargetCreated`, `TargetModified`, and `TargetAccessed`. The first group describes the shortcut file; the second represents target metadata held in the link. Do not treat either group wholesale as execution times. Check whether acquisition changed source timestamps before using them in a timeline.

A fictional shortcut to `WorkshopPlan.txt` could reflect normal document use. A Start Menu shortcut can also be installed without anyone launching its target. A copied or deliberately authored LNK needs further context before being treated as an automatically generated access trace. Missing tracker data is not evidence that a file was never accessed.

## Corroborate the link's origin and use

Record the link's contents and origin. Shortcut metadata alone does not prove that its target executed, that a named user read the contents, or that a remote address was contacted.

Compare [Jump Lists](jlecmd.md), filesystem metadata, available process creation events, and [Prefetch](pecmd.md). For a link with command-line arguments, inspect the text and acquired target separately without launching either.

## Missing records and blank target fields

For missing results, check input extensions and parser warnings. Blank target fields may reflect the link's flags and structure; they do not automatically indicate corruption. Use the shared setup for tool/runtime problems and record unsuccessful attempts.

## Sources and validation

Sources checked 2026-10-07:

- [Author's LECmd README](https://github.com/EricZimmerman/LECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/lecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Documentation review only; the parser commands have not been run.
