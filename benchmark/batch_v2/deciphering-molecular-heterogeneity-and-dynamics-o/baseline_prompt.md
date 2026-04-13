Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
Molecular Heterogeneity and Transcriptional Dynamics of Human Hippocampal Neural Stem Cells Across Neonatal, Adult, Aging, and Stroke-Injured States

## Core question
What is the molecular heterogeneity of human hippocampal neural stem cells across developmental stages and injury conditions, and can we identify the transcriptional dynamics that explain why adult neurogenesis is so rarely observed in humans?

## Motivation / gap
- Whether adult hippocampal neurogenesis persists in humans has been intensely debated, with conflicting evidence from both immunostaining and snRNA-seq studies
- Well-known neurogenic markers (DCX, PROX1, STMN2) lack specificity in humans because they are also expressed in GABAergic interneurons, risking contamination when identifying immature granule cells
- The homeostasis and developmental potentials of human hippocampal NSCs under different age contexts (neonatal, adult, aging) remain unclear
- Whether quiescent NSCs in the aging human hippocampus can be reactivated after injury (as shown in mice) was unknown
- No single-nucleus atlas had comprehensively profiled human hippocampal neurogenic lineages across neonatal through aging and injury states in one integrated study
- The transcriptional signatures distinguishing quiescent NSC subtypes from astrocytes had not been resolved in human tissue

## Core contribution (bullet form)
- Generated a single-nucleus atlas of 92,966 nuclei (after QC from 99,635) from 10 human hippocampal samples spanning neonatal (D4), adult (31-32y), aging (50-68y), and stroke injury (48y) conditions, identifying 16 major cell populations
- Discovered that pNSC and aNSC cell numbers decrease markedly with aging but are recovered in the stroke-injured hippocampus
- Identified new specific neuroblast markers (CALM3, NEUROD2, NRGN, NGN1) by excluding genes expressed in GABAergic interneurons, overcoming the lack of specificity of traditional markers like DCX
- Used cross-species integration (human, mouse, pig, rhesus macaque) combined with scHPF and Seurat analysis to identify and validate specific markers for human neurogenic lineage subtypes (qNSC1, qNSC2, pNSC, aNSC)
- RNA velocity and pseudotime analysis revealed that a subset of NSCs acquires quiescent properties after birth, most NSCs become deeply quiescent during aging, and certain deep quiescent NSCs are reactivated following stroke injury
- Median genes detected per nucleus: 3,001; mitochondrial gene threshold for QC: 20%

## Method in brief
Ten post-mortem human hippocampal tissues were collected from donors ranging from neonatal (day 4) to 68 years old, organized into four groups: neonatal (n=1), adult (n=2, ages 31-32), aging (n=6, ages 50-68), and stroke injury (n=1, age 48). The anterior-middle hippocampus containing the dentate gyrus was dissected for 10x Genomics single-nucleus RNA-sequencing. Counterpart hippocampi were used for immunostaining validation. Nuclei were isolated following the 10x Genomics protocol for adult brain tissue, with myelin removal and FACS sorting for DAPI-positive nuclei. After QC filtering (removal of debris, aggregates, and cells with >20% mitochondrial transcripts), 92,966 nuclei were retained with a median of 3,001 genes per nucleus.

Cells were clustered into 16 populations via UMAP using classical markers and differentially expressed genes. Neurogenic lineage identity was confirmed through cross-species integration with published mouse, pig, and macaque snRNA-seq data. Novel cell-type markers were identified using single-cell Hierarchical Poisson Factorization (scHPF) and Seurat's FindAllMarkers, with specificity verified by excluding genes co-expressed in GABAergic interneurons. Developmental trajectories were inferred using RNA velocity analysis and pseudotime reconstruction, revealing the transition from active to quiescent states during aging and reactivation following injury.

## Target venue
eLife


## Experimental Log

# Experimental Log: Human Hippocampal NSC Heterogeneity and Dynamics

## Overview

