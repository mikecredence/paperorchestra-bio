Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
Evaluating the Biome Smartphone App for Biodiversity Monitoring: Data Quality and Impact on Species Distribution Modeling in Japan

## Core question
Can community-sourced species occurrence data from the Biome smartphone app, combined with traditional survey data, improve species distribution model accuracy -- and by how much does blending these data sources reduce the sample size needed for reliable models?

## Motivation / gap
- Comprehensive biodiversity data is essential for conservation (30by30 targets, TNFD disclosures) but traditional expert surveys cannot achieve sufficient spatiotemporal resolution alone
- Community science platforms accumulate data rapidly but may have spatial biases (toward urban areas) and taxonomic biases (misidentification)
- No systematic evaluation had been conducted on the Biome app's data quality across taxa and species rarity levels
- The potential for smartphone-driven community data to complement traditional surveys in species distribution modeling was not quantified
- Traditional survey data is biased toward natural areas, potentially missing urban-natural gradients important for realistic species distribution estimates
- The threshold of data records needed for accurate SDMs (especially for endangered species) had not been characterized for blended data sources

## Core contribution (bullet form)
- Biome app accumulated >5.27 million observations of >40,957 species across Japan by July 2023, with ~5,407 records submitted per day (2022 average)
- Species identification accuracy exceeds 95% for birds, reptiles, mammals, and amphibians; seed plants at ~90%; insects, mollusks, and fishes below 90%
- SDMs for 132 terrestrial plants and animals showed incorporating Biome data into traditional surveys improved accuracy
- For endangered species, traditional data alone required >2,000 records for accurate models (Boyce index >= 0.9), while blending reduced this threshold to ~300 records
- Biome data provides uniform coverage across the urban-natural gradient, whereas traditional data is biased toward natural areas, explaining the improvement
- Optimal model accuracy achieved when training data consisted of 50-70% Biome data

## Method in brief
The Biome app uses a synergistic approach combining CNN-based image recognition with geospatial data for species identification. Users photograph organisms; the app records location/timestamp from EXIF data and suggests candidate species refined by local occurrence frequency. Gamification features (points for rare/endangered species, quests, leveling) incentivize participation. An automatic filtering pipeline excludes unclear images, non-wild individuals, and duplicate observations, yielding 2,373,303 filtered records (45.0% of total submissions).

Data quality was assessed by expert verification of identification accuracy at species, genus, and family levels across taxa, stratified by rarity. Species distribution models were built for 132 terrestrial species using MaxEnt, comparing three data configurations: traditional survey data only, Biome data only, and blended (Biome + Traditional). Environmental predictors included climate, land use, and topography variables. Model accuracy was evaluated using the Boyce index with spatial block cross-validation. Principal component analysis of environmental variables revealed that Biome data covered the urban-natural gradient uniformly while traditional data was skewed toward natural areas (PC1 accounting for 6.1% of variation, driven by land use, topography, and climate).

## Target venue
eLife


## Experimental Log

# Experimental Log: Biome App Data Quality and SDM Performance

## Data Accumulation Summary

### Table 1: Biome App Data Overview (as of 7 July 2023)

| Metric | Value |
|--------|-------|
| Total occurrence records | 5,275,457 |
| Total species documented | 40,957 |
| App downloads (by Sept 13, 2023) | 839,844 |
| Average daily submissions (2022) | 5,407 |
| Records passing automatic filtering | 2,373,303 |
| Filtering pass rate | 45.0% |
| Launch date | April 2019 |

### Table 2: Taxonomic Composition of Records

| Taxon | Fraction of Records (%) |
|-------|------------------------|
| Seed plants | 41.8 |
| Insects (including Arachnids) | 31.2 |
| Birds | Smaller fraction |
| Mammals | Smaller fraction |
| Reptiles | Smaller fraction |
| Amphibians | Smaller fraction |
| Fishes | Smaller fraction |
| Mollusks | Smaller fraction |
| Other plants (non-seed terrestrial) | Smaller fraction |
| Arthropods (non-insect) | Smaller fraction |
| Other animals (remaining invertebrates) | Smaller fraction |

Fig 2D shows the taxonomic composition as area sizes, with insects and seed plants dominating the dataset.

---

## Data Quality Assessment

### Table 3: Fraction of Wild Individual Records by Taxon

| Taxon | Fraction Wild (%) |
|-------|------------------|
| Insects | >97 |
| Birds | >97 |
| Reptiles | Moderate-High |
| Amphibians | Moderate-High |
| Mollusks | <90 |
| Seed plants | <90 |
| Mammals | <90 |
| Fishes | <90 |

### Table 4: Species-Level Identification Accuracy (Among Wild Records)

