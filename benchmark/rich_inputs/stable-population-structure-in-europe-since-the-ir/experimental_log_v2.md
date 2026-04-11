# Experimental Log: Stable European Population Structure

## Sample Overview

| Parameter | Value |
|-----------|-------|
| New genomes reported | 204 |
| Previously reported (Moots et al.) | 26 of the 204 |
| Archaeological sites | 53 |
| Countries represented | 18 |
| Radiocarbon dated | 126 |
| DNA extraction source | Petrous bone (n=203), teeth (n=1) |
| UDG treatment | Partial |
| Median sequencing depth | 0.92x |
| Depth range | 0.16x - 2.38x |

## SNP Coverage

| Metric | Value |
|--------|-------|
| SNP panel | 1240k |
| Median SNPs per sample | 685,058 |
| Min SNPs | 167,000 |
| Max SNPs | 1,029,345 |

## Published Data Integrated

| Category | Count |
|----------|-------|
| Present-day genomes | 2,033 |
| Prehistoric genomes | 1,998 |
| Published historical genomes | 764 |
| Total dataset | ~5,000 genomes |

## Time Periods Defined

| Period | Date Range |
|--------|-----------|
| Mesolithic and Neolithic | 10000 - 3500 BCE |
| Copper Age | 3500 - 2300 BCE |
| Bronze Age | 2300 - 1000 BCE |
| Iron Age | 1000 BCE - 1 CE |
| Imperial Rome & Late Antiquity | 1 CE - 700 CE |
| Medieval Ages & Early Modern | 700 CE - 1900 CE |
| Present-day | 1900 CE - onward |

## Geographic Regions Analyzed

| Region | New Genomes | First Historical Genomes? |
|--------|-------------|--------------------------|
| Armenia | Yes | Yes (first ever) |
| Algeria | Yes | Yes (first ever) |
| Austria | Yes | Yes (first ever) |
| France | Yes | Yes (first ever) |
| Italy | Yes | No (extends prior work) |
| Southeastern Europe | Yes | No |
| Western Europe | Yes | No |
| Other regions | Yes | Various |
| Total regions | 14 geographic categories | -- |

## PCA and Ancestry Analysis Methods

| Method | Purpose |
|--------|---------|
| PCA (smartpca v1600) | Project ancient genomes onto present-day variation |
| qpAdm | Ancestry decomposition modeling |
| Clustering | Identify genetic clusters within regions |
| Outlier detection | Individual pairwise qpAdm followed by clustering |
| Source tracing | One-component qpAdm modeling of outlier clusters |

### PCA Parameters

| Parameter | Value |
|-----------|-------|
| Individuals | 829 |
| SNPs | 480,712 |
| Outlier iterations | 5 |
| PCs for outlier removal | 10 |
| Projection | Least squares (lsqproject = YES) |

## Ancestry Outlier Analysis (Fig 5)

### Outlier Proportions by Region

| Region | Outlier Proportion |
|--------|-------------------|
| All regions combined | At least 7% |
| Italy (Imperial Rome) | High heterogeneity |
| Southeastern Europe | High heterogeneity |
| Western Europe | Moderate heterogeneity |
| Armenia | Lower heterogeneity |

### Sex Bias in Outliers (Fig 5 - supplement 1)

| Comparison | p-value | Result |
|-----------|---------|--------|
| Outlier vs non-outlier (male/female proportions) | 0.4117 | No significant difference |
| Outlier with/without source combined | 0.633 | No significant sex bias |

### Outlier Source Distances (Fig 5 - supplement 2)

| Metric | Value |
|--------|-------|
| Mean geographic distance to putative source | Calculated for each outlier |
| Interpretation | Cross-Mediterranean and cross-continental distances observed |

## Regional Case Studies

### Armenia (Fig 2)

| Finding | Detail |
|---------|--------|
| Genetic clusters | Two homogeneous clusters |
| Distinction | Temporal shift between clusters |
| PCA projection | Clusters project to distinct positions relative to present-day populations |

### Southeastern Europe (Fig 3)

