Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
High-Resolution snRNA-seq Atlas of Mouse Midbrain Dopamine Neurons Reveals Vulnerability Patterns in a 6-OHDA Lesion Model

## Core question
What is the molecular diversity landscape of mouse midbrain dopamine (mDA) neurons at high resolution, and how do distinct mDA neuron populations differ in their vulnerability to toxin-induced degeneration?

## Motivation / gap
- Previous scRNA-seq studies captured only small fractions of mDA neurons, raising sampling bias concerns
- Whole-cell dissociation for scRNA-seq is biased against sensitive neuron types; snRNA-seq overcomes this
- The diversity of mDA neurons exists as a continuum rather than discrete subtypes, requiring a new nomenclature framework
- The molecular basis for differential vulnerability of SNc vs VTA neurons in Parkinson's disease is poorly understood
- No comprehensive atlas combining high-resolution mDA neuron profiling with a lesion model existed

## Core contribution (bullet form)
- Sequenced ~70,000 mouse midbrain nuclei (36,051 intact + 32,863 lesioned hemisphere), capturing >20% of all mDA neurons per brain (50x improvement over prior studies)
- Organized mDA neuron diversity into 7 "territories" and multiple "neighborhoods" within a continuous gene expression landscape, avoiding misleading discrete subtype boundaries
- Mapped territories to anatomical locations in the adult mouse midbrain using fluorescent RNA in situ hybridization and immunohistochemistry
- Identified differential vulnerability across territories and neighborhoods after partial 6-OHDA lesions (0.7 and 1.5 ug doses), with SNc-associated territories showing greatest cell loss
- Defined vulnerability and resilience gene expression modules that correlate with normalized cell loss across territories and neighborhoods
- Integrated mouse atlas with human mDA neuron data from Parkinson's and Lewy body dementia patients

## Method in brief
DatCre/+; TrapCfl/fl mice expressing nuclear mCherry in dopamine neurons were used. Mice (n=6) received unilateral 6-OHDA injections (0.7 or 1.5 ug) into the medial forebrain bundle; tissues were collected 6 weeks post-lesion. Nuclei were isolated by fluorescence-activated nuclear sorting (FANS) for mCherry+ and mCherry- fractions and sequenced using 10X Genomics Chromium v3. Data underwent normalization, variance stabilization, and dimensional reduction (UMAP). Hierarchical clustering identified 71 clusters, which were organized into territories and neighborhoods based on dendrogram relationships and marker gene expression.

Differential vulnerability was assessed by computing normalized cell loss between intact and lesioned hemispheres for each territory and neighborhood. Vulnerability and resilience gene modules were derived from differentially expressed genes correlating with cell loss patterns. Anatomical mapping used fluorescent RNA in situ hybridization (FISH) with territory-specific probes combined with immunohistochemistry for TH, Sox6, Calb1, and other markers. Cross-species integration with human mDA nuclei was performed using Seurat canonical correlation analysis (CCA).

## Target venue
eLife


## Experimental Log

# Experimental Log: Midbrain Dopamine Neuron Atlas

## Dataset Overview

| Parameter | Value |
|-----------|-------|
| Total nuclei after QC | 68,914 |
| Intact hemisphere nuclei | 36,051 |
| Lesioned hemisphere nuclei | 32,863 |
| mDA neurons (total, both hemispheres) | ~40,000 |
| % mDA neurons captured per brain | >20% (consistently) |
| Improvement over prior study | 50-100x |
| Sequencing platform | 10X Genomics Chromium v3 |
| Mouse model | DatCre/+; TrapCfl/fl |
| Lesioned mice | n = 6 |
| 6-OHDA doses | 0.7 ug (n=3) and 1.5 ug (n=3) |
| Injection site | Medial forebrain bundle (MFB) |
| Collection time | 6 weeks post-lesion |

## Mouse Lines

| Line | Purpose |
|------|---------|
| DatCre | Dopamine transporter-driven Cre |
| TrapCfl (Rpl10a-mCherry) | Cre-dependent nuclear mCherry |
| Pitx3GFP | Additional validation |
| Untreated WT mice | 3 months (n=3) and 18 months (n=3) |
| All mice | Female |

## FANS Gating

| Strategy | Detail |
|----------|--------|
| Gating stringency | Relaxed to avoid excluding low-RFP nuclei |
| Result | ~Equal mCherry+ and mCherry- nuclei per sample |
| Benefit | Avoids bias against low-expressing mDA subtypes |

## Cluster Analysis

| Level | Count |
|-------|-------|
| Total clusters | 71 |
| Major cell types | Neurons, astrocytes, oligodendrocytes, microglia, endothelial, etc. |
| mDA neuron territories | 7 |
| Neighborhoods per territory | Multiple (variable) |
| Mostly-lesion (ML) clusters | Additional clusters appearing primarily in lesioned tissue |

## mDA Neuron Territories (Fig 3)

| Territory | Key Markers | Approximate Anatomical Location |
|-----------|-------------|-------------------------------|
| Territory 1 (SNc-lateral) | Sox6+, Calb1- | Lateral SNc |
| Territory 2 (SNc-medial) | Sox6+, specific markers | Medial SNc |
| Territory 3 (VTA-medial) | Calb1+, Sox6- | Medial VTA |
| Territory 4 (VTA-lateral) | Calb1+, specific markers | Lateral VTA |
| Territory 5 | Specific markers | Intermediate region |
| Territory 6 | Specific markers | -- |
| Territory 7 | Specific markers | -- |
| ML clusters | Clic4, Creb5, Mmp12, Sprr1a | Primarily in lesioned tissue |