Single-nucleus RNA-seq atlas of the human hippocampus across neonatal, adult, aging, and stroke-injured states. Identified NSC subtypes, novel markers, and transcriptional dynamics of neurogenesis decline and reactivation.

---

## Sample Collection

### Table 1: Donor Information

| Donor ID | Age | Group | Sex | Cause of Death | Post-Mortem Interval |
|----------|-----|-------|-----|---------------|---------------------|
| D4 | Postnatal day 4 | Neonatal | - | Congenital heart disease | ~3-4 hours |
| 31y | 31 years | Adult | Male | Cerebral infarction | ~3-4 hours |
| 32y | 32 years | Adult | Male | Traumatic death (motor vehicle) | ~3-4 hours |
| 48y | 48 years | Stroke injury | - | Hypoxic-ischemic encephalopathy | ~3-4 hours |
| 50y | 50 years | Aging | - | Hypertension | ~3-4 hours |
| 56y | 56 years | Aging | - | Lung carcinoma | ~3-4 hours |
| 60y | 60 years | Aging | - | Lung carcinoma | ~3-4 hours |
| 64y-1 | 64 years | Aging | - | Multiple organ failure | ~3-4 hours |
| 64y-2 | 64 years | Aging | - | Lung carcinoma | ~3-4 hours |
| 68y | 68 years | Aging | - | Urinary bladder carcinoma | ~3-4 hours |

### Table 2: Sample Group Summary

| Group | Number of Donors | Age Range | Notes |
|-------|-----------------|-----------|-------|
| Neonatal | 1 | Day 4 | Single neonatal sample |
| Adult | 2 | 31-32 years | Both male |
| Aging | 6 | 50-68 years | Includes 3 lung carcinoma cases |
| Stroke injury | 1 | 48 years | Hypoxic-ischemic encephalopathy |
| Total | 10 | D4 to 68y | 1 female, 9 males |

---

## Single-Nucleus RNA-Seq Quality Control

### Table 3: Sequencing and QC Summary

| Metric | Value |
|--------|-------|
| Total nuclei sequenced | 99,635 |
| Nuclei retained after QC | 92,966 |
| Nuclei removed | 6,669 |
| Median genes per nucleus | 3,001 |
| Mitochondrial gene threshold | 20% |
| QC filters applied | Cell debris removal, aggregate removal, mito-gene filtering |
| Sequencing platform | 10x Genomics |
| Region used | Anterior-middle hippocampus (with DG structure) |

### Table 4: Nuclei Isolation Protocol Key Steps

| Step | Details |
|------|---------|
| Tissue preparation | Frozen hippocampus minced with surgical scissors on ice |
| Equilibration medium | Hibernate A / B27 / GlutaMAX |
| Lysis buffer | 10 mM Tris-HCl, 10 mM NaCl, 3 mM MgCl2, 0.1% NP-40 substitute |
| Lysis incubation | 15 min on ice with gentle shaking |
| Trituration | 10-15 passes with Pasteur pipette |
| Filtration | 30 um MACS SmartStrainer |
| Centrifugation | 500 x g, 5 min, 4 C |
| Wash buffer | 1X PBS, 1.0% BSA, 0.2 U/ul RNase inhibitor |
| Myelin removal | Miltenyi Myelin Removal Beads II |
| Nuclear sorting | FACS for DAPI-positive nuclei |

---

## Cell Population Identification

### Table 5: 16 Major Cell Populations Identified

| Population | Abbreviation | Nuclei Count | Category |
|-----------|-------------|-------------|----------|
| Astrocyte 1 | AS1 | 1,146 | Glial |
| Astrocyte 2 / Quiescent NSC | AS2/qNSC | Present | Glial/Stem |
| Primed NSC | pNSC | Present | Stem |
| Active NSC | aNSC | Present | Stem |
| Neuroblast | NB | Present | Neurogenic |
| Granule Cell | GC | Present | Neuronal |
| GABAergic Interneuron | GABA-IN | Present | Neuronal |
| Pyramidal Neuron | PN | Present | Neuronal |
| Oligodendrocyte Progenitor | OPC | Present | Glial |
| Oligodendrocyte | OLG | Present | Glial |
| Microglia | MG | Present | Immune |
| Endothelial Cell | EC | Present | Vascular |
| Pericyte | Per | Present | Vascular |
| Cajal-Retzius Cell (Reelin+) | CR | Present | Neuronal |
| Unidentified 1 | UN1 | Present | Unknown |
| Unidentified 2 | UN2 | Present | Unknown |
| **Total** | - | **92,966** | - |

