# Experimental Log: Boosting biodiversity monitoring using smartphone-driven, rapidly accumulating community-sourced data

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsThe amount and quality of Biome dataBy 7 July 2023, Biome had accumulated 5,275,457 occurrence records of 40,957 species across the Japanese archipelago (Figure 2A).
- The amount of occurrence records submitted to Biome has increased across the years (Figure 2B).
- On average in 2022, users submitted 5,407 records per day.
- The two datasets demonstrated divergent distribution patterns along PC1 (Figure 2C).
- This component, accounting for 6.1% of the total variation, is primarily influenced by land use, topography, and climate (Supplementary File 1).
- The Biome data exhibited a relatively uniform distribution encompassing the entire gradient, while Traditional survey data was substantially biassed towards natural areas (Figure 2C).
- The majority of records are attributed to insects (31.2%) and to seed plants (41.8%), which are relatively accessible and can be easily photographed using smartphones (Figure 2D).biorxiv;2023.09.13.557657v6/FIG2F2fig2Figure 2.Description of data accumulated by Biome.Data distributions are shown base
- C Distributions of records along with PC1 of all environmental variables and standardised area occupancy of urban-type land uses.
- ‘Other plant’ consists of non-seed terrestrial plants; ‘insects’ include Arachnids and Insects; ‘arthropods’ cover any Arthropod not included in insects; ‘other animals’ covers all invertebrates not included in the taxa above.Out of all the records submitted to Biome, a total of 2,373,303 records (4
- The quality of Biome data varied across taxa and the rarities of species (Table 1).
- The fraction of the records of wild individuals exceeded 97% in insects and birds, while it was lower than 90% in molluscs, seed plants, mammals and fishes.
- Among the records of wild individuals, at the species level, identification accuracy was higher than 95% in birds, reptiles, mammals and amphibians but less than 90% in insects, fishes and seed plants.
- At the genus level, identification accuracy was higher than 90% in all taxa except for insects.
- In the case of fishes and seed plants, identifications became 5-6% more accurate at the genus level compared to the species level.
- The family was correctly identified in more than 94% of records in all taxa examined.
- Common species had higher identification accuracy than rare species (average value, 95% vs.
- seed plants and insects) is a challenging task.biorxiv;2023.09.13.557657v6/TBL1T1tbl1Table 1.Data quality of Biome.The fraction of records documenting wild individuals, and identification accuracy at species, genus and family levels among the records documenting wild individuals are shown.
- Species were identified only for records documenting wild individuals.The performance of species distribution modelsSDMs using Biome+Traditional data, including Biome data at 50%, were more accurate than those modelled only using Traditional survey data when the two datasets have the same amount of 
- Our analysis revealed that although the intercept of the Boyce Index (BI, model accuracy metric that ranges between −1 to 1) did not differ between the two datasets (generalised linear mixed model, see Methods: β=0.02±0.03, t=0.60, P=0.55), Biome+Traditional data consistently led to a more rapid inc
- For instance, BI which ranges from –1 to 1, exceeds 0.9 with 294±471 records (mean±SD across all species) in the Biome+Traditional data, whereas the Traditional survey data requires 2,129±4,157 records to achieve the same accuracy.
- This was also true in endangered species (included in Japanese national or prefectural red lists); although 2,336±3,718 Traditional survey records were required to exceed 0.9 of BI, only 338±571 were required for Biome+Traditional data.Because we controlled the proportion of Biome data within the Bi
- Therefore, the two datasets did not differ in the best model performances in each species (BIs of Biome+Traditional data: 0.81±0.20; Traditional survey data: 0.83±0.20).

## Tables

### Table 1.
> Data quality of Biome.The fraction of records documenting wild individuals, and identification accuracy at species, genus and family levels among the records documenting wild individuals are shown. Sp


### Table 2.
> List of species occurrence datasets used for constructing SDMs.To compare Biome dataset with the other datasets, iNaturalist and eBird data based on community science were classified as ‘Traditional s


### Table 3.
> Environmental data used for constructing SDMs.Years indicate the data collection period. Usage in the SDM shows how the variables were converted before using in the species distribution modelling.


## Figure Descriptions

### Figure 1.
Workflow of submitting records to Biome.(1) Users can upload images that were taken by the smartphone camera or import existing images from the storage, including those imported from external devices. (2) Users select whether the image is about animals or plants to activate the species identificatio

### Figure 2.
Description of data accumulated by Biome.Data distributions are shown based on all records submitted to Biome by 7 July 2023 (N=5,275,457). A Spatial distribution of records across Japan. B Accumulation of records through time. The barplot represents the number of records each month and the line sho

### Figure 3.
The accuracy of species distribution models.Accuracy of SDMs using Traditional survey data (grey dots and lines) and Biome+Traditional data (i.e. 50% of Biome data: green). Each SDM was performed with a specific dataset, species, and the amount of records. For each species and amount of records, we 

### Figure 4.
The workflow of checking accuracy of Biome data.

### Figure 5.
The workflow for selecting pseudo-absence (background) grid cells for SDMs using the Biome-Traditional dataset.In this process, both Biome data and Traditional dataset are utilised to determine the suitable locations for pseudo-absence grid cells. However, when constructing SDMs using the Traditiona

### Figure 6.
Japanese archipelago, coloured by altitude.Shaded area shows spatial block of test data. Retrieved from Wikipedia (2023, May 30), licensed under Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).