| Taxon | Species-Level Accuracy (%) | Genus-Level Accuracy (%) | Family-Level Accuracy (%) |
|-------|---------------------------|-------------------------|--------------------------|
| Birds | >95 | >95 | >95 |
| Reptiles | >95 | >95 | >95 |
| Mammals | >95 | >95 | >95 |
| Amphibians | >95 | >95 | >95 |
| Seed plants | ~90 | Higher than species | Higher than genus |
| Insects | <90 | <90 | Higher |
| Fishes | <90 | Higher | Higher |
| Mollusks | <90 | >90 | Higher |

Table 1 (in paper) shows detailed quality metrics across taxa and rarity levels. Species with moderate diversity (amphibians, reptiles, birds, mammals) had the highest accuracy. Genus-level accuracy exceeded 90% in all taxa except insects.

### Table 5: Identification Accuracy by Species Rarity

| Rarity Level | General Trend |
|-------------|---------------|
| Common species | Higher accuracy |
| Rare species | Lower accuracy |
| Endangered species | Lower accuracy, requires expert review |

Rare species generally showed lower identification accuracy, requiring expert identification and further AI improvement.

---

## Environmental Gradient Analysis

### Table 6: PCA of Environmental Variables

| Component | Variance Explained (%) | Primary Drivers |
|-----------|----------------------|-----------------|
| PC1 | 6.1 | Land use, topography, climate |

### Table 7: Data Distribution Along Urban-Natural Gradient

| Data Source | Coverage Pattern | Bias Direction |
|-------------|-----------------|----------------|
| Biome data | Relatively uniform across entire gradient | Minimal bias |
| Traditional survey data | Substantially biased | Toward natural areas |

Fig 2C shows divergent distribution patterns of Biome vs. Traditional data along PC1. The Biome data covers urban-to-natural environments uniformly, while traditional data clusters in natural areas.

---

## Species Distribution Modeling

### Table 8: SDM Experimental Design

| Parameter | Value |
|-----------|-------|
| Number of species modeled | 132 |
| Organism types | Terrestrial plants and animals |
| Geographic scope | Japanese archipelago |
| SDM algorithm | MaxEnt |
| Accuracy metric | Boyce index |
| Cross-validation | Spatial block design |
| Replicates per species/record count | 3 |

### Table 9: Data Sources for SDMs

| Dataset | Type | Source Description |
|---------|------|-------------------|
| Biome data | Community-sourced | Biome app filtered records |
| Traditional survey data | Expert surveys + GBIF | Government surveys, museum specimens, literature |
| iNaturalist | Community science (classified as Traditional) | Global platform observations |
| eBird | Community science (classified as Traditional) | Bird observation network |

Table 2 (in paper) lists all species occurrence datasets used for constructing SDMs. iNaturalist and eBird data were classified as Traditional survey data for comparison purposes.

### Table 10: Environmental Predictors Used in SDMs

| Variable Category | Examples | Data Collection Period |
|------------------|----------|----------------------|
| Climate | Temperature, precipitation | Various years |
| Land use | Urban, agricultural, forest cover | Various years |
| Topography | Elevation, slope | Various years |

Table 3 (in paper) details all environmental variables, collection periods, and how they were converted before use in SDMs.

---

## SDM Performance Results

### Table 11: SDM Accuracy by Data Source and Record Count

| Data Source | Records Needed for Boyce Index >= 0.9 (Endangered Species) | Relative Accuracy |
|-------------|----------------------------------------------------------|-------------------|
| Traditional survey data only | >2,000 records | Baseline |
| Biome + Traditional (blended) | ~300 records | Improved |
| Optimal Biome fraction in blend | 50-70% | Highest accuracy |

Fig 3 shows SDM accuracy (Boyce index) as a function of record count for Traditional (grey) and Biome+Traditional (green, 50% Biome). The blended data source consistently outperforms Traditional data alone, especially at lower record counts.

### Table 12: Relative Model Accuracy Comparison

| Comparison | Direction | Interpretation |
|-----------|-----------|----------------|
| Biome-blended vs. Traditional only | Positive (median) | SDMs with Biome data outperformed Traditional-only models |
| Low record counts (<500) | Larger improvement | Biome data most beneficial when traditional records are scarce |
| High record counts (>2000) | Smaller improvement | Both approaches converge at large sample sizes |

Appendix 1-figure 1 shows violin plots of relative model accuracy. Positive values indicate Biome-blended outperformance. The median is positive across conditions.

### Table 13: Optimal Blending Ratio

| Biome Data Fraction (%) | Relative Model Accuracy |
|--------------------------|------------------------|
| 0 (Traditional only) | Baseline |
| 10-30 | Moderate improvement |
| 50-70 | Maximum improvement |
| 80-100 | Declining (insufficient traditional data) |

Appendix 1 analysis shows the most accurate predictions when training data consisted of 50-70% Biome data, highlighting the need for both data types.

---

## Data Filtering Pipeline

### Table 14: Automatic Filtering Criteria

