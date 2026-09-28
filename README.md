# Kahris' Apps

Native game ports for iPhone and iPad, maintained by Kahris and available through AltStore Classic.

> **Work in progress.** This catalog is being rebuilt. Previous builds have been retired; new versions will be added here as they are ready.

## Add the source

Install [AltStore Classic with AltServer](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) on your iPhone/iPad and Mac, or follow the [Windows instructions](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows).

In AltStore Classic, open Sources and add this URL:

```text
https://raw.githubusercontent.com/chrissotraidis/altstore/main/source.json
```

The catalog is hosted from this repository's `main` branch. Choose an app from the source and follow its project-specific game-data setup guide. AltStore signs the downloaded IPA for your Apple account. See the [Classic getting-started guide](https://faq.altstore.io/altstore-classic/your-altstore) for refresh requirements and app limits.

The source serves iPhone/iPad apps. Mac, Android and Apple TV packages are distributed separately by the individual projects.

The catalog's downloads and metadata have been checked. Installation and updates through this source still need device testing; see the [launch status](docs/LAUNCH.md).

## Apps

The catalog uses the latest published iPhone/iPad releases. Release labels are retained where applicable; each project documents its known issues.

| App | What it is | Selected release | Device / minimum OS |
| --- | --- | --- | --- |
| [CaesarPad](https://github.com/chrissotraidis/caesarpad) | Caesar III through Augustus, designed for iPad | [0.1.0 Preview 1](https://github.com/chrissotraidis/caesarpad/releases/tag/v0.1.0-preview.1) | Designed for iPad; 14.0+ |
| [PeonPad](https://github.com/chrissotraidis/peonpad) | Warcraft II through Stratagus on iPad | [0.1.0 Preview 1](https://github.com/chrissotraidis/peonpad/releases/tag/v0.1.0-preview.1) | iPad; 16.0+ |

CaesarPad is designed for iPad; its package also declares iPhone support, which is not a claim of equivalent iPhone testing. Minimum OS values come from the app packages, not AltStore Classic's own requirements.

The catalog currently lists 2 apps.

## Game setup and support

Game data is not included in these downloads. Use each project's setup guide for its supported files and import process. Optional mods and texture packs may need separate installation.

Open the app's linked GitHub repository for controls, known issues, credits, licenses and support. For a broken source listing or download link, [open an issue here](https://github.com/chrissotraidis/altstore/issues). For an app crash or gameplay problem, use that app's issue tracker.

Back up saves before changing signing or installation setups. Update existing apps in place using the same signing identity; uninstalling can remove their data.


These are independently maintained community projects. Their upstream projects and game rights holders retain their respective rights. Inclusion in this catalog is not a claim of endorsement.

## Maintaining the catalog

This repository holds the catalog and documentation. App source code and IPA files stay in their existing project repositories and GitHub Releases.

```text
source.json                 AltStore catalog
README.md                   Installation, app list and support
docs/LAUNCH.md              Remaining launch work and message draft
docs/catalog-audit.json     Release selection and package evidence
scripts/validate_source.py  Catalog consistency check
```

Run `python3 scripts/validate_source.py` before committing catalog changes. This checks structure and consistency with the recorded audit; it is not an AltStore installation test.

For a new app release, publish and verify the new IPA first, then add its version entry at the start of the app's `versions` array. Use its actual version/build numbers and update the URL, date, size, checksum and permissions as necessary. Retain older entries. Refresh the audit and table, and test the candidate source before updating the public source. [Official update instructions](https://faq.altstore.io/developers/updating-apps)

Pushing application code or publishing a GitHub Release does not automatically change this catalog. Conversely, publishing a changed catalog can make a new version available immediately. Test future changes on a separate branch/source URL first.

Icons and screenshots link to pinned commits in the original repositories. Screenshots are existing iPad captures.

## Support my work

If you enjoy my work, you can optionally [support me on Patreon](https://www.patreon.com/cw/ChrisSotraidis). All apps and updates in this catalog remain freely available. Supporting is never required.

Based on the initial Classic source prepared by Matt from AltStore. [AltStore source format](https://faq.altstore.io/developers/make-a-source)
