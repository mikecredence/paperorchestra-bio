Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title

Chronic chemogenetic activation of negative memory engrams in the ventral hippocampus produces lasting anxiety, cognitive deficits, and neuroinflammatory changes in mice

## Core question

Does repeated reactivation of neurons encoding a negative memory (a "negative engram") in the ventral hippocampus produce chronic-stress-like behavioral and cellular pathology in mice, and do these effects differ between young and aged animals?

## Motivation / gap

- Chronic stress is a major risk factor for neuropsychiatric disorders (MDD, GAD, PTSD), but it is unclear whether the repeated internal reactivation of a negative memory alone can recapitulate the effects of chronic external stressors
- Previous work showed that acute reactivation of negative engrams modulates social avoidance and fear responses, but no study has examined the consequences of chronic stimulation over months
- Positive and negative memory engrams in vHPC are molecularly distinct, yet the specific inflammatory gene signatures of these engrams have not been characterized via RNA-seq and GSEA
- Young and aged brains respond differently to stress, but age-dependent vulnerability to chronic negative-engram activation has not been tested
- The glial consequences (microglia and astrocyte morphology/number) of chronic memory reactivation are unknown

## Core contribution (bullet form)

- RNA-seq with GSEA showed that negative vHPC engram cells upregulate pro-inflammatory genes (Spp1, Ttr, C1qb), while positive engram cells upregulate anti-inflammatory genes
- Three months of chemogenetic (hM3Dq/CNO) activation of negative engrams in vHPC increased anxiety-like behavior in both 6-month and 14-month-old TRAP2 mice (reduced center time in open field, reduced open-arm time in zero maze)
- Chronic negative-engram activation reduced spatial working memory (Y-maze) specifically in 14-month-old mice
- Fear extinction was impaired in 6-month-old hM3Dq mice, and fear generalization was heightened in both age groups
- Immunohistochemistry revealed significant changes in Iba1+ microglial and GFAP+ astrocytic number and morphology (ramification index, territory volume, branch length, endpoints) in hippocampal subregions
- Chronic stimulation did not cause neuronal death (NeuN counts unchanged in subiculum, vDG, vCA1)

## Method in brief

The study used TRAP2 (Targeted Recombination in Active Populations) transgenic mice to permanently tag neurons active during contextual fear conditioning with Cre-dependent hM3Dq-mCherry (excitatory DREADD) or mCherry control in the ventral hippocampus. Young (3-month) and old (11-month) cohorts received bilateral vHPC injections of AAV9-hSyn-DIO-hM3Dq-mCherry or control virus. After viral expression, mice underwent CFC and received 4-OHT to label the negative engram. Over the subsequent three months, mice received intraperitoneal CNO injections (either daily or on a periodic schedule) to chronically reactivate the tagged negative-memory ensemble.

Following the stimulation period (mice now 6 or 14 months old), a battery of behavioral tests was conducted: open field test and zero maze for anxiety, Y-maze for spatial working memory, contextual fear conditioning with extinction sessions, and fear generalization in a novel context. Molecular characterization included RNA-sequencing of FACS-sorted eYFP+ engram cells from a separate cohort (using an activity-dependent cfos-tTA/TRE-eYFP dual-virus system), GSEA on curated pro- and anti-inflammatory gene sets, and immunohistochemistry for Iba1 (microglia) and GFAP (astrocytes) with 3DMorph-based morphological analysis, plus NeuN staining to assess neuronal survival.

## Target venue

eLife


## Experimental Log

# Experimental Log: Chronic Activation of a Negative Engram Induces Behavioral and Cellular Abnormalities

## 1. Experimental Design Overview

