Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

# Idea Summary

## Working title
Emotional vocalizations alter behaviors and neurochemical release into the amygdala

## Core question
Do emotionally charged social vocalizations (mating vs. restraint) elicit distinct patterns of neuromodulator release (acetylcholine and dopamine) into the basolateral amygdala, and do these patterns depend on the listener's sex, hormonal state, and prior behavioral experience?

## Motivation / gap
- The BLA integrates auditory input with contextual and internal-state information to shape behavioral responses, but how neuromodulatory signals contribute to vocal processing is poorly understood
- Prior work demonstrated roles for DA and ACh in vocalization production, but their contribution to processing/interpreting social vocalizations remains unclear
- Internal state signals (sex, estrous stage, prior experience) are known to influence amygdala processing, yet the neurochemical mechanisms by which these factors modulate vocal communication have not been mapped
- The relationship between specific neuromodulator release patterns and behavioral responses to affective vocalizations has not been directly measured with microdialysis during vocal playback
- It is unknown whether a single prior experience with behaviors associated with vocalizations is sufficient to establish neurochemical response patterns

## Core contribution (bullet form)
- Showed that playback of restraint vocalizations increased ACh and decreased DA release in male mouse BLA, while mating vocalizations evoked the opposite pattern
- Demonstrated sex- and hormonal-state-dependent modulation: non-estrus females showed male-like patterns to mating playback, while estrus females showed increased both ACh and DA
- Found that experimental groups with increased ACh release showed the largest increases in aversive flinching behavior, suggesting a mechanistic link
- Established that a single 90-min experience with mating and restraint behaviors is sufficient to produce consistent neurochemical response patterns -- inexperienced mice showed no distinct patterns
- 5-HIAA (serotonin metabolite) did not show context-dependent changes, indicating specificity of the ACh/DA findings
- Proposed a model in which ACh and DA provide context-dependent information to BLA neurons that modulate output to downstream regions controlling behavioral responses

## Method in brief
Adult CBA/CaJ mice (n=83 total, p90-p180, both sexes) underwent a 6-day experimental protocol. On Days 1 and 2, each mouse experienced one bout each of mating behavior (high-intensity interactions including mounting) and sustained restraint (90 min each, counterbalanced order). After the Day 2 experience, a microdialysis guide tube was implanted above the BLA. On Day 6, a microdialysis probe was inserted and, after several hours of recovery/equilibration, 20-minute playback sessions of either mating or restraint vocal sequences were delivered. Microdialysis samples were collected in 10-minute intervals (Pre-Stim, Stim 1, Stim 2) and analyzed via liquid chromatography/mass spectrometry for ACh, DA, 5-HIAA, and other neurochemicals.

Vocal stimuli were constructed from recorded vocalizations during actual mating (USVs with harmonics, steps, complex structure from males; LFH calls from females; 545 syllables total) and restraint (primarily MFVs; 622 syllables total). Each playback session featured only one vocalization type, and each animal participated in a single session. Female estrous stage was determined by vaginal smear cytology before and after experiments. Inexperienced (INEXP) control groups underwent the same protocol but without prior mating/restraint experience, to test the role of prior experience. Behavioral responses (attending, still-and-alert, flinching, grooming, rearing, walking) were manually scored from video during each 10-minute sampling period.

## Target venue
eLife


## Experimental Log

# Experimental Log

> Pre-writing data tables and observations for the BLA neuromodulator release during vocal playback study.

---

## Animal and Experimental Summary

| Parameter | Value |
|-----------|-------|
| Species/Strain | CBA/CaJ mice (Jackson Labs) |
| Age | p90-p180 |
| Total animals | 83 |
| Sex | Male and female |
| Light cycle | Reversed dark/light |
| Experimental timing | Dark cycle |
| Housing | Same-sex groups until experiment week, then singly housed |
| Food/water | Ad libitum (except during experiment) |

---

## Experimental Timeline

| Day | Activity |
|-----|----------|
| Day 1 | Experience 1: mating or restraint (counterbalanced) |
| Day 2 | Experience 2: other behavior + guide tube implantation |
| Days 3-5 | Recovery |
| Day 6 | Microdialysis probe insertion, habituation, vocal playback + sampling |

---

## Vocal Stimuli Characteristics

### Mating Vocal Sequences

