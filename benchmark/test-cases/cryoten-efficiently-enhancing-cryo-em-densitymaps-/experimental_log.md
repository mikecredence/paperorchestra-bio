# Experimental Log: CryoTEN: Efficiently Enhancing Cryo-EM Density Maps Using Transformers

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- During the evaluation, each input cryo-EM map was sliced into 48 x 48 x 48 blocks, which were fed as input to CryoTEN in batches.
- The quality of the enhanced maps was then assessed.Evaluation on CryoEM primary mapsCryoTEN is first evaluated on the test set containing 150 cryo-EM deposited primary maps using various map-model validation metrics.
- Fourier Shell Correlation (FSC) of CryoTEN enhanced maps and original deposited cryo-EM primary maps are computed by comparing them with their corresponding atomic protein structures using phenix.mtriage [Afonine et al., 2018] tool.
- The unmasked map-model FSC resolution at both 0.143 (FSC@0.143) and 0.5 (FSC@0.5) thresholds are reported.
- Similarly, three Cross Correlation (CC) scores: CC box, CC mask, and CC peaks are computed for the maps by comparing them against their corresponding atomic structure using phenix.map model cc [Afonine et al., 2018] tool.
- Finally, to measure the resolvability of atoms in the maps, the Q-score [Pintilie et al., 2020] metrics is computed using UCSF Chimera [Pettersen et al., 2004] mapq plugin.
- The average scores of these metrics for the original deposited primary maps and the CryoTEN processed primary maps are reported in Table 1.biorxiv;2024.09.06.611715v1/TBL1T1tbl1Table 1.The comparison of the average map-model validation metrics scores of the 150 deposited cryo-EM primary maps in the 
- Similarly, the average map-model FSC@0.5 resolution of the CryoTEN processed maps is 3.73Å, 41.54% higher than 6.38Å for the deposited cryo-EM primary maps.
- Out of 150 maps, 100% of the CryoTEN processed maps exhibit an improvement in terms of the map-model FSC@0.143 resolution, and 96% of them show an improvement in terms of the map-model FSC@0.5 resolution.In terms of the CC scores, the CryoTEN processed maps have substantially higher average CC box a
- CryoTEN achieves an average CC box score of 0.8508, 17.66% higher than 0.7231 of the deposited cryo-EM maps, indicating that it improves the overall quality of the entire maps.
- The average CC peaks score of CryoTEN processed maps is 0.7475, 16.09% higher than 0.6439 of the deposited cryo-EM maps, indicating that it improves the quality of the regions with the highest density that are important for structure determination.However, the average CC Mask score of the CryoTEN pr
- But as the structure modeling results shown in Section “Improvement of protein structure modeling (map interpretability)” below, this minor reduction does not appear to affect the quality of the protein structural models built from the maps as the structures built from the CryoTEN-processed maps hav
- Figure 2 further compares the distribution of the map-model FSC resolution, Q-score, and CC scores between the deposited cryo-EM primary maps and CryoTEN processed maps.biorxiv;2024.09.06.611715v1/FIG2F2fig2Fig 2.The comparison of the map-model validation metrics scores of the 150 deposited cryo-EM 
- Half violin and box plots of (a) unmasked FSC@0.143 resolution, (b) unmasked FSC@0.5 resolution (7 outliers with FSC@0.5 > 20Å in deposited primary maps are hidden for better visualization), (c) average Q-score, and (d,e,f) CC box, CC mask, CC peaks scores respectively.Evaluation on CryoEM half maps
- Out of the 150 primary maps in the test set, 70 maps have corresponding unprocessed cryo-EM half map pairs available in EMDB.
- For each of them, one half map is chosen for the evaluation, resulting in 70 raw half maps for assessing CryoTEN.
- The results are reported in Table 2.biorxiv;2024.09.06.611715v1/TBL2T2tbl2Table 2.Comparison of average map-model validation metrics scores of the 70 deposited cryo-EM half maps and CryoTEN processed half maps.CryoTEN: Efficiently Enhancing Cryo-EM Density Maps using Transformers 5Similar to the res
- Since CryoTEN can enhance both processed and unprocessed cryo-EM maps, it can be used with existing post-processing tools such as RELION [Scheres, 2012, Rosenthal and Henderson, 2003] and CryoSPARC [Punjani et al., 2017] to improve the quality of any kind of density maps.
- Supplementary Figure 1 further compares the distributions of the FSC resolutions, Q-score, and CC scores of the deposited cryo-EM half maps and CryoTEN processed half maps.Improvement of protein structure modeling (map interpretability)To evaluate the impact of CryoTEN on improving the quality of pr
- We used the zone tool in UCSF ChimeraX [Pettersen et al., 2021] to extract chain-wise map regions from the maps.
- Out of all the chains extracted from 150 maps, phenix.map to model was able to build structural models for 700 chains from 124 maps successfully.
- To eliminate human influence, the modeled structures of the chains built from the 124 deposited maps and the corresponding CryoTEN processed maps are evaluated without any further model refinement.The generated atomic model for each chain is evaluated using phenix.chain comparison tool [Liebschner e
- The residue coverage score (%) is the percentage of Cα atoms in a modeled structure that are aligned within 3Å to its corresponding PDB structures.
- The sequence match score (%) is the percentage of residues in the modeled structure whose amino acid types exactly match those in the corresponding PDB structure.biorxiv;2024.09.06.611715v1/TBL3T3tbl3Table 3.The quality (residue coverage and sequence match scores) of structural models of 700 protein
- Moreover, the average sequence match score of the atomic models built from the CryoTEN processed maps is 43.52%, higher than 40.05% for the deposited primary maps, indicating that CryoTEN processing also improves the precision of determining the amino acid types of Cα atoms.For all 700 chains, CryoT
- Further refinement of the structural models by human experts still plays a crucial role in building high-quality atomic models as fully automated density map-based structure modeling methods that match the quality of expert-built models are still not available despite the significant progress [Giri 
- The deposited maps and the CryoTEN enhanced maps are overlaid with their corresponding protein structure (PDB ID: 7JHJ) to visualize their quality.
- A similar example (EMD-22937 of H1 A/Michigan/45/2015 ectodomain) is illustrated in Supplementary Figure 2.
- Specifically, in the case of EMD-22338, the structural model of Chain R built from the CryoTEN enhanced map has a residue coverage of 78.7%, higher than 72.9% from the deposited Cryo-EM map.
- Moreover, the residue coverage of Chain A and D for the former is 75.2% and 85.4% respectively, substantially higher than 63.3%, and 37.3% for the latter.biorxiv;2024.09.06.611715v1/FIG3F3fig3Fig 3.Comparison of an original deposited density map (EMD-22338) and its CryoTEN enhanced counterpart in su
- (a) The deposited density map (blue) is visualized at three contour levels (lower, recommended, and higher) in superimposition with the protein structure (PDB ID: 7JHJ).
- For instance, at the lower contour level, CryoTEN removes a lot of noise in the circled region, while at the high contour level, it adds some structural details that are missing in the circled regions of the deposited density mapsValidation of robustness of CryoTEN in improving structure modeling (m
- The average residue coverage and sequence match scores for the structural models in each group built from the deposited maps and the CryoTEN enhanced maps are reported in Table 4.
- The improvement for the medium resolution group is most pronounced, where the residue coverage of models is improved by 9.76 percentage points and sequence match improved by 4.03 percentage points.
- Due to the poor resolvability of the atoms in low resolution maps, there is only a marginal improvement of 0.49 percentage points in the average sequence match score, but the residue coverage score is improved by 6.22 percentage points.
- Due to better atom resolvability in high resolution maps, the models built from experimental deposited maps achieve a good residue coverage and sequence match of 78.98% and 66.15% respectively, which CryoTEN was able to further improve to 84.28% and 68.37%, respectively.
- The results demonstrate that CryoTEN can robustly improve the quality of cryo-EM density maps to build better structural models.biorxiv;2024.09.06.611715v1/TBL4T4tbl4Table 4.Robustness in improving map interpretability (structure modeling) for maps of various resolutions by CryoTEN.The 124 cryo-EM m
- The average quality scores of the chain structural models built from the deposited cryo-EM maps and their CryoTEN enhanced counterparts in each category are shown.Comparison with other deep learning methodsWe compare CryoTEN with two existing deep learning methods for enhancing cryo-EM density maps,
- While CryoTEN and EMReady processed all 150 maps in our test set, DeepEMhancer was able to process only 131 maps without crashing.
- Therefore, to make a fair comparison, we compare all the methods on only 131 maps in the test set in terms of average FSC@0.143, FSC@0.5, CC box, CC mask, CC peaks and Q-score.
- We also assess their running time and memory requirement on a subset of 20 test maps.biorxiv;2024.09.06.611715v1/TBL5T5tbl5Table 5.Comparison of map-model validation metrics scores of 131 deposited cryo-EM primary maps in the test dataset, DeepEMhancer enhanced maps, EMReady enhanced maps, and CryoT
- For instance, the FSC@0.143 and CC Box of CryoTEN is 2.44Å and 0.8499, substantially higher than 3.52Å and 0.6309 of DeepEMhancer.
- The performance of CryoTEN is relatively close to the best-performing EMReady in terms of all the metrics, and both of them substantially increase FSC@0.143, FSC@0.5, CC box, and CC peaks of the maps.
- EMReady has a CC mask score of 0.7913, sightly higher than 0.784 of the deposited maps, while CryoTEN has a slightly lower CC mask score of 0.7669.
- Because the quality of the density maps is indeed substantially improved by both EMReady and CryoTEN in terms of most of the metrics and better protein structures can be built from the CryoTEN processed maps, it is reasonable to hypothesize that CC mask is not sensitive to the change of the quality 
- On average, CryoTEN takes only 1.66 minutes to enhance a map with a standard deviation of ±0.42 minutes, whereas EMReady takes 19.65 minutes per map with a standard deviation of ±17.95 minutes and DeepEMhancer takes 43.27 minutes per map with a standard deviation of ±9.41 minutes.
- Moreover, on an NVIDIA A10 GPU, with batch size configured as 40 for all methods, CryoTEN consumes only 3.41 GB of GPU memory, compared to 21.88 GB of DeepEMhancer and 8.86 GB of EMReady.
- The per-map runtime and memory consumption for DeepEMhancer, and EMReady are reported in Supplementary Table 1.

## Tables

### Table 1.
> The comparison of the average map-model validation metrics scores of the 150 deposited cryo-EM primary maps in the test dataset and the corresponding CryoTEN processed maps.The scores are computed by 


### Table 2.
> Comparison of average map-model validation metrics scores of the 70 deposited cryo-EM half maps and CryoTEN processed half maps.


### Table 3.
> The quality (residue coverage and sequence match scores) of structural models of 700 protein chains built from the deposited 124 cryo-EM density maps and the CryoTEN processed maps.


### Table 4.
> Robustness in improving map interpretability (structure modeling) for maps of various resolutions by CryoTEN.The 124 cryo-EM maps are grouped into three categories: low, medium, and high resolution, c


### Table 5.
> Comparison of map-model validation metrics scores of 131 deposited cryo-EM primary maps in the test dataset, DeepEMhancer enhanced maps, EMReady enhanced maps, and CryoTEN enhanced maps as well as the


## Figure Descriptions

### Fig 1.
Overview of data processing and CryoTEN model architecture. (a) Data collection and preprocessing. (b) The CryoTEN model architecture along with the training and evaluation pipeline. (c) The structure of the CryoTEN model’s encoder, decoder, and residual convolution (ConvRes) block.

### Fig 2.
The comparison of the map-model validation metrics scores of the 150 deposited cryo-EM primary maps in the test dataset and the corresponding CryoTEN processed maps. Half violin and box plots of (a) unmasked FSC@0.143 resolution, (b) unmasked FSC@0.5 resolution (7 outliers with FSC@0.5 > 20Å in depo

### Fig 3.
Comparison of an original deposited density map (EMD-22338) and its CryoTEN enhanced counterpart in superimposition with the known protein structure from the PDB. (a) The deposited density map (blue) is visualized at three contour levels (lower, recommended, and higher) in superimposition with the p

## References
Total references in published paper: 25

### Key References (from published paper)
- New tools for the analysis and validation of cryo-EM maps and atomic models (, 2018)
- Topaz-denoise: general deep denoising models for cryoem and cryoet (, 2020)
- Artificial intelligence in cryo-em protein particle picking: Recent advances and remaining challenge (, 2024a)
- Cryotransformer: A transformer model for picking protein particles from cryo-em micrographs (, 2024b)
- Refinement of protein structures into low-resolution density maps using rosetta (, 2009)
- De novo atomic protein structure modeling for cryo-EM density maps using 3D transformer and hidden m (, 2024a)
- De novo atomic protein structure modeling for cryoem density maps using 3d transformer and hmm (, 2024b)
- CryoSegNet: accurate cryo-EM protein particle picking by integrating the foundational AI image segme (, 2024)
- Improvement of cryo-EM maps by simultaneous local and non-local deep learning (, 2023)
- Model-based local density sharpening of cryo-em maps (, 2017)
- Local computational methods to improve the interpretability and analysis of cryo-EM maps (, 2021)
- Macromolecular structure determination using X-rays, neutrons and electrons: recent developments in  (, 2019)
- UCSF chimera–a visualization system for exploratory research and analysis (, 2004)
- Ucsf chimerax: Structure visualization for researchers, educators, and developers (, 2021)
- Measurement of atom resolvability in cryo-EM maps with q-scores (, 2020)
- cryosparc: algorithms for rapid unsupervised cryoem structure determination (, 2017)
- Automatic local resolution-based sharpening of cryo-EM maps (, 2019)
- Optimal determination of particle orientation, absolute hand, and contrast loss in single-particle e (, 2003)
- Deepemhancer: a deep learning solution for cryo-em volume post-processing (, 2021)
- A bayesian view on cryo-em structure determination (, 2012)
- De novo main-chain modeling for EM maps using MAINMAST (, 2018)
- A fully automatic method yielding initial models from high-resolution cryo-electron microscopy maps (, 2018a)
- Automated map sharpening by maximization of detail and connectivity (, 2018b)
- Practical blind image denoising via swin-conv-UNet and data synthesis (, 2023)
- Cryodrgn: reconstruction of heterogeneous cryo-em structures using neural networks (, 2021)

## Ground Truth Reference
- Figures: 3
- Tables: 5
- References: 25