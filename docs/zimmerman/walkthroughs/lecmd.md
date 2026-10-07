# LECmd: distinguish shortcut metadata from the target file

**Question:** What target, arguments, and historical metadata does an acquired shortcut contain, and which claims need independent evidence?

## Prepare the input

Complete [setup and evidence handling](../setup.md). Acquire authorized copies of relevant `.lnk` files, including the source user's Recent directory when applicable. Preserve their original paths and filesystem metadata through the acquisition method; ordinary copying may change timestamps. Place working files in `C:\Cases\LAB-001\evidence\lnk` and record the source profile, hashes, and acquisition time.

Do not open a shortcut by double-clicking it: that can follow its target. This workflow parses bytes using a verified analysis tool.

## Parse the working copies

Use PowerShell:

```powershell
& 'C:\Tools\EZTools\LECmd.exe' --version
& 'C:\Tools\EZTools\LECmd.exe' --help
& 'C:\Tools\EZTools\LECmd.exe' -d 'C:\Cases\LAB-001\evidence\lnk' --csv 'C:\Cases\LAB-001\output\lnk'
```

The directory option recursively selects shortcuts by their expected extension. Save the version, command, counts, and parsing warnings. If the acquisition renamed extensions, document that fact before considering the author's `--all` option. Do not silently expand the scope to unrelated evidence.

## Inspect the output

Review the generated CSV headers and the complete record for each candidate. Preserve its source shortcut path, target path, arguments where present, working directory, volume details, and any target ID or extra-block context.

The manual separates `SourceCreated`, `SourceModified`, and `SourceAccessed` from `TargetCreated`, `TargetModified`, and `TargetAccessed`. The first group describes the shortcut file; the second represents target metadata held in the link. Neither group should be relabeled wholesale as “execution time.” Consider whether acquisition changed source timestamps before using them in a timeline.

A fictional shortcut to `WorkshopPlan.txt` could reflect normal document use. A Start Menu shortcut can also be installed without anyone launching its target. A copied or deliberately authored LNK needs further context before being treated as an automatically generated access trace. Missing tracker data is not evidence that a file was never accessed.

## Bound the conclusion and pivot

Write what the link contains, then explain why its origin matters. Shortcut metadata alone does not prove that its target executed, that a named user read the contents, or that a remote address was contacted.

Compare [Jump Lists](jlecmd.md), filesystem metadata, available process creation events, and [Prefetch](pecmd.md). For a link with command-line arguments, inspect the text and acquired target separately without launching either.

For missing results, check actual input extensions and parser warnings. For blank target fields, consider the link's flags and structure rather than assuming corruption. Resolve tool/runtime problems through the shared setup and preserve unsuccessful attempts.

## Sources and validation

Checked **2026-10-07**:

- [Author's LECmd README](https://github.com/EricZimmerman/LECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/lecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
