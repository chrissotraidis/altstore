#!/usr/bin/env python3
"""Check this catalog against the recorded package audit. Standard library only."""

from datetime import datetime
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def https(value):
    require(isinstance(value, str), "URL must be a string")
    parsed = urlparse(value)
    require(parsed.scheme == "https" and parsed.netloc, f"Invalid HTTPS URL: {value}")


def validate():
    source = json.loads((ROOT / "source.json").read_text(), object_pairs_hook=unique_keys)
    audit = json.loads((ROOT / "docs/catalog-audit.json").read_text(), object_pairs_hook=unique_keys)
    require(source.get("name") and isinstance(source.get("apps"), list), "Missing source name/apps")
    https(source["iconURL"])
    https(source["website"])
    evidence = {app["bundleIdentifier"]: app for app in audit["apps"]}
    seen = set()
    for app in source["apps"]:
        for field in ("name", "bundleIdentifier", "developerName", "localizedDescription", "iconURL"):
            require(isinstance(app.get(field), str) and app[field], f"Missing app field: {field}")
        bundle = app["bundleIdentifier"]
        require(bundle not in seen, f"Duplicate bundle ID: {bundle}")
        seen.add(bundle)
        require(bundle in evidence, f"No package audit for {bundle}")
        record = evidence[bundle]
        require(app["name"] == record["name"], f"Display name mismatch: {bundle}")
        require(app["appPermissions"] == record["appPermissions"], f"Permissions mismatch: {bundle}")
        https(app["iconURL"])
        require(app["iconURL"] == record["icon"]["imageURL"], f"Unaudited icon: {bundle}")
        versions = app.get("versions")
        require(isinstance(versions, list) and versions, f"Missing versions: {bundle}")
        identities = set()
        for version in versions:
            pair = (version.get("version"), version.get("buildVersion"))
            require(all(isinstance(v, str) and v for v in pair), f"Invalid version/build: {bundle}")
            require(pair not in identities, f"Repeated version/build: {bundle}")
            identities.add(pair)
            https(version["downloadURL"])
            require(urlparse(version["downloadURL"]).path.lower().endswith(".ipa"), f"Not an IPA: {bundle}")
            require(type(version["size"]) is int and version["size"] > 0, f"Invalid byte size: {bundle}")
            require(re.fullmatch(r"[0-9a-f]{64}", version["sha256"]), f"Invalid SHA-256: {bundle}")
            require(re.fullmatch(r"\d+(?:\.\d+)*", version["minOSVersion"]), f"Invalid minimum OS: {bundle}")
            datetime.fromisoformat(version["date"].replace("Z", "+00:00"))
        for field, audit_field in (("version", "version"), ("buildVersion", "buildVersion"),
                                   ("downloadURL", "downloadURL"), ("size", "size"),
                                   ("sha256", "sha256"), ("minOSVersion", "minimumOS")):
            require(versions[0][field] == record[audit_field], f"Latest {field} mismatch: {bundle}")
        for family, screenshots in app.get("screenshots", {}).items():
            require(family in {"iphone", "ipad"}, f"Unknown screenshot family: {family}")
            for shot in screenshots:
                https(shot["imageURL"])
                require(all(type(shot[k]) is int and shot[k] > 0 for k in ("width", "height")),
                        f"Missing screenshot dimensions: {bundle}")
                require(shot == record["screenshot"], f"Unaudited screenshot: {bundle}")
    require(seen == set(evidence), "Source and package-audit app lists differ")
    featured = source.get("featuredApps", [])
    require(len(featured) == len(set(featured)) and set(featured) <= seen, "Invalid featured app list")
    news_ids = [item["identifier"] for item in source.get("news", [])]
    require(len(news_ids) == len(set(news_ids)), "Duplicate news identifiers")
    print(f"PASS: {len(seen)} apps; versions, URLs, sizes, hashes, permissions and images match the audit.")
    print("AltStore installation, gameplay and in-place update tests remain separate checks.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
