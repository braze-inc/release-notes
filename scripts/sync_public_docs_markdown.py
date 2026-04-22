#!/usr/bin/env python3
"""Sync public docs markdown endpoints into section folders."""

from __future__ import annotations

import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

SITEMAP_URL = "https://www.braze.com/docs/sitemap.xml"
USER_AGENT = "Mozilla/5.0 (compatible; release-notes-sync/1.0)"
REQUEST_TIMEOUT_SECONDS = 30

SECTION_MAP = {
    "user_guide": "User Guide",
    "developer_guide": "Developer Guide",
    "api": "API",
    "partners": "Technology Partners",
    "releases": "What's New",
}
LOCALE_PREFIXES = {"de", "es", "fr", "ja", "ko", "pt-br", "pt_br"}


def fetch_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        return response.read()


def sitemap_urls(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for node in root.findall("sm:url", ns):
        loc_node = node.find("sm:loc", ns)
        if loc_node is None or not loc_node.text:
            continue
        urls.append(loc_node.text.strip())
    return urls


def build_targets(urls: list[str]) -> list[tuple[str, Path]]:
    targets: dict[Path, str] = {}
    for raw_url in urls:
        parsed = urlparse(raw_url)
        if parsed.netloc != "www.braze.com":
            continue

        path = parsed.path
        if not path.startswith("/docs/"):
            continue

        rel = path[len("/docs/") :].strip("/")
        if not rel:
            continue

        first = rel.split("/")[0]
        if first in LOCALE_PREFIXES:
            continue
        if first not in SECTION_MAP:
            continue

        section_folder = SECTION_MAP[first]
        suffix = "/".join(rel.split("/")[1:])
        markdown_url = f"https://www.braze.com{path.rstrip('/')}/index.md"

        parts = [section_folder]
        if suffix:
            parts.append(suffix)
        parts.append("index.md")
        targets[Path(*parts)] = markdown_url

    return sorted((url, dest) for dest, url in targets.items())


def main() -> int:
    staging_root = Path("sync-staging")
    if staging_root.exists():
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True, exist_ok=True)

    for section in SECTION_MAP.values():
        (staging_root / section).mkdir(parents=True, exist_ok=True)

    sitemap = fetch_bytes(SITEMAP_URL)
    targets = build_targets(sitemap_urls(sitemap))

    failures: list[str] = []
    fetched = 0

    for markdown_url, dest_rel in targets:
        dest_path = staging_root / dest_rel
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            content = fetch_bytes(markdown_url)
        except (HTTPError, URLError) as exc:
            failures.append(f"{markdown_url} ({exc})")
            continue

        dest_path.write_bytes(content)
        fetched += 1

    print(f"Discovered {len(targets)} markdown endpoints from sitemap.")
    print(f"Fetched {fetched} markdown files into {staging_root}.")

    if failures:
        print(f"Skipped {len(failures)} pages with fetch errors.")
        for failure in failures[:20]:
            print(f"- {failure}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
