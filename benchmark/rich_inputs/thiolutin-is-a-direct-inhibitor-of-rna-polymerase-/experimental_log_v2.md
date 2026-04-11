# Experimental Log

## 1. In Vitro Transcription -- Initial Attempts (Thiolutin Alone)

Purified 12-subunit yeast Pol II was tested for thiolutin sensitivity using a ssDNA template transcription assay with 32P-UTP labeling and 10% PAGE resolution.

### Table 1.1: Pol II Activity with Thiolutin Alone (ssDNA Template)

| Condition | Thiolutin (ug/mL) | DTT (equimolar) | Transcription Inhibition | Notes |
|---|---|---|---|---|
| No drug control | 0 | No | None | Normal RNA synthesis |
| Thiolutin only | 10 | No | None observed | No detectable inhibition |
| Thiolutin + DTT | 10 | Yes (1:1 molar) | None observed | DTT alone had no effect |
| Thiolutin only | 25 | No | None observed | Higher concentration also inactive |
| Thiolutin + DTT | 25 | Yes (1:1 molar) | None observed | Still no inhibition |

- Fig 1B: Representative gel shows equivalent RNA product bands across all thiolutin-treated and untreated lanes
- Experiments repeated at least 3 independent times with consistent results
- Conclusion: under standard buffer conditions without Mn2+, thiolutin (with or without equimolar DTT) fails to inhibit purified Pol II

---

## 2. Genetic Screens for Thiolutin Sensitivity Modifiers

Three independent screens were performed in S. cerevisiae to identify genes and pathways controlling thiolutin response.

### Table 2.1: Genetic Screen Parameters

| Screen Type | Library | Selection Condition | Method | Replicates |
|---|---|---|---|---|
| Forward genetics (UV mutagenesis) | WT strain CKY457, UV-mutagenized | 10 ug/mL thiolutin plates | Bulk segregant analysis + WGS | Multiple isolates |
| Manual Variomics | ~4000 gene-specific mutant pools on CEN plasmids | 10 ug/mL thiolutin plates | Colony picking, Sanger sequencing | Restruck for validation |
| HT Variomics Bar-seq (non-essential) | Haploid Variomics pool | SC-URA + 8 or 10 ug/mL thiolutin plates | Bar-seq (uptag + downtag) | 3 biological replicates |
| HT Variomics Bar-seq (essential) | Diploid Variomics pool | SC-URA + 8 or 10 ug/mL thiolutin plates | Bar-seq (uptag + downtag) | 3 biological replicates |
| HT Deletion Bar-seq (non-essential) | Haploid deletion pool | SC + 3 ug/mL thiolutin liquid, 20 gen | Bar-seq (uptag + downtag) | 3 biological replicates |
| HT Deletion Bar-seq (essential) | Diploid deletion pool | SC + 4 ug/mL thiolutin liquid, 20 gen | Bar-seq (uptag + downtag) | 3 biological replicates |

- For Variomics plate screens: 9 plates per replicate (6 x 10^7 cells/plate), grown 3 days, scraped, replated for additional 3 days on 9 new plates
- For deletion liquid screens: cultures diluted to 1 x 10^6 cells/mL every 5 generations to maintain log phase
- Fig S2: Uptag vs downtag fitness scores (log2 fold-change in relative abundance) showed excellent reproducibility; y=x dashed line, significantly resistant/sensitive mutants colored red
- 4683 deletion mutants' responses to 3356 compounds were used for hierarchical clustering; thiolutin clustered with specific compound signatures

### Table 2.2: Key Thiolutin-Resistant Mutants Identified

| Gene | Pathway | Screen Source | Allele Type | Dominance/Mechanism |
|---|---|---|---|---|
| YAP1 | Oxidative stress response / MDR | Forward genetics + manual Variomics | GOF (C-terminal cluster) | Dominant |
| YRR1 | MDR transcription factor | Forward genetics + manual Variomics | GOF | Dominant |
| SNQ2 | MDR efflux pump | Manual Variomics | GOF / overexpression | Dominant or dosage-dependent |
| TRR1 | Thioredoxin reductase (cytoplasmic) | Manual Variomics + HT Variomics | GOF or overexpression | Variomics resistant, deletion sensitive |
| TRX1 | Thioredoxin (cytoplasmic) | HT Variomics | GOF or overexpression | Variomics resistant, deletion neutral |
| PDR1 | MDR transcription factor | HT Deletion Bar-seq | LOF (deletion sensitive) | Major baseline MDR regulator |
| PDR5 | MDR efflux pump | HT Bar-seq | LOF deletion sensitive | Efflux transporter |

