# Browser to script

**Question:** Did a browser parent appear with a command or script interpreter in the selected endpoint scope?

**Query:** [browser-to-script.s1ql](../queries/sentinelone/browser-to-script.s1ql)

## Before running

Use SentinelOne Deep Visibility with process telemetry and permission to search the relevant endpoint group. Set an alert-sized console time window and record its timezone. Narrow to the relevant endpoint using console scope or an endpoint filter before broadening.

The example uses the published `SentinelOne.DeepVisibilityV2` source-parent convention: `src.process.name` identifies the process under review and `src.process.parent.name` identifies its parent. Those fields were checked against the source publication's reference schema. Operators, event population, and returned rows have not been tested here.

## Read the match

The filter selects rows with a listed browser in the source-parent field and a listed interpreter in the source-process field. It does not constrain event type, so inspect the returned event action and process tree before treating a row as a process launch. A name match alone does not establish a download, successful payload execution, or compromise.

## Next pivots

1. Preserve the endpoint, timestamp, event action, process UID, and Storyline ID.
2. Inspect the full parent and child paths, command lines, signer information, and user context.
3. Trace related file writes, downloaded content, URLs, and network destinations in the same window.
4. Compare the chain with approved support, installation, extension, and developer activity.

## Expected benign matches

Browser-based support tools, meeting applications, software installers, and developer workflows can launch interpreters. Prefer a specific validated path, signer, script, or workflow for tuning. Do not suppress all browsers or script interpreters.

**Status:** Published excerpt and field-reference review only. No console execution, synthetic event replay, or result evidence supplied.

**Provenance:** [Query Forge: Browser-to-Script Execution in SentinelOne — Basic Hunt](https://blueteamsecurity.org/blog/query-forge-sentinelone-browser-to-script-execution/).