| Filter Step | Purpose | Records Affected |
|-------------|---------|-----------------|
| Image clarity check | Exclude unclear/unidentifiable images | Removed unclear records |
| Wild vs. non-wild classification | Exclude captive/cultivated organisms | Removed non-wild records |
| Duplicate detection | Remove duplicate observations | Removed duplicates |
| Species verification (AI + community) | Correct misidentifications | Flagged/corrected records |

Fig 4 shows the complete workflow for checking accuracy of Biome data.

### Table 15: Filtering Pass Rates

| Stage | Input Records | Output Records | Pass Rate |
|-------|--------------|----------------|-----------|
| Total submitted | 5,275,457 | -- | -- |
| After all automatic filtering | -- | 2,373,303 | 45.0% |

---

## Gamification and User Engagement Features

### Table 16: Biome App Gamification Elements

| Feature | Description | Effect on Data Collection |
|---------|-------------|--------------------------|
| Points system | Earned for submissions and identification help | Incentivizes participation |
| Rarity bonus | More points for rare/endangered/invasive species | Targets underrepresented species |
| Leveling system | Users progress based on total points | Long-term engagement |
| Quests | Timed events for specific locations or species | Targeted monitoring campaigns |
| Social features | Viewing/commenting on others' records | Community building |
| Suggest identification | Users help identify others' records for points | Crowdsourced quality control |

---

## Endangered Species Location Privacy

### Table 17: Privacy Features

| Feature | Implementation |
|---------|---------------|
| Auto-concealment | Geolocations of species on national/prefectural red lists automatically hidden |
| Comparison to iNaturalist | iNaturalist requires manual user action to hide locations |

---

## Comparison with Other Community Science Platforms

### Table 18: Identification Accuracy Benchmarks

| Platform/Study | Accuracy Metric | Value |
|---------------|----------------|-------|
| Biome (seed plants) | Species identification | ~90% |
| PlantNet, PlantSnap, LeafSnap, iNaturalist, Google Lens | Auto-suggest identification (plants) | 69% |
| US invasive plant survey (volunteers) | Species identification | 72% |

Biome's higher accuracy attributed to community oversight via identification suggestion feature and AI algorithm leveraging local occurrence data.

---

## SDM Pseudo-Absence Selection

### Table 19: Background Point Selection Strategy

| SDM Configuration | Pseudo-Absence Selection Method |
|------------------|-------------------------------|
| Biome + Traditional | Both data sources inform background selection |
| Traditional only | Only Traditional data used (no Biome involvement) |

Fig 5 shows the workflow for selecting pseudo-absence grid cells, differing between blended and Traditional-only configurations.

---

## Figure Observations

- **Fig 1**: Workflow of Biome record submission. Steps: (1) upload image, (2) select animal/plant, (3) AI generates candidate species list, (4) alternative manual input, (5) submit record.

- **Fig 2**: Four-panel description of Biome data. (A) Spatial distribution across Japan. (B) Temporal accumulation showing monthly bars and cumulative line. (C) PC1 environmental gradient comparison showing Biome's uniform coverage vs. Traditional's natural-area bias. (D) Taxonomic composition dominated by insects and seed plants.

- **Fig 3**: SDM accuracy curves. Traditional data (grey) and Biome+Traditional (green) plotted against record count. Blended data achieves higher Boyce index, especially at lower record counts. For endangered species, the threshold drops from >2,000 to ~300 records.

- **Fig 3-supplement 1**: SDM accuracy evaluated against test data consisting only of Traditional survey data, confirming improvement from blending.

- **Fig 4**: Data quality checking workflow for Biome records.

- **Fig 5**: Pseudo-absence selection workflow for SDMs.

- **Fig 6**: Map of Japanese archipelago with altitude coloring and spatial block test data regions.

- **Appendix 1-figure 1**: Violin plots of relative model accuracy showing positive median, confirming Biome-blended models outperform Traditional-only models.

---

## Key Statistical Findings

### Table 20: Summary of Key Quantitative Results

| Finding | Value |
|---------|-------|
| Total Biome records (July 2023) | 5,275,457 |
| Species documented | 40,957 |
| Filtering pass rate | 45.0% |
| Daily submission rate (2022 avg) | 5,407 |
| App downloads | 839,844 |
| PC1 variance explained | 6.1% |
| Species modeled | 132 |
| Bird/reptile/mammal/amphibian ID accuracy | >95% |
| Seed plant ID accuracy | ~90% |
| Insect/fish/mollusk ID accuracy | <90% |
| Genus-level accuracy (most taxa) | >90% |
| Records for Boyce >= 0.9 (Traditional only, endangered) | >2,000 |
| Records for Boyce >= 0.9 (Blended, endangered) | ~300 |
| Optimal Biome fraction in blend | 50-70% |
| Fraction wild records (insects, birds) | >97% |
| Fraction wild records (fish, seed plants, mollusks, mammals) | <90% |

