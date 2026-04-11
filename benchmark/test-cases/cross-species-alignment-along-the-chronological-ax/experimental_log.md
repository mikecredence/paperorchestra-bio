# Experimental Log: Cross-species alignment along the chronological axis reveals evolutionary effect on structural development of human brain

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- First, we used 62 macaque features and 225 human features which were present in all the 100 times iterations to train the macaque and human prediction models, respectively (all the features see Table supplement 1 and 2 in Supplementary information).
- Using the trained models, we found that the macaque prediction model can well predict macaque ages (R = 0.5729, P < 0.001, MAE = 0.3758; Figure 2(A)) and the human prediction model can well predict human ages (R = 0.6153, P < 0.001, MAE = 1.1236; Figure 2(D)).
- We found that the trained monkey prediction model could well predict human ages (R = 0.4823, P < 0.001, MAE = 8.3610; Figure 2(B)), and the trained human prediction model can also predict macaque ages (R = 0.2898, P < 0.001, MAE = 7.6157; Figure 2(C)).
- However, we noticed that using the macaque prediction model to predict human ages showed better performance than using the trained human prediction model to predict macaque ages.biorxiv;2024.02.27.582251v1/FIG2F2fig2Figure 2.The prediction results for intra- and inter-/cross-species using brain stru
- The width of the curve denotes the 95% confidence interval around the linear fitting curve (black line).
- Prediction results for inter-species with orange for predicted human ages using macaque model and purple for predicted macaque ages using human model.To test the impact of different number of features on prediction performance, we first trained the macaque prediction model with 117 features and huma
- We found that the macaque prediction model and human prediction model can well predict macaque (R = 0.5825, P < 0.001, MAE = 0.3675) and human ages (R = 0.6039, P < 0.001, MAE = 1.1388), respectively.
- We also found that the trained monkey prediction model could well predict human ages (R = 0.4018, P < 0.001, MAE = 7.7185) and the trained human prediction model can also predict macaque ages (R = 0.3223, P < 0.001, MAE = 7.9514) (Figure supplement 1 in Supplementary information).Using the same top 
- We also observed that the trained macaque prediction model could well predict human ages (R = 0.4822, P < 0.001, MAE = 8.3606) and the trained human prediction model can also predict macaque ages (R = 0.2094, P = 0.0047, MAE = 6.1083).
- Consistently, we showed that the trained macaque prediction model predicting human ages outperformed the trained human prediction model predicting macaque ages even using different number of features for inter-/cross-species prediction (Figure supplement 2 in Supplementary information).Finally, to e
- The predicted results showed similar pattern with that predicted by combining male and female into one group (Figure supplement 3 in Supplementary information).By testing different number of features and sex effects, we observed consistent patterns for intra- and inter-/cross-species age prediction 
- On the contrary, when using human model to predict macaque age, the prediction error of the human model decreased as the macaque age increases (Figure 3).biorxiv;2024.02.27.582251v1/FIG3F3fig3Figure 3.Relationship between brain age gap (|Δ brain age|) and actual ages in human.
- The width of the curve denotes the 95% confidence interval.
- Positive association between |Δ brain age| and actual age in human ages was found (Pearson’s correlation: R = 0.9813, P < 0.001, MAE = 2.7120).
- Negative association between | Δ brain age | and actual ages in macaque was found (Pearson’s correlation: R = −0.3759, P < 0.001, MAE = 4.8697).Like above, we also conducted the above correlation analyses between actual ages and predicted age deviation using 117 macaque features and 239 human featur
- In addition, to test sex effects, the trends of the correlations between actual age and predicted age deviation are similar with that found using different sets of features suggesting the results had no significant difference between sexes (Figure supplement 3 in Supplementary information).
- The top five brain areas or white matter tracts showing highest correlations with ages were displayed (Figure 4).
- The common features of human and macaque have the highest proportion in gray matter areas but also some were located in white matter tracts (Figure 4(A)).
- For the macaque-specific features, the gray matter features are mainly located in the left dorsolateral prefrontal cortex (PFCdl, R = 0.4003), left medial prefrontal cortex (PMCm, R = 0.3966), right dorsolateral prefrontal cortex (PFCdl, R = 0.3723), right orbitomedial prefrontal cortex (PFCom, R = 
- For the human-specific features, the gray matter features are mainly located in left Putamen (Pu, R = 0.4437), right Pallidum (GP, R = 0.4284), left posterior insula (Ip, R = 0.3915), left Pallidum (GP, R = 0.3884) and right primary somatosensory cortex (S1, R = 0.3703) and the white matter features
- The top 5 brain areas of common gray matter features in human are right posterior insula (Ip, R = 0.3769), left posterior cingulate cortex (CCp, R = 0.3583), left ventrolateral premotor cortex (PMCvl, R = 0.3523), right posterior cingulate cortex (CCp, R = 0.3466) and right intraparietal cortex (PCi
- The top 5 common white matter tract features in human were left corticospinal tract (CT, R = 0.4654), right corticospinal tract (CT, R = 0.4499), right superior thalamic radiation (STR, R = 0.3344), left superior thalamic radiation (STR, R = 0.3212) and left cingulum subsection: peri-genual (Cs:Pg, 
- FA: fractional anisotropy; MD: mean diffusivity; RD: radial diffusivity; AD: axial diffusivity; GMV: gray matter volumes.Meanwhile, using 117 macaque features and 239 human features or the same top 62 features of human and macaque for intra- and inter-/cross-species predication, we observed the dist
- The highly correlated common feature in human is corticospinal tract (CT) while the highly correlated common macaque feature is anterior cingulate cortex (CCa) (Figure supplement 6 and 7 in Supplementary information).The brain cross-species age gap associated behavioral phenotypes, gray matter and w
- We observed that BCAP shows significant correlations with picture vocabulary test (R = 0.1588; P = 0.0323) and visual sensitivity test (R = − 2051; P = 0.0056) (Figure 5(A)).biorxiv;2024.02.27.582251v1/FIG5F5fig5Figure 5.The brain cross-species age gap (BCAP) correlations with behavioral phenotypes,
- The first three and last three white matter tracts in FA showing significantly positive and negative correlations with BCAP were: left arcuate fasciculus (AF, R = 0.3784), left optic radiation (OR, R = 0.3232), right arcuate fasciculus (AF, R = 0.3035) and anterior commissure (AC, R = 0.1215), right
- The first three and last three white matter tracts between BCAP and MD, RD, and AD see in Figure S8 in Supplementary information.

## Tables

### Table 1.
> Demographic information for human and macaque.


## Figure Descriptions

### Figure 1.
The flowchart for intra- and inter-/cross-species prediction using brain structure based cross-species age prediction model. Feature selection: the features with p < 0.01 from Pearson’s correlation between features consisted of gray matter volume (GMV), fractional anisotropy (FA), mean diffusion (MD

### Figure 2.
The prediction results for intra- and inter-/cross-species using brain structure based cross-species age prediction model. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval around the linear fitting curve (black line). The prediction mod

### Figure 3.
Relationship between brain age gap (|Δ brain age|) and actual ages in human. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval. The human brain age gap (|Δ brain age|) is defined as predicted human age using macaque model minus human act

### Figure 4.
The distribution of selected features for prediction. The selected features were analyzed based on five parameters (GMV, FA, MD, RD and AD) and three groups (human-specific, macaque-specific and common features in human and macaque). (A). The percentage of each group in each parameter. The macaque-s

### Figure 5.
The brain cross-species age gap (BCAP) correlations with behavioral phenotypes, gray matter, and white matter tracts. (A). Each dot depicts data from an individual participant. Visual Sensitivity Test and Picture Vocabulary Test showed negative and positive correlations with BCAP, respectively. (B).

### Figure supplement 1.
The prediction results of intra- and inter-species using prediction model with 117 selected macaque features and 239 selected human features. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval around the linear fitting curve (black line).

### Figure supplement 2.
The prediction results of intra- and inter-species using prediction model with 62 selected macaque features and 62 selected human features. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval. Normal distribution of predicted ages and actu

### Figure supplement 3.
The prediction results of intra- and inter-species in male and female. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval. The prediction in intra- and inter-species observed significant and no evolution differences between male and femal

### Figure supplement 4.
Relationship between brain age gap (|Δ brain age|) and actual ages in human and macaque with 117 selected macaque features and 239 selected human features. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval. (A). Positive relationship bet

### Figure supplement 5.
Relationship between brain age gap (|Δ brain age|) and actual ages in human and macaque with 62 selected macaque features and 62 selected human features. Each dot depicts data from an individual participant. The width of the curve denotes the 95% confidence interval. (A). Positive relationship betwe

### Figure supplement 6.
The distribution of features with 117 selected macaque features and 239 selected human features. The selected features were analyzed based on five parameters (GMV, FA, MD, RD and AD) and three groups (human-specific, macaque-specific and common features in human and macaque). (A). The percentage of 

### Figure supplement 7.
The distribution of features with 62 selected macaque features and 62 selected human features. The selected features were analyzed based on five parameters (GMV, FA, MD, RD and AD) and three groups (human-specific, macaque-specific and common features in human and macaque). (A). The percentage of ea

### Figure supplement 8.
The top three and last three features associated with E-age gap in MD, RD and AD. AF: arcuate fasciculus; VOF: vertical occipital fasciculus; ILF: inferior longitudinal fasciculus; FM: forceps major; MLF: middle longitudinal fasciculus; SLF II: superior longitudinal fasciculus II; Cs:Dorsal: cingulu

## References
Total references in published paper: 69

### Key References (from published paper)
- Analysis of partial volume effects in diffusion-tensor MRI (, 2001)
- Organizing Principles of Human Cortical Development—Thickness and Area from 4 to 30 Years: Insights  (, 2016)
- Primate auditory prototype in the evolution of the arcuate fasciculus (, 2020a)
- Primate auditory prototype in the evolution of the arcuate fasciculus (, 2020b)
- The Arcuate Fasciculus and language origins: Disentangling existing conceptions that influence evolu (, 2022)
- Mapping complementary features of cross-species structural connectivity to construct realistic “Virt (, 2017)
- The arcuate fasciculus and the disconnection theme in language and aphasia: history and current stat (, 2008)
- Decoding the role of the insula in human cognition: functional parcellation and large-scale reverse  (, 2013)
- A conserved pattern of differential expansion of cortical areas in simian primates (, 2013)
- Connectional asymmetry of the inferior parietal lobule shapes hemispheric specialization in humans,  (, 2021)
- Present simple and continuous: emergence of self-regulation and contextual sophistication in adolesc (, 2014)
- Looking for the optimal DTI acquisition scheme given a maximum scan time: are more b-values a waste  (, 2009)
- A convenient method of obtaining percentile norms and accompanying interval estimates for self-repor (, 2009)
- Amygdalo-cortical sprouting continues into early adulthood: implications for the development of norm (, 2002)
- Beyond the arcuate fasciculus: consensus and controversy in the connectional anatomy of language (, 2012)
- Quantitative assessment of prefrontal cortex in humans relative to nonhuman primates (, 2018)
- Evidence for segregated and integrative connectivity patterns in the human Basal Ganglia (, 2008)
- The early development of brain white matter: a review of imaging studies in fetuses, newborns and in (, 2014)
- What is special about the human arcuate fasciculus? Lateralization, projections, and expansion (, 2019)
- A multi-scanner neuroimaging data harmonization using RAVEL and ComBat (, 2021)
- Opportunities and limitations of genetically modified nonhuman primate models for neuroscience resea (, 2020)
- Harmonization of multi-site diffusion tensor imaging data (, 2017)
- The macaque ventral intraparietal area has expanded into three homologue human parietal areas (, 2022)
- No relative expansion of the number of prefrontal neurons in primate and human evolution (, 2016)
- Dependence of brain DTI maps of fractional anisotropy and mean diffusivity on the number of diffusio (, 2009)
- Comparative analysis of the macroscale structural connectivity in the macaque and human brain (, 2014)
- Experiments in macaque monkeys provide critical insights into age-associated changes in cognitive an (, 2019)
- Integration of emotion and cognition in the lateral prefrontal cortex (, 2002)
- Similar patterns of cortical expansion during human development and evolution (, 2010)
- The Multifaceted Role of the Ventromedial Prefrontal Cortex in Emotion, Decision Making, Social Cogn (, 2018)

## Ground Truth Reference
- Figures: 13
- Tables: 1
- References: 69