# KAPE: collect artifacts, then process the collection

Which files will the Target definitions collect, and which programs will the Modules run?

KAPE separates collection through Targets from program execution through Modules. Its `gkape` interface shows the command that will run as options are selected.

## Confirm permitted use and lab scope

The official FAQ states that commercial use on third-party networks or paid engagements is unavailable from January 1, 2026. Government, educational, research, and internal-company use is listed as free. Check the current FAQ and supplied EULA for the intended use. KAPE is not covered by a blanket open-source permission, and this example does not authorize MDR client deployment.

Follow the [shared setup](../setup.md). Use an explicitly identified lab source, with acquired material under `C:\Cases\LAB-001\evidence`, collection output under `C:\Cases\LAB-001\work\kape-collected`, and parser output under `C:\Cases\LAB-001\output\kape`. KAPE requires administrator rights. The exercise does not include workplace endpoints.

## Review the collection command

1. Open `gkape` from the KAPE directory and select **Use Target options**. Set the verified source and collection destination.
2. Select the required Target definitions and inspect their paths and scope. Check the updated command shown in the interface.
3. Use **Copy** to save the command before **Execute**. Leave `--tflush` and `--mflush` disabled: each deletes its destination directory.
4. Review collection logs and copied files, recording gaps and exclusions before analysis.

## Run reviewed Modules against the collection

Select **Use Module options**, using the collection as Module source and the separate output directory as destination. Review each Module's command and required binary, then preserve parser logs and outputs.

Targets collect a configured subset, not a complete image. KAPE does not automatically supply every Module binary. Missing programs and skipped files leave an incomplete run. Retain Target, Module, and parser revisions; updates change the procedure. Collection success alone does not indicate compromise.

## References

- [Official getting-started guide](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/2.-Getting-started.md)
- [Official gkape guide](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/5.-gkape.md)
- [Current licensing FAQ](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/50-Frequently-asked-questions.md)

Sources checked October 7, 2026. Documentation reviewed; KAPE not installed or run. No endpoint collection performed.
