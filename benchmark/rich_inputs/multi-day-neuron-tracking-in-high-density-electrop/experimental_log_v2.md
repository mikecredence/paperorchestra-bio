# Experimental Log

> Pre-writing data tables and observations for the EMD-based multi-day neuron tracking study.

---

## Datasets and Animal Information

| Animal | Probe Type | Brain Region | Number of Recordings | Time Span (days) | Notes |
|--------|-----------|-------------|---------------------|------------------|-------|
| AL031 | 4-shank Neuropixels 2.0 | Visual cortex V1 | Multiple | ~48 | 6 pairwise comparisons after outlier removal |
| AL032 | 4-shank Neuropixels 2.0 | Visual cortex V1 | Multiple | ~48 | 24 pairwise comparisons |
| AL036 | 4-shank Neuropixels 2.0 | Visual cortex V1 | Multiple | ~48 | 60 pairwise comparisons; datasets 1-2 excluded (large drift) |

---

## Recording Parameters

| Parameter | Value |
|-----------|-------|
| Probe | Neuropixels 2.0, 4-shank |
| Recording sites per shank section | 96 |
| Recording section length | 720 um |
| Brain area | Visual cortex area V1 |
| Species | Mouse |
| Time gap between recordings | 2 to 25 days |
| Total experimental span | Up to ~48 days |
| Spike sorting method | Kilosort 2.5 |
| Post-processing | ecephys spike sorting pipeline |
| Manual curation | None (to avoid bias) |
| Unit quality filter | KSgood label from Kilosort |

---

## EMD Algorithm Parameters

| Parameter | Description | Value/Details |
|-----------|------------|---------------|
| d_loc | 3D physical distance | Estimated from 10 peak-to-peak amplitudes on adjacent electrodes |
| d_wf | Waveform distance | Scalar waveform dissimilarity |
| omega | Weight parameter | Tuned to maximize reference unit recovery rate |
| Distance formula | d_ik = d_loc + omega * d_wf | Weighted combination |
| Stage 1 | Rigid drift correction | Estimates homogeneous vertical movement |
| Stage 2 | Unit assignment | Matches drift-corrected units |
| z-distance threshold | Post-hoc filter for plausible matches | 10 um |

---

## Validation Metrics Definitions

| Metric | Definition |
|--------|-----------|
| Recovery rate | Percentage of reference units correctly matched by EMD |
| Accuracy | Percentage of correctly matched reference units that pass the z-distance threshold |
| Reference units | KSgood units with strong and distinguishable visual responses in both datasets of a pair |
| Putative units | Units matched by EMD that lack reference receptive field information |
| Mixed units | Units that are reference in some session pairs and putative in others |
| Chains | Units tracked across at least three consecutive datasets |
| Similarity score | Sum of visual fingerprint (vfp) correlation and PSTH correlation |

---

## Overall Performance Summary

| Time Separation | Recovery Rate (avg) | Accuracy (at 10 um threshold) |
|----------------|--------------------|-----------------------------|
| Up to 1 week | ~90% | 99% |
| 5-7 weeks apart | ~78% | 95% |
| All pairs (1-47 days) | 84% | Not reported as single number |

---

## ROC Analysis (Fig 3)

| Metric | Value |
|--------|-------|
| Average z-distance across all reference pairs | 6.96 um |
| Z-distance threshold used | 10 um |
| False positive rate for KSgood units at 10 um threshold | 27% |

Fig 3 shows the ROC curve of matching accuracy vs. distance. The blue curve traces accuracy for reference units as the z-distance threshold varies. The red line shows the count of included reference units. At the average z-distance of 6.96 um (solid vertical line), accuracy is near ceiling. At the 10 um threshold (dashed vertical line), accuracy remains very high while including substantially more matched units.

---

## Recovery Rate and Accuracy by Time Gap (Fig 4b)

