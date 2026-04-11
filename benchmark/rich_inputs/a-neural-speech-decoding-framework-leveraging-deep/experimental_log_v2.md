# Experimental Log

> Pre-writing data tables and observations for the neural speech decoding framework study.

---

## Dataset Summary

| Parameter | Value |
|-----------|-------|
| Total participants | 48 |
| Sex distribution | 26 female, 22 male |
| Language | Native English speakers |
| Clinical condition | Refractory epilepsy with subdural ECoG grids |
| Hybrid-density (HB) participants | 5 |
| Low-density (LD) participants | 43 |
| Left hemisphere coverage | 32 participants |
| Right hemisphere coverage | 16 participants |
| IRB approval | NYU Grossman School of Medicine |

---

## ECoG Recording Parameters

| Parameter | HB Grid | LD Grid |
|-----------|---------|---------|
| Total electrodes | 128 | 64 |
| Macro contacts | 64 (8x8, 10 mm spacing) | 64 (8x8, 10 mm spacing) |
| Micro contacts | 64 (interspersed, 1 mm) | N/A |
| Macro spacing | 10 mm center-to-center | 10 mm center-to-center |
| Micro-macro spacing | 5 mm center-to-center | N/A |
| Original sampling rate | 2048 Hz | 2048 Hz |
| Downsampled rate | 512 Hz | 512 Hz |
| Coverage regions | Perisylvian cortex (STG, IFG, precentral, postcentral gyri) | Same |
| Manufacturer | PMT Corporation (FDA-approved) | Standard clinical |

---

## Speech Tasks

| Task | Abbreviation | Stimulus Modality | Trials per Word | Total Unique Words |
|------|-------------|-------------------|----------------|-------------------|
| Auditory Repetition | AR | Auditory | 2 | 50 |
| Auditory Naming | AN | Auditory (definition) | 1 | 50 |
| Sentence Completion | SC | Auditory (sentence) | 1 | 50 |
| Word Reading | WR | Visual (written) | 2 | 50 |
| Picture Naming | PN | Visual (drawing) | 2 | 50 |
| **Total per participant** | | | **400 trials** | **50 unique words** |

Average duration of produced speech per trial: 500 ms.

---

## Train/Test Split

| Split | Trials | Usage |
|-------|--------|-------|
| Training | 350 (80%) | Model fitting per participant |
| Testing | 50 (20%) | 10 randomly selected from each task |
| Cross-validation | Word-level | More stringent evaluation (separate analysis) |

---

## Experiment 1: Architecture Comparison (All 48 Participants)

### Main Decoding Performance (PCC: Pearson Correlation Coefficient)

| Architecture | Type | Non-Causal PCC (mean) | Causal PCC (mean) | Difference |
|-------------|------|----------------------|-------------------|------------|
| 3D ResNet | Convolutional | 0.804 | 0.798 | Not significant |
| 3D SWIN | Transformer | 0.793 | 0.796 | Not significant |
| LSTM | Recurrent | Lower than ResNet/SWIN | Lower than ResNet/SWIN | N/A |

Fig. 2a: Box plots showing PCC for each architecture in causal and non-causal modes across all 48 participants. Each data point is one participant. ResNet achieves the highest overall PCC but SWIN is closely competitive.

Key finding: The causal ResNet model (PCC=0.798) matches non-causal performance (PCC=0.804) with no statistically significant difference. This is critical for real-time BCI feasibility.

### STOI+ Metric Comparison

| Architecture | Non-Causal STOI+ | Causal STOI+ |
|-------------|-----------------|--------------|
| 3D ResNet | Highest | Comparable |
| 3D SWIN | Close to ResNet | Close to ResNet |
| LSTM | Lower | Lower |

Supplementary Fig. S1a confirms the same ranking using the STOI+ speech intelligibility metric.

---

## Experiment 2: Causal vs. Non-Causal Decoding

| Model | Causal PCC | Non-Causal PCC | Significant Difference? |
|-------|-----------|----------------|----------------------|
| 3D ResNet | 0.798 | 0.804 | No |
| 3D SWIN | 0.796 | 0.793 | No |
| LSTM | Lower | Lower | N/A |

