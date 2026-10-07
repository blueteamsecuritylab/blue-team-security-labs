# VSCMount: map historical snapshots on a lab volume

Does an available shadow copy contain an artifact missing from the acquired current state?

VSCMount maps existing volume shadow copies through symbolic links on the analysis host. Identify the intended lab source before running it; the workstation's system drive is outside this example's scope.

## Verify the source volume

Follow the [shared setup](../setup.md). Keep the acquired image under `C:\Cases\LAB-001\evidence\images`. The imaging workflow must expose its shadow copies to the host. Here, `Q:` represents the verified lab volume, not an assumed drive letter. Record image hash, source identity, mounting method, and write-protection arrangement.

## Create mappings and copy artifacts

Run from the VSCMount directory in the approved elevated lab environment:

```powershell
.\VSCMount.exe --dl Q --mp 'C:\Cases\LAB-001\work\vsc-links' --ud true
```

`--dl` selects the source drive and `--mp` the mapping directory. `--ud` requests snapshot creation timestamps in link names. Older documentation gives differing defaults; specify the value and check installed help.

Record which snapshot supplies each copied artifact. Keep its identifier and creation time with the working-evidence copy, then process that copy with the appropriate parser. Compare historical and current artifacts by source and time, not filename alone.

## Preserve snapshot provenance during cleanup

A snapshot's creation time is not every contained file's timestamp. Missing snapshots can reflect retention or acquisition limitations; an empty mapping does not prove a file never existed. Identical bytes in several snapshots still have distinct provenance, even when analysis copies are deduplicated.

Remove the mappings and unmount the image through the acquisition workflow. Review paths first: deleting underlying snapshots or recursively removing a linked evidence tree would destroy source material. No destructive cleanup command is included. If snapshots are missing, check the source drive and mounting method rather than switching to the live system volume.

## References

- [Official VSCMount manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/vscmount.txt)
- [VSCMount repository and CLI](https://github.com/EricZimmerman/VSCMount)

Sources checked October 7, 2026. Switches reviewed; no mapping, image mount, or parser execution performed.
