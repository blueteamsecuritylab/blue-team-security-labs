# VSCMount: expose historical lab snapshots for examination

**Question:** Does an existing volume shadow copy contain an artifact missing from the acquired current state?

VSCMount is a command-line tool that maps available volume shadow copies to symbolic-link paths. It interacts with the analysis host. Use it only within a planned lab acquisition workflow, with the intended source volume explicitly identified; it is not a command to run casually against the workstation's system drive.

## Prepare the source

Follow the [shared setup](../setup.md). Keep the acquired lab image under `C:\Cases\LAB-001\evidence\images`. The imaging workflow must already have exposed the authorized lab volume in a form that makes its shadow copies available. In this example, **Q:** is the verified lab volume, not a default or assumed drive letter. Record the image hash, mounting method, write-protection arrangement, and source-volume identity before proceeding.

## Map and inspect

From the reviewed VSCMount directory in the approved elevated lab environment:

```powershell
.\VSCMount.exe --dl Q --mp 'C:\Cases\LAB-001\work\vsc-links' --ud true
```

`--dl` identifies the source drive; `--mp` selects the base mapping directory. `--ud` requests snapshot creation timestamps in the symbolic-link names. Older documentation differs about its default, so specify the intended value and compare installed help before running.

Inspect the created mappings and record which snapshot supplies each artifact. Copy required files into a separately identified working-evidence location, preserving the snapshot identifier and timestamp in acquisition notes. Process those copies with the relevant parser. Compare historical and current artifacts by source and time, not just by filename.

## Review and clean up

Snapshot creation time is the snapshot's time, not the timestamp of every file it contains. Missing snapshots may reflect retention or acquisition limitations; an empty mapping does not prove the file never existed. Repeated snapshots can contain the same bytes, so retain provenance even when deduplicating analysis copies.

When finished, follow the acquisition workflow to remove the created mappings and unmount the lab image. Review the paths first; do not delete the underlying shadow copies or recursively remove a linked evidence tree. This guide supplies no destructive cleanup command. If snapshots are absent, verify the source drive and mounting method rather than switching to the live system volume.

## Sources and validation

- [Official VSCMount manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/vscmount.txt)
- [VSCMount repository and CLI](https://github.com/EricZimmerman/VSCMount)

Sources checked October 7, 2026. The documented switches were reviewed; no mapping, image mount, or parser execution was performed for this repository.
