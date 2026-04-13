Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: eLife

## Idea Summary

## Working title
Breath Shape Controls Intonation of Mouse Ultrasonic Vocalizations via the iRO Brainstem Circuit

## Core question
Does modulation of the expiratory breath waveform, in addition to laryngeal tension, control the pitch patterns (intonation) that define the diversity of mouse ultrasonic vocalization types?

## Motivation / gap
- It is thought that dynamic changes in laryngeal tension are the sole mechanism for pitch modulation in vocalizations
- Expiratory airflow velocity is presumed to only modulate loudness, not pitch
- Paradoxically, injecting air below the larynx increases pitch, but breath airflow does not strongly predict pitch in natural rodent vocalizations
- The intermediate Reticular Oscillator (iRO), a recently described brainstem vocalization CPG, can coordinate breathing and phonation, but its role in adult USV intonation is unknown
- No study has systematically characterized the relationship between breath waveform and pitch patterns across the full murine vocalization repertoire

## Core contribution (bullet form)
- Demonstrated that 6 of 10 USV syllable types primarily use positive intonation (pitch correlated with expiratory airflow changes) rather than laryngeal-only modulation
- Identified re-activation of the diaphragm (inspiratory muscle) during expiration as the mechanism creating breath waveform modulations during vocalization
- Found that the iRO is sufficient to induce most endogenous USV syllable types via optogenetic activation, producing primarily positive intonation patterns
- Distinguished two intonation mechanisms: positive (airflow-correlated, iRO-driven) and negative (airflow-anticorrelated, presumably laryngeal), which can combine within single vocalizations
- USV instantaneous frequency was typically 5-10 Hz (mean 7.5 Hz), occurring during rapid sniff episodes (8.5-10 Hz), with 88% of breaths containing a single syllable

## Method in brief
Male mice (n=6) were placed in whole-body plethysmography chambers modified with microphones to simultaneously record breathing and USVs during exposure to female urine. Vocalizations were classified as narrow-band ultrasonic sounds (40-120 kHz) during single breaths. The correlation between instantaneous expiratory airflow and pitch was computed for each vocalization to classify intonation as positive (r > 0, airflow predicts pitch) or negative (r < 0, pitch anticorrelated with airflow).

Electromyography (EMG) recordings from the diaphragm (inspiratory) and laryngeal muscles (thyroarytenoid, cricothyroid) were performed simultaneously with breathing and USV recordings to identify the muscle activation patterns underlying breath waveform modulations. Optogenetic activation of anatomically and molecularly defined iRO neurons (Penk+/Vglut2+ in the intermediate reticular tract) was performed using AAV-delivered ChR2 in adult mice. Light stimulation at various frequencies was used to entrain breathing and evoke USVs.

## Target venue
eLife


## Experimental Log

# Experimental Log: Breath Shape and Mouse Vocalization Intonation

## Basic Vocalization Parameters (Fig 1)

| Parameter | Value |
|-----------|-------|
| Animals for plethysmography | n = 6 male mice |
| Stimulus | Fresh female urine |
| Vocalization frequency range | 40-120 kHz (ultrasonic) |
| Typical fundamental frequency | ~75 kHz |
| Peak vocalization rate | ~4 events/second |
| Robust vocalization period | First 5-10 minutes |
| Mean instantaneous frequency of USV breaths | 7.5 Hz |
| Sniff episode frequency | 8.5-10 Hz |
| Syllables per breath | 88% single syllable |

## Breath Characteristics During Vocalization (Fig 1C-E)

### Breath Frequency Comparison

| Breath Type | Instantaneous Frequency |
|-------------|------------------------|
| With USV | 5-10 Hz (mean 7.5 Hz) |
| Without USV (sniffs) | 8.5-10 Hz |
| p-value (paired t-test) | 0.03 |

USV breaths are slightly slower than neighboring non-USV sniff breaths.

### Inspiratory and Expiratory Parameters (Fig 1D)