| Time Gap Category | Reference Units Recovered (light blue bars) | Accuracy at 10 um (green bars) |
|-------------------|---------------------------------------------|-------------------------------|
| 1-7 days | ~90% | ~99% |
| 1-2 weeks | Intermediate | Intermediate |
| 2-4 weeks | Lower than short-term | ~96-97% |
| 5-7 weeks | ~78% | ~95% |

Fig 4a shows the histogram distribution fits for all KSgood units (top panel), reference units alone (middle panel), and false positive identification. The false positive fraction for the full KSgood set is obtained by integration over the distance distribution.

---

## Drift Correction Impact (Supp Fig 2-1)

| Observation | Detail |
|-------------|--------|
| Drift correction effect | Improves recovery rate for most pairwise comparisons |
| Degree of improvement | Proportional to the magnitude of between-session drift |
| Animal AL031 | Moderate improvement |
| Animal AL032 | Moderate improvement |
| Animal AL036 | Large improvement for most pairs; datasets 1-2 excluded due to extreme drift |

Supplementary Figure 2-1 shows the effect of drift correction on reference unit yield for all three animals. Drift correction consistently improved recovery, with the magnitude of improvement scaling with drift size.

---

## EMD Cost as Drift Discontinuity Detector (Supp Fig 2-2)

| Animal | Observation |
|--------|-------------|
| AL036 | Large decrease in reference unit count after dataset 2, indicating a major tissue shift relative to probe |
| Detection method | Discontinuity detectable via EMD mean cost, location mean cost, and waveform mean cost |

Supplementary Figure 2-2 demonstrates that the EMD cost metric can flag datasets with extreme drift. In AL036, the drop in reference units after session 2 correlates with an anomalous increase in EMD cost.

---

## EMD Cost vs. Recovery Rate Relationship (Supp Fig 2-3)

| Metric | Correlation with Recovery Rate |
|--------|-------------------------------|
| Normalized EMD cost | Negative -- higher cost associates with lower recovery |
| Z-distance | Negative -- larger average distances associate with lower recovery |
| Physical distance | Negative correlation |
| Waveform distance | Negative correlation |

Supplementary Figure 2-3 plots normalized EMD cost, z-distance, physical distance, and waveform distance against recovery rate for all pairwise comparisons across all animals and shanks. Each triangle represents one dataset pair. Higher cost metrics consistently correspond to lower and more variable recovery rates.

---

## Tracked Unit Chains (Fig 5)

| Chain Type | Description | Loss Pattern |
|------------|-------------|-------------|
| Reference chains | Units that are reference in every consecutive pair | Similar loss rate within subject |
| Putative chains | Units that are putative (no visual response match) in every pair | Similar loss rate within subject |
| Mixed chains | Units that are reference in some pairs, putative in others | Similar loss rate within subject |
| Total tracked neurons with partial/no RF info | 552 | ~12 per dataset pair on average |

Fig 5 shows the number of reference, putative, and mixed units tracked for different chain durations across all three subjects. Loss rate is roughly consistent across chain types within the same animal, suggesting that tracking reliability is not driven primarily by the strength of visual responses.

---

## Example Mixed Chain Analysis (Fig 6)

| Day | Firing Rate Observation | Similarity Score Status |
|-----|------------------------|------------------------|
| Day 1 | Baseline rate established | Above or below reference threshold varies |
| Day 2 | Rate changes observed | Fluctuates |
| Day 13 | Intermediate | Score may dip below reference threshold |
| Day 23 | Continued tracking | Score may recover |
| Day 48 | Final time point | May or may not meet reference criteria |

Fig 6a shows firing rates and fractional rate changes across five recording days for one example mixed chain unit. Fig 6b plots visual response similarity (yellow), PSTH correlation (orange), and visual fingerprint correlation (blue) over time. The dashed black line indicates the reference unit threshold. Fig 6c displays the spatial-temporal waveform across all tracked days.

---

## Reference Unit Limitations