| Syllable Type | Frequency of Occurrence | Likely Emitter |
|--------------|------------------------|---------------|
| USVs (harmonics, steps, complex) | Majority | Male |
| LFH calls | Minority | Female |
| Total syllables | 545 | - |
| Stimulus duration | 20 minutes | - |
| Repetitions within stimulus | 7 repetitions of selected sequences | - |

### Restraint Vocal Sequences

| Syllable Type | Frequency of Occurrence | Emitter |
|--------------|------------------------|---------|
| MFVs (mid-frequency vocalizations) | Majority | Restrained mouse |
| USVs | Minor component | Restrained mouse |
| LFH | Minor component | Restrained mouse |
| Total syllables | 622 | - |
| Stimulus duration | 20 minutes | - |

Fig. 1A: Short sample of mating vocal sequence showing USVs and LFH calls.

Fig. 1B: Short sample of restraint vocal sequence showing predominant MFV syllables.

Fig. 1C: Syllable composition differs substantially between mating and restraint stimuli.

---

## Microdialysis Sampling Protocol

| Parameter | Value |
|-----------|-------|
| Probe target | Basolateral amygdala (BLA) |
| Sampling interval | 10 minutes |
| Analysis method | LC/MS (liquid chromatography/mass spectrometry) |
| Neurochemicals measured | ACh, DA, 5-HIAA, and others |
| Temporal framework | Pre-Stim (10 min), Stim 1 (10 min), Stim 2 (10 min) |
| Playback per session | One vocalization type only |
| Sessions per animal | One |

Fig. 1D: Experimental design schematic showing the 6-day protocol structure.

Fig. 1E: Detailed sequencing of vocal stimuli within the playback session.

---

## Experimental Groups

| Group | Sex | Experience | Playback Type | n |
|-------|-----|------------|--------------|---|
| EXP Male - Mating | Male | Experienced | Mating | 7 |
| EXP Male - Restraint | Male | Experienced | Restraint | 6 |
| EXP Estrus Female - Mating | Female (estrus) | Experienced | Mating | 6 |
| EXP Non-estrus Female - Mating | Female (non-estrus) | Experienced | Mating | 5 |
| INEXP Male - Mating | Male | Inexperienced | Mating | 7 |
| INEXP Male - Restraint | Male | Inexperienced | Restraint | 7 |
| INEXP Estrus Female - Mating | Female (estrus) | Inexperienced | Mating | 7 |

---

## Estrous Stage Determination

| Method | Details |
|--------|---------|
| Technique | Vaginal smear via sterile lavage |
| Staining | Crystal violet |
| Estrus indicators | Squamous epithelial cells |
| Proestrus indicators | Nucleated cornified cells |
| Diestrus indicators | Leukocytes |
| Confirmation | Samples before and after experiment day compared |

---

## Experiment 1: Male Neurochemical Responses to Vocal Playback

### ACh Release in Male Mice

| Group | Pre-Stim | Stim 1 | Stim 2 | Direction |
|-------|----------|--------|--------|-----------|
| Male - Restraint playback (n=6) | Baseline | Increased | Increased | Up with restraint vocalizations |
| Male - Mating playback (n=7) | Baseline | Decreased/No change | Decreased/No change | Down or unchanged with mating |

### DA Release in Male Mice

| Group | Pre-Stim | Stim 1 | Stim 2 | Direction |
|-------|----------|--------|--------|-----------|
| Male - Restraint playback | Baseline | Decreased | Decreased | Down with restraint vocalizations |
| Male - Mating playback | Baseline | Increased | Increased | Up with mating vocalizations |

### 5-HIAA in Male Mice

| Group | Pre-Stim | Stim 1 | Stim 2 | Direction |
|-------|----------|--------|--------|-----------|
| Male - Restraint playback | Baseline | No change | No change | Stable |
| Male - Mating playback | Baseline | No change | No change | Stable |

Fig. 3: ACh and DA show opposing, context-dependent release patterns in males. Restraint vocalizations increase ACh and decrease DA; mating vocalizations decrease ACh and increase DA. 5-HIAA is unaffected by vocalization type.

---

## Experiment 2: Male Behavioral Responses to Vocal Playback

