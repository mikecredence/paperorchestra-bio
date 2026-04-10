# Experimental Log: XRN1 as a Viral Mimicry Dependency

## Experiment 1: DepMap/CCLE correlation screen

Correlated gene knockout sensitivity (CERES score) with ISG expression across 1005 cell lines.

| Gene | Correlation (r) | FDR-adjusted p-value | Known Function |
|---|---|---|---|
| ADAR (p150) | -0.52 | <1e-10 | dsRNA editing (known control) |
| XRN1 | -0.41 | <1e-8 | 5'-3' RNA exonuclease |
| METTL3 | -0.33 | <1e-5 | RNA m6A modification |
| ALKBH5 | -0.28 | <1e-4 | RNA demethylation |
| DIS3 | -0.26 | <1e-3 | RNA exosome subunit |

Negative correlation = more essential in cells with high ISG expression (high retroelement load).

## Experiment 2: Enriched pathways among top hits

| Pathway | Enrichment Score | FDR | # Genes |
|---|---|---|---|
| RNA modification | 3.8 | <0.001 | 12 |
| Nucleic acid metabolism | 3.2 | <0.001 | 18 |
| RNA decay / surveillance | 2.9 | <0.005 | 8 |
| Nonsense-mediated decay | 2.4 | <0.01 | 6 |

## Experiment 3: XRN1 knockout functional validation

| Cell Line | ISG Status | XRN1 KO Viability (% of control) | dsRNA Fold Change | ISG Induction (fold) |
|---|---|---|---|---|
| A549 (high ISG) | High | 18 | 4.2x | 8.5x |
| HeLa (high ISG) | High | 22 | 3.8x | 7.1x |
| MCF7 (low ISG) | Low | 85 | 1.3x | 1.8x |
| HEK293 (low ISG) | Low | 91 | 1.1x | 1.2x |

## Experiment 4: Comparison of XRN1 vs ADAR1 dependency

| Feature | XRN1 | ADAR1 p150 |
|---|---|---|
| Mechanism | Degrades retroelement RNA (5'-3') | Edits dsRNA (A-to-I) |
| Dependency in high-ISG lines | Strong | Strong |
| Dependency in low-ISG lines | Weak | Weak |
| Loss phenotype | dsRNA accumulation, IFN response | dsRNA sensing, IFN response |
| Druggable? | Under investigation | Yes (clinical trials) |

## Notes

- XRN1 is a novel viral mimicry dependency distinct from the ADAR1 editing pathway.
- Cancer cells with high retroelement expression depend on XRN1 to degrade retroelement transcripts before they form dsRNA.
- This opens a new therapeutic axis: inhibiting XRN1 in high-retroelement tumors could phenocopy viral mimicry activation.