| Parameter | Detail |
|---|---|
| Mouse line | TRAP2 (Targeted Recombination in Active Populations 2) |
| Background strain | C57BL/6J (for RNA-seq); TRAP2 (for behavior/IHC) |
| Young cohort age at surgery | 3 months |
| Old cohort age at surgery | 11 months |
| Age at behavioral testing | 6 months (young) and 14 months (old) |
| Stimulation duration | 3 months |
| Virus (experimental) | AAV9-hSyn-DIO-hM3Dq-mCherry |
| Virus (control) | AAV9-hSyn-DIO-mCherry |
| Injection target | Bilateral ventral hippocampus (vHPC) |
| Engram labeling trigger | Contextual fear conditioning + 4-OHT injection |
| Chronic activation agent | Clozapine N-oxide (CNO), intraperitoneal |

## 2. RNA-Sequencing Experiment (Figure 1)

### 2.1 Viral strategy for engram labeling (separate cohort)

| Component | Detail |
|---|---|
| Virus 1 | AAV9-c-Fos-tTA |
| Virus 2 | AAV9-TRE-eYFP |
| Injection ratio | 1:1 cocktail |
| Target | Bilateral vHPC |
| Labeling control | Doxycycline (DOX) diet to inhibit tTA-TRE binding |
| DOX removal | Day 10 post-surgery (opens tagging window) |
| Behavioral experience | Day 11: CFC (negative) or male-to-female interaction (positive) |
| DOX reinstatement | Immediately after experience (closes tagging window) |
| Sacrifice | 24 hours after behavioral experience |
| Cell isolation | FACS sorting of eYFP+ cells |

### 2.2 GSEA Results

| Gene Set | Enrichment in Negative Engram | Enrichment in Positive Engram |
|---|---|---|
| Anti-inflammatory genes | Lower expression vs. untagged | Higher expression vs. untagged (enriched) |
| Pro-inflammatory genes | Higher expression vs. untagged (enriched) | Lower expression vs. untagged |

### 2.3 Notable Differentially Expressed Genes in Negative Engram

| Gene | Full Name | Function |
|---|---|---|
| Spp1 | Secreted phosphoprotein 1 (osteopontin) | Extracellular matrix protein in immune cells; mediates inflammatory responses; upregulated after chronic social stress |
| Ttr | Transthyretin | Serum transporter for thyroid hormones; detrimental when misfolded; increased after acute/chronic stress |
| C1qb | Complement C1q B chain | Involved in complement-mediated inflammatory processes and oxidative stress |

Fig 1d: GSEA enrichment score plot shows anti-inflammatory gene set enriched in positive vs. untagged cells, not in negative vs. untagged cells.
Fig 1f: GSEA enrichment score plot shows pro-inflammatory gene set enriched in negative vs. untagged cells, not in positive vs. untagged cells.

## 3. Behavioral Timeline (Figure 2)

| Step | Timepoint | Event |
|---|---|---|
| 1 | Day 0 | Bilateral vHPC virus injection (hM3Dq or mCherry) |
| 2 | ~2 weeks | Viral expression and surgical recovery |
| 3 | Post-recovery | CFC session to create negative memory |
| 4 | Post-CFC | 4-OHT IP injection to permanently tag active neurons |
| 5 | Months 1-3 | Chronic CNO injections to reactivate negative engram |
| 6 | After 3 months | Behavioral battery begins |

## 4. Anxiety-Related Behavioral Tests (Figure 3)

### 4.1 Open Field Test

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Total distance traveled | Baseline | No significant change | Baseline | No significant change | Two-way ANOVA |
| Time in center (s) | Baseline | Decreased | Baseline | Decreased | Two-way ANOVA + Tukey |
| Center entries | Baseline | Decreased | Baseline | Decreased | Two-way ANOVA + Tukey |
| Average speed | Baseline | No significant change | Baseline | No significant change | Two-way ANOVA |

Fig 3a: Open field results showing hM3Dq mice in both age groups spent less time in center and made fewer center entries, indicating elevated anxiety. Locomotor activity (distance, speed) was not affected, ruling out motor confounds.

### 4.2 Zero Maze Test

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Total distance traveled | Baseline | No significant change | Baseline | No significant change | Two-way ANOVA |
| Time in open arms (s) | Baseline | Decreased | Baseline | Decreased | Two-way ANOVA + Tukey |
| Open arm entries | Baseline | Decreased | Baseline | Decreased | Two-way ANOVA + Tukey |
| Average speed | Baseline | No significant change | Baseline | No significant change | Two-way ANOVA |

