# bstrings: find a lead without running the file

**Question:** Does a copied file contain readable text related to the investigation question?

bstrings searches files for strings or regular-expression matches. It reads the file as data. Start with a narrow keyword on a benign lab fixture; extracting a string does not validate the behavior described by that string.

## Prepare the input

Follow the [shared setup](../setup.md). Place a benign test file at `C:\Cases\LAB-001\evidence\sample.bin` and record its hash. Decide which term you are looking for and why. Keep results outside the evidence directory. This walkthrough searches for the literal `powershell`; it supplies no executable or malware sample.

## Search and preserve the results

Run from the reviewed tool directory in PowerShell:

```powershell
.\bstrings.exe -f 'C:\Cases\LAB-001\evidence\sample.bin' --ls 'powershell' --off -o 'C:\Cases\LAB-001\output\strings-powershell-run01.txt'
```

`-f` chooses one file, `--ls` narrows returned strings, and `--off` includes the documented offset and encoding information. The tool searches ASCII and Unicode strings by default. Save console messages with the command and input hash.

Open the text result as data. Record the full matching context, source file, and reported offset. If the question instead concerns IP-like text, first inspect the installed built-in patterns with `-p`, then use the documented `--lr ipv4` pattern on the same scoped input. Treat that result as text resembling an IPv4 address, not evidence of a connection.

## Review the limits

Strings can come from resources, unused code, documentation, or embedded data. A match for `powershell` does not prove PowerShell ran. A negative result does not rule out compressed, encrypted, encoded, or dynamically constructed content. Correlate leads with a format-aware parser or execution telemetry when available.

The manual states that searches append when the same `-o` filename is reused. Use a new output name for each run so earlier and later scopes do not blend. If results are empty, check file access, encoding settings, minimum string length, and the chosen term before widening scope. For large files, review the documented chunk-size option and available memory; do not silently skip files and report complete coverage.

## Sources and validation

- [Official bstrings manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/bstrings.txt)
- [bstrings repository](https://github.com/EricZimmerman/bstrings)

Sources checked October 7, 2026. Command syntax was reviewed against documentation; bstrings was not executed for this repository. No search hits are claimed.
