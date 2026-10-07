# Encoded PowerShell

**Question:** Which Windows PowerShell command lines include encoded-command fragments in the selected scope?

**Query:** [encoded-powershell.s1ql](../queries/sentinelone/encoded-powershell.s1ql)

## Before running

Use SentinelOne Deep Visibility with populated source-process names and command lines. Set a short console time window and an appropriate endpoint group. Preserve that scope in the hunt record.

The source publication uses `SentinelOne.DeepVisibilityV2` fields. The two referenced field names were reviewed against that source schema; console syntax and event population have not been tested here.

## Read the match

This literal excerpt searches `powershell.exe` and the substrings `-enc` or `-encodedcommand`. The longer substring also contains the shorter one. The example retains both conditions as published.

The literal query does not include PowerShell 7's `pwsh.exe`, an event-type predicate, or case-insensitive matching. Document those limits and check console matching behavior before adapting it. Truncated command lines or abbreviated switches can also leave gaps.

## Next pivots

1. Review the complete command line, process path, parent, user, and endpoint role.
2. Preserve the original encoded string. Decode it only as data in an approved isolated workflow.
3. Inspect related script files, child processes, and destinations around the event.
4. Compare recurrence with approved deployment and administration activity.

## Expected benign matches

Deployment tools, administrative automation, and security products can use encoded commands. A match can also be an unrelated argument containing the substring. Review the command's purpose before escalation or tuning.

**Status:** Published excerpt and field-reference review only. No console execution or decoded sample evidence supplied. This is hunting logic with no response action.

**Provenance:** [SentinelOne Threat Hunting With Deep Visibility — Encoded PowerShell behavior](https://blueteamsecurity.org/blog/sentinelone-threat-hunting-with-deep-visibility/).