Fig 3A: UMAP projection with territory color-coding shows continuous distribution.
Fig 3B: Sox6 and Calb1 co-expression delineates SNc (Sox6+) and VTA (Calb1+) regions.
Fig 3C: Hierarchical dendrograms with territory and neighborhood markers.

## Anatomical Mapping (Fig 4)

| Approach | Targets |
|----------|---------|
| Immunohistochemistry | TH, Sox6, Calb1, Aldh1a1 |
| Fluorescent RNA ISH | Territory-specific probes (Tacr3, others) |
| Animals per experiment | 2-3 |
| ML probe testing | On lesioned (n=3) and control mice |

Fig 4A: Color-coded UMAP with individual enriched genes.
Fig 4B-E: IHC and FISH staining confirming territory localization.
Fig 4F: Schematic of territory positions in ventral midbrain.

## 6-OHDA Lesion Results

### Normalized Cell Loss by Territory (Fig 5C)

| Territory | Normalized Cell Loss (%) | Vulnerability |
|-----------|------------------------|---------------|
| SNc-associated territories | Highest (>50-70%) | Most vulnerable |
| VTA-associated territories | Lower (<30%) | More resilient |
| Intermediate territories | Variable | -- |

Fig 5A-B: UMAP projections of intact vs lesioned hemisphere show differential depletion.
Fig 5C: Bar chart of normalized cell loss percentages per territory.
Fig 5D: Pairwise comparisons of cell loss across territories.

### Normalized Cell Loss by Neighborhood (Fig 5E)

| Observation | Detail |
|-------------|--------|
| Within-territory heterogeneity | Neighborhoods within same territory differ in vulnerability |
| Pairwise comparisons | Statistical tests between neighborhoods within territories |
| Pattern | Gradient of vulnerability even within SNc |

## Vulnerability and Resilience Modules (Fig 6)

### Vulnerability Module

| Territory | Module Expression | Cell Loss |
|-----------|------------------|-----------|
| High-loss territories | Higher vulnerability module expression | High |
| Low-loss territories | Lower vulnerability module expression | Low |
| Correlation | Positive correlation with cell loss |

Fig 6A: Violin plots of vulnerability module across territories with cell loss percentages at bottom.
Fig 6B: Violin plots across neighborhoods.

### Resilience Module

| Territory | Module Expression | Cell Loss |
|-----------|------------------|-----------|
| High-loss territories | Lower resilience module expression | High |
| Low-loss territories | Higher resilience module expression | Low |
| Correlation | Negative correlation with cell loss |

Fig 6C-D: Violin plots of resilience module show inverse pattern to vulnerability.

## Mostly-Lesion (ML) Clusters (Fig 7)

| Property | Value |
|----------|-------|
| Identification | Clusters predominantly present in lesioned hemisphere |
| Markers | Clic4, Creb5, Mmp12, Sprr1a |
| Interpretation | Stress-response states of surviving neurons |
| Transcriptional kinship | Can be linked to specific territories of origin |

Fig 7A-B: UMAP projections showing ML clusters marked with dashed circles in intact vs lesioned.
Fig 7C: Integrated dataset color-coded by territory.
Fig 7D-E: Sox6 and Calb1 expression in intact and lesioned nuclei.

## Human-Mouse Integration (Fig 8)

### Integration Dataset

| Species | Nuclei Count | Conditions |
|---------|-------------|------------|
| Human | 25,003 | Control + PD + LBD |
| Mouse | 33,052 | Intact + Lesioned |
| Integration method | Seurat CCA |

### Cross-Species Findings

| Observation | Detail |
|-------------|--------|
| Territory correspondence | Mouse territories map to human mDA subtypes |
| Disease overlap | PD-vulnerable human subtypes correspond to vulnerable mouse territories |
| Conservation | Gene expression programs partially conserved |

Fig 8A-B: UMAP projections of integrated human/mouse nuclei split by condition.
Fig 8C: Grouping by condition shows overlap between species.

## DAT Binding Autoradiography

| Method | Detail |
|--------|--------|
| Sections | 12 um fresh frozen |
| Ligand | 125I-RTI55 (50 pM) |
| Nonspecific binding | 100 uM nomifensine |
| Exposure | 2 days |
| Purpose | Validate dopamine terminal loss in lesioned striatum |

## Data Availability

| Resource | Accession |
|----------|-----------|
| Sequencing data | GEO: GSE233866 |
| Interactive visualization | CELLxGENE via perlmannlab.org/resources |

## Key Figure Observations

- Fig 1: Study design schematic with unilateral 6-OHDA injection, FANS, and 10X sequencing
- Fig 2A: UMAP of all nuclei with 71 clusters color-coded by cell type
- Fig 2B: Canonical DA markers (Th, Slc6a3, Slc18a2) in UMAP
- Fig 2C: Hierarchical dendrogram with cell-type markers
- Fig 3: Territory and neighborhood organization shows continuous landscape
- Fig 4: Anatomical mapping validates territory positions in midbrain sections
- Fig 5: Differential cell loss across territories confirms SNc > VTA vulnerability
- Fig 6: Vulnerability/resilience modules correlate with cell loss
- Fig 7: ML clusters represent stress-response states with traceable origins
- Fig 8: Human-mouse integration reveals conserved vulnerability patterns

