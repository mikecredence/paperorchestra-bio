## Working title
Stable population structure in Europe since the Iron Age, despite high mobility

## Core question
How did population structure across western Eurasia change during the historical period (3,000 YBP to present), and how can stable genetic structure persist despite evidence of high individual mobility?

## Motivation / gap
- Ancient DNA research has revealed dramatic population structure changes during European prehistory (14,000-3,000 YBP) driven by Neolithic farmer and Bronze Age Steppe migrations, but little is known about how structure changed from the historical period onward
- Regional studies of historical genomes (e.g., Rome, Iberian Peninsula) suggest heterogeneity and mobility, but no comprehensive cross-regional assessment of historical genetic structure has been performed
- It is unclear what types of demographic processes impacted western Eurasian genetic makeup over the last ~3,000 years from the end of the Bronze Age to present-day
- The Roman Empire's transportation networks and mobilization of people for trade, labor, and military created unprecedented opportunities for movement, but the genetic consequences are poorly understood
- Standard population genetics models predict that observed levels of long-range dispersal should erode population structure, creating a theoretical paradox

## Core contribution (bullet form)
- Collected whole genomes from 204 individuals across 53 archaeological sites in 18 countries, including first historical genomes from Armenia, Algeria, Austria, and France, with median sequencing depth of 0.92x (range: 0.16x to 2.38x) and median of 685,058 SNPs (167,000 to 1,029,345) per sample on the 1240k panel
- Identified 11% of historical individuals as ancestry outliers, and connected 7% to a putative source in a different region using one-component qpAdm modeling
- Demonstrated that FST-based spatial population structure is relatively stable from the Bronze Age to present-day across ~3,000 years, with isolation-by-distance patterns mirroring geography
- Wright-Fisher simulations showed that even 4% long-range dispersal leads to decreasing FST over 120 generations (~3,000 years with generation time of 25 years), and 8% dispersal causes dramatic collapse of spatial structure
- Found no significant sex bias among outliers vs non-outliers (chi-squared test, p = 0.4117, df = 2; combined outliers p = 0.633, df = 1)
- Proposed transient dispersal hypothesis: the Roman Empire's mobilization decoupled movement from reproduction, explaining the paradox of high mobility with stable structure

## Method in brief
DNA was extracted from powdered cochlear portions of petrous bones (n = 203) or teeth (n = 1) using 50 mg of bone powder with 18-hour Proteinase-K/EDTA incubation, eluted in 50 ul of 10 mM Tris-HCl, 1 mM EDTA, 0.05% Tween-20, pH 8.0. Libraries were prepared using partial uracil-DNA-glycosylase (UDG) treatment (30-minute) and double-indexed with PCR cycling: initial denaturation at 95C for 5 min, 12 cycles of 95C/15s, 60C/30s, 68C/30s, and final elongation at 68C for 5 min. Libraries were purified using MinElute and eluted in 25 uL of 1 mM EDTA, 0.05% Tween-20. Samples were screened requiring >20% alignment to hg19, C>T mismatch rate >=4% at 5'-end, library complexity for >=0.5x coverage, and contamination <=5%. Radiocarbon dating was performed on 126 samples; remaining samples dated by group assignment (n = 49) or archaeological context (n = 29). Data merged with 2,033 present-day, 1,998 prehistoric, and 764 published historical genomes.

Population structure was assessed by PCA on 829 present-day genomes (480,712 SNPs) using smartpca v16000, with ancient genomes projected. Ancestry clustering used qpAdm one-component models with hierarchical UPGMA clustering on dissimilarity matrices (d = -log10(p-value), cutoff = 1.3). Reference populations included 16 groups (e.g., Mbuti.DG n = 4, WHG n = 8, Russia_EBA_Yamnaya_Samara n = 9). FST was calculated on a sliding 10-by-10 degree spatial grid with lowess smoothing and 200 bootstrap replicates. Wright-Fisher spatial simulations used N = 50,000 and sigmaDisp = 0.02 as base parameters, with sigmaDispLR = 0.20 for long-range dispersal, tested at 4% and 8% dispersal rates over 120 generations.

## Target venue
eLife
