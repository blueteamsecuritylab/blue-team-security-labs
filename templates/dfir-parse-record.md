# DFIR parse record

Use this record for one input set and one tool/configuration run. Blank fields are prompts, not example findings. Keep actual evidence and private paths in the authorized case workspace.

| Item | Record |
| --- | --- |
| Case / lab identifier | |
| Investigation question | |
| Analyst and run time (UTC) | |
| Acquisition method and source | |
| Acquired copy and companion files | |
| Input SHA-256 and acquisition hashes | |
| Parser name, version, executable SHA-256 | |
| Runtime and analysis OS | |
| Batch / map / plugin files and SHA-256 | |
| Exact command or GUI actions | |
| Input and output locations | |
| Timestamp semantics and display timezone | |
| Conversion rules for naive timestamps | |
| Output hashes and record counts | |
| Warnings, failures, exclusions, and gaps | |
| Finding supported by returned records | |
| Corroborating source and record identifier | |
| Remaining uncertainty and next pivot | |

Retain the original parser output. Record any derived view, filter, aggregation, or hive replay separately. A hash identifies bytes; it does not prove acquisition quality or establish activity by itself.
