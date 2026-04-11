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
