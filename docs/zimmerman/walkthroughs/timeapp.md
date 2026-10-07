# TimeApp: record workstation time during an exercise

What clock value was displayed when the lab actions occurred?

TimeApp provides local/UTC time, stopwatch, and countdown functions, with optional public-IP display. It supplies visible timing context for a recording, not independent proof that the workstation clock is accurate.

## Record the clock state

Follow the [shared setup](../setup.md). Keep benign inputs under `C:\Cases\LAB-001\evidence` and recordings or notes under `C:\Cases\LAB-001\output\time-lab`. Record timezone and clock-synchronization state; leave the clock unchanged when comparing artifacts.

The catalog lists TimeApp under .NET 4. Check the selected build's requirements. Leave public-IP display disabled for local work: it can make an external lookup and expose the address in the recording. Enable it only for a scoped network test that needs it.

## Record an action sequence

1. Place TimeApp beside the benign lab application. Note whether its displayed time is local or UTC.
2. Start a screen recording or contemporaneous activity note, excluding unrelated windows and private data.
3. Create, rename, and save a benign training note. Record action order and the visible times.
4. If measuring elapsed time, note whether the stopwatch or countdown was used. Duration is not an artifact timestamp.
5. Preserve the recording's hash and compare separately acquired metadata or logs with the sequence. Record discrepancies without adjusting source artifacts.

## Compare clocks and timestamp meanings

The recording establishes the visible clock value during an action, not that a remote server or acquired device shared that clock. Display precision is not clock accuracy. Timezone offsets, delayed writes, and different artifact timestamp semantics can explain discrepancies.

Check timezone, synchronization, recording continuity, and the meaning of each timestamp before interpreting a mismatch. Retain the discrepancy in the notes. Public-IP display adds no timing assurance and does not establish device or user identity.

## References

- [Current author catalog](https://ericzimmerman.github.io/)
- [Official TimeApp manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/timeapp.txt)
- [TimeApp repository](https://github.com/EricZimmerman/timeapp)

Sources checked October 7, 2026. Documentation reviewed; GUI and proposed exercise not run. No time measurements claimed.