- Fig S1B-C: Forward genetics isolated thiolutin-resistant alleles of YAP1 and YRR1; Variomics identified SNQ2, TRR1 variants
- Fig S3: Recovered Variomics plasmids transformed into WT + empty vector (pRS416) control confirmed dominance or dosage dependence for MDR candidates
- Fig 2B: Comparison of Variomics vs deletion results -- MDR genes (YAP1, YRR1, SNQ2) showed resistance in Variomics but sensitivity or neutral effect upon deletion, consistent with GOF alleles

### Table 2.3: Key Thiolutin-Sensitive Deletion Mutants

| Gene Deletion | Pathway | Thiolutin Sensitivity | Holomycin Sensitivity |
|---|---|---|---|
| pdr1-delta | MDR transcription factor | Hypersensitive | Not tested as sensitive |
| snq2-delta | MDR efflux pump | Hypersensitive | Not sensitive |
| trr1-delta | Thioredoxin reductase | Hypersensitive | Not tested |
| sod1-delta | Cu-Zn superoxide dismutase | Hypersensitive | Not tested |
| zap1-delta | Zn2+ homeostasis TF | Hypersensitive | Hypersensitive |
| trx1-delta | Thioredoxin | Not sensitive | Not tested |
| trx2-delta | Thioredoxin | Not sensitive | Not tested |
| tsa1-delta | Thioredoxin peroxidase | Not sensitive | Not tested |

- Fig S1D: None of the tested MDR deletion mutants was thiolutin resistant; pdr1-delta and snq2-delta were hypersensitive
- Fig S4A: Same MDR deletion strains tested with holomycin showed no equivalent sensitivity, suggesting different cell permeability or efflux
- Fig S4B: OSR deletion mutants also did not show the same pattern of holomycin sensitivity as with thiolutin

---

## 3. Thioredoxin Pathway Genetic Dissection

### Table 3.1: Thioredoxin Mutant Thiolutin Sensitivity (Plate Growth Assays)

| Strain Genotype | Thiolutin Sensitivity | Interpretation |
|---|---|---|
| WT | Normal | Baseline |
| trr1-delta | Hypersensitive | Loss of thioredoxin reductase increases toxicity |
| trx1-delta | Normal (not sensitive) | Single thioredoxin deletion insufficient |
| trx2-delta | Normal (not sensitive) | Single thioredoxin deletion insufficient |
| trx1-delta trx2-delta | Resistant | Double deletion confers resistance |
| trr1-delta trx1-delta trx2-delta | Suppressed (resistance restored) | trx1/2 deletion suppresses trr1-delta hypersensitivity |

- Fig S1G: Serial dilution plate growth assays confirm these epistasis relationships
- Key interpretation: trr1-delta hypersensitivity is due to accumulation of oxidized thioredoxins, not loss of direct Trr1 anti-thiolutin activity
- Oxidized Trx1/Trx2 appear to be required for thiolutin toxicity in vivo; removing them (double deletion) confers resistance
- This genetic evidence supports a model where thiolutin oxidizes thioredoxins (or thioredoxins reduce thiolutin, becoming oxidized in the process)

---

## 4. Oxidative Stress Induction by Thiolutin

### 4.1 Yap1 Nuclear Relocalization

Yap1-EGFP fusion strain was treated and imaged by fluorescence microscopy. Yap1 is a redox-sensitive transcription factor that accumulates in the nucleus upon oxidation.

### Table 4.1: Yap1 Nuclear Localization Conditions