---

## NSC Subtype Heterogeneity

### Table 6: NSC Subtypes Identified in Neurogenic Lineage

| Subtype | Full Name | Key Properties | Identified By |
|---------|-----------|---------------|---------------|
| qNSC1 | Quiescent NSC type 1 | Quiescent transcriptional signature | scHPF + Seurat |
| qNSC2 | Quiescent NSC type 2 | Quiescent, distinct from qNSC1 | scHPF + Seurat |
| pNSC | Primed NSC | Intermediate between quiescent and active | scHPF + Seurat |
| aNSC | Active NSC | Actively proliferating | scHPF + Seurat |

### Table 7: Key Marker Genes by NSC Subtype

| Cell Type | Representative Specific Markers | Method |
|-----------|-------------------------------|--------|
| qNSC1 | LRRC3B, RHOJ, SLC4A4 | scHPF + FindAllMarkers |
| qNSC2 | Distinct from qNSC1 (see Fig 3A-B) | scHPF + FindAllMarkers |
| pNSC | Specific genes identified (Fig 3A-B) | scHPF + FindAllMarkers |
| aNSC | Proliferation-associated genes | scHPF + FindAllMarkers |
| Neuroblast | CALM3, NEUROD2, NRGN, NGN1 | Exclusion of GABA-IN genes |

---

## Marker Specificity Analysis

### Table 8: Traditional Markers and Their Specificity Problem

| Marker Gene | Traditional Use | Problem in Humans | Implication |
|------------|----------------|-------------------|-------------|
| DCX | Immature GC / neuroblast marker | Widely expressed in GABAergic interneurons | Risk of interneuron contamination |
| PROX1 | Immature GC marker | Expressed in GABAergic interneurons | Non-specific for neurogenesis |
| STMN2 | Immature GC marker | Expressed in GABAergic interneurons | Non-specific for neurogenesis |

### Table 9: Newly Identified Specific Neuroblast Markers

| Marker Gene | Specificity | Method of Identification |
|------------|------------|------------------------|
| CALM3 | Expressed in neuroblasts but NOT in GABAergic interneurons | Exclusion analysis |
| NEUROD2 | Expressed in neuroblasts but NOT in GABAergic interneurons | Exclusion analysis |
| NRGN | Expressed in neuroblasts but NOT in GABAergic interneurons | Exclusion analysis |
| NGN1 | Expressed in neuroblasts but NOT in GABAergic interneurons | Exclusion analysis |

### Table 10: NSC Marker Validation Against Literature

| Marker | Source | Finding in This Study |
|--------|--------|----------------------|
| ETNPPL | Previously reported as NSC marker | Highly expressed in qNSC1/2 (confirmed) |
| STMN1/2 | Previously reported in neuroblasts | Neuroblasts maintained in adult hippocampus (confirmed) |
| HOPX | Known NSC gene | Expressed in NSC populations |
| SOX2 | Known NSC gene | Expressed in NSC populations |
| VIM | Known NSC gene | Expressed in NSC populations |
| NES | Known NSC gene | Expressed in NSC populations |
| CHI3L1 | Known NSC gene | Expressed in NSC populations |
| ASCL1 | Neural progenitor / proliferation gene | Dynamic expression across ages |
| EOMES | Neural progenitor gene | Dynamic expression across ages |

---

## Cross-Species Integration

### Table 11: Cross-Species Comparison Design

