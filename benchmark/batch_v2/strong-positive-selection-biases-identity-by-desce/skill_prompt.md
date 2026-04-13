Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: Nature Communications

## Idea Summary

## Working title
Strong Positive Selection Biases IBD-Based Inferences of Demography and Population Structure in Plasmodium falciparum

## Core question
How does strong positive selection from antimalarial drug resistance bias identity-by-descent (IBD)-based estimates of effective population size and population structure in P. falciparum, and can removing IBD peak regions correct this bias?

## Motivation / gap
- IBD is widely used for malaria genomic surveillance to estimate Ne and population structure, but selection bias is largely ignored
- P. falciparum has undergone multiple strong selective sweeps from antimalarial drug resistance
- Selection increases local IBD sharing and generates longer haplotype blocks, violating assumptions of IBD-based demographic estimators
- The interplay between high background relatedness (from declining Ne), positive selection, and low SNP density (high recombination) makes it difficult to disentangle selection effects
- No systematic evaluation of how selection affects IBD distributions in Pf populations had been conducted
- No correction strategy for selection bias in IBD-based analyses had been proposed

## Core contribution (bullet form)
- Analyzed WGS data from 2,055 P. falciparum isolates from eastern SEA (including 640 new genomes) plus West African validation dataset
- Demonstrated via simulation and empirical data that positive selection distorts IBD segment length distributions, shifting them toward longer segments
- Showed that selection-biased IBD leads to underestimated effective population size and blurred population structure
- Developed an IBD peak removal strategy that partially restores accuracy, with effectiveness dependent on background relatedness level
- Found that correction is most beneficial in high-transmission settings (West Africa) with low background relatedness, but less necessary in low-transmission/high-relatedness settings (SEA)
- 80% of SEA isolates were monoclonal (Fws > 0.95); 50.7% of WAF isolates were monoclonal

## Method in brief
WGS data from 2,055 eastern SEA P. falciparum isolates (751 sequenced in-house including 640 new, 1,304 from MalariaGEN Pf6) spanning 14 years and 18 provinces across Cambodia, Thailand, Laos, and Vietnam were analyzed. Population genetic simulations using simplified models with strong positive selection, decreasing Ne, and high recombination were designed as single-population (Ne estimation) and multi-population (structure inference) models. A five-deme stepping-stone model was used to test selection effects on IBD-based population structure inference.

IBD was inferred using both true IBD from simulations and empirical haplotype-based methods. An IBD peak removal strategy identified genomic regions with excess IBD sharing (corresponding to known drug resistance loci) and excluded those segments before downstream analyses. IBD-based Ne was estimated using IBDNe. Population structure was assessed via IBD network community detection. Validation was performed on a West African dataset from MalariaGEN Pf6.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log: Selection Bias in IBD-Based Pf Inference

## Dataset Summary - Southeast Asia

| Parameter | Value |
|-----------|-------|
| Total analyzable isolates (SEA) | 2,055 |
| New isolates (sequenced in-house) | 640 |
| Total in-house (new + prior) | 751 |
| MalariaGEN Pf6 (eastern SEA) | 1,304 |
| Countries | 4 (Cambodia, Thailand, Laos, Vietnam) |
| Provinces | 18 |
| Time span | 14 years |

## Sequencing Coverage Distribution (Fig 1b)

| Coverage Threshold | % Isolates with >80% Genome Covered |
|-------------------|-------------------------------------|
| >= 5x | 79.3% |
| >= 10x | 68.0% |
| >= 25x | 46.1% |

## Monoclonality Assessment (Fig 1c-d)

| Population | Monoclonal (Fws > 0.95) | Polyclonal |
|-----------|------------------------|------------|
| SEA | 80% | 20% |
| WAF | 50.7% | 49.3% |
| Polyclonal with predominant clone (SEA) | 44.3% of polyclonal | -- |

The higher polyclonal rate in West Africa is consistent with higher transmission intensity and multiplicity of infection.

## Simulation Design

### Single-Population Model (Ne Estimation)

| Parameter | Value |
|-----------|-------|
| Purpose | Test selection effect on IBD distribution and Ne |
| Selection strength | Strong positive selection |
| Ne trajectory | Decreasing |
| Recombination rate | High (matching Pf) |
| IBD method | True IBD (from simulation) |

### Multi-Population Model (Structure Inference)

| Parameter | Value |
|-----------|-------|
| Model type | One-dimensional stepping-stone |
| Number of subpopulations | 5 (p1-p5) |
| Migration | Symmetric between adjacent demes |
| Favored allele | Introduced from one side, spreads across chain |
| Purpose | Test selection effect on IBD-based structure |

## Effects of Selection on IBD Distribution (Fig 2)

### IBD Segment Length (Fig 2a)

| Condition | Effect |
|-----------|--------|
| Neutral | Shorter IBD segments, exponential-like distribution |
| Under selection | Shift toward longer IBD segments |
| Implication | Selection inflates IBD length, mimicking more recent shared ancestry |

### Total Pairwise IBD (Fig 2b)

| Condition | Effect |
|-----------|--------|
| Neutral | Lower total pairwise IBD |
| Under selection | Increased total pairwise IBD between isolates |

### IBD Location Along Chromosome (Fig 2c)

| Condition | Effect |
|-----------|--------|
| Neutral | Uniform IBD distribution along chromosome |
| Under selection | Peaks of IBD centered on selected locus |

## Effects on Ne Estimation (Fig 2)

| Condition | Ne Estimate |
|-----------|-------------|
| Neutral simulation | Accurate (matches true Ne) |
| Selection simulation | Underestimated Ne |
| After peak removal | Partially restored accuracy |

