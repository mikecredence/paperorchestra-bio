# Benchmark Evaluation: DNA Foundation Models Test Case

Test date: 2026-04-09
Skill version: paper-builder v2 (with MCP integrations)

## Pipeline Stage Test Results

### Stage 0: Workspace Init
| Check | Result |
|-------|--------|
| Directory creation | PASS - 6 dirs created including snapshots/ |
| Worklog init | PASS - worklog.json created |
| Input validation | PASS - correctly flags missing inputs |

### Stage 1: Outline Agent
| Check | Result |
|-------|--------|
| Outline generated | PASS - complete JSON outline |
| Section count | 6 sections (Intro, Related Work, Methods, Results, Discussion, Conclusion) |
| Visualization plan | 8 items (1 diagram, 3 tables, 3 charts, 1 ablation table) |
| Literature queries | 4 macro + 9 micro queries |
| Must-cite items | 12 papers identified |
| Section coverage vs ground truth | Good alignment - all major sections present |

**Outline quality notes:**
- Added Discussion section (separate from Conclusion) which matches Nature Comms format
- Visualization plan covers all key data from experimental log
- Literature strategy queries are diverse and specific
- Must-cite list captures all 5 models + 3 specialized baselines + stats references

### Stage 2: Plot Agent
| Check | Result |
|-------|--------|
| Pooling impact figure | PASS - colorblind-friendly bars with IQR error bars |
| Variant effect figure | PASS - grouped bar chart, foundation vs specialized |
| PDF + PNG output | PASS - dual format |
| Academic styling | PASS - Okabe-Ito palette, 300 DPI, clean layout |

### Stage 3: Literature Agent (Citation Pipeline)
| Check | Result |
|-------|--------|
| Semantic Scholar verification | 4/8 real papers verified (rate-limited without API key) |
| Fake paper rejection | PASS - correctly rejected "This Paper Does Not Exist" |
| Web search fallback | PASS - verified 3 additional papers (DNABERT-2, HyenaDNA, Caduceus) |
| Multi-channel total | 7/8 real papers verified across both channels |
| DOI direct lookup | PASS - benchmark paper verified via DOI instantly |
| Cutoff date enforcement | PASS - field present in results |
| Deduplication | PASS - no duplicates detected |

**Citation pipeline summary:**
- Without API key: 50% verification rate on Semantic Scholar alone (rate limits)
- With web search fallback: 87.5% verification rate
- Estimated with API key: ~95%+ verification rate

### Stage 4: Citation Audit
| Check | Result |
|-------|--------|
| Orphaned citation detection | PASS - found vaswani_2017_attention (in text, not in bib) |
| Unused entry detection | PASS - found grover_2024, sei_2022 (in bib, not cited) |
| Coverage calculation | PASS - 77.8% correctly computed |
| Coverage threshold check | PASS - correctly flagged below 90% target |
| Citation count warning | PASS - flagged 7 citations as below 45-50 target |

### Stage 5: Refinement Agent
| Feature | Status |
|---------|--------|
| 0-100 scoring rubric | Implemented in reference doc |
| Score-delta ACCEPT/REVERT | Implemented in reference doc |
| Filesystem snapshots | Implemented (snapshots/ dir created) |
| Worklog | Implemented (worklog.json created) |
| Anti-gaming safeguards | Documented in reference doc |
| Preprint-to-published upgrade | Documented (requires bioRxiv MCP) |

*Note: Full refinement loop requires LaTeX compilation which needs pdflatex installed.*

## Comparison to PaperOrchestra Targets

| Metric | PaperOrchestra | Our Skill (tested) | Gap |
|--------|---------------|-------------------|-----|
| Citation target | ~46 per paper | 45-50 target | Aligned |
| Citation verification | Semantic Scholar (primary) | S2 + web search + bioRxiv + PubMed | Broader |
| Discovery channels | S2 + web search | S2 + web + bioRxiv + PubMed + ClinicalTrials | +3 channels |
| Anti-leakage | Yes (Appendix D.4) | Yes (writing + refinement agents) | Aligned |
| Refinement scoring | 0-100, 6 axes | 0-100, 6 axes | Aligned |
| Rollback capability | Filesystem snapshots | Filesystem snapshots | Aligned |
| Anti-gaming | Yes | Yes | Aligned |
| Orphan citation check | Yes (script) | Yes (citation_audit.py) | Aligned |
| Coverage enforcement | Yes (script) | Yes (citation_audit.py) | Aligned |
| Deduplication | Yes (dedupe_by_id.py) | Yes (built into verify_citation.py) | Aligned |
| Cutoff date enforcement | Yes (check_cutoff.py) | Yes (built into verify_citation.py) | Aligned |
| Worklog | Yes | Yes (worklog.json) | Aligned |
| Input validation | Yes (validate_inputs.py) | Yes (init_workspace.py) | Aligned |
| Simulated acceptance rate | 84% CVPR, 81% ICLR | Not measured (no ScholarPeer) | Gap |
| Human evaluation | 11 reviewers, 180 comparisons | Not available | Gap |
| LLM-as-judge | Gemini + GPT-5 | Not implemented | Gap |

## Known Gaps

1. **No ScholarPeer integration** - can't compute simulated acceptance rates
2. **No LLM-as-judge evaluation** - need to implement automated SxS comparison
3. **No LaTeX on this machine** - can't test full compilation pipeline
4. **PubMed MCP session expired** - graceful degradation works but PubMed channel untested
5. **bioRxiv MCP disconnected mid-session** - need stable connection for production use
6. **Semantic Scholar rate limits** - API key essential for batch verification (50% -> 95%+ hit rate)
7. **No Exa search** - paper-orchestra has this; we use broader MCP coverage instead

## Recommendations

1. **Get Semantic Scholar API key** - single biggest improvement for verification throughput
2. **Install LaTeX** (texlive) for full end-to-end testing
3. **Implement Citation F1 metric** - compare generated citations vs ground truth paper
4. **Add LLM-as-judge** - automated SxS evaluation using the refinement agent's scoring
5. **Build 10+ more test cases** from corpus_candidates.json
6. **Test MCP resilience** - ensure skill handles disconnected MCPs gracefully in production