| Issue | Detail |
|-------|--------|
| Similarity score driven primarily by | PSTH timing rather than visual fingerprint selectivity |
| Consequence | A single neuron can correlate (similarity > 1) with 20+ other neurons |
| Example | In AL032 shank 2, one day-1 neuron had 22 highly correlated day-2 neurons, 4 within 30 um |
| Non-reference units with high similarity | 33 out of 106 trackable neurons had similarity > 1 even without reference assignment |
| Breakdown of 33 high-similarity non-reference | 5 putative neurons + 28 mixed neurons |

---

## Kilosort Sorting Quality (Fig 7d)

| Parameter | Observation |
|-----------|-------------|
| KSgood unit selection | Based primarily on inter-spike-interval (ISI) violation rate |
| Believed to represent | Single units |
| Variability across sessions | Cluster quality and identity can vary due to sorting randomness |

Fig 7d illustrates Kilosort sorting quality metrics across sessions for representative data.

---

## Visual Stimulus and Validation Parameters (Fig 7c)

| Parameter | Value/Detail |
|-----------|-------------|
| Visual fingerprint (vfp) | Spatial selectivity map, values range [-1, 1] |
| PSTH | Peri-stimulus time histogram, values range [-1, 1] |
| Similarity score | Sum of vfp correlation + PSTH correlation |
| High correlation example (Fig 7c left) | Strong match between sessions |
| Just-above-threshold example (Fig 7c right) | Marginal match |

---

## Tracking Strategy Comparison

| Strategy | Description | Use Case |
|----------|-------------|----------|
| Anchor-based | Match all sessions to a single reference session (e.g., first day) | When one session has highest quality |
| Consecutive-pair | Match each session to the next, trace through chains | When drift is cumulative and anchor may be too distant |

---

## Key Algorithmic Steps (Algorithm 1)

| Step | Operation |
|------|-----------|
| 1 | Run Kilosort 2.5 independently on each recording session |
| 2 | Post-process with ecephys pipeline; select KSgood units |
| 3 | Compute EMD distance matrix (d_loc + omega * d_wf) for all unit pairs |
| 4 | Stage 1: Estimate rigid vertical drift from EMD solution |
| 5 | Apply drift correction to unit positions |
| 6 | Stage 2: Re-run EMD on drift-corrected units for final assignment |
| 7 | Apply z-distance threshold (10 um) to filter plausible matches |
| 8 | Validate against reference units (visual RF similarity) |

---

## Weight Parameter Tuning (Supp Fig 2-4)

| Observation | Detail |
|-------------|--------|
| omega tuning method | Grid search to maximize reference unit recovery rate |
| Balance | Tradeoff between physical distance and waveform similarity |
| Result | Optimal omega balances both features; neither alone is sufficient |

Supplementary Figure 2-4 provides details on how the weighting between location and waveform distance was selected.

---

## Performance on Non-Visually-Tuned Neurons

| Observation | Detail |
|-------------|--------|
| Fig 6 supplement Fig 2 | Demonstrates tracking of neurons with no specific visual tuning preference |
| Implication | Method generalizes beyond visually responsive units |
| Fig 5 supplement Figs 1-5 | Trackable units with strong visual responses are qualitatively similar to those without |

---

## Code and Reproducibility

| Resource | Location |
|----------|----------|
| Code repository | github.com/janelia-TDHarrisLab/Yuan-Neuron_Tracking |
| Reference count | 31 |

---

## Summary of Key Numbers

| Metric | Value |
|--------|-------|
| Average recovery rate (all pairs) | 84% |
| Recovery rate (up to 1 week) | ~90% |
| Recovery rate (5-7 weeks) | ~78% |
| Accuracy at 10 um (up to 1 week) | 99% |
| Accuracy at 10 um (5-7 weeks) | 95% |
| Average z-distance (all reference pairs) | 6.96 um |
| False positive rate (KSgood, 10 um threshold) | 27% |
| Total tracked neurons without full RF info | 552 |
| Average putative neurons per dataset pair | ~12 |
| Number of animals | 3 |
| Probe type | 4-shank Neuropixels 2.0 |
| Maximum tracking duration | 47-48 days |