Selection shifts IBD segments to longer lengths, which IBDNe interprets as evidence for smaller/more recent Ne, leading to underestimation.

## Effects on Population Structure (Fig 3)

### Stepping-Stone Model Results (Fig 3a-c)

| Metric | Neutral | With Selection | After Peak Removal |
|--------|---------|---------------|-------------------|
| Pairwise genetic differentiation | Clear gradient (p1-p5) | Blurred gradient | Partially restored |
| Community detection | 5 distinct communities | Fewer/merged communities | Better resolution |
| IBD network structure | Matches true structure | Distorted | Improved |

Fig 3b: Frequency trajectory of favored alleles shows spread from deme p1 to p5 over time.
Fig 3c: Heatmap of pairwise genetic relatedness shows selection blurs the stepping-stone pattern.

## Empirical IBD Coverage Profile - SEA (Fig 4)

### All Isolates (Fig 4a)

| Observation | Detail |
|-------------|--------|
| IBD peaks | Centered on known drug resistance genes |
| Peak genes | kelch13, dhfr, dhps, mdr1, crt, plasmepsin |
| Sexual commitment gene | Also shows IBD peak (*) |
| Y-axis scale | Higher IBD proportions |

### Unrelated Isolates (Fig 4b)

| Observation | Detail |
|-------------|--------|
| IBD peaks | Still visible but reduced |
| Y-axis scale | Lower IBD proportions (different scale) |
| Interpretation | Drug resistance selection creates IBD peaks even among unrelated genomes |

## Ne and Structure in SEA Empirical Data (Fig 5)

### Ne Estimation (Fig 5a)

| Analysis | Ne Estimate |
|----------|-------------|
| Before IBD peak removal | Lower Ne estimate |
| After IBD peak removal | Slightly higher Ne estimate |
| Change significance | Not dramatic in SEA (high background relatedness) |

### IBD Network Communities (Fig 5b)

| Community | Size | Key Feature |
|-----------|------|-------------|
| Community 1 (largest) | Large | -- |
| Community 2 | Medium | -- |
| Community 3 | Medium | -- |
| Community 4 | Small | -- |
| Community 5 | Small | -- |

### Drug Resistance Mutations by Community (Fig 5c)

| Community | Resistance Pattern |
|-----------|-------------------|
| Varies by community | Different drug resistance allele frequencies |
| Interpretation | Communities partially defined by shared resistance haplotypes |

### Geographic Consistency (Fig 5d)

| Finding | Detail |
|---------|--------|
| Community assignment | Generally consistent with geographic origin |
| Before vs after peak removal | Minimal change in SEA |

## West African Validation (Fig 6)

### Ne Estimation (Fig 6a)

| Analysis | Ne Estimate |
|----------|-------------|
| Before IBD peak removal (blue) | Lower (underestimated) |
| After IBD peak removal (red, dotted) | Higher (more accurate) |
| Change | More pronounced than in SEA |

### Community Detection Before Peak Removal (Fig 6b)

| Finding | Detail |
|---------|--------|
| Dominant community | One large community absorbs most isolates |
| Resolution | Poor - structure blurred by selection |

### Community Detection After Peak Removal (Fig 6c)

| Finding | Detail |
|---------|--------|
| Community structure | Dominant community splits into smaller communities |
| Resolution | Improved - geographic structure better resolved |
| Communities shown | Only those with >= 20 isolates |

Key finding: Removing IBD peaks has a much larger effect in West Africa (high transmission, low background relatedness) than in SEA (low transmission, high background relatedness).

## Comparison: SEA vs West Africa

| Feature | SEA | West Africa |
|---------|-----|-------------|
| Transmission intensity | Low | High |
| Background genetic relatedness | High | Low |
| Monoclonal fraction | 80% | 50.7% |
| Effect of peak removal on Ne | Minimal | Substantial |
| Effect of peak removal on structure | Minimal | Substantial |
| Recommendation | Correction may not be necessary | Correction strongly recommended |

## Drug Resistance Loci Identified in IBD Peaks

| Gene | Drug Resistance | Chromosome |
|------|----------------|------------|
| kelch13 | Artemisinin | 13 |
| dhfr | Pyrimethamine | 4 |
| dhps | Sulfadoxine | 8 |
| mdr1 | Mefloquine/chloroquine | 5 |
| crt | Chloroquine | 7 |
| Plasmepsin 2/3 | Piperaquine | 14 |

## Key Figure Observations

- Fig 1a: Map showing sampling locations and collection years across SEA
- Fig 1b: Coverage distribution histograms at 5x, 10x, 25x thresholds
- Fig 1c: Bimodal Fws distribution with 80% monoclonal
- Fig 1d: Predominant genome ratio distribution for polyclonal isolates
- Fig 2a-c: Simulation demonstrates selection distorts IBD length, total sharing, and chromosomal distribution
- Fig 3: Stepping-stone model shows selection blurs population structure; peak removal partially restores it
- Fig 4: Empirical IBD coverage profiles show peaks at drug resistance loci
- Fig 5: SEA Ne and community structure minimally affected by peak removal
- Fig 6: West African Ne and community structure substantially improved by peak removal

## Statistical and Methodological Notes

| Method | Application |
|--------|-------------|
| IBDNe | Ne estimation from IBD segment length distribution |
| IBD network analysis | Community detection for population structure |
| Hierarchical clustering | Grouping IBD sharing matrices |
| dEploid | Deconvolution of polyclonal infections |
| Fws | Within-sample diversity for monoclonality assessment |
| True IBD (simulation) | Avoids IBD calling artifacts in simulation validation |
| MalariaGEN Pf6 | Source of publicly available genomes |