| Parameter | USV Breaths | Non-USV Breaths | p-value | Test |
|-----------|-------------|-----------------|---------|------|
| Inspiratory time (Ti) | Similar | Similar | 0.40 | Paired t-test |
| Expiratory time (Te) | Similar | Similar | 0.18 | Paired t-test |
| Ti/Te ratio | Similar | Similar | 0.25 | Paired t-test |

### Airflow Parameters (Fig 1E)

| Parameter | USV Breaths | Non-USV Breaths | p-value | Test |
|-----------|-------------|-----------------|---------|------|
| Peak inspiratory flow (pif) | Larger | Smaller | 0.01 | Paired t-test |
| Peak expiratory flow (pef) | Similar | Similar | 0.27 | Paired t-test |

## USV Syllable Type Distribution (Fig 1F)

| Syllable Type | Approximate % of Total USVs |
|---------------|----------------------------|
| Down FM | Most common (~25-30%) |
| Flat | Common (~20-25%) |
| Short | Common (~15-20%) |
| Chevron | Moderate (~8-12%) |
| Step Down | Moderate (~5-10%) |
| Multi | Less common (~5-8%) |
| Step Up | Less common (~3-5%) |
| Up FM | Less common (~3-5%) |
| Complex | Rare (~2-3%) |
| Two-syllable | Rare (~1-2%) |

10 distinct syllable types defined by unique pitch patterns compose the adult murine lexicon.

## Intonation Analysis: Two Mechanisms (Fig 2)

### Correlation Between Airflow and Pitch by USV Type

| USV Type | Primary Intonation | Correlation (r) Direction | Classification |
|----------|-------------------|--------------------------|----------------|
| Down FM | Positive | r > 0 (pitch tracks airflow) | Positive intonation |
| Flat | Positive | r > 0 | Positive intonation |
| Short | Positive | r > 0 | Positive intonation |
| Chevron | Positive | r > 0 | Positive intonation |
| Step Down | Positive/Mixed | r ~ 0 or mixed | Mixed |
| Multi | Positive | r > 0 | Positive intonation |
| Step Up | Negative | r < 0 (pitch anticorrelates with airflow) | Negative intonation |
| Up FM | Negative | r < 0 | Negative intonation |
| Complex | Mixed | Uses both mechanisms | Combined |
| Two-syllable | Mixed | Uses both mechanisms | Combined |

Key finding: 6 of 10 USV types primarily use positive intonation (pitch follows airflow), while others use negative intonation or a combination.

### Statistical Comparison of Correlation Coefficients (Fig S5)

