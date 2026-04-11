# Experimental Log: Agent-based model demonstrates the impact of nonlinear, complex interactions between cytokines on muscle regeneration

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsABM outputs align with calibration and validation dataFollowing parameter density-based calibration, the unknown parameters were narrowed into a final calibration parameter set (Supplemental table 1).
- The model data were consistent with the experimental trends, and the 95% confidence interval was within the SD for all calibration data time points except for SSCs at day 3 (Fig.
- Macrophage (total, M1, and M2), neutrophil, and capillary counts, which were not used for model calibration, were found to also be consistent with experimental trends and allowed us to independently validate model outputs (Fig.
- 3D-H).biorxiv;2023.08.14.553247v2/FIG3F3fig3Figure 3.ABM calibration and validation.
- ABM parameters were calibrated so that model outputs for CSA recovery, SSC, and fibroblast counts were consistent with experimental data (A-C)76,102.
- Separate outputs from those used in calibration were compared to experimental data97,102,107,108 to validate the ABM (D-H).
- Error bars represent experimental standard deviation, and model 95% confidence interval is indicated by the shaded region.
- Injections of VEGF-A led to faster CSA recovery, more damaged tissue clearance, and a concentration dependent dose response, consistent with prior studies73.
- Cell depletion simulations predicted decrease in all markers of regeneration, consistent with prior studies73,109,110.
- When simulating hindered angiogenesis conditions, the model aligned with experimental studies showing detriments in CSA recovery, increased neutrophil and macrophage cells, and elevated ECM collagen density, indicating progression of fibrosis within the microenvironment111.
- This difference is likely due to the fact that the model did not include cross regulation with interferons which are upregulated with TNF-α KO112.
- Second, macrophage depletion simulations predicted decreased TGF-β concentrations throughout the simulation while experiments measured an initial decrease in concentration followed by increased concentrations at days 7 and 14.
- This difference may be due to the fact that macrophage depletion was experimentally induced with clodronate-containing liposomes which could have reduced consistency of depletion across the time course and other downstream impacts that were not represented by decreasing macrophages in the model pert
- Refer to table 8 for model input conditions and supplemental table 6 for information on experimental references.Analysis of ABM perturbations leads to new insights regarding cytokine and cell dynamicsThe model allowed for new insights into the dynamics of muscle regeneration by providing additional 
- VEGF-A levels remained elevated compared to control simulations following the injection at day 5 post injury (Fig.
- CSA recovery had the highest increase at 28 days post injury with the high (103) relative concentration delivered) VEGF-A injection followed by the extra high (2×103) relative concentration delivered) injection (Fig.
- The medium (750 relative concentration delivered) and low (500 relative concentration delivered) VEGF-A injections had higher CSA recovery 15 days post injury but were not significantly different from the control at day 28.
- In contrast, HGF levels were elevated from day 5 to day 28 with hindered angiogenesis, as were TGF-β and IL-10 (Fig.
- MCP-1 concentration had a lower overall peak level with elevated levels from days 21 to 28 (Fig.
- 5B).biorxiv;2023.08.14.553247v2/FIG5F5fig5Figure 5.Dose dependent response with VEGF-A injection compared to hindered angiogenesis.
- MCP-1, TGF-β, and IL-10 concentrations were elevated a later stages of regeneration with hindered angiogenesis (H, I, L).
- MMP-9 concentration was lower at the simulation midpoint but elevated at late regeneration stages (K).Cytokine knockout perturbations revealed crosstalk and temporal interplay between cytokines (Fig.
- For example, with MCP-1 KO there was an overall increase in cytokine levels for all other cytokines within the microenvironment except for VEGF-A at 12 hours post injury (Fig.
- By 7 days post injury TNF-α, TGF-β, IL-10, and MMP-9 had decreased from unaltered regeneration day 7 levels but VEGF-A and HGF were elevated.
- With TNF-α KO there was a decrease in TGF-β at early timepoints but a strong increase by day 28 (Fig.
- Following IL-10 KO there was an increase in TNF-α that peaked at 7 days post injury (Fig.
- HGF was slightly decreased throughout and TGF-β was strongly decreased by day 7.
- MMP-9 was decreased at 12 hours and 28 days post injury but heavily increased at day 7.biorxiv;2023.08.14.553247v2/FIG6F6fig6Figure 6.Heatmaps of changes in cytokine concentration at various timepoints throughout regeneration following individual cytokine knockout (KO) demonstrating cross-talk betwe
- With MCP-1 KO there was an increase in all cytokines except VEGF-A at 12 hours post injury.
- Over the course of regeneration there was continued increasing elevation of HGF, increases in VEGF-A, and TGF-β decreased at day 7 followed by a strong increase by day 28 post injury (A).
- In the TNF-α KO simulations, there was an early decrease in TGF-β that shifts to strong increases by day 28.
- MMP-9 increased throughout the duration, HGF and IL-10 were decreased, VEGF-A lagged in the beginning but was increased during mid to late timepoints (B).
- Following IL-10 KO there were increases in TNF-α, decreases in HGF and TGF-β, and elevated MMP-9 at day 7 that decreased by day 28 (C).Cytokine dynamic analysis leads to new model perturbations that predict improved regenerationLHS-PRCC of cytokine decay and diffusion parameters elucidated temporal 
- Of all cytokine parameters, the model outputs were most sensitive to HGF decay, with all outputs except M1 cell count being significantly impacted.
- PRCC plots showed that TGF-β and MMP decay were positively correlated and HGF decay was negatively correlated with CSA recovery, with higher significance at timepoints after 12 days (Supplemental Fig.
- Correlation plots for various cytokine concentrations and regeneration metrics showed trends in cytokine dependent cell behaviors such as the TNF-α concentration that led to heightened fibroblast cell counts as well as the corresponding TNF-α concentration threshold that results in diminished fibrob
- These PRCC trends guided cytokine parameter perturbations to include lower HGF and VEGF-A decay, higher TGF-β, MMP-9, and MCP-1 decay, and higher MCP-1 diffusion because each of the cytokine modifications indicated some form of enhanced regeneration outcome metrics (Supplemental Table 3).
- All these perturbations except MCP-1 decay show increased CSA, increased healthy capillaries, and increased SSCs (Fig.
- Finally, a combination of all changes except for MCP-1 decay was simulated.
- 7A), as well as increased M1 macrophage counts (Fig.
- 7B), decreased M2 macrophage counts (Fig.
- 7C), increased fibroblasts (Fig.
- During early regeneration, lower HGF decay, higher TGF decay, and MCP-1 diffusion contributed to increased SSCs while lowered VEGF decay increased angiogenesis.
- The combined cytokine perturbation predicted a 13% improvement in CSA recovery compared to the unaltered regeneration amount at 28 days.
- The combined cytokine perturbation also had higher peaks in SSC and fibroblast counts than any of the singular cytokine perturbations, indicating the synergistic effects of altering the cytokine dynamics in combination.biorxiv;2023.08.14.553247v2/FIG7F7fig7Figure 7.Combined alterations of various cy
- All tested alterations except higher MCP-1 decay resulted in higher CSA recovery compared to the control (A).
- M1 cell count was higher for all perturbations with the highest peaks with increased MCP-1 diffusion and the combined cytokine alteration perturbation (B).
- Higher MCP-1 decay resulted in the largest M2 peak and higher MCP-1 diffusion, higher TGF-β decay, and the combined cytokine alteration had a lower M2 peak than the control (C).
- All perturbations except the combined and higher MMP-9 decay resulted in increased capillaries as a result of additional capillary sprouts (F).

## Tables

### Table 1.
> Neutrophil Agent Rules


### Table 2.
> Macrophage Agent Rules


### Table 3.
> SSC Agent Rules


### Table 4.
> Fibroblast Agent Rules


### Table 5.
> Fiber Agent Rules


### Table 6.
> Microvasculature Rules


### Table 7.
> Model parameters of spatial mechanisms


### Table 8.
> Model perturbation input conditions and corresponding published experimental results


### Table 9.
> Summary of cytokine sensitivity analysis. Significance was determined with α=0.05, and a Bonferroni correction for the number of tests. + and - represent statistically significant positive and negativ


### Supplemental Table 1.
> Unknown model parameters calibrated using LHS to recapitulate published literature


### Supplemental Table 2.
> Criteria utilized for CaliPro model calibration


### Supplemental Table 3.
> Cytokine perturbations based on PRCC


### Supplemental Table 4.
> CPM model parameters


### Supplemental Table 5.
> CPM agent Adhesion parameters


### Supplemental Table 6.
> Experimental data description for model comparison


## Figure Descriptions

### Figure 1.
Flowchart of ABM rules. The model starts with initialization of the geometry and the prescribed injury. This is followed by recruitment of cells based on relative cytokine amounts within the microenvironment. The inflammatory cells, SSCs, and fibroblasts follow their literature defined rules and pro

### Figure 2.
Overview of ABM simulation of muscle regeneration following an acute injury. A. Simulated cross-sections of a muscle fascicle that was initially defined by spatial geometry from a histology image. Muscle injury was simulated by replacing a section of the healthy fibers with necrotic elements. In res

### Figure 3.
ABM calibration and validation. ABM parameters were calibrated so that model outputs for CSA recovery, SSC, and fibroblast counts were consistent with experimental data (A-C)76,102. Separate outputs from those used in calibration were compared to experimental data97,102,107,108 to validate the ABM (

### Figure 4.
ABM perturbation outputs are compared to various literature experimental results. Each perturbation model output is compared to the available corresponding published result. The top triangles indicate the literature findings and the bottom triangles indicate the model outputs. Red triangles represen

### Figure 5.
Dose dependent response with VEGF-A injection compared to hindered angiogenesis. VEGF-A concentration response to varied levels of VEGF injection (A). Hindered angiogenesis resulted in slower and overall decreased CSA recovery (B). Capillary count was dependent on VEGF-A injection level (C). Total m

### Figure 6.
Heatmaps of changes in cytokine concentration at various timepoints throughout regeneration following individual cytokine knockout (KO) demonstrating cross-talk between cytokines. With MCP-1 KO there was an increase in all cytokines except VEGF-A at 12 hours post injury. Over the course of regenerat

### Figure 7.
Combined alterations of various cytokine dynamics enhance muscle regeneration outcomes. All tested alterations except higher MCP-1 decay resulted in higher CSA recovery compared to the control (A). M1 cell count was higher for all perturbations with the highest peaks with increased MCP-1 diffusion a

### Supplemental Figure 1.
Overview of Calibration Methods. Latin hypercube sampling is used to generate 600 unique parameter sets given starting bounds, each of which was run in triplicate. The simulations were filtered given specified criteria (i.e. fitting within experimental bounds for CSA recovery) and then alternative d

### Supplemental Figure 2.
PRCC plots for various model outputs over time to illustrate how the significance of cytokine decay and diffusion parameters varies at different points throughout regeneration. Black dots indicate statistically significant (P < 0.05) correlation for that timepoint. (A) CSA recovery had correlations 

### Supplemental Figure 3.
Cytokine concentrations are correlated with cell counts and recovery metrics at various stages of regeneration. There is an optimal MCP-1 concentration that tends to result in higher M1 counts 1 day post injury (A). IL-10 concentration is positively correlated with M2 count 3 days post injury (B). V

### Supplemental Figure 4.
Non-perfused capillaries for each cytokine perturbation. The combined cytokine perturbation had the lowest number of non-perfused capillaries and all other perturbations resulted in less non-perfused capillaries compared to the control.

### Supplemental Figure 5.
Overview of ABM simulation with different initial histology configuration

## References
Total references in published paper: 160

### Key References (from published paper)
- Stem Cells for the Treatment of Skeletal Muscle Injury Sports injury Stem cells Tissue engineering F (, 2009)
- MUSCLE INJURIES IN ATHLETES (, 2011)
- Clinical practice guide for muscular injuries: epidemiology, diagnosis, treatment and prevention (, 2011)
- Muscle injuries: optimising recovery (, 2007)
- Muscle injuries and repair: Current trends in research (, 2002)
- Mechanisms Regulating Muscle Regeneration: Insights into the Interrelated and Time-Dependent Phases  (, 2020)
- Divergent Roles of Inflammation in Skeletal Muscle Recovery From Injury (, 2020)
- Agent-based model provides insight into the mechanisms behind failed regeneration following volumetr (, 2021)
- Endogenous expression of angiogenesis-related factors in response to muscle injury (, 2006)
- Usage of Growth Factors in Acute Muscle Injuries (, 2015)
- Growth factors in skeletal muscle regeneration (, 1996)
- Proteolytic modulation of tumor microenvironment signals during cancer progression (, 2022)
- Cytokine dynamics and targeted immunotherapies in autoimmune encephalitis (, 2022)
- Binding to the Extracellular Matrix and Proteolytic Processing: Two Key Mechanisms Regulating Vascul (, 2010)
- Agent-based model illustrates the role of the microenvironment in regeneration in healthy and mdx sk (, 2018)
- Computational modeling of muscle regeneration and adaptation to advance muscle tissue regeneration s (, 2016)
- A Coupled Mechanobiological Model of Muscle Regeneration In Cerebral Palsy (, 2021)
- Delayed skeletal muscle repair following inflammatory damage in simulated agent-based models of musc (, 2023)
- Computational Models Provide Insight into In Vivo Studies and Reveal the Complex Role of Fibrosis in (, 2020)
- CaliPro: A Calibration Protocol That Utilizes Parameter Density Estimation to Explore Parameter Spac (, 2021)
- Agent-based computational model investigates muscle-specific responses to disuse-induced atrophy (, 2015)
- Multiscale Model of Antiviral Timing, Potency, and Heterogeneity Effects on an Epithelial Tissue Pat (, 2022)
- Multi-Scale Modeling of Tissues Using CompuCell3D (, 2012)
- A mathematical model of skeletal muscle regeneration (, 2018)
- Muscle cell-derived cytokines in skeletal muscle regeneration (, 2022)
- Increments in cytokines and matrix metalloproteinases in skeletal muscle after injection of tissue-d (, 2002)
- Satellite cells and the muscle stem cell niche (, 2013)
- From innate to adaptive immune response in muscular dystrophies and skeletal muscle regeneration: Th (, 2014)
- Chemotaxing neutrophils enter alternate branches at capillary bifurcations (, 2020)
- The dual roles of neutrophils and macrophages in inflammation: A critical balance between tissue dam (, 2006)

## Ground Truth Reference
- Figures: 12
- Tables: 15
- References: 160