| Treatment | Concentration | Nuclear Localization | Time Course |
|---|---|---|---|
| DMSO (vehicle control) | 1% | Cytoplasmic (no relocalization) | Monitored at multiple time points |
| Thiolutin | 10 ug/mL | Strong nuclear accumulation | Rapid, sustained signal |
| Holomycin | 10 ug/mL | Nuclear accumulation | Similar kinetics to thiolutin |
| H2O2 (positive control) | 0.4 mM | Strong nuclear accumulation | Rapid response |

- Fig S5A: Representative fluorescence images at indicated time points after treatment
- Fig S5B: Quantification of nuclear/cytoplasmic EGFP signal ratio for individual cells after 10 ug/mL thiolutin treatment shows significant increase over DMSO control
- Both thiolutin and holomycin induce Yap1 nuclear localization comparable to peroxide, consistent with induction of oxidative stress

### 4.2 Glutathione Depletion

Growing WT yeast cultures were washed and treated with indicated conditions at 30 degrees C for 1 hour, then assayed for reduced glutathione (GSH) and total glutathione.

### Table 4.2: Glutathione Measurements After Thiolutin Treatment

| Condition | Reduced GSH (relative) | Total Glutathione (relative) | Oxidized GSSG (calculated) | Significance |
|---|---|---|---|---|
| DMSO control | Baseline | Baseline | Baseline | -- |
| Thiolutin (10 ug/mL) | Decreased | Depleted | Increased | p <= 0.01 (two-tailed paired t-test) |

- Fig S6A: Three independent replicates performed; error bars represent standard deviation of the mean
- Thiolutin significantly depletes total glutathione in vivo, supporting redox cycling as a partial mechanism for oxidative stress induction
- Fig S6B: Thiolutin can be reduced by DTT and subsequently reoxidized, consistent with redox cycling capacity

---

## 5. Metal Homeostasis and Thiolutin Sensitivity

### Table 5.1: Metal-Related Genetic Interactions

| Gene / Condition | Metal Pathway | Thiolutin Effect | Holomycin Effect | Other Drug Effects |
|---|---|---|---|---|
| zap1-delta | Zn2+ homeostasis TF | Hypersensitive | Hypersensitive | Not sensitive to H2O2 |
| zap1-delta + Mn2+ | Mn2+ supplementation | Not tested | Not tested | zap1-delta does not confer Mn2+ sensitivity |
| WT + Zn2+ supplement | Zn2+ addition | Partially suppresses thiolutin sensitivity | -- | -- |
| Mn-related mutants | Mn2+ transport/homeostasis | Identified in Bar-seq screens | -- | -- |
| Cu-related mutants | Cu2+ homeostasis | Identified in Bar-seq screens | -- | -- |

- Fig S8A: zap1-delta is hypersensitive to holomycin but not to H2O2, separating Zn2+ chelation from general oxidative stress
- Fig S8B: zap1-delta does not confer sensitivity to Mn2+, indicating specificity
- Fig S8C: Zn2+ supplementation partially suppresses thiolutin sensitivity, consistent with Zn2+ chelation contributing to but not fully explaining thiolutin toxicity
- Fig S7: Validation of several statistically significant resistant/sensitive mutants reconstructed in haploid BY4741 or diploid BY4743 backgrounds; mid-log growth at 30 degrees C measured by Tecan plate reader; 3 independent repeats, error bars = SD
- Failed to validate slight sensitivity in ERV1/erv1-delta and MIA40/mia40-delta strains that were statistically significant in Bar-seq

### Table 5.2: Doubling Time Measurements for Metal Mutants (Tecan Plate Reader)

| Strain | Condition | Relative Doubling Time | Replicates | Error (SD) |
|---|---|---|---|---|
| WT | SC | Baseline | 3 | Reported |
| WT | SC + thiolutin | Increased | 3 | Reported |
| zap1-delta | SC | Normal | 3 | Reported |
| zap1-delta | SC + thiolutin | Strongly increased (hypersensitive) | 3 | Reported |
| WT | SC + Zn2+ supplement + thiolutin | Partially rescued | 3 | Reported |

- Doubling times derived from growth curves measured by Tecan plate reader
- Three independent repeats performed for each strain/condition
- Error bars represent standard deviation of the mean

---

## 6. Thiolutin + Mn2+ + DTT: Direct Pol II Inhibition In Vitro

