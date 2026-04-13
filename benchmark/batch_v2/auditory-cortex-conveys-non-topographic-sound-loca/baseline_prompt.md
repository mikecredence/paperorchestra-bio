Write a complete research paper as a LaTeX manuscript.
Output two files:
1. main.tex - the complete paper
2. references.bib - BibTeX bibliography

Target venue: Nature Communications

## Idea Summary

## Working title
Characterizing Auditory Spatial Information in Auditory Cortex Projections to Primary Visual Cortex

## Core question
Do auditory cortex (AC) inputs to primary visual cortex (V1) encode sound location, and if so, is this spatial information topographically organized to match the retinotopic map in V1?

## Motivation / gap
- Binding spatiotemporally congruent multimodal stimuli is fundamental to perception, but the cortical mechanisms are poorly understood
- AC sends direct projections to V1 across species, and these are thought to mediate audiovisual interactions in V1 neurons
- AC neurons show tuning to sound location, but it is unknown whether the AC-to-V1 projection specifically relays spatial auditory information
- In the superior colliculus, auditory and visual spatial maps are in register, enabling binding of congruent stimuli -- does a similar organization exist in cortex?
- V1-projecting AC neurons selectively encode certain sound features less represented within AC, but spatial coding in these projections was uncharacterized
- If AC inputs were retinotopically arranged in V1, this could provide a substrate for binding spatially congruent audiovisual stimuli

## Core contribution (bullet form)
- AC axons in V1 layer 1 carry information about both ipsilateral and contralateral sound source locations
- Population decoding of AC boutons in V1 can accurately estimate sound location (azimuth and elevation)
- AC inputs to V1 are NOT retinotopically organized -- auditory spatial RFs do not match the visual RF of postsynaptic V1 neurons
- AC auditory RFs span a wider range than the visual field coverage of V1, including sounds from ipsilateral space well beyond the visual representation
- Audiovisual modulations of V1 neuron responses do not depend on spatial congruency of sound and light stimuli
- V2L (secondary visual area lateral) inputs to V1 show retinotopic visual RFs but minimal auditory spatial coding, contrasting with AC inputs

## Method in brief
A custom speaker-LED array was built with 39 positions (13 columns x 3 rows, covering 10-degree azimuth steps and 20-degree elevation steps) to present spatially controlled auditory and visual stimuli. Head-fixed mice were positioned at the center, allowing stimulus presentation spanning 20 degrees ipsilateral to 100 degrees contralateral in azimuth, and 20 degrees up/down in elevation. Auditory stimuli were white noise bursts (2-20 kHz) and visual stimuli were flashing LEDs.

Dual-color two-photon calcium imaging was used to simultaneously record AC (or V2L) axon boutons expressing GCaMP6s in V1 layer 1 and postsynaptic V1 neurons in layer 2/3 expressing jRGECO1a. This allowed direct comparison of auditory spatial tuning in presynaptic AC inputs and visual RFs of their target neurons. N=7 AC-injected mice and N=3 V2L-injected mice were used. A spatial modulation index (SMI) was computed to quantify spatial selectivity of individual boutons.

Decoding analysis used a maximum-likelihood framework to determine how accurately sound location could be estimated from population activity of AC boutons. Additional experiments with a single speaker spanning -90 to +90 degrees azimuth (2-80 kHz white noise) tested full azimuthal coverage including ipsilateral space. Audiovisual congruency experiments presented a fixed LED in the visual RF while varying speaker position to test whether V1 modulation depended on spatial match.

## Target venue
Nature Communications


## Experimental Log

# Experimental Log: Auditory Spatial Information in AC-to-V1 Projections

## Experimental Setup

### Stimulus Array Parameters

| Parameter | Value |
|-----------|-------|
| Total positions | 39 |
| Azimuth columns | 13 |
| Elevation rows | 3 |
| Azimuth step size | 10 degrees |
| Elevation step size | 20 degrees |
| Ipsilateral coverage | 20 degrees |
| Contralateral coverage | 100 degrees |
| Elevation range | -20 to +20 degrees |
| Auditory stimulus | White noise bursts, 2-20 kHz |
| Visual stimulus | Flashing white LED |
| Stimulus duration | 1 second |

---

## Animal and Imaging Summary

### Table 1: Experimental Animals

| Condition | N mice | N imaging sessions | Calcium indicator (axons) | Calcium indicator (somata) |
|-----------|--------|-------------------|--------------------------|---------------------------|
| AC-injected | 7 | 42 | GCaMP6s | jRGECO1a |
| V2L-injected | 3 | 15 | GCaMP6s | jRGECO1a |

### Table 2: Imaging Configuration

