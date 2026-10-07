# PECmd: Prefetch run times and file references

Check whether an acquired Prefetch collection records a lab executable running within the investigation window.

## Acquire the Prefetch collection

Follow [setup and evidence handling](../setup.md). Preserve an authorized copy of the source host's `C:\Windows\Prefetch` directory, source paths, collection time, hashes, and Windows build. Place the `.pf` copies in `C:\Cases\LAB-001\evidence\prefetch` and keep exports elsewhere. Filenames used here are illustrative.

Record whether Prefetch was enabled and whether acquisition was complete, when known. Missing Prefetch leaves a coverage gap; it does not rule out execution.

## Export the run timeline

```powershell
& 'C:\Tools\EZTools\PECmd.exe' --version
& 'C:\Tools\EZTools\PECmd.exe' --help
& 'C:\Tools\EZTools\PECmd.exe' -d 'C:\Cases\LAB-001\evidence\prefetch' --csv 'C:\Cases\LAB-001\output\prefetch'
```

`-d` processes the collection recursively; `--csv` selects the export directory. Save the version, command, parse counts, and errors. This command stays within acquired files. The optional shadow-copy switch broadens the operation beyond this collection.

## Separate run times from filesystem times

Inspect the headers of the main CSV and companion timeline CSV. Review executable name, source Prefetch path, run count, last recorded run, earlier stored runs, and volume/file references. Keep decoded run-time values distinct from the Prefetch file's filesystem timestamps.

Filter the timeline to the intended window, then inspect each candidate's main record. A fictional `PAINT.EXE` run during a drawing exercise can explain a nearby match; temporal proximity alone does not make it malicious.

Prefetch can corroborate execution, but does not provide a complete lifetime run history or identify the person at the keyboard. File references do not prove that contents were read or exported. The hexadecimal filename component is not a cryptographic hash of the executable.

## Corroboration and parse failures

Compare candidate runs with endpoint process telemetry, event logs, and the acquired binary where available. Record the artifact and timestamp supporting each conclusion, alongside missing context.

For missing or failed rows, check format support, truncation, collection scope, and parser messages. Older analysis Windows environments may fail to decompress newer Prefetch formats; use shared setup guidance to resolve compatibility. Skipped files remain unresolved inputs, not negative findings.

## Sources

Checked 2026-10-07:

- [Author's PECmd README](https://github.com/EricZimmerman/PECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/pecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

Validation: Documentation review only; parser and GUI examples have not been run.
