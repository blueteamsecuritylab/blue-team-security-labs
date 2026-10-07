# bstrings: search file bytes for a lead

Does the copied file contain a readable string relevant to the investigation?

bstrings searches file bytes for literal strings and regular-expression matches without executing the input. A match describes content, not behavior.

## Choose one file and one search term

Follow the [shared setup](../setup.md). Place a benign fixture at `C:\Cases\LAB-001\evidence\sample.bin` and record its hash. The example searches for `powershell`; it includes no executable or malware sample. Keep results outside the evidence directory.

## Preserve context and offsets

Run in PowerShell from the bstrings directory:

```powershell
.\bstrings.exe -f 'C:\Cases\LAB-001\evidence\sample.bin' --ls 'powershell' --off -o 'C:\Cases\LAB-001\output\strings-powershell-run01.txt'
```

`-f` selects the file, `--ls` filters returned strings, and `--off` includes offset and encoding information. ASCII and Unicode searches are enabled by default. Save console messages with the command and input hash.

Read the result as text and record each relevant string's full context, source file, and reported offset. For IP-like strings, inspect built-in patterns with `-p`, then use `--lr ipv4` on the same input. That identifies text resembling an IPv4 address; it does not establish a connection.

## Interpret matches and empty results

Strings can occur in resources, unused code, documentation, or embedded data. `powershell` in a file does not prove PowerShell ran. Empty results do not exclude compressed, encrypted, encoded, or dynamically constructed content. Use a format-aware parser or execution telemetry to investigate the lead.

Reusing an `-o` filename appends results, so give each run a separate name. For empty output, check access, encoding, minimum string length, and the search term before expanding scope. For large inputs, review chunk size and available memory. Record skipped files; they limit coverage.

## References

- [Official bstrings manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/bstrings.txt)
- [bstrings repository](https://github.com/EricZimmerman/bstrings)

Sources checked October 7, 2026. Command syntax reviewed; bstrings not run. No search hits claimed.