Non-causal models can use past, present, and future neural signals (including auditory/somatosensory feedback). Causal models are restricted to past and current signals only. The lack of significant performance drop with causal ResNet and SWIN indicates that these architectures do not heavily depend on auditory feedback signals.

---

## Experiment 3: Left vs. Right Hemisphere Decoding

Fig. 3a: Comparison between left (n=32) and right (n=16) hemisphere participants using causal models.

| Hemisphere | n | Causal ResNet PCC | Causal SWIN PCC | Significant Difference? |
|-----------|---|-------------------|-----------------|----------------------|
| Left | 32 | High | High | No significant difference |
| Right | 16 | High | High | between hemispheres |

This is a notable finding because most prior speech decoding work focuses on left hemisphere (dominant for speech). Successful right-hemisphere decoding could enable prostheses for patients with left hemisphere damage.

---

## Experiment 4: High-Density vs. Low-Density Grids

Fig. 3b: Example hybrid-density ECoG array with 128 electrodes (64 red = low-density, 64 green + red = hybrid-density).

| Grid Type | n Participants | Electrode Count | Decoding Performance |
|-----------|---------------|-----------------|---------------------|
| Hybrid-density (HB) | 5 | 128 | High PCC |
| Low-density (LD) | 43 | 64 | High PCC |

The framework successfully decodes speech with both sampling densities, though comparison is limited by the small HB sample (n=5).

---

## Experiment 5: PCC Distribution Across Participants

Fig. 3c: Distribution of per-participant decoding PCC values.

| PCC Range | Proportion of Participants | Notes |
|-----------|--------------------------|-------|
| 0.52-0.64 | Small minority | Lower end of performance |
| 0.64-0.80 | ~52% | Moderate to good performance |
| 0.80-0.91 | ~48% | High performance |
| Overall range | 0.52-0.91 | Causal ResNet |
| Median | 0.81 | Causal ResNet |
| Mean | 0.798 | Causal ResNet |

---

## Experiment 6: Occlusion Analysis (Cortical Contribution Mapping)

Fig. 4: Contribution of each cortical location projected onto standardized MNI brain atlas, averaged over all participants.

| Cortical Region | Causal Model Contribution | Non-Causal Model Contribution |
|----------------|--------------------------|------------------------------|
| STG (superior temporal gyrus) | Lower | Higher (auditory feedback) |
| IFG (inferior frontal gyrus) | Moderate | Moderate |
| Precentral gyrus (motor) | Higher | Moderate |
| Postcentral gyrus (somatosensory) | Moderate | Moderate |

Key finding: Non-causal models rely substantially on STG, which processes auditory feedback from the participant's own speech. Causal models eliminate most of this STG contribution, shifting reliance to motor cortex areas (precentral gyrus). This confirms that causal models decode motor planning rather than auditory feedback.

Red indicates higher contribution, yellow indicates lower contribution in the visualization.

---

## Speech Synthesizer Architecture

| Component | Description |
|-----------|-------------|
| Voiced pathway | Harmonic excitation at F0 -> 6 formant filters (each with frequency and amplitude) -> voice component |
| Unvoiced pathway | Noise excitation -> noise filter -> unvoiced component |
| Combination | Voice + unvoice components combined based on voicing parameter |
| Differentiability | Fully differentiable end-to-end for backpropagation |

Fig. 5: Architecture diagram showing the two pathways merging at time t based on speech parameters.

### Speech Parameters

| Parameter | Symbol | Count | Description |
|-----------|--------|-------|-------------|
| Fundamental frequency | F0 | 1 | Pitch of voiced speech |
| Voicing | V | 1 | Voiced vs. unvoiced classification |
| Formant frequencies | F1-F6 | 6 | Resonant frequencies of vocal tract |
| Formant amplitudes | A1-A6 | 6 | Amplitude at each formant |
| Noise parameters | Various | Multiple | Spectral shape of unvoiced components |

---

## ECoG Decoder Architectures

| Architecture | Type | Key Layers | Temporal Operations |
|-------------|------|-----------|-------------------|
| 3D ResNet | Convolutional | Temporal + spatial conv layers, residual connections, spatiotemporal pooling, transposed temporal conv | Causal: past/current only; Non-causal: bidirectional |
| LSTM | Recurrent | LSTM layers | Causal: forward only; Non-causal: bidirectional |
| 3D SWIN | Transformer | Shifted window attention | Causal: masked attention; Non-causal: full attention |