The critical discovery: combining thiolutin with both a reductant (DTT) and Mn2+ enables direct Pol II inhibition.

### Table 6.1: Cofactor Requirements for Pol II Inhibition

| Thiolutin | DTT | Mn2+ (MnCl2) | Pol II Transcription | Result |
|---|---|---|---|---|
| No | No | No | Active | Baseline control |
| Yes | No | No | Active | No inhibition (replicates Fig 1) |
| Yes | Yes | No | Active | DTT alone insufficient |
| Yes | No | Yes | Active | Mn2+ alone insufficient |
| Yes | Yes | Yes | Inhibited | All three components required |
| No | Yes | Yes | Active | DTT + Mn2+ without thiolutin has no effect |
| No | No | Yes | Active | Mn2+ alone has no effect |
| No | Yes | No | Active | DTT alone has no effect |

- Fig 4: Key experiment demonstrating the three-component requirement
- Inhibition observed specifically at the initiation step
- This resolves the conflict between classic studies (which used partially purified fractions likely containing Mn2+) and recent negative results (which used purified Pol II without Mn2+)

### Table 6.2: Effect of Excess DTT on Thiolutin/Mn2+ Inhibition

| Thiolutin (ug/mL) | DTT Concentration | MnCl2 | Pol II Activity | Notes |
|---|---|---|---|---|
| 10 | Equimolar (1:1) | Present | Inhibited | Standard inhibition |
| 10 | 2x molar excess | Present | Inhibited | Still inhibitory |
| 10 | 5x molar excess | Present | Partially active | Inhibition weakened |
| 10 | Large excess (mM range) | Present | Active (no inhibition) | Excess DTT abrogates inhibition |

- Excess DTT abrogates thiolutin inhibitory activity, suggesting that over-reduction destroys the active species
- This is consistent with a model where a specific partially reduced form of thiolutin (not fully reduced) is the active inhibitor
- Practical implication: standard in vitro transcription buffers containing mM DTT would mask thiolutin activity

### Table 6.3: Order of Addition Experiments

| Order of Addition | Pol II Inhibition | Interpretation |
|---|---|---|
| Thiolutin/Mn2+/DTT added before template DNA, then add DNA | Strong inhibition | Active species must bind free Pol II |
| Template DNA added first, then thiolutin/Mn2+/DTT | Reduced or no inhibition | Cannot inhibit pre-formed Pol II-DNA complex |
| Pol II + DNA preincubated, then thiolutin added | No inhibition | Confirms requirement for free Pol II |

- Critical order: thiolutin must contact Pol II before template DNA binding
- This behavior is stereotypical of RNAP clamp inhibitors (analogous to myxopyronin, corallopyronin, ripostatin class in E. coli)
- Distinct from active site inhibitors, NTP uptake channel blockers, or RNA exit channel inhibitors which can act on elongating complexes

---

## 7. Elongation Assay on Bubble Template

A transcription bubble template (pre-melted DNA that bypasses the initiation requirement) was used to test whether thiolutin affects elongation when the initiation block is circumvented.

### Table 7.1: Bubble Template Elongation Results

| Template Type | Thiolutin/Mn2+/DTT | Transcription Outcome | Observations |
|---|---|---|---|
| Normal dsDNA | Yes | Inhibited (no initiation) | Confirms initiation block |
| Bubble template | No | Normal elongation | Control |
| Bubble template | Yes | Pause-prone, defective elongation | Partial read-through with pausing |

- Thiolutin inhibits initiation on normal templates but shows defective/pause-prone elongation on bubble templates
- This distinguishes thiolutin from myxopyronin/corallopyronin/ripostatin (Myx/Cor/Rip), which do not inhibit elongation on bubble templates
- Possible similarity to lipiarmycin (Lpm), which locks the clamp in a partially/fully open state, but Lpm has never been tested on bubble templates
- The exact thiolutin binding site on Pol II remains unclear; data cannot exclude inhibition of regions other than clamp-controlling switch regions

---

## 8. Genome-Wide Pol II Occupancy Changes (ChIP-seq)

