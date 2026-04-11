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