| Parameter | Value |
|-----------|-------|
| Imaging modality | Dual-color two-photon volumetric calcium imaging |
| Axon imaging depth | Layer 1 of V1 |
| Soma imaging depth | Layer 2/3 of V1 |
| Axon indicator | GCaMP6s (green) |
| Soma indicator | jRGECO1a (red) |

---

## Experiment 1: Modality and Spatial Sensitivity in AC vs. V2L Inputs

### Table 3: Fraction of Responsive Boutons (AC vs. V2L)

| Input Source | Auditory Responsive (%) | Visual Responsive (%) | Both (%) | Statistical Test |
|-------------|------------------------|----------------------|----------|-----------------|
| AC boutons | High (majority) | Low (minority) | Small fraction | Two-sided paired t-test |
| V2L boutons | Low (minority) | High (majority) | Small fraction | Two-sided paired t-test |

Fig 2a shows that auditory responses were much more frequent than visual ones in AC boutons, whereas V2L boutons were dominated by visual responses.

Fig 2b breaks down the fraction of boutons responsive to auditory only, visual only, or both stimuli in AC and V2L axons.

### Table 4: Spatial Modulation Characteristics

| Measure | AC Boutons | V2L Boutons | V1 Somata |
|---------|-----------|-------------|-----------|
| Spatial selectivity | Variable (some broad, some narrow) | Visually tuned | Visually tuned |
| Spatial modulation index (SMI) | Ranges from low to high | Not primary auditory | Sharp visual RFs |
| Dominant modality for spatial info | Auditory | Visual | Visual |

---

## Experiment 2: Sound Location Decoding from AC Inputs

### Table 5: Decoding Accuracy

| Dimension | AC Inputs Accuracy | V2L Inputs Accuracy | Shuffled Control | N (AC) | N (V2L) | Statistical Test |
|-----------|-------------------|--------------------|--------------------|--------|---------|-----------------|
| Azimuth | Significantly above chance | Near chance | Baseline | 8 mice, 42 sessions | 3 mice, 15 sessions | Two-sided paired t-test |
| Elevation | Significantly above chance | Near chance | Baseline | 8 mice, 42 sessions | 3 mice, 15 sessions | Two-sided paired t-test |

Fig 3a shows log-likelihood distributions across speaker positions for example trials, with maximum likelihood closely matching true speaker position.

Fig 3b shows elevation and azimuth decoding accuracy for AC and V2L inputs compared to shuffled data.

Fig 3c reports the distance between decoded and actual speaker position.

### Table 6: Decoding Analysis Parameters

| Parameter | Value |
|-----------|-------|
| Decoding method | Maximum-likelihood framework |
| Cross-validation | Leave-one-out or similar |
| Population sampling | Bootstrapped from AC boutons in V1 L1 |
| Spatial dimensions decoded | Azimuth and elevation separately |

---

## Experiment 3: Retinotopic Organization Assessment

### Table 7: Comparison of Auditory RF vs Visual RF Properties

| Property | AC Inputs (Auditory RF) | V1 Somata (Visual RF) | V2L Inputs (Visual RF) |
|----------|------------------------|-----------------------|------------------------|
| Spatial specificity | Broad | Sharp | Sharp (retinotopic) |
| Total span | Larger than V1 visual field | Contralateral visual space + small ipsilateral | Contralateral visual space |
| Ipsilateral coverage | Substantial fraction tuned to ipsilateral sounds | Minimal (small frontal portion) | Minimal |
| Topographic organization | Non-topographic | Retinotopic | Retinotopic |
| Alignment with V1 retinotopic map | No alignment detected | Intrinsic | Aligned |

Fig 4 demonstrates that AC inputs in V1 are not retinotopically matched. The azimuth peak of AC bouton populations does not correlate with the visual RF centers of underlying V1 neurons.

### Table 8: Key Findings on AC Spatial RF Properties

| Finding | Detail |
|---------|--------|
| AC bouton auditory RFs vs V1 visual RFs | Less spatially specific than V1 visual RFs |
| Total auditory RF span | Larger than visual field coverage of V1 |
| Ipsilateral sound representation | Large fraction of AC inputs selective for ipsilateral sounds outside V1 visual range |
| Topographic map | No evidence of topographic organization of auditory spatial info in AC-to-V1 projection |
| Broadband test (2-80 kHz) | Non-topographic result holds even with full auditory spectrum stimulation |

---

## Experiment 4: Ipsilateral and Contralateral Sound Tuning

### Table 9: Extended Azimuth Experiment

| Parameter | Value |
|-----------|-------|
| Speaker range | -90 to +90 degrees azimuth |
| Speaker spacing | 20 degrees |
| Auditory stimulus | 2-80 kHz white noise |
| Key finding | AC boutons tuned to sounds in both ipsi- and contralateral hemifields |