Pol II ChIP-seq was performed after thiolutin treatment to assess genome-wide transcriptional effects in vivo.

### Table 8.1: Major Categories of Pol II Occupancy Changes

| Gene Category | Direction of Change | Magnitude | Consistency with Known Pathways |
|---|---|---|---|
| Ribosomal protein genes | Decreased occupancy | Major effect | Consistent with Tor pathway inhibition |
| Stress-responsive genes | Increased occupancy | Significant | Consistent with stress induction (ESR) |
| Highly transcribed genes (general) | Decreased occupancy | Widespread | Tor pathway downstream targets |
| Housekeeping genes | Variable | Minor to moderate | Mixed effects |

- Widespread Pol II occupancy changes observed across the genome
- Major effects are consistent with prior observations for Tor pathway inhibition and general stress induction
- These patterns suggest that in vivo thiolutin effects on transcription are largely indirect (via signaling pathway perturbation) rather than direct Pol II targeting
- Conclusion: thiolutin use in vivo should be restricted to studying its own mechanisms, not as a general transcription inhibitor tool

---

## 9. Holomycin Comparison

### Table 9.1: Thiolutin vs Holomycin Cellular Effects

| Property | Thiolutin | Holomycin |
|---|---|---|
| Structure | Dithiolopyrrolone with intramolecular disulfide | Closely related dithiolopyrrolone |
| Yeast growth inhibition at low concentration | Yes | No (fails to inhibit at low doses) |
| MDR mutant sensitivity profile | pdr1-delta and snq2-delta hypersensitive | Not sensitive in same MDR deletion strains |
| OSR mutant sensitivity profile | sod1-delta hypersensitive | Different pattern from thiolutin |
| Yap1 nuclear localization induction | Yes (10 ug/mL) | Yes (10 ug/mL) |
| zap1-delta sensitivity | Hypersensitive | Hypersensitive |
| Zn2+ chelation (in vitro, reduced form) | Yes | Yes |
| Redox cycling capacity | Supported by genetic/biochemical data | Demonstrated (spontaneous reoxidation by O2) |

- Fig S4: MDR and OSR deletion mutants do not show equivalent holomycin hypersensitivity compared to thiolutin
- Different cell permeability and/or efflux pump specificity may explain the divergent sensitivity profiles
- Both compounds share Zn2+ chelation and redox properties but differ in cellular uptake/efflux dynamics

---

## 10. Proteasome Connection

- Proteasome-related mutants were identified in high-throughput screens as modifiers of thiolutin sensitivity
- Consistent with previous reports that thiolutin inhibits proteasome activity, likely through Zn2+ chelation of Zn2+-dependent metallopeptidases
- Fig S6 references: proteasome involvement in thiolutin resistance

---

## 11. Hierarchical Clustering of Chemical-Genetic Profiles

- 4683 deletion mutants' fitness responses to 3356 compounds were clustered
- Thiolutin clustered with a specific set of compounds, shown in Fig 2 inset
- This chemical-genetic profile provides an unbiased view of thiolutin's mode of action in the context of thousands of bioactive compounds

---

## 12. Proposed Unified Model

Based on all genetic and biochemical data, the following model emerges:

### Table 12.1: Thiolutin Mode of Action -- Pathway Summary

| Step | Process | Evidence Type | Key Experiments |
|---|---|---|---|
| 1 | Thiolutin enters cell (subject to MDR efflux by Pdr1/Snq2) | Genetic | pdr1-delta, snq2-delta hypersensitivity |
| 2 | Intramolecular disulfide reduced by thioredoxins (Trx1/Trx2) and/or glutathione | Genetic + biochemical | trx1-delta trx2-delta resistance; glutathione depletion |
| 3a | Reduced thiolutin chelates Zn2+ | Biochemical (prior work) | zap1-delta sensitivity; Zn2+ supplementation rescue |
| 3b | Reduced thiolutin chelates Mn2+ and Cu2+ | Genetic | Metal homeostasis mutants in screens |
| 3c | Thiolutin redox cycling generates ROS | Genetic + biochemical | sod1-delta sensitivity; Yap1 relocalization; GSH depletion |
| 4 | Thio/Mn2+/reductant complex directly inhibits Pol II initiation | Biochemical | In vitro transcription with purified Pol II |
| 5 | In vivo, Tor pathway inhibition and stress responses dominate transcriptional changes | Genomic | Pol II ChIP-seq patterns |

