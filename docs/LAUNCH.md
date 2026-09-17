# Launch plan

Prepared on 17 September 2026. This is the working launch record, not a claim that AltStore has featured or certified the source.

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
| KartPad | Use 0.4.24 build 49. Do not silently promote the newer diagnostics build. |
| UTP | Use Preview 3 on iOS 17+. The newer issue-specific iOS 15 test does not replace it. |
| SunPad | Use iPhone/iPad Preview 13. Verify Classic re-signs and loads its root-level `gGMSE01_recomp.dylib`. |
| DinoPad | Offer Prototype Mode only. The public IPA excludes Restored Adventure; its private-mode README screenshots are not used. |
| PeonPad | Label iPad-only. Preview 1 is actually version 0.1.0 **build 4**. Explain desktop extraction and manual `data.Wargus` setup. |
| CaesarPad | Describe as designed for iPad. Its IPA also declares iPhone; that does not establish a tested iPhone experience. |
| Bellpad | Preserve the project's spelling, **Bellpad**. Its plist omits `MinimumOSVersion`; executable metadata confirms iOS 17.0. Verify install behavior; repair app packaging in its own project if Classic rejects it. |
| DevilTouch | Source-only preview. Keep it out of the installable catalog until a public IPA is separately prepared and released. |

The source uses Matt's initial name concept and the owner's requested app order. The five source highlights are KartPad, HarkinianPad, GoldenPad, SunPad and SpaghettiPad. This is independent of Matt's proposed Featured Lists placement.

## Next steps, in order

1. **Review the lineup and descriptions.** If an app needs code changes before launch, finish and publish that app's new IPA in its own repository, then update this catalog. Otherwise the existing release stays selected.
2. **Use the hosted catalog for testing.** This repository's `main` branch hosts the source; the README contains its permanent raw URL. No separate server or website is required for this setup. The source is public to anyone with its URL, while device acceptance and Featured Lists placement remain pending. Run `python3 scripts/validate_source.py` before subsequent catalog changes.
3. **Test through AltStore Classic.** Add that exact source URL on a real device. Check the source name, all app cards, icons, screenshot proportions and preview labels. Install the selected apps through the source, complete their documented game-data setup, and verify launch, input, audio and saving. Give SunPad's nested signing and UTP's libraries explicit attention. Check PeonPad on iPad and that iPad-only restrictions are respected. Start with KartPad and HarkinianPad if testing incrementally.
4. **Test an update with preserved data.** Using a staging source URL and a backed-up app, verify an older selected build can update to a newer build using the same Apple account/bundle setup. Confirm imported files, settings and saves remain. Do not put old versions ahead of newer ones in the public catalog to simulate an update. Record failures before changing app code.
5. **Send Matt the source and results.** Ask about Featured Lists eligibility, required art/metadata, and whether preview apps or an additional review affect inclusion. A working source and a featured listing are separate milestones. The message below is ready to adapt; it has not been sent.
6. **Announce the tested lineup.** Resolve or remove failed candidates first. Update this record and README to reflect actual testing. Update the selected app READMEs with the source link after those apps are accepted. Add an optional source news item when the launch is ready.

Screenshots are documentation captures, not fresh captures of every selected IPA. Review their presentation in Classic. StarshipPad uses its explicitly identified Simulator hero. Capture public Prototype Mode gameplay for DinoPad before adding its screenshot. Extra iPhone screenshots are optional polish.

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
| DinoPad | Pending; Prototype Mode | Pending |
| Bellpad | Pending; package metadata check | Pending |
| PeonPad | Pending; iPad and manual data setup | Pending |

## Reply to Matt

Draft to send once the repository is available. Adjust the testing sentence to match what has actually been completed.

> Hey Matt, thanks again for putting that source together. I've used it as the starting point for my Classic catalog:
>
> https://github.com/chrissotraidis/altstore
>
> Source URL: https://raw.githubusercontent.com/chrissotraidis/altstore/main/source.json
>
> It currently lists 14 apps, with descriptions, icons, screenshots and package metadata checked against their published IPAs. Most are developer previews, labeled accordingly. DevilTouch will follow once I publish its first IPA.
>
> I'm working through installation and update testing in Classic now. Is there anything else you'd like me to prepare for Featured Lists, or any requirements around preview apps, artwork or review that I should account for?

After device testing, replace the testing sentence with a precise result or a short list of the remaining exceptions. Do not claim all 14 work through Classic based only on the package audit.

## When you release an app update

Keep building and releasing in the app's existing repository. A code push alone changes nothing here.

Publish a new versioned IPA asset, inspect and test it, then prepend its entry to that app's `versions` array. Use the IPA's internal version/build numbers rather than deriving them from the filename or Git tag. Refresh the audit, release table, permissions and images if changed. Run the validator and test the candidate source before updating `main`.

Do not overwrite an existing release asset under the same version and URL. Keep older version entries when possible, especially when increasing minimum OS requirements. No automatic cross-repository release promotion is configured.

References: [source format](https://faq.altstore.io/developers/make-a-source), [app updates](https://faq.altstore.io/developers/updating-apps), [Classic setup](https://faq.altstore.io/altstore-classic/your-altstore). Exact project and release references are in [catalog-audit.json](catalog-audit.json).
