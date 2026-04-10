# Experimental Log: sRNAfrag Pipeline Development and Benchmarking

## Experiment 1: miRNA fragmentation benchmark

Detection of known mature miRNA loci from precursor sequences.

| Metric | Value |
|---|---|
| Total precursor miRNAs tested | 1,881 |
| Mature miRNA loci correctly detected | 1,762 |
| Sensitivity (recall) | 93.7% |
| False positive loci | 42 |
| Precision | 97.7% |
| F1 Score | 95.6% |

## Experiment 2: 5' seed sequence recovery via multi-mapping

| Approach | Seed Sequences Recovered | % of Known Seeds | Unique to Method |
|---|---|---|---|
| Standard (unique mappers only) | 312 | 52% | 0 |
| sRNAfrag (multi-mapping) | 548 | 91% | 236 |

Key finding: Multi-mapping analysis nearly doubles seed sequence recovery.

## Experiment 3: snoRNA fragment conservation across species

| Species Pair | Conserved Fragment Events | Shared snoRNA Families |
|---|---|---|
| Human - Mouse | 682 | 145 |
| Human - Drosophila | 312 | 68 |
| Human - C. elegans | 198 | 41 |
| Mouse - Drosophila | 219 | 52 |
| Total unique events (in >=2/4 species) | 1,411 | -- |

## Experiment 4: Fragment biotype distribution (human dataset)

| sRNA Biotype | Total Fragments Detected | % of All Fragments |
|---|---|---|
| miRNA | 4,820 | 38.2 |
| snoRNA | 3,115 | 24.7 |
| tRNA | 2,890 | 22.9 |
| snRNA | 1,024 | 8.1 |
| rRNA-derived | 512 | 4.1 |
| Other | 255 | 2.0 |

## Notes

- The 1,411 snoRNA conservation events across eukaryotes suggest functional fragmentation, not random degradation.
- Multi-mapping utilization is critical; discarding these reads loses ~40% of meaningful signal.
- The conserved 5' seed concept from miRNAs may extrapolate to other small RNA fragment classes.
- Pipeline is biotype-agnostic by design, so users can apply it to any annotated sRNA class.
