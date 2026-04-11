# Experimental Log: Agent-Based Model of Nonlinear Cytokine Interactions in Muscle Regeneration

> Data tables and results extracted from full-text analysis

---

## Model Architecture Summary

| Component | Details |
|---|---|
| Framework | Cellular Potts Model (CPM) |
| Software | CompuCell3D v4.3.1 |
| Language | Python-based |
| Literature references | >100 published studies |
| Total rules | ~100 |
| Cell/structure types | 7 (fibers, SSC, fibroblasts, neutrophils, macrophages, microvessels, lymphatic vessels) |
| Cytokines modeled | TNF-alpha, TGF-beta, HGF, VEGF-A, MCP-1, MMP-9, IL-10 |
| Simulation domain | Cross-section of murine skeletal muscle fascicle |
| Code availability | https://zenodo.org/records/10403014 |

---

## Agent Rule Summary

### Neutrophil Agent Rules (Table 1)

| Behavior | Description |
|---|---|
| Recruitment | Based on relative cytokine amounts in microenvironment |
| Chemotaxis | Follows cytokine gradients |
| Phagocytosis | Removes necrotic tissue |
| Apoptosis | Time-dependent and signal-dependent |
| Cytokine secretion | Contributes to inflammatory signaling |

### Macrophage Agent Rules (Table 2)

| Behavior | Description |
|---|---|
| Recruitment | Monocyte-derived, cytokine-dependent |
| M1 phenotype | Pro-inflammatory, tissue clearance |
| M2 phenotype | Anti-inflammatory, pro-regenerative |
| Phenotype switching | M1 to M2 transition based on microenvironment |
| Cytokine secretion | TNF-alpha (M1), TGF-beta, IL-10 (M2) |

### SSC Agent Rules (Table 3)

| Behavior | Description |
|---|---|
| Activation | Triggered by injury signals and HGF |
| Proliferation | Regulated by HGF and other growth factors |
| Differentiation | Myoblast commitment and fusion |
| Fusion | Incorporation into damaged fibers for repair |
| Self-renewal | Maintenance of stem cell pool |

### Fibroblast Agent Rules (Table 4)

| Behavior | Description |
|---|---|
| Activation | TGF-beta dependent |
| Proliferation | Growth factor regulated |
| ECM deposition | Collagen production |
| Apoptosis | Programmed cell death during remodeling |

### Fiber Agent Rules (Table 5)

| Behavior | Description |
|---|---|
| Necrosis | Injury-induced fiber death |
| Regeneration | CSA recovery via SSC fusion |
| Growth | Cross-sectional area increase during repair |

### Microvasculature Rules (Table 6)

| Behavior | Description |
|---|---|
| Angiogenesis | VEGF-A dependent new vessel formation |
| Perfusion | Capillary functional status |
| Fragmentation | Loss of perfusion following injury |
| Recovery | Restoration of capillary network |

---

## Model Calibration

### Calibration Methodology

| Parameter | Value |
|---|---|
| Unknown parameters | 52 |
| LHS parameter sets | 600 |
| Replicates per set | 3 (triplicate) |
| Calibration targets | CSA recovery, SSC count, fibroblast count |
| Method | LHS + ADS (alternative density subtraction) |
| Sensitivity analysis | PRCC (partial rank correlation coefficient) |

### Calibration Data Fit Summary

| Output | Alignment with Experimental Data | Notes |
|---|---|---|
| CSA recovery | Within experimental SD at all time points | Fig. 3A |
| SSC count | Within SD except day 3 | Fig. 3B - 95% CI outside SD at day 3 |
| Fibroblast count | Within experimental SD at all time points | Fig. 3C |

### Validation Outputs (Not Used in Calibration)

| Output | Consistency with Experimental Trends | Figure |
|---|---|---|
| Total macrophage count | Consistent | Fig. 3D |
| M1 macrophage count | Consistent | Fig. 3E |
| M2 macrophage count | Consistent | Fig. 3F |
| Neutrophil count | Consistent | Fig. 3G |
| Capillary count | Consistent | Fig. 3H |

---

## Model Perturbation Results (Table 8)

### Perturbation Comparison with Published Experiments

| Perturbation | Model Prediction (CSA) | Published Result (CSA) | Agreement |
|---|---|---|---|
| VEGF-A injection (low dose) | Increased recovery | Increased recovery | Yes |
| VEGF-A injection (high dose) | Increased recovery (plateaus) | Increased recovery | Yes |
| Cell depletion | Decreased regeneration markers | Decreased regeneration | Yes |
| Hindered angiogenesis | Decreased CSA recovery | Decreased CSA recovery | Yes |
| TNF-alpha KO | Increased CSA recovery | Decreased CSA recovery | No |
| Macrophage depletion (TGF-beta) | Decreased throughout | Initial decrease then increase at d7/d14 | Partial |

### Detailed Perturbation Outcomes

