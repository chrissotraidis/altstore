# Kahris' Apps: launch plan

Updated on 17 September 2026. The catalog is hosted and contains 14 apps. DevilTouch's updated IPA is being prepared separately. Classic source testing and Matt's Featured Lists placement are the remaining distribution steps.

## What is ready

- [x] Review all 15 requested public repositories and their release notes.
- [x] Select 14 published iPhone/iPad IPAs; exclude Mac, Android and Apple TV artifacts.
- [x] Download all 14 selected IPAs anonymously, verify ZIP integrity, and match byte sizes and SHA-256 against GitHub asset metadata.
- [x] Read actual bundle IDs, display names, versions, build numbers, device families and privacy descriptions from the packages.
- [x] Inspect code signatures/entitlements, including SunPad's nested module and UTP's dynamic libraries.
- [x] Confirm iOS platform and deployment targets from Mach-O build commands.
- [x] Write descriptions based on project READMEs and selected release notes.
- [x] Add 14 app icons and 13 existing iPad screenshots using verified, commit-pinned public URLs and actual dimensions.
- [x] Prepare the source, README, package audit and local validator.

Package inspection did not constitute a new full game-data/license audit, gameplay test or AltStore install. Existing release boundaries and upstream notices still apply. Public downloads were inspected locally; no ROMs, saves or signing material were collected.

## Decisions already made

| Project | Decision |
| --- | --- |
| KartPad | Use yesterday's 0.4.24 build 49, published September 16. September 17's build 51 is explicitly a diagnostic preview with extra instrumentation, so it is excluded under the owner's instruction. |
| UTP | Use the newest published IPA, `v0.1.0-issue-6-test.1`, as requested by the owner, who confirms it works. Its package targets iOS 15+. GitHub still labels it an iOS 15 compatibility test/prerelease; this catalog does not edit that historical record. See the update-numbering note below. |
| SunPad | Keep the latest iPhone/iPad Preview 13. Signing the app and its internal module is part of installation, not a reason to rebuild it for this catalog. Verify the Classic installation path. |
| DinoPad | Ready for the lineup per the owner; keep public 0.1.2. Describe it as Dinosaur Planet for iPhone and iPad. The release's term Prototype Mode refers to the original game content, not the readiness of the app. Restored Adventure modifications are not bundled. |
| PeonPad | Label iPad-only. Preview 1 is actually version 0.1.0 **build 4**. Explain desktop extraction and manual `data.Wargus` setup. |
| CaesarPad | Describe as designed for iPad. Its IPA also declares iPhone; that does not establish a tested iPhone experience. |
| Bellpad | Preserve the project's spelling, **Bellpad**. Its plist omits `MinimumOSVersion`; executable metadata confirms iOS 17.0. Verify install behavior; repair app packaging in its own project if Classic rejects it. |
| DevilTouch | Updated IPA in preparation in its own project. Add it once the owner has completed that release and its metadata is verified. |

The source and app developer labels use the alias **Kahris**. Existing GitHub account URLs and app bundle identifiers are unchanged. App order follows the owner's list; the five source highlights are KartPad, HarkinianPad, GoldenPad, SunPad and SpaghettiPad. This is independent of Matt's proposed Featured Lists placement.

## UTP update numbering

The old Preview 3 IPA and the newest compatibility IPA both report **version 0.1.0, build 3** internally. Their files and checksums differ. The catalog now serves the compatibility IPA and uses its actual iOS 15 minimum, but this change cannot create an automatic version-based update notification for existing Preview 3 installations.

Do not invent a higher build number in the JSON or create two entries with the same version/build. The previous download is retained in the audit history instead. For automatic upgrades, the next UTP release needs a new internal build number, then a matching catalog entry. If replacing an existing installation manually, use the same signing identity and preserve app data; do not uninstall merely to force an update.

## SunPad installation

SunPad's IPA includes the app and an internal executable module, `gGMSE01_recomp.dylib`. Both must be signed for the user's device. Keep the existing public unsigned IPA in the catalog; signing occurs in the installation workflow. The remaining check is whether the installed Classic/AltServer version signs and launches that package correctly. No signing credentials belong in this repository, and no new SunPad build is requested merely because the module exists.

## Next steps, in order

