# Browser to script

Search a selected endpoint window for a browser parent paired with a command or script interpreter.

Query: [browser-to-script.s1ql](../queries/sentinelone/browser-to-script.s1ql)

## Set the scope

Use SentinelOne Deep Visibility with process telemetry and access to the endpoint group. Start with the alert window, record the console timezone, and select the relevant endpoint before broadening the search.

In the published `SentinelOne.DeepVisibilityV2` example, `src.process.name` identifies the process under review and `src.process.parent.name` identifies its parent. These fields were checked against the publication's reference schema; console operators, event population, and returned rows remain untested.

## Interpret a result

The filter pairs a listed browser in the source-parent field with a listed interpreter in the source-process field. It has no event-type predicate. Inspect the event action and process tree before describing a launch; a name match does not establish a download, successful payload execution, or compromise.

## Follow up

1. Preserve the endpoint, timestamp, event action, process UID, and Storyline ID.
2. Inspect the full parent and child paths, command lines, signer information, and user context.
3. Trace related file writes, downloaded content, URLs, and network destinations in the same window.
4. Compare the chain with approved support, installation, extension, and developer activity.

## Check legitimate activity

Support tools, meeting applications, installers, and developer workflows can launch interpreters from a browser. Tune against a validated path, signer, script, or workflow. Avoid blanket suppression of browsers or interpreters.

Validation: published excerpt and field-reference review. It has not been run in a console or replayed against synthetic events; no result evidence is included.

**Provenance:** [Query Forge: Browser-to-Script Execution in SentinelOne — Basic Hunt](https://blueteamsecurity.org/blog/query-forge-sentinelone-browser-to-script-execution/).