| Species | Data Type | Source | Purpose |
|---------|-----------|--------|---------|
| Human | snRNA-seq (this study) | 10 donors, 92,966 nuclei | Primary dataset |
| Mouse | snRNA-seq (published) | Hochgerner et al. 2018 | Cross-species validation |
| Pig | snRNA-seq (published) | Franjic et al. 2022 | Cross-species validation |
| Rhesus macaque | snRNA-seq (published) | Franjic et al. 2022 | Cross-species validation |
| Cynomolgus monkey | Immunostaining | 3-month female, 2.3 kg | Protein-level validation |

Fig 2A: UMAP integration of human, mouse, pig, and macaque data confirms neurogenic lineage identity across species.

---

## Age-Dependent Changes in NSC Populations

### Table 12: NSC Population Changes Across Age Groups

| Cell Population | Neonatal (D4) | Adult (31-32y) | Aging (50-68y) | Stroke Injury (48y) |
|----------------|--------------|----------------|----------------|---------------------|
| qNSC1 | Present | Present | Present (deep quiescence) | Present |
| qNSC2 | Present | Present | Present (deep quiescence) | Present |
| pNSC | Abundant | Markedly decreased | Markedly decreased | Recovered |
| aNSC | Abundant | Markedly decreased | Markedly decreased | Recovered |
| Neuroblast | Present | Reduced | Reduced | Present |
| Granule Cells | Present | Present | Present | Some loss (by %) |

Fig 1E: Quantification of cell population percentages across groups shows pNSC and aNSC decrease markedly with aging but recover in the injured hippocampus.

Fig 5A-B: Feature plots and quantification of neurogenic populations during aging (neonatal, adult, aging).

### Table 13: Gene Expression Dynamics Across Ages

| Gene Category | Representative Genes | Neonatal | Adult | Aging | Injury |
|--------------|---------------------|----------|-------|-------|--------|
| qNSC-specific (new) | LRRC3B, RHOJ, SLC4A4 | Expressed | Maintained | Deep quiescence signature | Present |
| NSC markers | HOPX, SOX2, VIM, NES, CHI3L1 | High | Reduced | Low | Reactivated |
| Proliferation genes | ASCL1, EOMES | High | Low | Very low | Partially reactivated |
| Neuroblast markers (new) | CALM3, NEUROD2, NRGN | Present | Reduced | Rare | Present |

Fig 5C shows dynamic gene expression of representative genes across ages.

---

## RNA Velocity and Pseudotime Analysis

### Table 14: Developmental Trajectory Analysis (Neonatal)

| Analysis | Key Finding |
|----------|------------|
| RNA velocity (neonatal D4) | Developmental trajectory from qNSC through pNSC/aNSC to neuroblast/GC |
| Pseudotime reconstruction | Continuous gradient from stem cells to differentiated neurons |
| qNSC1 vs qNSC2 vs pNSC GO terms | Differentially enriched biological processes (Fig 4B) |
| Direction of differentiation | qNSC -> pNSC -> aNSC -> NB -> GC |

Fig 4A: RNA velocity vectors in the neonatal neurogenic lineage show directional flow from qNSCs through to granule cells.
Fig 4B: GO term analysis of DEGs comparing qNSC1/qNSC2 with pNSC reveals distinct biological process enrichment.
Fig 4C: Pseudotime reconstruction places neurogenic lineage cells on a continuous developmental trajectory.

---

## Stroke-Induced Reactivation

### Table 15: Neurogenic Lineage in Injured Hippocampus (48y Stroke)

| Cell Type | Status in Injury | Evidence |
|-----------|-----------------|---------|
| qNSC1 | Present | snRNA-seq |
| qNSC2 | Present | snRNA-seq |
| Reactivated pNSC/aNSC | Recovered (vs aging controls) | snRNA-seq + immunostaining |
| Neuroblast | Present | snRNA-seq |
| NES+/Ki67+ cells | Detected in injured DG | Immunofluorescence |
| VIM+ cells | Detected with radial morphology | Immunofluorescence |
| CHI3L1+/NES+ cells | Detected as active NSCs | Immunofluorescence |

