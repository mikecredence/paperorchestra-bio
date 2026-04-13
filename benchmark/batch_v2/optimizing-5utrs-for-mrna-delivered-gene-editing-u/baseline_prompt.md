Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Communications

## Idea Summary

# Idea Summary

## Working title
Optimizing 5'UTRs for mRNA-Delivered Gene Editing Using Deep Learning

## Core question
Can deep learning models trained on massively parallel reporter assay data be used to design de novo 5'UTR sequences that maximize protein expression from mRNA therapeutics, specifically for mRNA-delivered gene editing enzymes?

## Motivation / gap
- mRNA therapeutics are rapidly advancing (COVID vaccines, protein replacement, cancer immunotherapy) but methods to optimize the primary sequence for increased expression remain underdeveloped
- Most mRNA therapies use 5'UTRs from alpha- and beta-globin genes by default, leaving substantial room for optimization
- UTR effects are difficult to predict because cis-regulatory elements affect multiple molecular processes and interact with cell-type-specific RNA-binding proteins and microRNAs
- Quantitative deep learning models predicting translation from 5'UTR sequence have recently emerged but have not been applied to guide de novo UTR design for therapeutics
- The degree to which 5'UTR performance is conserved across cell types relevant to mRNA therapeutics (T cells, hepatocytes) was unknown
- megaTAL gene editors are well-suited to mRNA delivery due to their compact single-chain design, but optimal 5'UTR sequences for these cargo have not been explored

## Core contribution (bullet form)
- Measured translation efficiency (Mean Ribosome Load) from ~205,000 randomized 5'UTR variants across three cell types (HEK293T, T cells, HepG2) and found MRL highly correlated between cell lines (r2 = 0.837-0.871 between different cell types)
- Demonstrated that Optimus 5-Prime, trained only on HEK293T data, generalizes well to T cells and HepG2 predictions (r2 up to 0.937 on held-out test set)
- Designed de novo 5'UTRs using gradient descent (Fast SeqProp) and generative neural networks (Deep Exploration Networks/DENs), with and without VAE regularization, achieving gene editing efficiencies exceeding 40% for TGFBR2 and 80% for PDCD1 in K562 cells
- Found that designed 5'UTRs matched or exceeded the performance of the top 0.02% of random MPRA library sequences, with one design achieving up to 50% higher TGFBR2 editing than all controls
- Developed a new model, Optimus 5-Prime(25), for fully randomized 25-nt 5'UTRs, capturing effects near the 5' cap including out-of-frame uAUG positional effects and 5'-proximal poly-C/T enhancement
- Showed that editing efficiency is correlated between cell types and gene targets, though the single best-performing UTR was specific to one cargo and cell type

## Method in brief
The study uses Massively Parallel Reporter Assays (MPRAs) based on polysome profiling. In vitro transcribed (IVT) mRNA libraries with either a 50-nt fully random region (preceded by a 25-nt constant segment) or a 25-nt fully random region (preceded only by GGG for T7 transcription) were transfected into HEK293T, T cells, and HepG2 cells. After 8 hours of incubation with cycloheximide, cell lysates were fractionated on sucrose gradients to separate polysome fractions, and each fraction was sequenced. Mean Ribosome Load (MRL) was calculated for each 5'UTR by multiplying normalized read counts by corresponding ribosome numbers. After filtering for sequences with at least 100 reads across all datasets, approximately 204,803 common variants were obtained.

For model-based design, the previously developed Optimus 5-Prime convolutional neural network was used as the predictive oracle. Two design algorithms were employed: Fast SeqProp (gradient-based sequence optimization) and Deep Exploration Networks (DENs, generative neural networks that take random latent vectors and output optimized sequences). Both approaches were tested with and without Variational AutoEncoder (VAE) regularization to constrain designs to the distribution of natural-like sequences. Designed 5'UTRs were then experimentally validated by incorporating them into mRNA encoding megaTAL gene editing enzymes targeting TGFBR2 and PDCD1 genes, transfecting into K562 and Jurkat cells, and measuring gene editing efficiency via flow cytometry for surface protein knockout.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the 5'UTR optimization for mRNA gene editing study.

---

## MPRA Library Design

