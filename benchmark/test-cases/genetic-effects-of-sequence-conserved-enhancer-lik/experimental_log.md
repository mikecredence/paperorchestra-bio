# Experimental Log -- Conserved Enhancer-Like Elements and Complex Traits

## 2024-01-15 -- Dataset assembly

Compiled epigenomic datasets and GWAS summary statistics for the analysis.

| Resource | Count |
|---|---|
| Epigenomic datasets | 313 |
| Tissues / cell types | 106 |
| GWAS datasets (total) | 468 |
| GWAS ancestry: European (EUR) | ~400 |
| GWAS ancestry: East Asian (EAS) | ~68 |

## 2024-02-10 -- CELE identification pipeline

Ran the conservation x enhancer intersection pipeline. Elements required both human-mouse sequence conservation and enhancer-like biochemical activity (H3K27ac/H3K4me1/DNase signal).

Pipeline scales linearly across all 313 epigenomic datasets -- no bottleneck observed.

## 2024-03-05 -- Heritability enrichment results (S-LDSC)

Tested heritability enrichment of CELEs for representative traits across tissues.

| Trait | Top enriched tissue | Enrichment (fold) | P-value |
|---|---|---|---|
| BMI | Hypothalamus / CNS | >2x | <1e-5 |
| Schizophrenia | Brain (cortex) | >2x | <1e-5 |
| Height | Musculoskeletal | significant | <0.05 |
| Type 2 diabetes | Pancreatic islets | significant | <0.05 |
| LDL cholesterol | Liver | significant | <0.05 |

Note: Many traits showed tissue-specific patterns consistent with known biology.

## 2024-03-20 -- Cross-ancestry comparison

| Ancestry | Number of GWAS | Traits with significant CELE enrichment |
|---|---|---|
| EUR | ~400 | Majority of tested traits |
| EAS | ~68 | Consistent enrichment for shared traits |

Cross-ancestry replication supports biological relevance rather than LD artifacts.

## 2024-04-01 -- Candidate gene discovery

Fine-mapping within CELEs nominated novel candidate genes not reported in previous GWAS.

| Trait | Novel candidate genes identified | Previously reported genes overlapping |
|---|---|---|
| BMI | Multiple new loci | Yes, strong overlap with known GWAS hits |
| Schizophrenia | Multiple new loci | Yes, strong overlap with known GWAS hits |

Functional validation notes: Nominated genes show relevant expression patterns and pathway membership for their respective traits.

## Summary

Conserved enhancer-like elements provide a powerful lens for interpreting GWAS across tissues and ancestries. The resource (313 epigenomic datasets, 106 tissues, 468 GWAS) is comprehensive and identifies novel biology for BMI and schizophrenia.