Fig. 6a: Speech Encoder architecture (temporal convolutions + channel MLPs).
Fig. 6b: ECoG Decoder architecture using 3D ResNet with downsampling and upsampling paths.

---

## Training Pipeline

| Stage | Input | Output | Purpose |
|-------|-------|--------|---------|
| Stage 1: Speech auto-encoder pre-training | Participant's speech spectrograms | Pre-trained Speech Encoder + Synthesizer | Generate reference speech parameters |
| Stage 2: ECoG Decoder training | ECoG signals + reference parameters | Trained ECoG Decoder | Map neural signals to speech parameters |
| Inference | ECoG signals | Spectrograms -> speech waveforms | Decode speech from brain activity |

Spectrogram inversion (spectrograms to audio waveforms) uses a separate algorithm after the synthesizer output.

---

## Comparison with Prior Work

| Approach Category | Method | Typical PCC | Naturalness | Causal? | Code Available? |
|------------------|--------|-------------|-------------|---------|----------------|
| Linear models | Various | ~0.6 or lower | Limited | Varies | No |
| Articulatory decoding | RNN-based | Robust | Synthetic voice | No | No |
| WaveNet vocoder | CNN-based | Limited | Natural | No | No |
| GAN-based | Adversarial | Limited | Natural | No | No |
| Unit selection | Hybrid | Limited | Natural | No | No |
| This work (ResNet) | CNN + Diff. Synthesizer | 0.798 (causal) | Natural | Yes | Yes |
| This work (SWIN) | Transformer + Diff. Synthesizer | 0.796 (causal) | Natural | Yes | Yes |

---

## Key Performance Metrics

| Metric | Definition | Best Model | Value |
|--------|-----------|-----------|-------|
| PCC (Pearson Correlation Coefficient) | Correlation between original and decoded spectrogram | Causal ResNet | 0.798 (mean) |
| STOI+ | Extended short-time objective intelligibility | Causal ResNet | Highest (see Supp. Fig. S1a) |
| PCC range | Min-max across participants | Causal ResNet | 0.64-0.91 |
| PCC median | 50th percentile | Causal ResNet | 0.81 |

---

## Statistical Tests

| Test | Comparison | Result |
|------|-----------|--------|
| Paired comparison | Causal vs. non-causal ResNet | No significant difference |
| Paired comparison | Causal vs. non-causal SWIN | No significant difference |
| Group comparison | Left vs. right hemisphere (causal) | No significant difference |
| Architecture ranking | ResNet vs. SWIN vs. LSTM | ResNet >= SWIN > LSTM |

---

## Figure Observations Summary

| Figure | Key Observation |
|--------|----------------|
| Fig. 1 | Two-stage framework: ECoG Decoder -> Speech Parameters -> Speech Synthesizer -> Spectrogram; auto-encoder provides speech parameter guidance |
| Fig. 2a | ResNet achieves highest PCC (0.804 non-causal, 0.798 causal); SWIN closely follows; LSTM lags behind |
| Fig. 2 | Causal models match non-causal performance for ResNet and SWIN |
| Fig. 3a | No significant PCC difference between left and right hemisphere participants |
| Fig. 3b | HB grid layout with 128 electrodes shown; both HB and LD grids decode effectively |
| Fig. 3c | 48% of participants achieve PCC between 0.80-0.91 |
| Fig. 4 | Occlusion analysis: non-causal models rely on STG (auditory feedback); causal models shift to motor areas |
| Fig. 5 | Speech Synthesizer combines voiced (harmonic + formants) and unvoiced (noise) pathways |
| Fig. 6a | Speech Encoder uses temporal convolutions and channel MLPs |
| Fig. 6b | 3D ResNet ECoG Decoder with residual connections and up/downsampling |

---

## Open-Source Deliverables

| Component | Description |
|-----------|-------------|
| ECoG Decoder code | Multiple architectures (ResNet, SWIN, LSTM) |
| Speech Synthesizer code | Differentiable synthesizer module |
| Preprocessing tools | ECoG signal processing pipeline |
| Visualization tools | Spectrogram and decoding result visualization |
| Training pipeline | Two-stage training with speech parameter guidance |

---

## Reference Count
48 references cited in the paper.
