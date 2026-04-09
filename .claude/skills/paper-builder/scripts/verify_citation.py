#!/usr/bin/env python3
"""
Verify academic citations using the Semantic Scholar API.

Usage:
    python verify_citation.py "Paper Title Here"
    python verify_citation.py --batch citations.json
    python verify_citation.py --batch citations.json --output verified.json
    python verify_citation.py --batch citations.json --cutoff 2025-01-15

Supports:
    - Single and batch verification
    - API key for higher rate limits (env: SEMANTIC_SCHOLAR_API_KEY)
    - DOI-based lookup when available
    - Fuzzy title matching with configurable threshold
    - Cutoff date enforcement for venue submission deadlines
    - Deduplication by paperId, DOI, or normalized title

The script searches the Semantic Scholar API, uses fuzzy title matching to
confirm identity, and returns structured citation data including BibTeX keys.
"""

import sys
import json
import re
import os
import time
import argparse
import hashlib
import requests
from difflib import SequenceMatcher


SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"
SEARCH_ENDPOINT = f"{SEMANTIC_SCHOLAR_API}/paper/search"
PAPER_ENDPOINT = f"{SEMANTIC_SCHOLAR_API}/paper"
PAPER_FIELDS = "title,authors,year,venue,abstract,citationCount,externalIds,publicationTypes"
RATE_LIMIT_DELAY = 1.0  # seconds between API calls (unauthenticated)
RATE_LIMIT_DELAY_AUTH = 0.2  # seconds with API key (higher throughput)

# API key from environment variable (optional, increases rate limits)
API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")


def get_headers() -> dict:
    """Return request headers, including API key if available."""
    headers = {}
    if API_KEY:
        headers["x-api-key"] = API_KEY
    return headers


def get_rate_delay() -> float:
    """Return appropriate rate limit delay based on auth status."""
    return RATE_LIMIT_DELAY_AUTH if API_KEY else RATE_LIMIT_DELAY


def normalize_title(title: str) -> str:
    """Normalize a title for comparison: lowercase, strip punctuation."""
    title = title.lower().strip()
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title


def fuzzy_match_score(title_a: str, title_b: str) -> float:
    """Compute similarity between two titles (0.0 to 1.0)."""
    norm_a = normalize_title(title_a)
    norm_b = normalize_title(title_b)
    return SequenceMatcher(None, norm_a, norm_b).ratio()


def generate_bibtex_key(authors: list, year: int, title: str) -> str:
    """Generate a BibTeX key like 'vaswani_2017_attention'."""
    if authors:
        last_name = authors[0].get("name", "unknown").split()[-1].lower()
        last_name = re.sub(r'[^\w]', '', last_name)
    else:
        last_name = "unknown"

    stop_words = {'a', 'an', 'the', 'of', 'for', 'in', 'on', 'and', 'with', 'to',
                  'by', 'is', 'are', 'via', 'from', 'using', 'towards', 'based'}
    words = normalize_title(title).split()
    keyword = "paper"
    for w in words:
        if w not in stop_words and len(w) > 2:
            keyword = w
            break

    return f"{last_name}_{year}_{keyword}"


def generate_bibtex_entry(paper: dict, key: str) -> str:
    """Generate a BibTeX entry string from paper data."""
    authors_str = " and ".join(
        a.get("name", "Unknown") for a in paper.get("authors", [])
    )
    venue = paper.get("venue", "")
    year = paper.get("year", "")
    title = paper.get("title", "")

    # Extract DOI if available
    external_ids = paper.get("externalIds", {}) or {}
    doi = external_ids.get("DOI", "")

    entry_type = "article"
    venue_field = "journal"
    if venue:
        venue_lower = venue.lower()
        conf_keywords = ["conference", "proceedings", "workshop", "symposium",
                         "cvpr", "iclr", "neurips", "nips", "icml", "aaai",
                         "eccv", "iccv", "acl", "emnlp", "naacl", "sigir",
                         "kdd", "www", "chi", "uist", "miccai", "ismb",
                         "recomb", "bibm"]
        if any(k in venue_lower for k in conf_keywords):
            entry_type = "inproceedings"
            venue_field = "booktitle"

    lines = [
        f"@{entry_type}{{{key},",
        f"  title     = {{{title}}},",
        f"  author    = {{{authors_str}}},",
    ]
    if venue:
        lines.append(f"  {venue_field:10s}= {{{venue}}},")
    if year:
        lines.append(f"  year      = {{{year}}},")
    if doi:
        lines.append(f"  doi       = {{{doi}}},")
    lines.append("}")

    return "\n".join(lines)


