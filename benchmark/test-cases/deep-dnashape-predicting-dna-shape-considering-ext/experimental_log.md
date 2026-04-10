# Experimental Log: Deep DNAshape

## Method comparison: Deep DNAshape vs. k-mer approaches

| Method | Flanking region support | Throughput | Training required | Accuracy |
|---|---|---|---|---|
| Deep DNAshape (ours) | Extended (arbitrary length) | High | Yes (deep learning) | Superior |
| DNAshapeR (k-mer) | Limited to k-mer window | High | No (lookup table) | Baseline |
| MD simulation | Full context | Very low | No | Gold standard |
| Structural experiments | Full context | Very low | No | Gold standard |

## DNA shape features predicted

| Feature | Description | Deep DNAshape R2 vs. simulation | k-mer R2 vs. simulation |
|---|---|---|---|
| Minor Groove Width (MGW) | Width of the minor groove | Improved over k-mer | Baseline |
| Roll | Angle between consecutive base pair planes | Improved over k-mer | Baseline |
| Propeller Twist (ProT) | Twist of bases within a pair | Improved over k-mer | Baseline |
| Helix Twist (HelT) | Rotation between base pair steps | Improved over k-mer | Baseline |

## Flanking region influence analysis

| Flanking distance (bp from core) | Effect on core shape (MGW delta, A) | Significance |
|---|---|---|
| 0-2 | Large | Well-known |
| 3-5 | Moderate | Captured by extended k-mer |
| 6-10 | Small but significant | Only captured by Deep DNAshape |
| >10 | Detectable in some contexts | Novel finding |

## Notes

- 2024-01-20: Deep learning model architecture finalized; trained on curated structural dataset.
- 2024-02-08: Comparison with DNAshapeR shows consistent improvement across all four shape features.
- 2024-02-25: Flanking region analysis reveals quantitative effects extending beyond 10 bp from core -- this is new.
- 2024-03-05: High-throughput benchmarking on large sequence sets confirms scalability.
- Key insight: protein-DNA binding specificity studies should incorporate flanking context beyond what k-mer methods provide.
