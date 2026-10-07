# EZViewer: inspect documents and raw bytes

What content can be read without opening the file in its usual authoring application?

EZViewer displays supported document, spreadsheet, text, web, and PDF formats read-only. Unsupported files open in a hex view with a data interpreter.

## Open a working copy

Follow the [shared setup](../setup.md). Use a benign document such as `C:\Cases\LAB-001\evidence\documents\training-note.docx`, record its hash, and retain the original separately. The current GUI download is listed under .NET 9; check requirements for the selected build.

1. Load the copied document using the file-opening control. Confirm its filename and path.
2. Read the relevant passages. Use **Ctrl plus mouse-wheel scrolling** to zoom.
3. For an unsupported file, inspect the hex display and record offsets and bytes. Renaming the extension to force another view can obscure the actual format.
4. Compare the displayed content with the file's purpose. A filename alone cannot establish document origin.
5. Save notes separately. Label any screenshot with the input hash, viewer build, and whether it shows rendered content or raw bytes.

## Distinguish a view from a complete parse

Read-only mode prevents editing through EZViewer, but does not guarantee that every document feature or embedded object appears. Visible text supports a content observation; it does not prove a user read the document or an embedded command executed. Binary fields shown in hex need format-aware interpretation.

For incomplete rendering, preserve the file and compare it with an appropriate parser. Missing content in the view does not establish that it never existed. For launch errors, check runtime, extraction, and file access using the shared setup. Suspicious-file inspection belongs in the authorized analysis environment; viewing requires neither executing the input nor following its links.

## References

- [Author catalog and requirements](https://ericzimmerman.github.io/)
- [Official EZViewer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/ezviewer.txt)

Sources checked October 7, 2026. Documentation reviewed; GUI not run. No screenshot or rendered result claimed.
