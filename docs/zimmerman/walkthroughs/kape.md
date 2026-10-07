# KAPE: review collection separately from processing

**Question:** Which artifacts will be collected, and which programs will process them?

KAPE uses **Targets** to collect files and **Modules** to run programs. Those are different operations with different outputs. The graphical `gkape` interface displays the command it will execute, which provides a useful review point before touching a lab source.

## Check licensing and inputs

The current official FAQ states that, effective January 1, 2026, KAPE is unavailable for commercial use involving third-party networks or paid engagements. It lists government, educational, research, and internal-company use as free. Review the current FAQ and supplied EULA for your intended use; this lab guide is not an MDR client-deployment instruction or a blanket open-source license statement.

Follow the [shared setup](../setup.md). Keep acquired lab material under `C:\Cases\LAB-001\evidence`. Identify the authorized source volume explicitly. Place copied artifacts under `C:\Cases\LAB-001\work\kape-collected` and parser outputs under `C:\Cases\LAB-001\output\kape`. KAPE's official getting-started documentation requires administrator rights. Do not run it on a workplace endpoint as part of this exercise.

## Review and execute an authorized lab workflow

1. Open `gkape` from the KAPE directory. Select **Use Target options**. Set the verified lab source and the separate collection destination.
2. Select only the reviewed Target definitions needed for the question. Inspect their paths and scope; the displayed command updates as selections change.
3. Use **Copy** to preserve the proposed command in the run notes. Review it before **Execute**. Keep destination-flush options disabled: `--tflush` and `--mflush` delete their respective destination directories.
4. Review collection logs and copied files before analysis. Record gaps and exclusions.
5. For a separate processing run, select **Use Module options** with the collection as Module source and the output directory as Module destination. Review each Module command and its required binary before execution. Preserve the resulting parser logs and outputs.

## Review the boundaries

Targets collect a configured subset, not a complete disk image. Modules run their configured programs; KAPE does not automatically supply every required binary. Missing programs or skipped files mean the run is incomplete. Updating Target, Module, or parser definitions changes the procedure, so record and preserve their revisions. A successful collection is not a finding of compromise.

## Sources and validation

- [Official getting-started guide](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/2.-Getting-started.md)
- [Official gkape guide](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/5.-gkape.md)
- [Current licensing FAQ](https://github.com/EricZimmerman/KapeDocs/blob/master/Pages/50-Frequently-asked-questions.md)

Sources checked October 7, 2026. Documentation was reviewed; KAPE was not installed or executed, and no endpoint collection was performed for this repository.
