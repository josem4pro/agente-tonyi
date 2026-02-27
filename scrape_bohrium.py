#!/usr/bin/env python3
"""Scrape all unique URLs from bohrium.md and save as individual markdown files.

Uses the existing selenium_adapter from inference/ for headless Chrome + markdownify.
"""

import os
import sys
import re
import time
from urllib.parse import urlparse, urlunparse

# Add inference to path so we can import selenium_adapter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "inference"))

from selenium_adapter import selenium_readpage, cleanup_driver


def normalize_url(url):
    """Remove fragment and normalize trailing slash for dedup comparison."""
    parsed = urlparse(url.strip())
    normalized = urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, "")
    )
    return normalized.rstrip("/")


def url_to_filename(url):
    """Convert URL to a meaningful filename for NotebookLM."""
    parsed = urlparse(url.strip())
    path = parsed.path.strip("/")

    if not path or path == "/":
        host = parsed.netloc.replace(".", "_")
        return f"{host}_home"

    # Build name from path
    name = path.replace("/", "__")

    # Remove common doc prefixes to keep names short
    name = re.sub(r"^en__docs__?", "", name)
    name = re.sub(r"^docs__?", "", name)

    if not name:
        host = parsed.netloc.replace(".", "_")
        return f"{host}__docs_index"

    return name


def main():
    bohrium_file = os.path.join(os.path.dirname(__file__), "bohrium.md")

    with open(bohrium_file, "r") as f:
        raw_urls = [line.strip() for line in f if line.strip().startswith("http")]

    # Deduplicate by normalized URL (strips fragments, normalizes trailing slashes)
    seen = set()
    unique_urls = []
    for url in raw_urls:
        norm = normalize_url(url)
        if norm not in seen:
            seen.add(norm)
            unique_urls.append(url.strip())

    print(f"Total URLs in bohrium.md: {len(raw_urls)}")
    print(f"Unique pages after dedup: {len(unique_urls)}")

    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), "bohrium_docs")
    os.makedirs(output_dir, exist_ok=True)

    # Scrape each unique URL
    success = 0
    failed = []

    for i, url in enumerate(unique_urls, 1):
        filename = url_to_filename(url)
        filepath = os.path.join(output_dir, f"{filename}.md")

        print(f"\n[{i}/{len(unique_urls)}] {url}")
        print(f"  -> {filename}.md")

        try:
            content = selenium_readpage(url)

            # Add metadata header for NotebookLM context
            header = f"# {filename.replace('__', ' > ').replace('_', ' ')}\n\n"
            header += f"**Source URL:** {url}\n\n---\n\n"
            full_content = header + content

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(full_content)

            chars = len(content)
            print(f"  OK ({chars:,} chars)")
            success += 1

            # Polite delay between requests
            time.sleep(1.5)

        except Exception as e:
            print(f"  FAIL: {e}")
            failed.append((url, str(e)))

    # Cleanup selenium driver
    try:
        cleanup_driver()
    except Exception:
        pass

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"Scraping complete: {success}/{len(unique_urls)} pages saved")
    print(f"Output directory: {output_dir}/")

    if failed:
        print(f"\nFailed ({len(failed)}):")
        for url, err in failed:
            print(f"  - {url}: {err}")

    # Write index file
    index_path = os.path.join(output_dir, "_INDEX.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# Bohrium Documentation Index\n\n")
        f.write(f"Scraped {success} pages from bohrium.md\n\n")
        for url in unique_urls:
            fname = url_to_filename(url)
            status = "OK" if url not in dict(failed) else "FAILED"
            f.write(f"- [{fname}]({fname}.md) — {url} [{status}]\n")

    print(f"\nIndex written to: {index_path}")


if __name__ == "__main__":
    main()
