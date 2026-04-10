# Experimental Log -- TKSM Long-Read Simulator

## 2024-01-30 -- Module architecture finalized

Each step is a standalone module. Current module inventory:

| Module | Input | Output | Purpose |
|---|---|---|---|
| Transcriptome sampler | GTF + expression matrix | Transcript pool | Sample isoforms by abundance |
| Truncation | Transcript pool | Truncated reads | Model incomplete reverse transcription |
| PCR | Molecule pool | Amplified pool | PCR duplication and bias |
| Fragmentation | Full-length reads | Fragments | For cDNA fragmentation protocols |
| Error model | Clean reads | Noisy reads | Platform-specific error injection |
| Adapter ligation | Reads | Adapted reads | Add sequencing adapters |
| Single-cell wrapper | Cell barcodes + reads | SC-tagged reads | Single-cell LR support |

## 2024-02-28 -- Validation against real ONT and PacBio data

Compared TKSM-simulated read characteristics to real datasets (SIRV spike-in and human GM12878).

### Read length distribution comparison (KS test)

| Dataset | Platform | TKSM KS statistic | Competitor A (NanoSim-T) | Competitor B (IsoSeqSim) |
|---|---|---|---|---|
| SIRV | ONT | 0.032 | 0.085 | 0.110 |
| GM12878 | ONT | 0.041 | 0.092 | 0.125 |
| SIRV | PacBio | 0.028 | 0.078 | 0.045 |
| GM12878 | PacBio | 0.038 | 0.088 | 0.052 |

Lower KS = better fit. TKSM consistently closest to real data distributions.

### Error rate comparison (simulated vs real)

| Platform | Real error rate (%) | TKSM (%) | NanoSim-T (%) | IsoSeqSim (%) |
|---|---|---|---|---|
| ONT R10 | 5.2 | 5.4 | 6.1 | 4.0 (underestimates) |
| PacBio HiFi | 0.3 | 0.3 | 0.8 | 0.4 |

## 2024-03-20 -- Benchmarking downstream tools with TKSM ground truth

Used TKSM to generate gold-standard simulated datasets with known isoforms, then ran isoform detection tools.

### Isoform detection accuracy (F1-score on TKSM-simulated data)

| Tool | TKSM ONT sim | TKSM PacBio sim | Real ONT (SIRV, known truth) |
|---|---|---|---|
| FLAIR | 0.78 | 0.82 | 0.76 |
| StringTie2 | 0.81 | 0.85 | 0.80 |
| FLAMES | 0.75 | 0.80 | 0.74 |
| Bambu | 0.83 | 0.87 | 0.82 |

Tool rankings on TKSM-simulated data match those on real SIRV data, supporting the simulator's fidelity.

## 2024-04-05 -- Scalability and runtime

| Reads simulated | TKSM runtime (min) | NanoSim-T runtime (min) | IsoSeqSim runtime (min) |
|---|---|---|---|
| 100K | 2.1 | 8.5 | 5.2 |
| 1M | 12.5 | 78.0 | 45.0 |
| 10M | 95.0 | 680.0 | 410.0 |

TKSM is 5-7x faster than NanoSim-T and 3-4x faster than IsoSeqSim due to modular parallelization.

## 2024-04-12 -- PCR module validation

| PCR cycles | Expected duplication rate | TKSM simulated rate | Real ONT cDNA rate |
|---|---|---|---|
| 10 | ~5% | 4.8% | 5.1% |
| 14 | ~15% | 14.2% | 15.5% |
| 18 | ~30% | 28.5% | 31.0% |

PCR module accurately recapitulates duplication as function of cycle number.