| Library | 5'UTR Architecture | Random Region | Constant Region | CDS | 3'UTR |
|---------|-------------------|---------------|----------------|-----|-------|
| Fixed-end (50nt) | 25nt constant + 50nt random | 50 nt | 25 nt at 5' end | EGFP | BGH (bovine growth hormone) |
| Random-end (25nt) | GGG + 25nt random | 25 nt | Only 3 G's at 5' end (T7 requirement) | EGFP | BGH |

---

## Cell Lines and Replicates

| Cell Line | Type | Replicates | Culture Medium | Transfection Method |
|-----------|------|-----------|---------------|-------------------|
| HEK293T | Kidney (established) | 2 | Standard | Lonza 4D Nucleofector |
| T cells | Primary (from PBMCs) | 2 | TCGM with IL-2 | Lonza 4D Nucleofector |
| HepG2 | Hepatocyte (established) | 1 | EMEM + 10% FBS | Lonza 4D Nucleofector |

---

## MPRA Protocol Parameters

| Parameter | Value |
|-----------|-------|
| IVT mRNA per transfection | 1 ug |
| Cells per transfection | 1,000,000 |
| Incubation time | 8 hours |
| Translation inhibitor | Cycloheximide (100 ug/mL) |
| Cycloheximide incubation | 5 min (added dropwise) |
| Fractionation | Sucrose gradient (polysome profiling) |
| Sequencing platform | Illumina |
| Metric | Mean Ribosome Load (MRL) |
| MRL calculation | Normalized read count per fraction x corresponding ribosome number |

---

## Library Coverage After Filtering

| Filter Criterion | Number of 5'UTR Variants |
|-----------------|-------------------------|
| Common across all 5 replicates (3 cell types), >= 100 reads | 204,803 |
| Top coverage subset for correlation analysis | 20,000 |

---

## Cross-Cell-Type MRL Correlation (Fig 1C, Supp Fig 1C)

| Comparison | r2 (20,000 top sequences) |
|------------|--------------------------|
| HEK293T vs. T cells | 0.837-0.870 |
| HEK293T vs. HepG2 | 0.847-0.871 |
| HEK293T replicate 1 vs. replicate 2 | 0.938 |
| T cell replicate 1 vs. replicate 2 | 0.814 |

Fig 1C shows scatter plots of MRL values for the top 20,000 sequences between all pairs of cell line replicates with regression lines and r2 values.

Supplementary Figure 1D shows that r2 decreases as more sequences with lower coverage are included, likely an artifact of decreasing data quality rather than biological differences.

---

## Optimus 5-Prime Prediction Performance (Fig 1D)

| Prediction Target | r2 (on 20,000 held-out sequences) |
|-------------------|----------------------------------|
| HEK293T (training cell type) | 0.937 |
| T cells | Lower than HEK293T but still high |
| HepG2 | Lower than HEK293T but still high |

Fig 1D compares Optimus 5-Prime predictions (trained on HEK293T only) against measured MRL in each cell type. The highest correlation is with HEK293T, as expected, but generalization to T cells and HepG2 is strong.

---

## Retraining Results (Supp Fig 2)

| Observation | Detail |
|-------------|--------|
| Retraining on each cell line | Did not consistently improve performance |
| Implication | HEK293T-trained model already captures most of the relevant 5'UTR regulatory logic |

Supplementary Figure 2 shows that for every cell line and replicate, retraining Optimus 5-Prime from scratch on cell-type-specific data and evaluating on the held-out 20,000 test sequences does not systematically outperform the original HEK293T model.

---

## Multi-Output Model Performance (Supp Fig 3)

| Model Variant | Architecture Change | Performance |
|---------------|-------------------|-------------|
| Multi-output Optimus 5-Prime | Same architecture but 3 outputs (one per cell type) + learnable linear scalings for replicate bias | Comparable to individual models |

---

## 3-mer Positional Model (Supp Fig 4)

| Parameter | Value |
|-----------|-------|
| Model type | Ridge regression |
| Feature vector length | 3,072 (3-mers with position) |
| Regularization coefficient | 1e-5 |
| Training data normalization | z-normalized |
| Test set | 20,000 highest-coverage sequences per cell line replicate |

Supplementary Figure 4 shows that simple k-mer models with position capture substantial variance but underperform deep learning models.

---

## 25-nt Random-End Library Results (Fig 3)

