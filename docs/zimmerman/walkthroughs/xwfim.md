# XWFIM: prepare and verify a licensed X-Ways installation

Which X-Ways version and supporting files will the analysis workstation use?

XWFIM downloads and manages X-Ways Forensics or X-Ways Investigator installations. It changes application files rather than parsing evidence. Use valid download credentials and the appropriate X-Ways license.

## Separate the installation from case data

Follow the [shared setup](../setup.md). Keep acquired material under `C:\Cases\LAB-001\evidence` and use a dedicated software destination such as `C:\Tools\XWays-Lab`. The catalog lists XWFIM under .NET 4; verify the selected build's runtime requirements.

Credentials, license material, and settings belong outside public files, screenshots, and shared logs. Enter credentials in the authorized application using the correct entitlement; XWFIM does not provide an X-Ways license.

## Install and verify the selected version

1. Supply valid credentials through XWFIM's credential interface.
2. Choose the X-Ways version from the dropdown and record the selection.
3. Confirm installation directory and folder name before **Install**. Review download and installation messages; the destination must be separate from case data.
4. Open **Tools → Verify installation**, select the installed directory, choose whether to generate a log, and select **Verify**. Check the XLSX log for sensitive content before retaining or sharing it.
5. Record version and supporting components, then review configuration before opening evidence. Installation completion does not validate an analysis method.

## Create a portable copy only after first launch

**Tools → Create portable installation** requires a successful X-Ways launch to create `WinHex.cfg`. Use a reviewed destination drive under the applicable license, confirm it before **Create**, and exclude unrelated or private files.

For a missing `WinHex.cfg`, check the intended installation and first launch rather than borrowing another investigator's configuration. Preserve reported verification differences and examine them before replacing files. Installation verification does not establish evidence integrity, tool accuracy, or license compliance.

## References

- [Official XWFIM manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/xwfim.txt)
- [Author catalog](https://ericzimmerman.github.io/)
- [X-Ways](https://www.x-ways.net/)

Sources checked October 7, 2026. Documentation reviewed; no credentials entered, software installed, portable copy created, or GUI run.
