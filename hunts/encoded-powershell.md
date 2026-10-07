# Encoded PowerShell

Find Windows PowerShell command lines containing encoded-command fragments.

Query: [encoded-powershell.s1ql](../queries/sentinelone/encoded-powershell.s1ql)

## Set the scope

Use SentinelOne Deep Visibility with populated source-process names and command lines. Select a short console window and the relevant endpoint group, then record that scope in the hunt record.

The two `SentinelOne.DeepVisibilityV2` field names were reviewed against the publication's reference schema. Console syntax and event population remain untested.

## Interpret a result

The published query searches `powershell.exe` for `-enc` or `-encodedcommand`. The longer substring contains the shorter one; both conditions are retained from the article.

The query omits PowerShell 7's `pwsh.exe`, an event-type predicate, and case-insensitive matching. Check console matching behavior before adapting it, and record any changes. Truncated command lines and abbreviated switches can leave gaps.

## Follow up

1. Review the complete command line, process path, parent, user, and endpoint role.
2. Preserve the original encoded string. Decode it only as data in an approved isolated workflow.
3. Inspect related script files, child processes, and destinations around the event.
4. Compare recurrence with approved deployment and administration activity.

## Check legitimate activity

Deployment tools, administrative automation, and security products can use encoded commands. An unrelated argument can also contain the searched substring. Establish the command's purpose before escalation or tuning.

Validation: published excerpt and field-reference review. It has not been run in a console; no decoded sample evidence is included. The query performs no response action.

**Provenance:** [SentinelOne Threat Hunting With Deep Visibility — Encoded PowerShell behavior](https://blueteamsecurity.org/blog/sentinelone-threat-hunting-with-deep-visibility/).