### Figure 3–figure supplement 1.
Accuracy of SDMs using Traditional survey data (grey dots and lines) and Biome+Traditional data (i.e. 50% of Biome data: green), evaluated against test data only consisting of Traditional survey data.

### Appendix 1–figure 1.
The violin plots of relative model accuracy between SDMs using Biome-blended data and Traditional survey data.The median values are shown as grey dots. The positive relative model accuracy indicates that SDMs that used Biome data outperformed models that used Traditional survey data.

## References
Total references in published paper: 81

### Key References (from published paper)
- Habitat classification for 69 near threatened plants based on national vegetation survey data (, 2018)
- Standards for distribution models in biodiversity assessments (, 2019)
- Web image search revealed large-scale variations in breeding season and nuptial coloration in a mutu (, 2017)
- lme4: linear mixed-effects models using S4 classes (, 2015)
- . bioclim: the first species distribution modelling package, its early applications and relevance to (, 2014)
- Deep learning for early warning signals of tipping points (, 2021)
- Community assembly and shifts in plant trait distributions across an environmental gradient in coast (, 2009)
- Assessing citizen science data quality: an invasive species case study (, 2011)
- Patterns of distribution in Japanese land mammals (, 1994)
- The art of modelling range-shifting species (, 2010)
- A statistical explanation of MaxEnt for ecologists (, 2011)
- Modeling the rarest of the rare: a comparison between multi-species distribution models, ensembles o (, 2023)
- Trends and gaps in the use of citizen science derived data as input for species distribution models: (, 2021)
- A Double machine learning trend model for citizen science data (, 2023)
- Citizen science across two centuries reveals phenological change among plant species and functional  (, 2022)
- Practice of citizen science for developing biodiversity monitoring methods using mobile devices (, 2021)
- A framework for the detection and attribution of biodiversity change (, 2023)
- Species interactions: next-level citizen science (, 2021)
- Assessing the accuracy of free automated plant identification applications (, 2023)
- Young people in iNaturalist: a blended learning framework for biodiversity monitoring (, 2023)
- Evaluating the ability of habitat suitability models to predict species presences (, 2006)
- Estimates of observer expertise improve species distributions from citizen science data (, 2018)
- Incorporating climate change into spatial conservation prioritisation: A review (, 2016)
- Multiple forms of engagement and motivation in ecological citizen science (, 2023)
- Biodiversity modeling advances will improve predictions of nature’s contributions to people (, 2023)
- ENMeval 2.0: Redesigned for customizable and reproducible modeling of species’ niches and distributi (, 2021)
- City-size bias in knowledge on the effects of urban nature on people and biodiversity (, 2020)
- Achieving Integrative, Collaborative Ecosystem Management (, 2006)
- TreeGOER: A database with globally observed environmental ranges for 48,129 tree species (, 2023)
- iPhenology: Using open-access citizen science photos to track phenology at continental scale (, 2023)

## Ground Truth Reference
- Figures: 8
- Tables: 3
- References: 81