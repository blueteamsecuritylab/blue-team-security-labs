# PECmd: recover recorded Prefetch run times

**Question:** Does the acquired Prefetch collection contain recorded runs for a lab executable during the time window under review?

## Prepare the input

Follow [setup and evidence handling](../setup.md). Acquire an authorized copy of the source host's `C:\Windows\Prefetch` directory. Preserve source paths, collection time, hashes, and Windows build. Put working `.pf` files in `C:\Cases\LAB-001\evidence\prefetch`; write results outside that directory. A filename in this guide is illustrative, not evidence from an investigation.

Record whether Prefetch was enabled and whether the collection was complete if that information is available. Its absence on a host is a coverage issue, not a verdict about execution.

## Parse and export

Use the approved installation in PowerShell:

```powershell
& 'C:\Tools\EZTools\PECmd.exe' --version
& 'C:\Tools\EZTools\PECmd.exe' --help
& 'C:\Tools\EZTools\PECmd.exe' -d 'C:\Cases\LAB-001\evidence\prefetch' --csv 'C:\Cases\LAB-001\output\prefetch'
```

The directory option recursively processes the selected collection; `--csv` selects the output directory. Capture the installed version, exact command, parse counts, and errors. Keep this first pass on acquired files. The documented shadow-copy option would broaden the operation and is unnecessary for this example.

## Inspect the outputs

The manual describes a main CSV and a companion timeline CSV. Find the actual generated files and inspect their headers. Review executable name, source Prefetch path, run count, last recorded run, any earlier stored runs, and volume/file-reference context. Distinguish the source file's filesystem timestamps from the run-time values decoded inside it.

Filter the timeline to the intended window, then return to the main record for context. A fictional `PAINT.EXE` run during a lab drawing task is an ordinary explanation for a match. Do not label it malicious solely because it ran near a suspicious event.

Prefetch can corroborate program execution, but does not supply a complete lifetime execution history or identify the person at the keyboard. Referenced files do not, by themselves, establish that their contents were read or exported. Avoid equating the hexadecimal filename component with a cryptographic hash of the executable.

## Pivot and troubleshoot

Correlate a candidate run with endpoint process telemetry, event logs, and the acquired binary when available. Write the exact artifact and timestamp supporting the conclusion, then list missing context.

For failed or missing rows, check source format support, truncated files, collection scope, and parser messages. Older analysis Windows environments can fail to decompress newer Prefetch formats; use the shared setup to resolve compatibility. Record failures instead of treating skipped files as negative findings.

## Sources and validation

Checked **2026-10-07**:

- [Author's PECmd README](https://github.com/EricZimmerman/PECmd)
- [Official manual chapter](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/pecmd.txt)
- [Author's current catalog](https://ericzimmerman.github.io/)

**Validation status:** Documentation checked; parser/GUI run not performed in this session.
