# Chris Sotraidis: Native Classics

Native game ports for iPhone and iPad, distributed through AltStore Classic.

**Preparation status:** 14 published IPAs have been checked and listed. End-to-end installation through this source is still pending. Most apps are previews; see the [launch checklist](docs/LAUNCH.md) before announcing or requesting a feature.

## Add the source

Install [AltStore Classic with AltServer](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) on your iPhone/iPad and Mac, or follow the [Windows instructions](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows).

In AltStore Classic, open Sources and add this URL:

```text
https://raw.githubusercontent.com/chrissotraidis/altstore/main/source.json
```

The catalog is hosted from this repository's `main` branch. Choose an app from the source and follow its project-specific game-data setup guide. AltStore signs the downloaded IPA for your Apple account. See the [Classic getting-started guide](https://faq.altstore.io/altstore-classic/your-altstore) for refresh requirements and app limits.

The source serves iPhone/iPad apps. Mac, Android and Apple TV packages are distributed separately by the individual projects.

## Apps

Names follow the projects' READMEs and the downloaded apps' display names. Versions below are the selected public iOS releases, not necessarily the most recently uploaded diagnostic artifact.

| App | What it is | Selected release | Device / minimum OS |
| --- | --- | --- | --- |
| [KartPad](https://github.com/chrissotraidis/kartpad) | Mario Kart Wii for iPhone and iPad | [0.4.24](https://github.com/chrissotraidis/kartpad/releases/tag/v0.4.24-ios.1) | iPhone / iPad; 16.0+ |
| [HarkinianPad](https://github.com/chrissotraidis/harkinianpad) | Ocarina of Time for iPhone and iPad | [0.1.0 Preview 5](https://github.com/chrissotraidis/harkinianpad/releases/tag/v0.1.0-preview.5) | iPhone / iPad; 14.0+ |
| [GoldenPad](https://github.com/chrissotraidis/goldenpad) | GoldenEye 007 for iPhone and iPad | [0.1.0 Preview 9](https://github.com/chrissotraidis/goldenpad/releases/tag/v0.1.0-preview.9) | iPhone / iPad; 17.0+ |
| [SunPad](https://github.com/chrissotraidis/sunpad) | Super Mario Sunshine for iPhone and iPad | [0.1.0 Preview 13](https://github.com/chrissotraidis/sunpad/releases/tag/v0.1.0-preview.13) | iPhone / iPad; 16.0+ |
| [SpaghettiPad](https://github.com/chrissotraidis/spaghettipad) | Mario Kart 64 for iPhone and iPad | [0.1.0 Preview 6](https://github.com/chrissotraidis/spaghettipad/releases/tag/v0.1.0-preview.6) | iPhone / iPad; 15.0+ |
| [UTP](https://github.com/chrissotraidis/utp) | Unreal Tournament 99 for iPhone and iPad | [0.1.0 Preview 3](https://github.com/chrissotraidis/utp/releases/tag/v0.1.0-preview.3) | iPhone / iPad; 17.0+ |
| [BrawlerPad](https://github.com/chrissotraidis/brawlerpad) | Super Smash Bros. 64 for iPhone and iPad | [0.1.0 Preview 2](https://github.com/chrissotraidis/brawlerpad/releases/tag/v0.1.0-preview.2) | iPhone / iPad; 17.0+ |
| [MaskPad](https://github.com/chrissotraidis/maskpad) | Majora's Mask for iPhone and iPad | [0.1.2](https://github.com/chrissotraidis/maskpad/releases/tag/v0.1.2) | iPhone / iPad; 14.0+ |
| [StarshipPad](https://github.com/chrissotraidis/starshippad) | Star Fox 64 for iPhone and iPad | [0.1.0 Preview 5](https://github.com/chrissotraidis/starshippad/releases/tag/v0.1.0-preview.5) | iPhone / iPad; 16.0+ |
| [PaperPad](https://github.com/chrissotraidis/paperpad) | Paper Mario for iPhone and iPad | [0.1.0 Preview 2](https://github.com/chrissotraidis/paperpad/releases/tag/v0.1.0-preview.2) | iPhone / iPad; 15.0+ |
| [CaesarPad](https://github.com/chrissotraidis/caesarpad) | Caesar III through Augustus, designed for iPad | [0.1.0 Preview 1](https://github.com/chrissotraidis/caesarpad/releases/tag/v0.1.0-preview.1) | Designed for iPad; 14.0+ |
| [DinoPad](https://github.com/chrissotraidis/dinopad) | Dinosaur Planet: Prototype Mode | [0.1.2](https://github.com/chrissotraidis/dinopad/releases/tag/v0.1.2) | iPhone / iPad; 15.0+ |
| [Bellpad](https://github.com/chrissotraidis/bellpad) | Animal Crossing for iPhone and iPad | [0.1.0 Preview 2](https://github.com/chrissotraidis/bellpad/releases/tag/v0.1.0-preview.2) | iPhone / iPad; 17.0+ |
| [PeonPad](https://github.com/chrissotraidis/peonpad) | Warcraft II through Stratagus on iPad | [0.1.0 Preview 1](https://github.com/chrissotraidis/peonpad/releases/tag/v0.1.0-preview.1) | iPad; 16.0+ |
| [DevilTouch](https://github.com/chrissotraidis/deviltouch) | Diablo and Hellfire through DevilutionX on iPad | Awaiting a public IPA | iPad |

DevilTouch is planned but is not in `source.json` because it has no public IPA. DinoPad offers **Prototype Mode only**, without Restored Adventure. CaesarPad is designed for iPad even though its current IPA declares both iPhone and iPad. Minimum OS values are package targets, not a promise of testing on every supported device.

The source's five highlighted apps follow the first five projects in the requested lineup. All 14 available apps remain in the catalog.

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

Icons and screenshots link to pinned commits in the original repositories. The initial audit checked that those images are accessible and decodable. Most screenshots are existing iPad documentation captures; StarshipPad's is a Simulator capture. DinoPad needs a suitable public Prototype Mode capture before adding a screenshot.

Based on the initial Classic source prepared by Matt from AltStore. [AltStore source format](https://faq.altstore.io/developers/make-a-source)
