# TimeApp: document the clock during a lab exercise

**Question:** What time did the analysis workstation display during the recorded lab actions?

TimeApp shows time and includes stopwatch and countdown functions. The author catalog also describes optional public-IP display. Use it as a visible clock in a benign lab recording, then compare the resulting artifacts with the recorded actions. It does not independently certify that the system clock is accurate.

## Prepare the exercise

Follow the [shared setup](../setup.md). Keep the benign exercise inputs under `C:\Cases\LAB-001\evidence` and the recording or notes under `C:\Cases\LAB-001\output\time-lab`. Record the analysis host's timezone and clock-synchronization state using your normal workstation checks. Do not change the clock to make a timeline fit.

The current catalog lists TimeApp in the .NET 4 column. Verify the selected build's actual requirements. Keep public-IP display disabled unless it is necessary for an explicitly scoped network test; displaying it can require an external lookup and can expose the lab's address in a recording.

## Record a small sequence

1. Open TimeApp and arrange its time display beside the benign lab application. Record whether the displayed value is local time or UTC.
2. Start a screen recording or a contemporaneous activity note. Keep unrelated windows and private data out of frame.
3. Perform a short, documented action sequence on benign files: for example, create a training note, rename it, and save it. Write down the action order and the displayed times.
4. If measuring elapsed time, use the documented stopwatch or countdown function and record which one was used. Do not interpret elapsed duration as an artifact timestamp.
5. Finish the recording, preserve its hash, and compare separately acquired file metadata or logs with the recorded sequence. Note differences without adjusting the source artifacts.

## Interpret and troubleshoot

The recording can show the clock value visible during an action. It does not prove a remote server or acquired device used the same clock, and display precision does not equal clock accuracy. Timezone offsets, delayed writes, and artifact-specific timestamp semantics can explain differences.

If a comparison appears inconsistent, check timezone, clock synchronization, recording continuity, and the meaning of each artifact's timestamp first. Preserve the discrepancy in the notes. Public-IP information is generally unnecessary for this local exercise and does not establish device or user identity.

## Sources and validation

- [Current author catalog](https://ericzimmerman.github.io/)
- [Official TimeApp manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/timeapp.txt)
- [TimeApp repository](https://github.com/EricZimmerman/timeapp)

Sources checked October 7, 2026. Documented capabilities were reviewed; the GUI and proposed exercise were not executed for this repository. No time measurements are claimed.
