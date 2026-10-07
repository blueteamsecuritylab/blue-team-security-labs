# Timeline Explorer: filter and tag parser output

Which rows answer the investigation question, and which rows are hidden by the view?

Timeline Explorer sorts, filters, groups, and exports CSV, TSV, XLSX, and text data. Plugins can interpret timestamps and other values; a generic CSV may instead load as strings.

## Retain the complete parser export

Follow the [shared setup](../setup.md). Open an unchanged export such as `C:\Cases\LAB-001\output\mft\mft.csv`, with its source artifact hash, parser build, and command recorded. Only the first XLSX sheet loads. Export other required sheets separately.

## Filter, group, and tag

1. Inspect headers and **View → Messages** for the ingestion result, selected plugin, and errors.
2. Select a relevant cell and press **Ctrl+Shift+F** to filter that column by its value. Check the operator. Apply a justified time scope only after confirming the column is interpreted as a timestamp.
3. Drag a header into the grouping area. Keep identifying columns visible to distinguish similarly named files or accounts.
4. If **Line** and **Tag** columns are present, mark relevant rows in **Tag** and record the reasoning outside the grid.
5. Use **File → Export** to save a separate analysis selection. Export reflects the visible filters, sorting, and layouts. Retain the full input and record those settings.

## Check what the view leaves out

Press **Ctrl+E** to clear filters and examine surrounding rows before concluding an item is absent. Check timezone interpretation and timestamp precision; subseconds can matter for closely spaced changes. Rows remain the source parser's interpretation, not independent events created by the viewer.

If timestamps behave like text, inspect plugin recognition, unmodified headers, and **Messages** before converting data. Saved sessions retain file references and tags, but do not replace the underlying CSVs. A filtered export is an analysis selection, not the complete collection.

## References

- [Official Timeline Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/timelineexplorer.txt)
- [Author-maintained plugins](https://github.com/EricZimmerman/TLEFilePlugins)

Sources checked October 7, 2026. Documentation reviewed; GUI not run. No filtered rows or timeline findings supplied.
