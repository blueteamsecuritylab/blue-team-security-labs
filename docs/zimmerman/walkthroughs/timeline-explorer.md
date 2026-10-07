# Timeline Explorer: review parser rows without losing context

**Question:** Which rows answer the question, and what was hidden by the current view?

Timeline Explorer opens CSV, TSV, XLSX, and text data for sorting, filtering, grouping, and review. Tool-specific plugins can interpret timestamps and other values. A generic CSV may instead be treated as strings, so check the loaded format before relying on date filters.

## Prepare the input

Follow the [shared setup](../setup.md). Use a preserved parser export such as `C:\Cases\LAB-001\output\mft\mft.csv`, with the source artifact hash, parser build, and command in the notes. Keep the complete export unchanged. For XLSX input, the official manual states that only the first sheet loads; export other required sheets separately.

## Filter, tag, and export

1. Open the CSV in Timeline Explorer. Inspect the headers and **View → Messages** for ingestion information, plugin selection, and errors.
2. Select a relevant cell and use **Ctrl+Shift+F** to apply its value as a column filter. Check the filter operator and add a justified time scope if the column is interpreted as a timestamp.
3. Drag a column header into the grouping area to group related rows. Keep identifying columns visible so similarly named files or accounts remain distinguishable.
4. When **Line** and **Tag** columns are available, mark relevant rows in **Tag**. Record the reasoning for each selected lead outside the grid.
5. Export the current view through **File → Export** to a new analysis file. The export reflects visible data, including active filters, sorting, and layouts. Preserve the full input and write the active filters in the notes.

## Check the interpretation

Use **Ctrl+E** to clear filters and inspect surrounding rows before declaring an item absent. Review timestamp precision and timezone interpretation; retaining subseconds can matter when comparing closely spaced changes. A row represents the source parser's interpretation, not an independent event created by Timeline Explorer.

If a timestamp column behaves like text, check plugin recognition and the unmodified CSV headers. Review **Messages** rather than silently converting data. A saved session can retain open-file references and tags; it is not a replacement for preserving the underlying CSVs. Exported snippets are analysis selections, so avoid presenting them as the complete collection.

## Sources and validation

- [Official Timeline Explorer manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/timelineexplorer.txt)
- [Author-maintained plugins](https://github.com/EricZimmerman/TLEFilePlugins)

Sources checked October 7, 2026. The documented GUI steps were reviewed; the GUI was not executed for this repository. No filtered rows or timeline findings are supplied.