| Behavior | Restraint Playback (n=6) | Mating Playback (n=7) |
|----------|--------------------------|------------------------|
| Still-and-alert | Increased during playback | No significant change |
| Flinching | Increased during playback | No significant change |
| Attending | Increased during Stim 1 | Increased during Stim 1 |
| Grooming | No significant change | Variable |
| Rearing | Variable | Variable |
| Walking | Variable | Variable |

Fig. 3A-B: Behavioral boxplots showing occurrences of each behavior during Pre-Stim, Stim 1, and Stim 2 periods.

---

## Experiment 3: Sex and Estrous Effects on Mating Playback Responses

### Attending Behavior

| Statistical Test | Result |
|-----------------|--------|
| Time effect | F(2,30) = 32.6, p < 0.001, eta-squared = 0.7 |
| Time x Sex interaction | F(2,30) = 0.12, p = 0.9, eta-squared = 0.008 |

Attending behavior increased during Stim 1 regardless of sex or estrous stage.

### ACh Release by Sex/Estrous State (Mating Playback)

| Group | Pre-Stim | Stim 1 | Stim 2 | Pattern |
|-------|----------|--------|--------|---------|
| Male (n=7) | Baseline | Decreased | Decreased | Decreased ACh |
| Non-estrus Female (n=5) | Baseline | Decreased (similar to males) | Decreased | Male-like pattern |
| Estrus Female (n=6) | Baseline | Increased | Increased | Opposite to males |

### DA Release by Sex/Estrous State (Mating Playback)

| Group | Pre-Stim | Stim 1 | Stim 2 | Pattern |
|-------|----------|--------|--------|---------|
| Male | Baseline | Increased | Increased | Reward-associated |
| Non-estrus Female | Baseline | Increased (similar to males) | Increased | Male-like pattern |
| Estrus Female | Baseline | Increased | Increased | Also increased (unlike ACh divergence) |

Fig. 4A-D: Behavioral and neurochemical responses to mating vocal playback broken down by sex and estrous stage.

Fig. 4: Non-estrus females show neurochemical patterns similar to males during mating playback. Estrus females diverge specifically in ACh release (increased instead of decreased), while DA remains elevated. The estrus-specific ACh increase is associated with vigilance.

---

## Experiment 4: Flinching Behavior and ACh Release Association

| Group | ACh Change | Flinching Change | Co-occurrence |
|-------|-----------|------------------|--------------|
| Male - Restraint | Increased | Increased | Both present in both Stim periods |
| Male - Mating | Decreased | No change | Neither present |
| Estrus Female - Mating | Increased | Increased | Both present in both Stim periods |
| Non-estrus Female - Mating | Decreased | No change | Neither present |

Key finding: Every group showing significantly increased ACh release also displayed significantly increased flinching behavior, and this co-occurrence was present during both Stim 1 and Stim 2 periods. This temporal matching across multiple groups suggests a mechanistic relationship between ACh release and aversive behavioral responses.

---

## Experiment 5: Experience Dependence

### Experienced vs. Inexperienced -- ACh Release

| Comparison | EXP | INEXP | Difference |
|-----------|-----|-------|-----------|
| Male - Restraint (ACh) | Increased during playback | No distinct pattern | Significant |
| Male - Mating (ACh) | Decreased during playback | No distinct pattern | Significant |
| Estrus Female - Mating (ACh) | Increased during playback | No distinct pattern | Significant |

### Experienced vs. Inexperienced -- DA Release

| Comparison | EXP | INEXP | Difference |
|-----------|-----|-------|-----------|
| Male - Restraint (DA) | Decreased during playback | No distinct pattern | Significant |
| Male - Mating (DA) | Increased during playback | No distinct pattern | Significant |
| Estrus Female - Mating (DA) | Increased during playback | No distinct pattern | Significant |

### Experienced vs. Inexperienced -- Behavioral Responses

| Comparison | EXP | INEXP | Key Finding |
|-----------|-----|-------|------------|
| Flinching (restraint, males) | Increased | Not increased | Experience-dependent |
| Still-and-alert (restraint, males) | Increased | Not increased | Experience-dependent |
| Attending (all groups) | Increased | Also increased | Not experience-dependent |

Fig. 5: A single bout each of mating (90 min) and restraint (90 min) experience was sufficient to establish consistent patterns of ACh release and specific behavioral responses. No pre-stim baseline differences between EXP and INEXP mice for any behavior.