---

## 13. Key Reagents and Resources

### Table 13.1: Chemicals and Sources

| Reagent | Supplier | Use |
|---|---|---|
| Thiolutin | Cayman Chemical | Primary compound under study |
| DTT | Gold Biotechnology | Reductant for in vitro assays |
| TCEP | Gold Biotechnology | Alternative reductant |
| 5-FOA | Gold Biotechnology | Plasmid counterselection |
| MnCl2 | Sigma | Mn2+ source for in vitro transcription |
| ZnCl2 | JT Baker | Zn2+ supplementation experiments |
| MgCl2 | BDH Chemicals | Buffer component |

### Table 13.2: Key Strains

| Strain | Background | Use |
|---|---|---|
| CKY457 | WT S. cerevisiae | UV mutagenesis base strain; Variomics plasmid host |
| BY4741 | Haploid S288C derivative | Deletion library reconstruction/validation |
| BY4743 | Diploid S288C derivative | Essential gene deletion library |
| Yap1-EGFP | Tagged endogenous YAP1 | Fluorescence relocalization assay |
| Various deletion strains | BY4741/BY4743 | Individual gene function testing |

---

## 14. Statistical Methods and Reproducibility

| Assay | Replicates | Statistical Test | Threshold |
|---|---|---|---|
| In vitro transcription | >= 3 independent experiments | Representative gels shown | Qualitative (gel imaging) |
| Bar-seq screens | 3 biological replicates | Log2 fold-change; significance by uptag/downtag concordance | Colored red = significant in both tags |
| Glutathione measurement | 3 independent replicates | Two-tailed paired t-test | p <= 0.01 |
| Growth curves (Tecan) | 3 independent repeats | Mean +/- SD | Visual comparison of doubling times |
| Yap1 relocalization | Multiple cells quantified | Nuclear/cytoplasmic ratio | Quantified per cell |

---

## 15. Key Figure Observations Summary

- Fig 1A: Structures of thiolutin and holomycin showing the intramolecular disulfide bond
- Fig 1B: Gel image showing no Pol II inhibition by thiolutin +/- equimolar DTT on ssDNA template
- Fig 2A: Schematic of 4 library types used for high-throughput screening
- Fig 2B: Comparison showing different resistant/sensitive gene sets between Variomics (GOF+LOF) and deletion (LOF only) libraries
- Fig S1A: Schematic of forward genetics (UV mutagenesis + WGS) and Variomics screening workflows
- Fig S1B-E: MDR pathway mutant characterization
- Fig S1F-G: Thioredoxin pathway mutant epistasis
- Fig S2: Uptag vs downtag correlation plots demonstrating Bar-seq reproducibility
- Fig S3: Dominance testing of MDR Variomics candidates vs empty vector control
- Fig S4: Holomycin sensitivity profiles differ from thiolutin for MDR and OSR mutants
- Fig S5A-B: Yap1-EGFP nuclear relocalization quantification after thiolutin/holomycin/H2O2
- Fig S6A: Glutathione depletion by thiolutin (3 replicates, p <= 0.01)
- Fig S6B: DTT reduces thiolutin, which can be reoxidized (redox cycling evidence)
- Fig S7: Tecan plate reader validation of Bar-seq hits; ERV1 and MIA40 sensitivity not validated
- Fig S8A-C: zap1-delta sensitivity to thiolutin/holomycin; Zn2+ supplementation rescue
- Fig 4 (referenced in discussion): Three-component (thiolutin + DTT + Mn2+) Pol II inhibition demonstration

---

## 16. Reference Count and Scope

- Total references cited: 109
- Covers literature on dithiolopyrrolone chemistry, RNAP clamp inhibitors (myxopyronin, corallopyronin, ripostatin, lipiarmycin), yeast MDR and OSR pathways, metal homeostasis, Tor signaling, thioredoxin biology, mRNA stability methods, and chemical-genetic profiling approaches