Fig 6A: Feature plots of neurogenic lineage in the injured hippocampus showing qNSC1, qNSC2, reactivated pNSC/aNSC, and NB.
Fig 6B: Immunofluorescence images confirm active NSC cells (NES+/Ki67+, VIM+, CHI3L1+/NES+) with radial morphology in the 48-year-old injured hippocampal dentate gyrus.

---

## Gene Set Score Analysis

### Table 16: Distinguishing qNSCs from Astrocytes

| Analysis | Purpose | Outcome |
|----------|---------|---------|
| Gene set score analysis | Separate qNSCs from transcriptionally similar astrocytes | Successfully distinguished despite transcriptional overlap |
| AS2/qNSC population | Initially clustered together due to similarity | Resolved into distinct populations |

---

## Analytical Tools and Methods

### Table 17: Computational Methods Used

| Method | Application |
|--------|------------|
| 10x Genomics snRNA-seq | Single-nucleus transcriptomics |
| UMAP | Dimensionality reduction and visualization |
| Seurat (FindAllMarkers) | Differential gene expression and marker identification |
| scHPF (Hierarchical Poisson Factorization) | Cell-type specific gene identification |
| RNA velocity | Developmental trajectory inference |
| Pseudotime reconstruction | Ordering cells along developmental continuum |
| Cross-species UMAP integration | Validation of cell type identity across species |
| Gene set score analysis | Distinguishing transcriptionally similar populations |
| Immunofluorescence / immunostaining | Protein-level validation of markers |
| GO term analysis | Functional annotation of DEGs |

### Table 18: Key QC and Processing Statistics

| Parameter | Value |
|-----------|-------|
| Total nuclei pre-QC | 99,635 |
| Total nuclei post-QC | 92,966 |
| Retention rate | 93.3% |
| Median genes/nucleus | 3,001 |
| Mito gene threshold | 20% |
| Number of cell populations | 16 |
| Number of NSC subtypes | 4 (qNSC1, qNSC2, pNSC, aNSC) |
| Cross-species datasets integrated | 4 (human, mouse, pig, macaque) |
| Total donors | 10 |
| Age groups | 4 (neonatal, adult, aging, injury) |

---

## Key Figure Observations

- Fig 1B-D: UMAP visualization of 92,966 nuclei into 16 populations with classical markers and DEGs
- Fig 1E: Cell composition varies substantially across neonatal, adult, aging, and injured hippocampus; pNSC and aNSC markedly decrease with age but recover after stroke
- Fig 1-supplement 1F: Average detected genes per cell type similar across groups, ruling out artifacts from global gene expression changes
- Fig 2: Cross-species integration confirms neurogenic lineage conservation
- Fig 3A-B: scHPF and FindAllMarkers identify top specific genes for each NSC subtype
- Fig 3C: UMAP visualization of predicted cell-type specific genes
- Fig 3D: Heatmap showing traditional neuroblast/imGC markers are non-specific due to GABAergic interneuron expression
- Fig 4A: RNA velocity in neonatal hippocampus shows developmental trajectory direction
- Fig 5: Age-dependent decline of neurogenic populations quantified
- Fig 6: Stroke injury reactivates deep quiescent NSCs, confirmed by both snRNA-seq and immunostaining

---

## References to Prior Conflicting Studies

### Table 19: Prior Studies on Human Adult Hippocampal Neurogenesis

| Study Finding | Evidence Type | Conclusion |
|--------------|---------------|-----------|
| No neurogenesis after adolescence | Marker immunostaining | Negative (multiple studies) |
| Neurogenesis persists but declines | Marker immunostaining | Positive (multiple studies) |
| No adult neurogenic trajectories | snRNA-seq | Negative (one study) |
| NSCs and immature neurons found in adult/aged hippocampi | snRNA-seq | Positive (two studies) |
| This study | snRNA-seq + immunostaining + cross-species | Supports persistence with deep quiescence and injury reactivation |

