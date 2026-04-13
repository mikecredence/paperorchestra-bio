# Experimental Log: Stable Population Structure in Europe Since the Iron Age

## Dataset Overview

| Parameter | Value |
|-----------|-------|
| Newly reported genomes | 204 |
| Archaeological sites | 53 |
| Countries | 18 |
| Previously reported individuals (subset) | 26 |
| Radiocarbon-dated samples | 126 |
| Group-assigned dates | 49 |
| Archaeological context dates | 29 |
| DNA source: petrous bone | n = 203 |
| DNA source: teeth | n = 1 |
| Median genome-wide depth | 0.92x |
| Depth range | 0.16x to 2.38x |
| Median SNPs per sample (1240k panel) | 685,058 |
| SNP range | 167,000 to 1,029,345 |
| Published present-day genomes integrated | 2,033 |
| Published prehistoric genomes integrated | 1,998 |
| Published historical genomes integrated | 764 |
| Contaminated samples excluded | n = 9 |

---

## Time Period Definitions

| Period | Date Range |
|--------|-----------|
| Mesolithic and Neolithic | 10000 BCE - 3500 BCE |
| Copper Age | 3500 BCE - 2300 BCE |
| Bronze Age | 2300 BCE - 1000 BCE |
| Iron Age | 1000 BCE - 1 CE |
| Imperial Rome & Late Antiquity | 1 CE - 700 CE |
| Medieval Ages & Early Modern | 700 CE - 1900 CE |
| Present-day | 1900 CE - onward |

---

## Regional Population Structure Analysis

### Ancestry cluster identification
- Average genetic clusters per region during historical period: 10
- Minimum clusters: 2
- Maximum clusters: 23
- Regions analyzed: 14 geographical regions across 3 sub-periods

### Armenia (Figure 2)
- Population highly homogeneous at any given time
- Two distinct genetic clusters separated by temporal split around 772-403 BCE
- Earlier cluster C1: newly reported samples (n = 5) from Beniamin + published (n = 6) from 5 other sites
- Later cluster C3: newly reported samples (n = 12) from Beniamin dating 403 BCE-500 CE, genetically similar to present-day Armenians
- C3 modeled using ~50% of C1 plus additional Steppe ancestry

### Southeastern Europe (Figure 3)
- Core group with Central European-like ancestry (C6)
- Clusters with Northern European (C7) and Eastern Mediterranean (C8) ancestry
- Individuals of eastern nomadic (Sarmatian-like) ancestry: C2, n = 2
- Imperial Roman & Late Antiquity period: high heterogeneity

### Western Europe (Figure 4)
- Heterogeneous Imperial Roman & Late Antiquity population
- Sarmatian-like ancestry individuals: C8, n = 2
- Individual R10667 from Wels, Austria (frontier of Roman Empire) modeled using Canary Islander or Iron Age Kerkouane outlier ancestry

---

## Ancestry Outlier Analysis (Figure 5)

### Outlier identification criteria
- Ancestry cluster underrepresented: <5% of individuals in region OR at most 2 individuals
- Time range considered: Bronze Age to present-day
- First-generation migrant identification: 100% one-component qpAdm model from different region

### Outlier proportions

| Category | Proportion |
|----------|-----------|
| Total outliers | 11% |
| Outliers with identified source | 7% |

Note: 7% is conservative; actual non-local proportion expected to be higher.

### Sex bias analysis (chi-squared test)

| Comparison | Test | p | df |
|------------|------|---|------|
| Males vs females across outlier/non-outlier groups | chi-squared | 0.4117 | 2 |
| Combined outliers vs non-outliers | chi-squared | 0.633 | 1 |

---

## Population Structure Stability (Figure 6)

### FST Analysis
- FST calculated on sliding 10x10 degree spatial grid
- Isolation-by-distance pattern recovered in each time period
- Large decrease in FST from Mesolithic & Neolithic to Bronze Age (~10,000-2300 BCE)
- From Bronze Age onward: FST does not decrease further with time
- Confidence intervals: 200 bootstrap replicates
- European and Mediterranean population structure relatively stable over last 3,000 years

### PCA Genetic Maps
- PCA performed on 829 present-day individuals (480,712 SNPs)
- Historical period genomes projected onto same PC space
- Historical period structure mirrors present-day geographic structure
- Prehistoric genomes show much weaker correspondence to present-day PCA

---

## Simulation Analysis (Figure 7)

### Wright-Fisher spatial population model

| Parameter | Value |
|-----------|-------|
| Population size (N) | 50,000 |
| Base dispersal (sigmaDisp) | 0.02 |
| Long-range dispersal (sigmaDispLR) | 0.20 |
| Calibrated maximum FST | ~0.03 |
| Simulation duration | 120 generations |
| Generation time assumed | 25 years |
| Total time simulated | ~3,000 years |

### Simulation results