| Perturbation | CSA Recovery | Tissue Clearance | Inflammatory Cells | ECM/Fibrosis |
|---|---|---|---|---|
| VEGF-A injection | Faster recovery | More clearance | - | - |
| Cell depletion | Decreased | Decreased | Decreased | - |
| Hindered angiogenesis | Decreased | - | Elevated neutrophils + macrophages | Elevated collagen density |
| TNF-alpha KO | Model: increased | - | - | - |

- Fig. 4 summarizes perturbation outputs as triangles: red = decrease, blue = increase, gray = no significant change
- Top triangles = literature findings, bottom triangles = model outputs

---

## VEGF-A Dose Response

### VEGF-A Concentration Effects

| VEGF-A Dose Level | CSA Recovery | Capillary Count | SSC Peak | Macrophage Count |
|---|---|---|---|---|
| Control (no injection) | Baseline | Baseline | Baseline | Baseline |
| Low VEGF-A injection | Increased | Increased | Varied | Similar to control |
| Medium VEGF-A injection | Further increased | Further increased | Varied | Similar to control |
| High VEGF-A injection | Plateaus (threshold reached) | Further increased | Varied | Similar to control |
| Hindered angiogenesis | Decreased | Decreased | Decreased | Elevated at late time points |

- Fig. 5A: VEGF-A concentration response shows dose-dependent relationship
- Fig. 5B: Hindered angiogenesis leads to slower and overall decreased CSA recovery
- Fig. 5C: Capillary count depends on VEGF-A injection level
- Fig. 5D: Total macrophage count is similar between control and VEGF-A injections but higher at late time points with hindered angiogenesis
- Fig. 5E: SSC peak varied with VEGF-A dose

---

## Cytokine Knockout Cross-Talk Analysis

### MCP-1 KO Effects Over Time (Fig. 6A)

| Cytokine | 12 hours | Early Regen | Day 7 | Day 28 |
|---|---|---|---|---|
| HGF | Increased | Continued increase | Elevated | Elevated |
| VEGF-A | Decreased | - | Increasing | Increased |
| TGF-beta | Increased | - | Decreased | Strong increase |
| TNF-alpha | Increased | - | - | - |
| IL-10 | Increased | - | - | - |
| MMP-9 | Increased | - | - | - |

### TNF-alpha KO Effects Over Time (Fig. 6B)

| Timepoint | General Effect on Other Cytokines |
|---|---|
| 12 hours | Cross-regulation changes observed |
| Early regen | Cascading temporal impact |
| Day 7 | Continued downstream effects |
| Day 28 | Long-term alterations in cytokine balance |

- Fig. 6 shows heatmaps of cytokine concentration changes at various timepoints following individual KO
- Removal of one cytokine has cascading temporal impact on other cytokines, demonstrating complex cross-talk

---

## Cytokine Sensitivity Analysis (Table 9 / PRCC)

### Significant PRCC Correlations

| Cytokine Parameter | CSA Recovery | SSC Count | Fibroblast Count |
|---|---|---|---|
| HGF decay | Significant | Significant | Significant |
| TGF-beta decay | Significant | Significant | Significant |
| MMP-9 decay | Significant | Significant | Significant |
| TNF-alpha decay | - | - | Significant |
| MCP-1 diffusion | - | Significant | - |
| TNF-alpha diffusion | - | Significant | - |
| VEGF-A decay | - | - | - |
| IL-10 decay | - | - | - |

- Statistical significance determined with alpha=0.05 and Bonferroni correction
- "+" and "-" represent positive and negative correlations respectively
- Fig. S2A: CSA recovery correlated with HGF, TGF-beta, and MMP-9 decay
- Fig. S2B: SSC count correlated with HGF, TGF-beta, MMP-9 decay and MCP-1 and TNF diffusion
- Fig. S2C: Fibroblast count correlated with HGF, TGF-beta, MMP-9, and TNF-alpha decay
- Black dots in PRCC plots indicate statistically significant correlations at each timepoint

---

## Combined Cytokine Perturbation Results (Fig. 7)

### Individual and Combined Alterations

| Perturbation | CSA Recovery vs Control | M1 Peak | M2 Peak |
|---|---|---|---|
| Higher MCP-1 diffusion | Higher | Highest peaks | Lower |
| Lower HGF decay | Higher | Higher | - |
| Lower VEGF-A decay | Higher | Higher | - |
| Higher TGF-beta decay | Higher | Higher | Lower |
| Higher MMP-9 decay | Higher | Higher | - |
| Higher MCP-1 decay | Lower (only one worse than control) | - | Largest peak |
| Combined alteration | Highest (13% increase at day 28) | Highest peak (with MCP-1 diffusion) | Lower |

### Combined Optimal Perturbation Composition

| Component | Direction of Change |
|---|---|
| HGF decay | Decreased |
| VEGF-A decay | Decreased |
| TGF-beta decay | Increased |
| MMP-9 decay | Increased |
| MCP-1 diffusion | Increased |

