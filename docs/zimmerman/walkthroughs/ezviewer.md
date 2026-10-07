# EZViewer: inspect a copied document or unknown file

**Question:** What can be read from the copied file without opening its usual authoring application?

EZViewer is a read-only viewer for several document, spreadsheet, text, web, and PDF formats. Unsupported files are displayed in a hex view with a data interpreter. Use it to inspect a working copy and decide which specialist parser is needed next.

## Prepare the input

Follow the [shared setup](../setup.md). Use a benign lab document such as `C:\Cases\LAB-001\evidence\documents\training-note.docx`, with a recorded hash. Keep the original artifact separate. Obtain the current viewer from the author catalog and check the requirements for that exact build; the current GUI download is listed under .NET 9.

## Open and inspect

1. Start EZViewer on the analysis workstation. Use its file-opening control to load the copied document, confirming the filename and path.
2. Read the rendered content and record the passages relevant to the lab question. The manual documents **Ctrl plus mouse-wheel scrolling** for zooming.
3. If the file is unsupported, inspect the hex display instead. Note offsets and the actual bytes being interpreted; do not rename the extension merely to force a particular viewer.
4. Compare the visible content with the file's purpose. For example, a benign training note can establish what the viewer displays, while its filename alone cannot establish the document's origin.
5. Save analysis notes separately. If screenshots are useful, label the input hash, viewer build, and whether the image shows rendered content or raw bytes.

## What the view means

Read-only viewing prevents editing through EZViewer; it is not a guarantee that every document feature or embedded object is represented. Text visible on screen is evidence of content in the copied artifact, not proof that a user read it or that an embedded command executed. An unknown binary shown in hex needs format-aware analysis before its fields are interpreted.

If a document looks incomplete, retain the file and compare with an appropriate parser rather than assuming the missing portion never existed. If launch fails, check the runtime, extraction, and file access guidance in the shared setup. Keep any suspicious-file work inside the authorized analysis environment; this guide does not require running the input or following links inside it.

## Sources and validation

- [Author catalog and requirements](https://ericzimmerman.github.io/)
- [Official EZViewer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/ezviewer.txt)

Sources checked October 7, 2026. The documented capabilities and viewing workflow were reviewed; the GUI was not executed for this repository. No screenshot or rendered result is claimed.