| Finding | Detail |
|---------|--------|
| Imperial Roman period | Highly heterogeneous population |
| Outlier ancestries | Multiple non-local ancestries detected |
| Clustering | Multiple distinct genetic clusters in same time period |

### Western Europe (Fig 4)

| Finding | Detail |
|---------|--------|
| Imperial Roman period | Heterogeneous population |
| Cross-Mediterranean contacts | Evidence for gene flow from eastern Mediterranean |
| Temporal stability | Structure stabilizes after Imperial period |

### Italy - Imperial Rome (Fig 3 - supplement 1)

| Finding | Detail |
|---------|--------|
| PCA spread | Wide dispersion across PCA space |
| Outlier proportion | High |
| Ancestry sources | Diverse, including eastern Mediterranean, North Africa |

## Stability of Population Structure

| Time Period | Structure Relative to Geography |
|-------------|-------------------------------|
| Iron Age | Mirrors geography |
| Imperial Rome & Late Antiquity | Mirrors geography (despite high mobility) |
| Medieval & Early Modern | Mirrors geography |
| Present-day | Mirrors geography |

Key finding: Despite 7%+ outliers indicating individual mobility, the overall population genetic structure closely tracks geography across all historical periods.

## Migration Simulation Results

| Simulation Parameter | Finding |
|---------------------|---------|
| Model type | Stepping-stone with local panmixia |
| Observed dispersal rate | Determined from outlier proportion |
| Predicted outcome (standard model) | Collapse of population structure |
| Actual observation | Structure maintained |
| Implication | Effective migration rate lower than apparent dispersal |

The simulation shows that under standard population genetics models with local random mating, the observed level of cross-regional dispersal (~7%+ per generation) would homogenize population structure. Since structure persists, effective migration must be substantially lower.

## Transient Dispersal Hypothesis

| Factor | Contribution |
|--------|-------------|
| Improved transportation | Roads, waterways enabling rapid cross-continental travel |
| Roman Empire mobilization | Trade, labor, military movement |
| Travel timescale | Weeks to months (within lifetimes) |
| Prehistoric migration timescale | Hundreds of years for continental traverse |
| Key distinction | Movement without proportional reproduction at destination |

Fig 5 - supplement 3: Example routes and travel times across the Roman Empire using orbis.stanford.edu model. Routes shown are fastest summer routes for civilians using road, river, coastal, and open sea travel.

## SNP Coverage Quality Control (Fig 2 - supplement 3)

| Analysis | Result |
|----------|--------|
| Median SNPs vs cluster size | No significant correlation |
| SNPs: outlier vs non-outlier clusters | No significant difference |

## Three-Way Ancestry Components (Present-Day Europeans)

| Component | Origin |
|-----------|--------|
| Western Hunter-Gatherer (WHG) | Pre-Neolithic |
| Neolithic Farmer | ~7,500 BCE expansion |
| Bronze Age Steppe Herder | ~3,500 BCE migration |

These components were largely established by the end of the Bronze Age and remain stable through the historical period with minor regional variation.

## Data Availability

| Resource | Accession |
|----------|-----------|
| New sequences (raw) | PRJEB53565 (ENA) |
| Mapped sequences | PRJEB53564 (ENA) |
| Previously reported | PRJEB49419 (ENA) |
| Published data | Allen Ancient Data Resource (AADR) |

## Key Figure Observations

- Fig 1A: Timeline showing 204 new genomes alongside published genomes ordered by time and region
- Fig 1B: Map of sampling locations (new in black, published in gray)
- Fig 2: Armenia case study showing two temporally distinct genetic clusters
- Fig 2 - supplement 2: All regional ancestry clusters mapped and projected onto PCA
- Fig 3: Southeastern Europe showing high heterogeneity in Imperial Roman period
- Fig 4: Western Europe showing heterogeneity with cross-Mediterranean contacts
- Fig 5A: Outlier proportions by region
- Fig 5B: Network visualization of source-to-outlier relationships across regions
- Fig 5C: Individual examples of cross-regional ancestry connections
