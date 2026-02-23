"""
SearXNG Adapter - Transforms SearXNG responses to Serper-compatible format.

Replaces paid Serper.dev API with local SearXNG metasearch instance.
"""

import os
import json
import requests
from urllib.parse import urlparse
from datetime import datetime

SEARXNG_URL = os.environ.get("SEARXNG_URL", "")


def _parse_date(date_str):
    """Convert ISO 8601 date to human-readable format."""
    if not date_str:
        return ""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y")
    except (ValueError, TypeError):
        return date_str


def _extract_domain(url):
    """Extract domain name from URL for source field."""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")
        return domain
    except Exception:
        return ""


def searxng_search(query, num_results=10):
    """
    Perform web search via SearXNG and return Serper-compatible format.

    Returns dict with "organic" key containing list of results.
    """
    params = {
        "q": query,
        "format": "json",
        "categories": "general",
    }

    try:
        response = requests.get(
            f"{SEARXNG_URL}/search",
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return {"organic": [], "error": str(e)}

    organic = []
    for result in data.get("results", [])[:num_results]:
        item = {
            "title": result.get("title", ""),
            "link": result.get("url", ""),
            "snippet": result.get("content", ""),
        }
        date = _parse_date(result.get("publishedDate", ""))
        if date:
            item["date"] = date
        domain = _extract_domain(result.get("url", ""))
        if domain:
            item["source"] = domain
        organic.append(item)

    return {"organic": organic}


def searxng_scholar(query, num_results=10):
    """
    Perform academic search via SearXNG (arxiv + google scholar engines).

    Returns dict with "organic" key in Serper Scholar-compatible format.
    """
    params = {
        "q": query,
        "format": "json",
        "categories": "science",
        "engines": "arxiv,google scholar",
    }

    try:
        response = requests.get(
            f"{SEARXNG_URL}/search",
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return {"organic": [], "error": str(e)}

    organic = []
    for result in data.get("results", [])[:num_results]:
        item = {
            "title": result.get("title", ""),
            "snippet": result.get("content", ""),
        }
        # ArXiv results have pdf_url
        pdf_url = result.get("pdf_url", "")
        if pdf_url:
            item["pdfUrl"] = pdf_url
        elif result.get("url", ""):
            item["pdfUrl"] = result["url"]

        # Date handling - arxiv uses publishedDate
        date = result.get("publishedDate", "")
        if date:
            try:
                dt = datetime.fromisoformat(date.replace("Z", "+00:00"))
                item["year"] = dt.year
            except (ValueError, TypeError):
                pass

        # Publication info from engine metadata
        authors = result.get("author", "")
        journal = result.get("journal", "")
        if authors or journal:
            pub_parts = []
            if authors:
                pub_parts.append(str(authors))
            if journal:
                pub_parts.append(str(journal))
            item["publicationInfo"] = " - ".join(pub_parts)

        organic.append(item)

    return {"organic": organic}