1. **Finish DevilTouch separately.** When its updated IPA is published, verify its actual version/build, bundle ID, permissions, minimum OS, byte size and checksum, then add its listing. The existing 14 apps can be tested now.
2. **Use the hosted catalog for testing.** This repository's `main` branch hosts the source; the README contains its permanent raw URL. No separate server or website is required for this setup. The source is public to anyone with its URL, while device acceptance and Featured Lists placement remain pending. Run `python3 scripts/validate_source.py` before subsequent catalog changes.
3. **Test through AltStore Classic.** Add that exact source URL on a real device. Check the source name, all app cards, icons, screenshot proportions and preview labels. Install the selected apps through the source, complete their documented game-data setup, and verify launch, input, audio and saving. Give SunPad's nested signing and UTP's libraries explicit attention. Check PeonPad on iPad and that iPad-only restrictions are respected. Start with KartPad and HarkinianPad if testing incrementally.
4. **Test an update with preserved data.** Using a staging source URL and a backed-up app, verify an older selected build can update to a newer build using the same Apple account/bundle setup. Confirm imported files, settings and saves remain. Do not put old versions ahead of newer ones in the public catalog to simulate an update. Record failures before changing app code.
5. **Send Matt the source and results.** Ask about Featured Lists eligibility, required art/metadata, and whether preview apps or an additional review affect inclusion. A working source and a featured listing are separate milestones. The message below is ready to adapt; it has not been sent.
6. **Announce the tested lineup.** Resolve or remove failed candidates first. Update this record and README to reflect actual testing. Update the selected app READMEs with the source link after those apps are accepted. Add an optional source news item when the launch is ready.

Screenshots are documentation captures, not fresh captures of every selected IPA. Review their presentation in Classic. StarshipPad uses its explicitly identified Simulator hero. Capture DinoPad gameplay from the public release before adding its screenshot; the existing README hero shows the separate Restored Adventure modification. This optional image does not block including DinoPad. Extra iPhone screenshots are also optional polish.

## Classic test record

For each app, record the tested IPA/hash, device model and OS, Classic/AltServer versions, installation result, game setup, launch, controls, audio, save/relaunch and update result. Do not record device identifiers or game data in this repository.

| App | Source install / launch | In-place update and data preservation |
| --- | --- | --- |
| KartPad | Pending | Pending |
| HarkinianPad | Pending | Pending |
| GoldenPad | Pending | Pending |
| SunPad | Pending; nested module | Pending |
| SpaghettiPad | Pending | Pending |
| UTP | Pending; nested libraries | Pending |
| BrawlerPad | Pending | Pending |
| MaskPad | Pending | Pending |
| StarshipPad | Pending | Pending |
| PaperPad | Pending | Pending |
| CaesarPad | Pending; test on iPad | Pending |
| DinoPad | App ready per owner; Classic source install pending | Pending |
| Bellpad | Pending; package metadata check | Pending |
| PeonPad | Pending; iPad and manual data setup | Pending |

## Reply to Matt

Unsent draft. The repository and source URL are already available. Adjust the testing sentence to match what has actually been completed.

> Hey Matt, thanks again for putting that source together. I've expanded it into Kahris' Apps, my Classic catalog:
>
> https://github.com/chrissotraidis/altstore
>
> Source URL: https://raw.githubusercontent.com/chrissotraidis/altstore/main/source.json
>
> It currently lists 14 apps with descriptions, icons and verified IPA metadata. Screenshots are included for 13. DevilTouch will follow once its updated IPA is ready.
>
> Next I'm testing installation and updates through the source in Classic. Is there anything else you'd like me to prepare for Featured Lists, or any requirements around preview apps, artwork or review that I should account for?

After device testing, replace the testing sentence with a precise result or a short list of the remaining exceptions. Do not claim all 14 work through Classic based only on the package audit.

## When you release an app update

Keep building and releasing in the app's existing repository. A code push alone changes nothing here.

Publish a new versioned IPA asset, inspect and test it, then prepend its entry to that app's `versions` array. Use the IPA's internal version/build numbers rather than deriving them from the filename or Git tag. Refresh the audit, release table, permissions and images if changed. Run the validator and test the candidate source before updating `main`.

Do not overwrite an existing release asset under the same version and URL. Keep older version entries when possible, especially when increasing minimum OS requirements. No automatic cross-repository release promotion is configured.

References: [source format](https://faq.altstore.io/developers/make-a-source), [app updates](https://faq.altstore.io/developers/updating-apps), [Classic setup](https://faq.altstore.io/altstore-classic/your-altstore). Exact project and release references are in [catalog-audit.json](catalog-audit.json).
