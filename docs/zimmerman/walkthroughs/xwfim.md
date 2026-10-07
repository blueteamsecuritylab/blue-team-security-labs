# XWFIM: prepare and verify a licensed X-Ways installation

**Question:** Which X-Ways installation and supporting files will the lab use?

XWFIM manages local X-Ways Forensics or X-Ways Investigator installations. It downloads and changes application files; it is not an evidence parser. Use it during controlled workstation preparation, with valid X-Ways download credentials and the appropriate license.

## Separate software from evidence

Follow the [shared setup](../setup.md). Keep acquired material under `C:\Cases\LAB-001\evidence`, outside the installation destination. Choose a reviewed software path such as `C:\Tools\XWays-Lab`. The current author catalog lists XWFIM in the .NET 4 column; check the selected build's actual runtime requirements.

Credentials, license material, and installation settings can be sensitive. Enter credentials only into the authorized application, and keep them out of public repository files, screenshots, and logs shared with others. Do not use someone else's entitlement or assume the manager provides an X-Ways license.

## Prepare and verify

1. Open XWFIM and supply valid download credentials through its credential interface.
2. Select the intended X-Ways version in the version dropdown. Record why that version is being prepared.
3. Confirm the installation directory and X-Ways folder name before selecting **Install**. Use a dedicated destination, not an existing case directory. Review download and installation messages.
4. Use **Tools → Verify installation**. Select the installed directory, choose whether to generate a log, and select **Verify**. The manual describes an XLSX verification log when logging is enabled; preserve it after checking for sensitive content.
5. Record the installed version and supporting components before opening evidence in X-Ways. Configuration review remains necessary; a completed install is not validation of an analysis method.

## Portable installation and troubleshooting

The documented **Tools → Create portable installation** workflow requires that X-Ways has already been launched successfully to create `WinHex.cfg`. Only create a portable copy on a reviewed destination drive under your license terms. Confirm the destination before selecting **Create**, and keep unrelated or private files off that drive.

If `WinHex.cfg` is missing, check the intended installation and first-launch requirement rather than copying configuration from a different investigator. If verification reports differences, preserve the log and examine them before replacing files. XWFIM's verification concerns software installation integrity; it does not verify case evidence, tool accuracy, or license compliance by itself.

## Sources and validation

- [Official XWFIM manual](https://github.com/EZToolsManuals/EZToolsManuals/blob/main/manuscript/xwfim.txt)
- [Author catalog](https://ericzimmerman.github.io/)
- [X-Ways](https://www.x-ways.net/)

Sources checked October 7, 2026. The documented workflow was reviewed; no credentials were entered, software installed, portable copy created, or GUI execution performed for this repository.
