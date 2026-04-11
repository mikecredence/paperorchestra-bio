# Idea Summary: Boosting biodiversity monitoring using smartphone-driven, rapidly accumulating community-sourced data

## Working title
Boosting biodiversity monitoring using smartphone-driven, rapidly accumulating community-sourced data

## Core question
AbstractComprehensive biodiversity data is crucial for ecosystem protection. The ‘Biome’ mobile app, launched in Japan, efficiently gathers species observations from the public using species identification algorithms and gamification elements. The app has amassed >6M observations since 2019. Nonetheless, community-sourced data may exhibit spatial and taxonomic biases. Species distribution models (SDMs) estimate species distribution while accommodating such bias. Here, we investigated the quality

## Motivation / gap
- IntroductionNature underpins human society, and the conservation of ecosystems and associated ecosystem services contributes to the sustainable development of human society, yet these services have be
- Kunming-Montreal Global Biodiversity Framework (KM-GBF) by the United Nations envisions reversing the nature loss by 2030.
- As direct means for nature conservation, KM-GBF targeted making 30% of Earth’s land and ocean area as protected areas by 2030 (i.e.
- As an indirect but influential way, KM-GBF requires companies to “monitor, assess, and transparently disclose their risks, dependencies and impacts on biodiversity through their operations, supply and

## Core contribution (bullet form)
Extracted from abstract:
AbstractComprehensive biodiversity data is crucial for ecosystem protection. The ‘Biome’ mobile app, launched in Japan, efficiently gathers species observations from the public using species identification algorithms and gamification elements. The app has amassed >6M observations since 2019. Nonetheless, community-sourced data may exhibit spatial and taxonomic biases. Species distribution models (SDMs) estimate species distribution while accommodating such bias. Here, we investigated the quality of Biome data and its impact on SDM performance. Species identification accuracy exceeds 95% for birds, reptiles, mammals, and amphibians, but seed plants, mollusks, and fishes scored below 90%. Our SDMs for 132 terrestrial plants and animals across Japan revealed that incorporating Biome data into traditional survey data improved accuracy. For endangered species, traditional survey data required >2,000 records for accurate models (Boyce index ≥ 0.9), while blending the two data sources reduced this to around 300. The uniform coverage of urban-natural gradients by Biome data, compared to traditional data biased towards natural areas, may explain this improvement. Combining multiple data sources better estimates species distributions, aiding in protected area designation and ecosystem service assessment. Establishing a platform for accumulating community-sourced distribution data will contribute to conserving and monitoring natural ecosystems.

## Method in brief
MethodsOccurrence record accumulation through mobile app BiomeIn April 2019, a free smartphone app called Biome was launched for the Japanese markets. The app has been downloaded 839,844 times by September 13, 2023. The app allows users to collect data on the distribution of plants and animals using their mobile devices. Users can post photographs of the plants and animals they find, and the app automatically records the location and timestamp from EXIF data. If the EXIF data is unavailable, users can manually input the locality and timestamp.To support species identification, the app provides users with two options. First, the app provides a list of candidate species based on the image and metadata (e.g., location and timestamp). Biome employs a synergistic approach that integrates image recognition technology and geospatial data to facilitate species identification. The image recognition algorithm, constructed upon convolutional neural networks, classifies species at higher taxonomic levels. Subsequently, these candidates are refined based on their frequency of recent occurrences in the geographical area. Consequently, as the correctly identified records accumulate for a given area, species identification AI will improve the accuracy. Second, users can seek help from other users. If a user selects the “ask Biomers” button, their occurrence record is added to a waiting list that appears on the home screen. Other users can suggest possible identifications for the records, as 

## Target venue
eLife