Fig 5 shows individual AC bouton responses to sounds across the full azimuthal range from -90 to +90 degrees. Some boutons prefer ipsilateral locations, others contralateral, and some are broadly tuned.

### Table 10: Distribution of Preferred Sound Locations

| Hemifield | Fraction of Spatially Selective AC Boutons |
|-----------|------------------------------------------|
| Ipsilateral (negative azimuth) | Substantial proportion |
| Contralateral (positive azimuth) | Substantial proportion |
| Broadly tuned / non-selective | Present but variable |

---

## Experiment 5: Audiovisual Spatial Congruency

### Table 11: AV Congruency Experiment Design

| Parameter | Value |
|-----------|-------|
| LED position | Within V1 neuron RF (azimuth center: 40-60 degrees) |
| Speaker positions | -40 to +40 degrees azimuth, 20-degree steps |
| Congruency definition | 0 degrees = matched speaker and LED position |
| Negative values | Speaker in lower azimuth |
| Positive values | Speaker in higher azimuth |
| Imaging target | GCaMP6f-expressing L2/3 neurons in V1 |

### Table 12: AV Congruency Results

| Condition | V1 Modulation | Dependence on Spatial Congruency |
|-----------|--------------|----------------------------------|
| LED alone | Baseline visual response | N/A |
| LED + spatially matched sound (0 deg) | Modulated | No preferential enhancement |
| LED + spatially mismatched sound | Modulated | No significant difference from matched |

Fig 6 shows that audiovisual interactions in V1 do not depend on the spatial coherence between auditory and visual stimuli. V1 neuron responses to LED flashes are modulated by concurrent sounds regardless of where the sound originates.

---

## Summary of Statistical Tests

### Table 13: Statistical Analyses Employed

| Comparison | Test | Key Finding |
|-----------|------|-------------|
| Fraction of auditory vs visual responsive boutons (AC) | Two-sided paired t-test | Auditory responses significantly more frequent |
| Fraction of auditory vs visual responsive boutons (V2L) | Two-sided paired t-test | Visual responses significantly more frequent |
| Azimuth decoding accuracy (AC vs shuffled) | Two-sided paired t-test | Significant above-chance decoding for AC |
| Elevation decoding accuracy (AC vs shuffled) | Two-sided paired t-test | Significant above-chance decoding for AC |
| AV modulation vs spatial congruency | Statistical test applied | No significant effect of congruency |

---

## Histological Observations

### Table 14: Axon Distribution by Cortical Depth

| Cortical Layer | AC Axon Density | V2L Axon Density |
|---------------|----------------|-----------------|
| Layer 1 (superficial) | Highest | Highest |
| Layer 2/3 | Decreasing | Decreasing |
| Deeper layers | Minimal | Minimal |

Fig 1e shows coronal histological sections confirming AC and V2L axon presence in V1.

Fig 1f shows normalized fluorescence intensity from AC (blue) and V2L (yellow) axons at different cortical depths, with both peaking in L1. Data from N=7 AC-injected and N=3 V2L-injected mice.

---

## Figure Summary

- **Fig 1**: Complete experimental setup including 3D array rendering, mouse positioning, trial structure, dual-color imaging schematic, histology, depth profiles, and example bouton responses with SMI values.

- **Fig 2**: Modality fractions and spatial sensitivity comparison between AC and V2L inputs to V1. Auditory dominates AC inputs; visual dominates V2L inputs.

- **Fig 3**: Population decoding of sound location from AC boutons. Accurate azimuth and elevation estimation from AC inputs but not V2L inputs.

- **Fig 4**: AC inputs lack retinotopic matching. No correlation between auditory RF position of AC boutons and visual RF position of underlying V1 neurons.

- **Fig 5**: Full azimuth experiment (-90 to +90 deg) demonstrating AC bouton tuning to both ipsilateral and contralateral sound sources.

- **Fig 6**: Audiovisual congruency test showing V1 modulation by sound is independent of sound-light spatial alignment.

---

## Datasets and Metrics

| Item | Description |
|------|-------------|
| Primary data | Two-photon calcium imaging time series from AC and V2L boutons in V1 L1 |
| Secondary data | Simultaneous L2/3 soma calcium imaging (jRGECO1a) |
| Spatial modulation index (SMI) | Quantifies spatial selectivity of individual boutons |
| Decoding accuracy | Maximum-likelihood decoding of azimuth and elevation |
| Boyce index or RF fitting | Elliptical RF fits for V1 soma visual fields |
| Response metric | Mean fluorescence signal over stimulus presentation window |
| Cross-validation | Applied in decoding analysis |
| Shuffled controls | Time-shuffled data used as null distribution for responsiveness |

