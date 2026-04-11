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
