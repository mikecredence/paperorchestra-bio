# Experimental Log: Embedding-Based Alignment (EBA)

## Method comparison on structural similarity benchmarks

| Method | Type | Training required | Twilight zone performance | Overall accuracy |
|---|---|---|---|---|
| EBA (ours) | pLM embedding + alignment | No | Best | Highest |
| BLAST | Classical sequence | No | Poor | Moderate |
| HHblits | Profile-profile | No (but needs MSA) | Moderate | Good |
| pLM cosine similarity | pLM embedding (no alignment) | No | Moderate | Below EBA |
| Other pLM methods | pLM-based | Varies | Below EBA | Below EBA |

## Performance in the twilight zone (< 20% sequence identity)

| Method | Structural similarity detection rate | False positive rate |
|---|---|---|
| EBA (ours) | Highest | Low |
| BLAST | Very low | Low |
| HHblits | Moderate | Low |
| pLM cosine similarity | Moderate | Moderate |

## Alignment quality metrics

| Metric | EBA | Classical (BLAST/HHblits) | Other pLM methods |
|---|---|---|---|
| TM-score correlation | Highest | Lower | Intermediate |
| Alignment coverage | High | Variable | Variable |
| Residue-level accuracy (vs. structural alignment) | Superior | Baseline | Intermediate |

## Key properties

| Property | Value |
|---|---|
| Training required | None |
| Parameter optimization | None |
| Input | Protein sequences (any length) |
| Output | Pairwise alignment with scores |
| pLM backbone | Standard protein language model |

## Notes

- 2024-01-14: EBA pipeline implemented; embedding extraction + dynamic programming alignment.
- 2024-02-02: Benchmark on structural similarity datasets shows EBA outperforms all baselines in twilight zone.
- 2024-02-16: No training or parameter optimization needed -- a major practical advantage.
- 2024-03-01: Alignment quality correlates well with TM-score even at very low sequence identity.
- Key insight: pLM embeddings encode enough structural information that simple alignment algorithms on embedding similarity recover structural homology.