| Observation | Detail |
|-------------|--------|
| Out-of-frame uAUGs near 5' end | Smaller inhibiting effect when close to cap (Fig 3B) |
| Poly-C/T tracts near 5' end | Small enhancing effect that increases with proximity to cap (Fig 3C) |
| Optimus 5-Prime on 25-nt library | Less accurate (due to 5'-proximal effects not captured by model trained on fixed-end library) |
| New model | Optimus 5-Prime(25) trained specifically on 25-nt fully variable UTRs (Fig 3D-E) |

---

## 5'UTR Design Algorithms

| Algorithm | Type | Description |
|-----------|------|-------------|
| Fast SeqProp | Gradient descent | Optimizes sequence via backpropagation through the predictive model |
| DEN (Deep Exploration Network) | Generative neural network | Takes 100-dim latent vector, outputs 50x4 continuous logit representing sequence |
| VAE regularization | Distribution constraint | Constrains designed sequences to resemble natural/observed sequence distribution |
| No additional regularization | Unconstrained | Pure optimization of predicted MRL |

---

## DEN Architecture Details (Supp Fig 7)

| Layer | Specification |
|-------|-------------|
| Input | 100-dimensional continuous latent vector |
| Output | 50 x 4 continuous-valued logit (representing 50-nt sequence) |
| Layers | Conv and ConvTranspose with varying filters, widths, strides, padding, activations |
| Training | Generator optimizes against frozen Optimus 5-Prime predictor |

---

## Inverse Regression DEN (Supp Fig 8)

| Feature | Detail |
|---------|--------|
| Additional input | Target MRL value |
| Architecture modification | Target MRL processed through two dense layers, concatenated to each conv layer input |
| Purpose | Generate sequences targeting specific (intermediate) MRL levels |

---

## Design Strategy Combinations

| Design ID | Algorithm | Regularization | UTR Length |
|-----------|-----------|---------------|-----------|
| Fast SeqProp | Gradient descent | None | 50 nt |
| Fast SeqProp + VAE | Gradient descent | VAE | 50 nt |
| DEN | Generative network | None | 50 nt |
| DEN + VAE | Generative network | VAE | 50 nt |

---

## Control Sequences (Supp Fig 5)

| Control Set | Selection Criteria | N Sequences |
|-------------|-------------------|-------------|
| High MRL controls | From fixed-end MPRA; >= 1000 reads, no uATGs, no starting TG; top 20 by MRL, 4 selected | 4 |
| Submaximal MRL controls | Same filters; selected from middle range | Multiple |
| Random controls | Randomly selected from library | Multiple |

---

## Gene Editing Experimental Setup (Fig 2)

| Parameter | Value |
|-----------|-------|
| Gene editor | megaTAL |
| Gene targets | TGFBR2, PDCD1 |
| Cell lines for editing | K562, Jurkat |
| mRNA 5'UTR architecture | Same as MPRA (constant region + variable region) |
| Readout | Flow cytometry (surface protein knockout) |
| Delivery | Individual transfection per 5'UTR |

---

## Gene Editing Efficiency Results (Fig 2C-D, Fig 4, Supp Fig 11, Supp Fig 23)

| Target Gene | Cell Line | Editing Efficiency (designed UTRs) | Comparison to Controls |
|-------------|-----------|-----------------------------------|----------------------|
| TGFBR2 | K562 | Exceeding 40% | Matches or exceeds top 0.02% of random library |
| PDCD1 | K562 | Exceeding 80% | Strong performance across designs |
| TGFBR2 | K562 (best single design) | Up to 50% higher than all controls | Specific to one cargo/cell type |
| PDCD1 | K562 (same best design) | Did not maintain advantage | Cargo/cell-type specificity |

Fig 2C-D show editing efficiency for multiple designed 5'UTRs against TGFBR2. Most designs achieve high editing efficiency.

Fig 4A-B show that designed 5'UTRs support strong gene editing activity for TGFBR2, with one standout design achieving dramatically higher efficiency.

Fig 4C-D show cross-target comparison where the best TGFBR2 design does not maintain its advantage for PDCD1.

---

## Cross-Target and Cross-Cell-Type Editing Correlation

| Observation | Detail |
|-------------|--------|
| Editing efficiency correlation between cell types | Present (editing efficiency is correlated) |
| Editing efficiency correlation between gene targets | Present but imperfect |
| Best performing UTR | Specific to one cargo and cell type |
| Overall design reliability | Most designs result in high editing efficiency |

---

## Intermediate MRL Design Validation (Fig 2E)

| Design Target | Observed MRL | Conformity |
|--------------|-------------|-----------|
| Intermediate MRL values | Matched target values | Designs targeting sub-maximal expression levels achieved their intended output |

Fig 2E demonstrates that the inverse regression DEN can generate sequences that achieve specific intermediate MRL values, not just maximum expression.

---

## Linear k-mer Model Validation of Designs (Supp Fig 6)

| Parameter | Value |
|-----------|-------|
| Model | Linear k-mer (272-long weight vector + bias) |
| Test set performance | Pearson r = 0.5213 on 25,931 held-out UTRs (no uAUG, > 250 reads) |
| Purpose | Independent validation that designed sequences score high on a simpler model |

---

## Key Sequence Features Identified

| Feature | Effect | Location Dependence |
|---------|--------|-------------------|
| Out-of-frame uAUG | Inhibitory (reduces translation) | Smaller effect when close to 5' cap |
| Poly-C tracts | Enhancing (increases translation) | Effect increases near 5' cap |
| Poly-T tracts | Enhancing (increases translation) | Effect increases near 5' cap |
| In-frame AUG | Strong inhibitory | Position-dependent |

---

## Model Architecture Summary

| Model | Input | Architecture | Output | Training Data |
|-------|-------|-------------|--------|--------------|
| Optimus 5-Prime (original) | 50-nt 5'UTR sequence (one-hot) | CNN | MRL prediction | HEK293T MPRA (fixed-end library) |
| Optimus 5-Prime (retrained) | 50-nt 5'UTR sequence | CNN | Cell-type-specific MRL | Cell-type-specific MPRA |
| Multi-output Optimus 5-Prime | 50-nt 5'UTR sequence | CNN with 3 outputs | MRL for 3 cell types | All cell type data |
| Optimus 5-Prime(25) | 25-nt 5'UTR sequence | CNN | MRL prediction | Random-end 25-nt MPRA |
| 3-mer positional model | 3-mer features with position | Ridge regression | MRL prediction | Per cell-type MPRA |

---

## T Cell Preparation Details

| Step | Protocol |
|------|----------|
| Source | PBMCs from healthy donors |
| Isolation | Ficoll-Paque gradient centrifugation |
| Activation | Anti-CD3/CD28 antibodies + IL-2 |
| Plating density | 1 million cells/mL in TCGM |
| Post-transfection incubation | 37C, 5% CO2 for 8 hours |
| Lysis | 300 uL cold lysis buffer, ice 10 min, triturate 10x through 25-gauge needle |
| Centrifugation | 16,000 rpm, 5 min, 4C |
| DNase treatment | 1.5 uL of 1U/uL DNase, 30 min on ice |
| Storage | -80C |

---

## HepG2 Preparation Details

| Step | Protocol |
|------|----------|
| Culture medium | EMEM + 10% FBS |
| Seeding density | 2e5/mL in T-75 flask (20 mL) |
| Expansion time | 3 days before transfection |
| Passage number | 6 |

---

## Random-End Library Construction

| Parameter | Value |
|-----------|-------|
| Backbone vector | pET28-IVT-Fixed-AgeI-EGFP-NheI (amplified to remove 25-nt defined prefix) |
| Assembly method | NEBuilder HiFi DNA Assembly Master Mix (NEB) |
| Reaction volume | 20 uL |
| Backbone amount | 200 ng |
| Primer amount | 10 pmol |
| 50-nt random primer | Bri036_T7_N50_ATG |
| 25-nt random primer | Bri043_T7_N25_ATG |

---

## Summary of Key Numbers

| Metric | Value |
|--------|-------|
| Total 5'UTR variants measured | ~204,803 (common across all replicates) |
| Cell types profiled | 3 (HEK293T, T cells, HepG2) |
| Cross-cell-type r2 range | 0.837-0.871 |
| Within-cell-type replicate r2 | 0.814-0.938 |
| Optimus 5-Prime r2 on HEK293T test set | 0.937 |
| TGFBR2 editing efficiency (best designs, K562) | > 40% |
| PDCD1 editing efficiency (best designs, K562) | > 80% |
| Best single design improvement over controls (TGFBR2) | Up to 50% higher |
| Random library percentile matched by designs | Top 0.02% |
| Reference count | 64 |