Fig 3b: Zero maze results confirmed anxiety phenotype -- hM3Dq groups spent less time in open arms and entered open areas fewer times, without changes in overall locomotion.

### 4.3 Y-Maze (Spatial Working Memory)

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Spontaneous alternation (%) | ~50% | ~50% (no change) | ~50% | Decreased (impaired) | Two-way ANOVA + Tukey |
| Total arm entries | No change | No change | No change | No change | Two-way ANOVA |

Fig 3c: Y-maze results showing spatial working memory impairment (reduced alternation %) only in 14-month-old hM3Dq mice, suggesting age-dependent vulnerability.

## 5. Fear Memory Tests (Figure 4)

### 5.1 Contextual Fear Conditioning (Initial CFC Session)

| Parameter | Value |
|---|---|
| Context | Context A |
| Number of foot shocks | 4 |
| Shock intensity | 1.5 mA |
| Shock duration | 2 seconds |
| Session duration | 300 seconds |
| Engram tagging | IP injection of 4-OHT immediately after CFC |

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Average % freezing (CFC) | Comparable | Comparable | Comparable | Comparable | Two-way ANOVA RM |
| Total % freezing (CFC) | Comparable | Comparable | Comparable | Comparable | Two-way ANOVA RM |

Fig 4a-iii: No significant difference between groups during initial CFC, confirming equivalent fear acquisition prior to chronic stimulation.

### 5.2 Fear Extinction

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Freezing across extinction sessions | Decreased over sessions | Impaired extinction (higher freezing) | Decreased over sessions | Similar to mCherry | Two-way ANOVA RM + Tukey |

Fig 4b: Young (6-month) hM3Dq mice showed impaired fear extinction relative to mCherry controls, maintaining elevated freezing levels across extinction sessions.
Fig 4b: Old (14-month) hM3Dq mice did not show a statistically significant extinction impairment compared to mCherry controls.

### 5.3 Fear Generalization

| Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Freezing in novel context | Low | Elevated (generalized fear) | Low | Elevated (generalized fear) | Two-way ANOVA + Tukey |

Fig 4c: Both young and old hM3Dq mice showed heightened freezing in a novel context that was never paired with shock, indicating fear generalization across both age groups.

## 6. Summary of Behavioral Effects by Age and Group

| Behavioral Domain | 6mo hM3Dq vs mCherry | 14mo hM3Dq vs mCherry |
|---|---|---|
| Anxiety (OFT center time) | Increased anxiety | Increased anxiety |
| Anxiety (zero maze open arms) | Increased anxiety | Increased anxiety |
| Spatial working memory (Y-maze) | No impairment | Impaired |
| Fear extinction | Impaired | Not significantly impaired |
| Fear generalization | Heightened | Heightened |
| Locomotor activity | No change | No change |

## 7. Microglial Analysis (Figure 5a-j)

### 7.1 Iba1+ Cell Counts

| Region / Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Number of Iba1+ cells | Baseline | Changed | Baseline | Changed | Two-way ANOVA + Tukey |

Fig 5c: Number of Iba1+ microglia was altered by chronic negative engram stimulation in hippocampus.

### 7.2 Microglial Morphology (3DMorph Analysis)

| Morphological Parameter | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Ramification index | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Cell territory volume | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Average centroid distance | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Number of endpoints | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Average branch length | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Number of branch points | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Longest branch length | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |

Fig 5d-j: Multiple morphological parameters of Iba1+ microglia were significantly altered by chronic negative engram stimulation. Changes are consistent with a shift toward a more activated/reactive microglial phenotype.

## 8. Astrocyte Analysis (Figure 5k-q)

### 8.1 GFAP+ Cell Counts

| Region / Measure | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Number of GFAP+ cells | Baseline | Changed | Baseline | Changed | Two-way ANOVA + Tukey |