def search_paper(query_title: str, max_retries: int = 2) -> dict | None:
    """Search Semantic Scholar for a paper by title."""
    params = {
        "query": query_title,
        "limit": 5,
        "fields": PAPER_FIELDS,
    }

    for attempt in range(max_retries + 1):
        try:
            resp = requests.get(SEARCH_ENDPOINT, params=params,
                                headers=get_headers(), timeout=15)
            if resp.status_code == 429:
                wait = min(2 ** attempt * 2, 30)
                print(f"  Rate limited, waiting {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            data = resp.json()
            return data
        except requests.RequestException as e:
            if attempt < max_retries:
                time.sleep(get_rate_delay())
                continue
            print(f"  API error: {e}", file=sys.stderr)
            return None

    return None


def lookup_by_doi(doi: str, max_retries: int = 2) -> dict | None:
    """Look up a paper directly by DOI (more reliable than search)."""
    url = f"{PAPER_ENDPOINT}/DOI:{doi}"
    params = {"fields": PAPER_FIELDS}

    for attempt in range(max_retries + 1):
        try:
            resp = requests.get(url, params=params,
                                headers=get_headers(), timeout=15)
            if resp.status_code == 404:
                return None
            if resp.status_code == 429:
                wait = min(2 ** attempt * 2, 30)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            if attempt < max_retries:
                time.sleep(get_rate_delay())
                continue
            print(f"  DOI lookup error: {e}", file=sys.stderr)
            return None

    return None


def lookup_by_arxiv_id(arxiv_id: str, max_retries: int = 2) -> dict | None:
    """Look up a paper directly by arXiv ID."""
    url = f"{PAPER_ENDPOINT}/ARXIV:{arxiv_id}"
    params = {"fields": PAPER_FIELDS}

    for attempt in range(max_retries + 1):
        try:
            resp = requests.get(url, params=params,
                                headers=get_headers(), timeout=15)
            if resp.status_code == 404:
                return None
            if resp.status_code == 429:
                wait = min(2 ** attempt * 2, 30)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            if attempt < max_retries:
                time.sleep(get_rate_delay())
                continue
            print(f"  arXiv lookup error: {e}", file=sys.stderr)
            return None

    return None


def check_cutoff(year: int, cutoff_date: str | None) -> dict:
    """Check if a paper's year falls within the cutoff date."""
    if not cutoff_date:
        return {"within_cutoff": True, "note": ""}

    try:
        cutoff_year = int(cutoff_date.split("-")[0])
        if year > cutoff_year:
            return {
                "within_cutoff": False,
                "note": f"Published {year}, after cutoff year {cutoff_year}. "
                        f"Treat as concurrent work, not prior art."
            }
        return {"within_cutoff": True, "note": ""}
    except (ValueError, IndexError):
        return {"within_cutoff": True, "note": "Could not parse cutoff date"}


def verify_single(query_title: str, threshold: float = 0.70,
                  doi: str | None = None, arxiv_id: str | None = None,
                  cutoff_date: str | None = None) -> dict:
    """
    Verify a single citation. Returns a result dict with:
    - verified: bool
    - match_score: float
    - paper data (if verified)
    - bibtex_key, bibtex_entry (if verified)
    - cutoff_status (if cutoff_date provided)
    """
    result = {
        "query_title": query_title,
        "verified": False,
        "match_score": 0.0,
        "reason": "",
    }

    best_match = None

    # Try direct lookup by DOI first (most reliable)
    if doi:
        paper = lookup_by_doi(doi)
        if paper and paper.get("title"):
            score = fuzzy_match_score(query_title, paper["title"])
            if score >= threshold:
                best_match = paper
                result["match_score"] = round(score, 3)
                result["lookup_method"] = "DOI"

    # Try direct lookup by arXiv ID
    if not best_match and arxiv_id:
        paper = lookup_by_arxiv_id(arxiv_id)
        if paper and paper.get("title"):
            score = fuzzy_match_score(query_title, paper["title"])
            if score >= threshold:
                best_match = paper
                result["match_score"] = round(score, 3)
                result["lookup_method"] = "arXiv"

    # Fall back to title search
    if not best_match:
        data = search_paper(query_title)
        if not data or not data.get("data"):
            result["reason"] = "No results from Semantic Scholar API"
            return result

        best_score = 0.0
        for paper in data["data"]:
            if not paper.get("title"):
                continue
            score = fuzzy_match_score(query_title, paper["title"])
            if score > best_score:
                best_score = score
                best_match = paper

        if best_match is None:
            result["reason"] = "No papers with valid titles in results"
            return result

        result["match_score"] = round(best_score, 3)
        result["lookup_method"] = "title_search"

        if best_score < threshold:
            result["reason"] = (
                f"Best match '{best_match['title']}' has similarity "
                f"{best_score:.3f} < threshold {threshold}"
            )
            return result

    # Verified!
    year = best_match.get("year", 0) or 0
    external_ids = best_match.get("externalIds", {}) or {}
    bibtex_key = generate_bibtex_key(
        best_match.get("authors", []),
        year,
        best_match.get("title", "")
    )

    result.update({
        "verified": True,
        "reason": "Matched via Semantic Scholar",
        "title": best_match.get("title", ""),
        "authors": [a.get("name", "") for a in best_match.get("authors", [])],
        "year": year,
        "venue": best_match.get("venue", ""),
        "abstract": best_match.get("abstract", ""),
        "citation_count": best_match.get("citationCount", 0),
        "doi": external_ids.get("DOI", ""),
        "arxiv_id": external_ids.get("ArXiv", ""),
        "paper_id": best_match.get("paperId", ""),
        "bibtex_key": bibtex_key,
        "bibtex_entry": generate_bibtex_entry(best_match, bibtex_key),
    })

    # Check cutoff date
    if cutoff_date:
        cutoff_result = check_cutoff(year, cutoff_date)
        result["cutoff_status"] = cutoff_result

    return result


def deduplicate_results(results: list) -> list:
    """Remove duplicate citations by paperId, DOI, or normalized title."""
    seen_ids = set()
    seen_dois = set()
    seen_titles = set()
    deduped = []

    for r in results:
        if not r.get("verified"):
            deduped.append(r)
            continue

        paper_id = r.get("paper_id", "")
        doi = r.get("doi", "")
        norm_title = normalize_title(r.get("title", ""))
        title_hash = hashlib.md5(norm_title.encode()).hexdigest()

        if paper_id and paper_id in seen_ids:
            r["deduplicated"] = True
            r["dedup_reason"] = f"Duplicate paperId: {paper_id}"
            deduped.append(r)
            continue

        if doi and doi in seen_dois:
            r["deduplicated"] = True
            r["dedup_reason"] = f"Duplicate DOI: {doi}"
            deduped.append(r)
            continue

        if title_hash in seen_titles:
            r["deduplicated"] = True
            r["dedup_reason"] = f"Duplicate title: {r.get('title', '')}"
            deduped.append(r)
            continue

        r["deduplicated"] = False
        if paper_id:
            seen_ids.add(paper_id)
        if doi:
            seen_dois.add(doi)
        seen_titles.add(title_hash)
        deduped.append(r)

    return deduped


def main():
    parser = argparse.ArgumentParser(
        description="Verify academic citations via Semantic Scholar API"
    )
    parser.add_argument("title", nargs="?", help="Paper title to verify")
    parser.add_argument("--batch", help="JSON file with list of titles to verify")
    parser.add_argument("--output", "-o", help="Output JSON file for batch results")
    parser.add_argument("--threshold", type=float, default=0.70,
                        help="Fuzzy match threshold (default: 0.70)")
    parser.add_argument("--cutoff", help="Cutoff date (YYYY-MM-DD) for venue deadline")
    parser.add_argument("--dedupe", action="store_true", default=True,
                        help="Deduplicate results (default: enabled)")
    args = parser.parse_args()

    if API_KEY:
        print("Using authenticated API (higher rate limits)", file=sys.stderr)
    else:
        print("No API key found. Set SEMANTIC_SCHOLAR_API_KEY for higher rate limits.",
              file=sys.stderr)

    if args.batch:
        with open(args.batch) as f:
            data = json.load(f)

        # Support both list of strings and list of dicts
        if isinstance(data, dict):
            titles_data = data.get("titles", data.get("citations", []))
        else:
            titles_data = data

        results = []
        verified_count = 0
        for i, item in enumerate(titles_data):
            if isinstance(item, str):
                title = item
                doi = None
                arxiv_id = None
            else:
                title = item.get("title", "")
                doi = item.get("doi")
                arxiv_id = item.get("arxiv_id")

            print(f"[{i+1}/{len(titles_data)}] Verifying: {title}", file=sys.stderr)
            result = verify_single(title, threshold=args.threshold,
                                   doi=doi, arxiv_id=arxiv_id,
                                   cutoff_date=args.cutoff)
            results.append(result)
            if result["verified"]:
                verified_count += 1
            time.sleep(get_rate_delay())

        if args.dedupe:
            results = deduplicate_results(results)
            unique_verified = sum(1 for r in results
                                 if r.get("verified") and not r.get("deduplicated"))
        else:
            unique_verified = verified_count

        print(f"\nVerified: {verified_count}/{len(titles_data)} "
              f"(unique: {unique_verified})", file=sys.stderr)

        output = {
            "results": results,
            "verified": verified_count,
            "unique_verified": unique_verified,
            "total": len(titles_data),
            "cutoff_date": args.cutoff,
        }
        if args.output:
            with open(args.output, "w") as f:
                json.dump(output, f, indent=2)
            print(f"Results saved to {args.output}", file=sys.stderr)
        else:
            print(json.dumps(output, indent=2))

    elif args.title:
        result = verify_single(args.title, threshold=args.threshold,
                               cutoff_date=args.cutoff)
        print(json.dumps(result, indent=2))

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
