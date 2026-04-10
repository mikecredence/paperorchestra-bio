"""Shared configuration for BiomedWritingBench pipeline."""

import time
from pathlib import Path

# ============================================================
# Paths
# ============================================================
BENCHMARK_DIR = Path(__file__).parent.parent
SCRIPTS_DIR = BENCHMARK_DIR / "scripts"
TEST_CASES_DIR = BENCHMARK_DIR / "test-cases"
GROUND_TRUTH_DIR = BENCHMARK_DIR / "ground_truth"
RESULTS_DIR = BENCHMARK_DIR / "results"
SCHEMA_PATH = BENCHMARK_DIR / "schema.json"
CANDIDATES_PATH = BENCHMARK_DIR / "corpus_candidates.json"

# ============================================================
# APIs
# ============================================================
BIORXIV_API = "https://api.biorxiv.org"
BIORXIV_DETAILS = f"{BIORXIV_API}/details/biorxiv"
BIORXIV_PUBLISHED = f"{BIORXIV_API}/publisher/biorxiv"

CLAUDE_MODEL = "claude-sonnet-4-20250514"

# ============================================================
# Rate Limiting
# ============================================================
BIORXIV_RATE = 1.0  # seconds between bioRxiv API calls


class RateLimiter:
    """Simple rate limiter for API calls."""

    def __init__(self, min_interval: float):
        self.min_interval = min_interval
        self.last_call = 0.0

    def wait(self):
        elapsed = time.time() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.time()


biorxiv_limiter = RateLimiter(BIORXIV_RATE)

# ============================================================
# Subfield Mappings
# ============================================================
SUBFIELD_CATEGORIES = [
    "genomics", "bioinformatics", "drug_discovery", "neuroscience",
    "immunology", "clinical", "cancer_biology", "structural_biology",
    "cell_biology", "epidemiology", "methods",
]

# Map bioRxiv categories to our subfields
BIORXIV_CATEGORY_MAP = {
    "genomics": "genomics",
    "bioinformatics": "bioinformatics",
    "genetics": "genomics",
    "molecular biology": "cell_biology",
    "cell biology": "cell_biology",
    "neuroscience": "neuroscience",
    "immunology": "immunology",
    "microbiology": "immunology",
    "cancer biology": "cancer_biology",
    "pharmacology and toxicology": "drug_discovery",
    "biochemistry": "structural_biology",
    "biophysics": "structural_biology",
    "epidemiology": "epidemiology",
    "clinical trials": "clinical",
    "pathology": "clinical",
    "systems biology": "bioinformatics",
    "synthetic biology": "methods",
    "developmental biology": "cell_biology",
    "plant biology": "genomics",
    "ecology": "epidemiology",
    "evolutionary biology": "genomics",
}

# Venue -> typical section structure
VENUE_SECTIONS = {
    "Nature Communications": ["Abstract", "Introduction", "Results", "Discussion", "Methods"],
    "Nature Methods": ["Abstract", "Main", "Results", "Discussion", "Online Methods"],
    "Nature Biotechnology": ["Abstract", "Main", "Results", "Discussion", "Methods"],
    "Nature Genetics": ["Abstract", "Main", "Results", "Discussion", "Methods"],
    "eLife": ["Abstract", "Introduction", "Results", "Discussion", "Materials and Methods"],
    "Genome Biology": ["Abstract", "Background", "Results", "Discussion", "Conclusions", "Methods"],
    "PLOS Computational Biology": ["Abstract", "Introduction", "Results", "Discussion", "Methods"],
    "Nucleic Acids Research": ["Abstract", "Introduction", "Materials and Methods", "Results", "Discussion"],
    "BMC Genomic Data": ["Abstract", "Background", "Results", "Discussion", "Conclusions", "Methods"],
    "Scientific Data": ["Abstract", "Background & Summary", "Methods", "Data Records", "Technical Validation"],
}

DEFAULT_SECTIONS = ["Abstract", "Introduction", "Methods", "Results", "Discussion", "Conclusion"]


def venue_sections(venue: str | None) -> list[str]:
    """Get typical section structure for a venue."""
    if not venue:
        return DEFAULT_SECTIONS
    for key, sections in VENUE_SECTIONS.items():
        if key.lower() in venue.lower():
            return sections
    return DEFAULT_SECTIONS


def slugify(title: str, max_len: int = 50) -> str:
    """Convert a paper title to a kebab-case slug."""
    import re
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug[:max_len]