### 8.2 Astrocyte Morphology (3DMorph Analysis)

| Morphological Parameter | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Statistical Test |
|---|---|---|---|---|---|
| Ramification index | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Cell territory volume | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Average centroid distance | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Number of endpoints | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Average branch length | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Number of branch points | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |
| Longest branch length | Baseline | Altered | Baseline | Altered | Two-way ANOVA + Tukey |

Fig 5k-q: GFAP+ astrocytes showed significant morphological changes paralleling microglial alterations following chronic negative engram activation.

## 9. Neuronal Survival (Supplemental Figure 1)

| Region | 6mo mCherry | 6mo hM3Dq | 14mo mCherry | 14mo hM3Dq | Significance |
|---|---|---|---|---|---|
| Subiculum (NeuN+ cells) | Baseline | No change | Baseline | No change | Not significant |
| vDG (NeuN+ cells) | Baseline | No change | Baseline | No change | Not significant |
| vCA1 (NeuN+ cells) | Baseline | No change | Baseline | No change | Not significant |

- Statistical analysis: Two-way ANOVA with Tukey post-hoc
- Sample size: n = 3 mice/group x 18 single tile ROIs per brain region
- Chronic stimulation did not induce detectable neuronal death in any hippocampal subregion

## 10. Statistical Methods Summary

| Analysis | Test Used | Post-hoc | Notes |
|---|---|---|---|
| Behavioral comparisons (2 factors: age x treatment) | Two-way ANOVA | Tukey's multiple comparisons | Used for OFT, zero maze, Y-maze, generalization |
| Repeated-measures behavioral data (freezing over time) | Two-way ANOVA RM | Tukey's post-hoc | Used for CFC acquisition, extinction curves |
| Cell counts (NeuN, Iba1, GFAP) | Two-way ANOVA | Tukey's post-hoc | n = 3 mice/group |
| Morphological parameters | Two-way ANOVA | Tukey's post-hoc | 3DMorph-based quantification |
| RNA-seq / GSEA | Gene Set Enrichment Analysis | -- | A priori curated gene sets for pro/anti-inflammatory pathways |

## 11. Key Experimental Parameters

| Parameter | Value |
|---|---|
| CFC shock intensity | 1.5 mA |
| CFC shock duration | 2 seconds |
| CFC number of shocks | 4 |
| CFC session length | 300 seconds |
| 4-OHT route | Intraperitoneal injection |
| Chronic stimulation duration | 3 months |
| Stimulation agent | CNO (clozapine N-oxide) |
| IHC markers | Iba1 (microglia), GFAP (astrocytes), NeuN (neurons) |
| Morphology software | 3DMorph (MATLAB-based) |
| RNA-seq cell isolation | FACS of eYFP+ cells |
| Viral system for RNA-seq | AAV9-c-Fos-tTA + AAV9-TRE-eYFP |
| Viral system for DREADD | AAV9-hSyn-DIO-hM3Dq-mCherry |
| Mouse line for behavior | TRAP2 |
| Mouse line for RNA-seq | C57BL/6J |
| Reference count | 91 |

## 12. Figure Summary

- Fig 1: GSEA of RNA-seq data comparing positive and negative vHPC engrams; negative engrams enriched for pro-inflammatory genes, positive for anti-inflammatory genes
- Fig 2: Experimental timeline schematic for TRAP2 chronic stimulation paradigm across young and old cohorts
- Fig 3: Behavioral results for anxiety (OFT, zero maze) and spatial working memory (Y-maze) after 3 months of chronic stimulation
- Fig 4: Fear conditioning, extinction, and generalization results showing impaired extinction (young) and heightened generalization (both ages)
- Fig 5: Microglial and astrocytic number and morphology changes in hippocampus after chronic negative engram activation
- Supp Fig 1: NeuN+ cell counts confirming no neuronal death from chronic stimulation
- Supp Fig 2: Representative 3DMorph images for GFAP+ astrocytes and Iba1+ microglia across all groups