Fig. 6: In INEXP mice, vocal playback failed to evoke distinct neuromodulator patterns. ACh, DA, and 5-HIAA all showed no significant context-dependent changes.

Fig. 6A-C: Boxplots of ACh, DA, and 5-HIAA change from baseline for INEXP groups across both stimulus periods.

---

## Behavioral Classification Scheme

| Behavior | Description | Valence Association |
|----------|-------------|-------------------|
| Attending | Orienting toward sound source | Neutral/alerting |
| Still-and-alert | Freezing with apparent vigilance | Aversive/cautious |
| Flinching | Startle-like reflexive movement | Aversive |
| Grooming | Self-directed grooming | Comfort/displacement |
| Rearing | Standing on hind limbs | Exploratory |
| Walking | Locomotion within arena | General activity |

---

## Probe Placement Verification

| Group | Verification Method |
|-------|-------------------|
| All groups | Infusion of fluorescent dextran tracers through microdialysis probe |
| Histology | Post-experiment brain sectioning, fluorescence microscopy |
| Target region | BLA confirmed by probe tracks within amygdalar subdivisions |

Fig. 2: Microdialysis probe locations for all EXP and INEXP groups. Colored lines indicate recovered probe tracks from fluorescent tracers. Black dashed lines indicate major amygdalar subdivisions.

---

## Proposed Mechanistic Model

### ACh Pathway (Aversive Processing)

| Component | Role |
|-----------|------|
| Source | Basal forebrain cholinergic neurons |
| Target receptors | M1 mAChRs on CeA-projecting BLA neurons |
| Effect | Enhanced excitatory responses to aversive cues |
| Downstream | CeA activation -> defensive behaviors |
| Behavioral output | Flinching, still-and-alert behavior |

### DA Pathway (Appetitive Processing)

| Component | Role |
|-----------|------|
| Source | VTA dopaminergic neurons |
| Target receptors | D1 receptors on NAc-projecting BLA neurons |
| Effect | Enhanced responses to appetitive cues |
| Downstream | NAc activation -> approach/reward-seeking |
| Behavioral output | Reduced aversive responses, approach |

Fig. 7A: Cholinergic modulation model for aversive vocalization processing.

Fig. 7B: Dopaminergic modulation model for appetitive vocalization processing.

---

## Summary of Key Statistical Results

| Analysis | Test | Key Statistic | p-value |
|----------|------|--------------|---------|
| Attending (time effect, mating playback) | Repeated-measures ANOVA | F(2,30) = 32.6 | p < 0.001 |
| Attending (time x sex, mating playback) | RM ANOVA interaction | F(2,30) = 0.12 | p = 0.9 |
| Attending effect size (time) | Eta-squared | 0.7 | - |
| Attending effect size (time x sex) | Eta-squared | 0.008 | - |
| Pre-Stim baselines (EXP vs. INEXP) | Comparison across groups | No differences | Not significant |

---

## Datasets and Methods Summary

| Component | Details |
|-----------|---------|
| Vocalization recording chamber | Plexiglass (28x28x20 cm) in acoustic chamber (Industrial Acoustics) |
| Acoustic lining | Anechoic foam |
| Neurochemical analysis | LC/MS |
| Behavioral scoring | Manual from video recordings |
| Microdialysis equilibration | Several hours post-probe insertion |
| Probe placement confirmation | Fluorescent dextran tracer infusion + histology |

---

## Figure Summary

| Figure | Key Finding |
|--------|------------|
| Fig. 1 | Experimental design, vocal stimuli characteristics, and playback protocol |
| Fig. 2 | Probe placement verification in BLA for all groups |
| Fig. 3 | Males: restraint vocalizations increase ACh/decrease DA; mating vocalizations show opposite pattern |
| Fig. 4 | Sex/estrous effects: non-estrus females similar to males; estrus females show unique ACh increase to mating |
| Fig. 5 | Single experience sufficient: EXP mice show distinct patterns, INEXP show no changes |
| Fig. 6 | INEXP mice lack context-dependent neuromodulator patterns |
| Fig. 7 | Proposed model: ACh (basal forebrain) and DA (VTA) provide opposing contextual signals to BLA |

---

## Reference Count
103 references cited in the paper.