- Fig. 7A: All perturbations except higher MCP-1 decay resulted in higher CSA recovery vs control
- Fig. 7B: M1 cell count was higher for all perturbations, with highest peaks for increased MCP-1 diffusion and the combined perturbation
- Combined perturbation achieves 13% increase in CSA recovery at day 28 compared to unaltered regeneration
- Combined alterations produce greater fibroblast and SSC proliferation compared to individual changes

---

## Nonlinear Effects and Thresholds

### Observed Nonlinear Relationships (Fig. S3)

| Relationship | Observation | Timepoint |
|---|---|---|
| MCP-1 concentration vs M1 count | Optimal concentration exists (non-monotonic) | Day 1 |
| IL-10 concentration vs M2 count | Positive correlation | Day 3 |
| VEGF-A concentration vs fragmented capillaries | Negative correlation | Day 5 |
| TGF-beta concentration vs SSC count | Higher TGF-beta leads to lower SSC | Day 7 |
| HGF vs CSA recovery | Limited impact beyond a threshold | Multiple |
| TNF-alpha vs fibroblast count | Non-monotonic relationship | Multiple |

---

## Spatial Model Parameters (Table 7)

| Parameter Category | Description |
|---|---|
| Cell dimensions | Pixel-based representation in CPM |
| Diffusion coefficients | Cytokine-specific spatial diffusion |
| Decay rates | Cytokine degradation parameters |
| Chemotaxis coefficients | Cell-type-specific attraction to gradients |
| Contact energies | Cell-cell and cell-ECM interaction energies |
| Temperature (CPM) | Boltzmann temperature for stochastic fluctuations |

---

## Model Discrepancies with Literature

| Perturbation | Model Prediction | Experimental Finding | Likely Reason |
|---|---|---|---|
| TNF-alpha KO (CSA) | Increased recovery | Decreased recovery | Model lacks interferon cross-regulation (upregulated with TNF-alpha KO) |
| Macrophage depletion (TGF-beta kinetics) | Decreased throughout | Initial decrease then increase at d7/d14 | Clodronate-liposome depletion may be inconsistent over time; downstream effects not modeled |

---

## Key Metrics and Datasets

| Metric | Description | Used For |
|---|---|---|
| CSA recovery (%) | Cross-sectional area recovery of muscle fibers | Primary regeneration outcome |
| SSC count | Satellite stem cell numbers over time | Calibration target |
| Fibroblast count | Fibroblast numbers over time | Calibration target |
| Total macrophage count | Combined M1+M2 macrophages | Validation |
| M1 macrophage count | Pro-inflammatory macrophages | Validation |
| M2 macrophage count | Anti-inflammatory macrophages | Validation |
| Neutrophil count | Neutrophil numbers over time | Validation |
| Capillary count | Functional microvessel count | Validation |
| ECM collagen density | Extracellular matrix collagen | Fibrosis indicator |
| Cytokine concentrations | Spatial concentrations of 7 cytokines | Mechanistic analysis |

### Reference Datasets for Calibration and Validation

| Purpose | Data Source | Outputs Used |
|---|---|---|
| Calibration | Published experimental studies (refs 76, 102) | CSA, SSC, fibroblast counts |
| Validation (macrophage) | Published data (refs 97, 102, 107, 108) | Macrophage (total, M1, M2) |
| Validation (neutrophil) | Published experimental data | Neutrophil count |
| Validation (capillary) | Published experimental data | Capillary count |
| Perturbation comparison | 8 separate published studies | Various outcome measures |

---

## Figure Summary

| Figure | Content |
|---|---|
| Fig. 1 | Flowchart of ABM rules showing decision trees for all agent types |
| Fig. 2A | Simulated cross-sections of muscle fascicle at various regeneration stages |
| Fig. 2B | ABM screen captures showing cell and cytokine dynamics |
| Fig. 3A-C | Calibration: CSA, SSC, fibroblast model outputs vs experimental data |
| Fig. 3D-H | Validation: macrophage, neutrophil, capillary counts vs experimental data |
| Fig. 4 | Perturbation comparison matrix (triangles) vs published experiments |
| Fig. 5 | VEGF-A dose response and hindered angiogenesis effects |
| Fig. 6 | Cytokine KO cross-talk heatmaps |
| Fig. 7 | Combined cytokine perturbation results showing enhanced regeneration |
| Fig. S1 | Calibration methodology overview (LHS + ADS + PRCC) |
| Fig. S2 | PRCC plots for cytokine sensitivity over time |
| Fig. S3 | Nonlinear cytokine-cell count correlations |

---

## Therapeutic Implications

| Strategy | Mechanism | Precedent |
|---|---|---|
| Platelet-rich plasma (PRP) delivery | Contains VEGF and TGF-beta | Enhanced muscle recovery reported |
| Plasminogen activators | Convert ECM-bound cytokines to freely diffusible forms | Studied in cancer therapeutics |
| Exogenous cytokine delivery | Direct supplementation of beneficial cytokines | Various experimental settings |
| Synthetic biomaterials | Controlled cytokine release at injury site | Clinical relevance demonstrated |