| Long-range dispersal rate | Outcome after 120 generations |
|--------------------------|-------------------------------|
| 0% (base only) | Stable FST ~0.03 |
| 4% | Decreasing FST; spatial structure eroding |
| 8% | Dramatic FST decrease; structure collapses; hardly detectable in first two PCs |

---

## Methods Parameters

### DNA Extraction and Library Preparation

| Parameter | Value |
|-----------|-------|
| Bone powder used | 50 mg |
| Incubation | 18-hour in Proteinase-K and EDTA |
| Elution volume | 50 ul |
| Elution buffer | 10 mM Tris-HCl, 1 mM EDTA, 0.05% Tween-20, pH 8.0 |
| DNA extract for library prep | 12.5-25 uL |
| UDG treatment | Partial (30 minute) |
| PCR initial denaturation | 95C for 5 min |
| PCR cycles | 12 |
| PCR cycle conditions | 95C/15s, 60C/30s, 68C/30s |
| PCR final elongation | 68C for 5 min |
| Post-indexing purification elution | 25 uL of 1 mM EDTA, 0.05% Tween-20 |

### Sample Screening Criteria

| Criterion | Threshold |
|-----------|-----------|
| Reads aligned to hg19 | >20% |
| C>T mismatch rate at 5'-end | >=4% |
| G>A mismatch rate at 3'-end | >=4% |
| Minimum achievable coverage | 0.5x |
| Maximum contamination | <=5% |

### Contamination Assessment Methods
1. Damage pattern and polymorphism in mtDNA (Schmutzi)
2. Atypical X/Y chromosome to autosome coverage ratios (ANGSD)
3. X chromosome heterozygosity in males (chrX:5000000-154900000 in hg19) (ANGSD)

### Genotyping and Data Processing

| Parameter | Value |
|-----------|-------|
| SNP panel | 1240k |
| Genotype calling | Pseudohaploid (random allele selection) |
| Alignment reference | hg19 |
| Aligner | bwa 0.7.15-r1140, seed disabled (-l 350) |
| Minimum mapping quality | 25 |
| CpG transition SNPs excluded | n = 76,678 |
| Final SNP count (Human Origin Panel) | 481,259 |

### PCA Parameters

| Parameter | Value |
|-----------|-------|
| Software | smartpca v16000 |
| Outlier iterations | 5 |
| PC outlier removal | 10 components |
| altnormstyle | NO |
| lsqproject | YES |
| Individuals after outlier removal | 829 |
| SNPs used | 480,712 |
| Samples removed as outliers | 55 |

### qpAdm Reference Populations

| Population | n |
|-----------|---|
| Mbuti.DG | 4 |
| WHG | 8 |
| Russia_Ust_Ishim.DG | 1 |
| CHG | 2 |
| EHG | 3 |
| Iran_GanjDareh_N | 8 |
| Israel_Natufian_published | 3 |
| Jordan_PPNB | 6 |
| Laos_Hoabinhian | 1 |
| Russia_EBA_Yamnaya_Samara | 9 |
| Onge | 6 |
| Spain_ElMiron | 1 |
| Turkey_N_published | 8 |
| Russia_MA1_HG | 1 |
| Morocco_Iberomaurusian | 6 |
| Czech_Vestonice16 | 1 |

### Clustering Parameters

| Parameter | Value |
|-----------|-------|
| Algorithm | UPGMA (hierarchical clustering) |
| Dissimilarity metric | d = -log10(p-value) from qpAdm |
| Flat cluster cutoff | 1.3 (nominal p = 0.05) |
| Outlier threshold | <5% of region population OR <=2 individuals |
| Model competition p-value threshold | 0.01 |

### FST Calculation

| Parameter | Value |
|-----------|-------|
| Grid cell size | 10 degrees longitude x 10 degrees latitude |
| Grid slide increments | 1 degree (9 times) |
| Total spatial grids | 10 |
| FST estimator | Hudson's (corrected for unequal sample size) |
| Smoothing | Lowess (statsmodels v0.12.2) |
| Bootstrap replicates | 200 |

---

## Statistics Summary

All statistical tests used in this study:

1. **Chi-squared test** - sex bias among outlier vs non-outlier groups (p = 0.4117, df = 2; p = 0.633, df = 1)
2. **qpAdm / qpWave modeling** - ancestry clade testing and admixture modeling with one-component and two-component models
3. **Hierarchical clustering (UPGMA)** - grouping genetically similar individuals within regions
4. **Principal Component Analysis (PCA)** - genetic structure visualization using smartpca with projection of ancient genomes
5. **FST (Hudson's estimator)** - spatial genetic differentiation with correction for unequal sample sizes
6. **Lowess smoothing** - FST vs geographic distance visualization
7. **Spatial bootstrap** - confidence intervals for FST smoothing estimates (200 replicates)
8. **Wright-Fisher simulation** - neutral spatial population genetic model with long-range dispersal
9. **Radiocarbon dating (AMS)** - direct dating of 126 samples, calibrated via OxCal
10. **mapDamage v2.0.8** - ancient DNA damage pattern characterization