| USV Type | n | Significance |
|----------|---|-------------|
| Step down | 293 | * (p < 0.05, one-way ANOVA with Sidak's post-hoc) |
| Flat | 337 | * |
| Short | 168 | * |
| Chevron | 99 | * |
| Multi | 58 | * |
| Step up | 40 | * |

## EMG Recordings (Fig 3)

### Muscle Activity During Normal Breath

| Muscle | Phase | Activity |
|--------|-------|----------|
| Diaphragm | Inspiration | Active |
| Diaphragm | Expiration | Inactive |
| Thyroarytenoid (laryngeal) | Post-inspiration | Active |
| Cricothyroid (laryngeal) | Post-inspiration | Active |

### Muscle Activity During Vocalization Breaths (Fig 3B-C)

| Muscle | Observation |
|--------|-------------|
| Diaphragm | Re-activated during expiration (ectopic burst) |
| Laryngeal muscles | Anti-phase activity with diaphragm |
| Correspondence | Diaphragm re-activation coincides with pitch decrease; relaxation with pitch increase |

Key finding: Re-activation of the inspiratory diaphragm during expiration creates a "mini-breath" nested within the vocal breath, modulating airflow speed and consequently pitch.

### EMG-Pitch Correspondence

| Event | Airflow Effect | Pitch Effect |
|-------|---------------|-------------|
| Diaphragm re-activation (inspiration) | Slows expiration | Pitch decreases |
| Diaphragm relaxation | Expiration resumes/accelerates | Pitch increases |
| Laryngeal muscle co-activation | -- | Additional modulation |

## iRO Circuit Anatomy (Fig 4)

### iRO Neuron Identification

| Marker | Cell Type |
|--------|-----------|
| Penk+ | Proenkephalin-expressing |
| Vglut2+ | Glutamatergic |
| Location | Medial to compact nucleus ambiguus (cNA) in ventral iRT |
| Verified in | n = 5 mice (Penk-Cre;Vglut2-Flp;Ai65) |

### Optogenetic Activation Setup (Fig 4B)

| Parameter | Value |
|-----------|-------|
| Virus | AAV CreON-FlpON-ChR2::YFP |
| Injection | Bilateral stereotaxic into iRO |
| Stimulation | Various frequencies (e.g., 10 Hz) |
| Light fiber | Implanted over injection site |

## iRO Optogenetic Results (Fig 4, Fig S6)

### Breathing Entrainment

| Observation | Detail |
|-------------|--------|
| Light stimulation (10 Hz) | Breathing rate entrained to stimulation frequency |
| Amplitude | Increased during stimulation |
| USV production | Occurs at peak of expiration |

### Evoked USV Syllable Types

| Finding | Detail |
|---------|--------|
| USV types produced | Most of the 10 endogenous syllable types |
| Intonation mechanism | Primarily positive intonation |
| Interpretation | iRO can produce breath-waveform modulation sufficient for most USV types |
| Negative intonation | Rare in evoked USVs, suggesting separate neural component |

### Cell-Type Specificity (Fig S6)

| Cell Type | Breathing Modulation | USV Production |
|-----------|---------------------|----------------|
| Penk+Vglut2+ (iRO) | Strong entrainment | USVs produced |
| Other nearby populations | Variable | Reduced or absent |

## Vocalization Onset Timing (Fig S1, S2, S3)

| Parameter | Value |
|-----------|-------|
| USV onset relative to expiration | Biased to early expiration |
| Complex vocalizations | Later onset and offset during expiration |
| Total events analyzed | 1,850 |

Fig S1: Raster plot of USV onset/offset aligned to expiration start shows onset bias to early expiration.
Fig S4: Raster plot showing breaths after ~1200 have late onset, delaying subsequent inspiration.

## Two-Mechanism Model of Intonation (Fig 5H)

| Mechanism | Source | Neural Substrate | Effect |
|-----------|--------|-----------------|--------|
| Positive intonation | Breath airflow modulation | iRO -> breathing CPG | Pitch tracks airflow |
| Negative intonation | Laryngeal tension modulation | RAm/laryngeal premotor neurons | Pitch anticorrelated with airflow |
| Combined | Both mechanisms | iRO + laryngeal circuits | Complex pitch patterns |

## Key Figure Observations

- Fig 1A: Simultaneous recording of USVs (~75 kHz) and expiratory airflow shows temporal correspondence
- Fig 1B: Breathing and USV rates during female urine exposure
- Fig 1C: USV breaths have slightly lower instantaneous frequency than sniff breaths
- Fig 1D-E: USV breaths have larger inspiratory flow but similar timing to non-USV breaths
- Fig 1F: Distribution of the 10 syllable types
- Fig 2A: Example down FM USV showing airflow-pitch correlation (positive intonation)
- Fig 2: Scatter plots of airflow vs pitch for each USV type reveal positive, negative, or mixed correlations
- Fig 3A: Normal breath EMG shows restricted diaphragm activity to inspiration
- Fig 3B-C: During vocalization, diaphragm re-activates during expiration, creating the breath modulation
- Fig 4A: iRO neuron labeling in Penk-Cre;Vglut2-Flp mouse
- Fig 4: iRO optogenetic activation entrains breathing and produces USVs with primarily positive intonation
- Fig S6: Cell-type specific optogenetic effects confirm iRO identity

