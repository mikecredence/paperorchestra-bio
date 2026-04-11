# Experimental Log

> Pre-writing data tables and observations for the miniML synaptic event detection study.

---

## Datasets Used

| Dataset | Species | Preparation | Recording Type | Key Details |
|---------|---------|-------------|---------------|-------------|
| MF-GC (training) | Mouse | Cerebellar mossy fiber to granule cell | Voltage-clamp (mEPSCs) | Holding potential -100 mV or -80 mV; 50 kHz sampling; 2.9 kHz filtering |
| MF-GC (event-free) | Mouse | Same as above + synaptic blockers | Voltage-clamp | 50 uM D-APV, 10 uM NBQX, 10 uM bicuculline, 1 uM strychnine |
| Calyx of Held | Mouse (P9) | Brainstem auditory synapse | Voltage-clamp | Large-amplitude events |
| Human iPSC neurons | Human | iPSC-derived cortical glutamatergic | Voltage-clamp (sEPSCs) | 8-week cultures; holding potential -80 mV; ~51% neurons showed events |
| Zebrafish | Zebrafish | Various preparations | Electrophysiology | Spontaneous/miniature EPSCs |
| Drosophila | Drosophila | Neuromuscular junction / central | Electrophysiology | Spontaneous/miniature EPSCs |
| Simulated ground-truth | Synthetic | Event-free recording + generated events | Simulated | Multiple SNR levels for benchmarking |
| Optical recordings | Mouse | Various | Glutamate sensors, Ca2+ indicators, voltage imaging | Lower sampling rate; lower SNR |

---

## Model Architecture

| Layer | Type | Details |
|-------|------|---------|
| Block 1-N | 1D Convolution + ReLU + Average Pooling | Multiple blocks; extract temporal features from input segment |
| LSTM | Bidirectional LSTM | Captures temporal dependencies across convolutional output |
| Dense 1 | Fully connected | Intermediate representation |
| Dense 2 (output) | Fully connected + sigmoid | Outputs label in [0, 1] |

Table 1 in the paper provides the complete overview of model architecture parameters.

---

## Experiment 1: Model Training and Classification Performance

### Training Metrics

| Metric | Training Set | Validation Set | Notes |
|--------|-------------|----------------|-------|
| Loss (binary cross-entropy) | Decreasing over epochs | Decreasing, converges | Fig. 1C |
| Accuracy | Increasing over epochs | Increasing, converges | Fig. 1C |
| ROC AUC | ~1.0 | ~1.0 | Fig. 1D; dashed line = random classifier at 0.5 |

Fig. 1C shows loss and accuracy curves over training epochs for both training and validation sets. Both converge indicating no significant overfitting. Fig. 1D shows the ROC curve for the best-performing model with AUC near 1.0. Fig. 1E shows UMAP representation of training data at the input to the final layer, demonstrating clear linear separability of the two event classes after training.

### Saliency Analysis

Fig. 1-Supplement 1A shows saliency maps for four example events. Darker regions correspond to the most discriminative data segments, typically centered on the event waveform onset and peak. Fig. 1-Supplement 1B shows UMAP of the original (untransformed) training data with poor separability. Fig. 1-Supplement 1C shows UMAP after model transformation with clear separability.

### Impact of Dataset Size, Class Balance, and Architecture

| Dataset Size (fraction) | Loss | Accuracy | AUC | Notes |
|------------------------|------|----------|-----|-------|
| Small (e.g., 10%) | Higher | Lower | Lower | Fig. 1-Supplement 2A-D |
| Medium (e.g., 50%) | Moderate | Moderate | Moderate | Performance improves with more data |
| Full (100%) | Lowest | Highest | Highest | Best performance; log-scale x-axis |

Fig. 1-Supplement 2A-D show that loss decreases, accuracy increases, and AUC increases with larger training dataset sizes (5-fold cross-validation). Shaded areas represent standard deviation.

---

## Experiment 2: Event Detection in Continuous Recordings

### Detection Workflow Parameters

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| Window size | Length of input segment | Matches training data length |
| Stride | Step size for sliding window | Up to 5% of window size without performance loss |
| Min peak height | Threshold on confidence trace | Configurable; model is robust to choice |

Fig. 2A illustrates the detection workflow: time-series is reshaped with window + stride, model outputs confidence per window, peak detection localizes events.

### Detection Examples

Fig. 2B shows an example of event detection in a voltage-clamp recording from a cerebellar granule cell. Detected events are marked. The confidence trace shows clear peaks at event locations.

### Runtime Performance

| Hardware | Recording Duration | Sampling Rate | Total Samples | Runtime |
|----------|-------------------|---------------|---------------|---------|
| CPU only | 120 s | 50 kHz | 6,000,000 | Longer (varies by CPU) |
| GPU | 120 s | 50 kHz | 6,000,000 | < 20 s |

Fig. 2-Supplement 1A shows that runtime can be minimized by using stride sizes up to 5% of the window without impacting detection. Fig. 2-Supplement 1B compares runtimes across different hardware configurations for a standard 120-s recording at 50 kHz.

### Stride vs. Detection Performance

| Stride (% of window) | Detected Events | Runtime (relative) |
|----------------------|----------------|-------------------|
| 1% | Baseline count | Longest |
| 2% | ~Same as baseline | Shorter |
| 5% | ~Same as baseline | Much shorter |
| 10% | Slightly fewer | Even shorter |
| 25% | Noticeably fewer | Fastest |

Fig. 2-Supplement 1A: stride sizes up to 5% of event window preserve detection without loss; beyond that, events may be missed.

### Event-Free Control Data

| Condition | Events Detected | Notes |
|-----------|----------------|-------|
| Normal MF-GC recording | Many events | Fig. 2-Supplement 3A; confidence peaks above threshold |
| Same cell + synaptic blockers (NBQX, APV, Bicuculline, Strychnine) | 0 events | Fig. 2-Supplement 3B; no confidence peaks above threshold |

This validates that miniML does not produce false positives when synaptic transmission is pharmacologically blocked. Addition of bicuculline blocks tonic inhibition, reducing holding current and noise.

---

## Experiment 3: Systematic Benchmarking Against Existing Methods

### Methods Compared

| Method | Category | Implementation |
|--------|----------|---------------|
| miniML | Deep learning (CNN-LSTM) | This work |
| MiniAnalysis | Commercial software (manual) | Synaptosoft |
| Template matching (Clements-Bekkers) | Matched filter | Scaling factor approach |
| Deconvolution | Template-based | Wiener deconvolution approach |
| Finite-difference (threshold on derivative) | Threshold-based | First derivative crossing |
| Finite-difference (threshold on raw data) | Threshold-based | Amplitude threshold crossing |

### Benchmarking Setup

| Parameter | Value |
|-----------|-------|
| Ground truth generation | Event-free recordings superimposed with simulated events at known times and amplitudes |
| Amplitude distribution | Log-normal |
| SNR levels tested | Multiple (e.g., 9 dB, 10.8 dB, and others) |
| Evaluation metrics | Precision, Recall, F1 score |

Fig. 3A shows the benchmarking scheme. Fig. 3B shows example ground-truth data at SNR = 9 dB with event-free recording superimposed with generated events.

### Detection Performance at Various SNR Levels

| Method | Precision (high SNR) | Recall (high SNR) | F1 (high SNR) | Precision (low SNR) | Recall (low SNR) | F1 (low SNR) |
|--------|---------------------|-------------------|---------------|---------------------|------------------|--------------|
| miniML | Highest | Highest | Highest | Highest | Competitive | Highest |
| Template matching | Moderate | Moderate | Moderate | Lower | Moderate | Lower |
| Deconvolution | Moderate | Moderate | Moderate | Lower | Moderate | Lower |
| MiniAnalysis | Not tested at all SNRs | Not tested at all SNRs | N/A | N/A | N/A | N/A |
| Finite-diff (derivative) | Lower | Variable | Lower | Much lower | Variable | Much lower |
| Finite-diff (raw) | Lower | Variable | Lower | Much lower | Variable | Much lower |

Fig. 3C (left) shows detection method outputs for example data. Fig. 3C (right) shows improvement in SNR relative to the input for each method. MiniAnalysis is omitted from some panels.

### Extended Benchmarking and Threshold Dependence

| Method | Sensitivity to Threshold | Notes |
|--------|------------------------|-------|
| miniML | Minimal | Robust across a wide range of thresholds |
| Template matching | Moderate | Performance degrades with suboptimal threshold |
| Deconvolution | Moderate | Trade-off between precision and recall |
| Finite-difference methods | High | Strongly dependent on threshold setting |

Fig. 3-Supplement 1C shows recall, precision, and F1 for five detection methods across varying thresholds. miniML maintains high performance across threshold choices, while other methods show the typical precision-recall trade-off.

Fig. 3-Supplement 1A shows an example event-free recording and its power density spectrum. Fig. 3-Supplement 1B shows data with superimposed simulated events and the amplitude histogram at SNR 10.8 dB.

---

## Experiment 4: Generalization Across Preparations and Species

### Preparations Tested

| Preparation | Species | Event Type | Transfer Learning Required? |
|------------|---------|------------|---------------------------|
| Cerebellar granule cell (MF-GC) | Mouse | mEPSCs | No (training data source) |
| Calyx of Held | Mouse (P9) | mEPSCs | Minimal / TL |
| Human iPSC-derived neurons | Human | sEPSCs | TL recommended |
| Olfactory bulb / other | Zebrafish | sEPSCs / mEPSCs | TL with few hundred events |
| Neuromuscular junction | Drosophila | mEPSCs | TL with few hundred events |

Fig. 4-Supplement 1A-F show amplitude histograms and detected events for multiple preparations, comparing miniML against matched-filtering and finite-threshold approaches.

### Transfer Learning Requirements

| Scenario | Labeled Events Needed | Training Time | Notes |
|----------|----------------------|---------------|-------|
| Similar waveforms to training data | 0 (direct application) | None | Mouse cerebellar GC-like waveforms |
| Moderately different waveforms | ~100-300 labeled events | Minutes | Retraining via TL |
| Very different waveforms or data types | ~300-500 labeled events | Minutes | Full TL retraining recommended |

### Detection Comparison Across Methods per Preparation

| Preparation | miniML Unique Events | Template Match Unique | Finite-Diff Unique | Overlap |
|------------|---------------------|----------------------|-------------------|---------|
| Mouse GC | Some | Some | Some | Large overlap; see Fig. 4-Supplement 1B-C |
| Other preps | Similar pattern | Similar pattern | Similar pattern | See Fig. 4-Supplement 1D-F |

Fig. 4-Supplement 1B-C show color-coded examples of events unique to each method for mouse granule cell recordings. Fig. 4-Supplement 1D-F show the same for additional preparations.

---

## Experiment 5: Application to Optical Time-Series Data

### Optical Recording Types

| Sensor/Indicator | Signal Type | Sampling Rate | SNR | Challenge |
|-----------------|------------|---------------|-----|-----------|
| Glutamate reporters (e.g., iGluSnFR) | Extracellular glutamate transients | Lower than ephys | Low | Slow kinetics |
| Ca2+ indicators | Intracellular calcium transients | Lower than ephys | Low-moderate | Indirect readout |
| Voltage indicators | Membrane voltage | Variable | Low | Fastest of optical methods |

miniML was successfully applied to optical time-series via transfer learning, detecting subthreshold synaptic events in imaging data that pose particular challenges due to low sampling rate and low SNR.

---

## Experiment 6: GUI and Software Implementation

### Software Features

| Feature | Description |
|---------|-------------|
| Python package | Open-source implementation |
| GUI | Graphical user interface similar to MiniAnalysis / SimplyFire |
| Data loading | Load, inspect, and analyze electrophysiological data |
| Event marking | Detected events marked by red dots |
| Event parameters | Displayed in tabular form; individual events can be enlarged and rejected |
| Results export | Final results saved for downstream analysis |

Fig. 2-Supplement 2A shows the analysis workflow. Fig. 2-Supplement 2B shows a screenshot of the GUI.

---

## Electrophysiology Recording Parameters

| Parameter | Value |
|-----------|-------|
| Species | C57BL/6J mice (1-5 months; P9 for Calyx of Held) |
| Slice thickness | 300 um parasagittal |
| ACSF composition | 125 NaCl, 25 NaHCO3, 20 glucose, 2.5 KCl, 2 CaCl2, 1.25 NaH2PO4, 1 MgCl2 (mM) |
| Intracellular solution | 150 K-D-gluconate, 10 NaCl, 10 HEPES, 3 MgATP, 0.3 NaGTP, 0.05 EGTA (mM); pH 7.3 |
| Holding potential (mEPSCs) | -100 mV or -80 mV |
| Holding potential (mEPSPs) | Resting membrane potential |
| Filter frequency | 2.9 kHz |
| Digitization rate | 50 kHz |
| Recording duration | Typically 120 s |
| Liquid junction potential correction | +13 mV |
| Temperature | Room temperature (21-25 C) |

### Human iPSC Neuron Recording Parameters

| Parameter | Value |
|-----------|-------|
| Cell type | iPSC-derived cortical glutamatergic neurons |
| Culture age | 8 weeks |
| Holding potential | -80 mV |
| ACSF | 135 NaCl, 10 HEPES, 10 glucose, 5 KCl, 2 CaCl2, 1 MgCl2 (mM) |
| Fraction with events | ~51% of neurons |

---

## Summary of Key Figure Observations

| Figure | Observation |
|--------|-------------|
| Fig. 1A | Workflow overview: extract labeled segments, train DNN, apply to novel data |
| Fig. 1B | Model architecture: CNN blocks -> Bi-LSTM -> Dense layers -> [0,1] output |
| Fig. 1C | Training loss and accuracy converge for both training and validation |
| Fig. 1D | ROC AUC near 1.0 for best model |
| Fig. 1E | UMAP shows linear separability after model training |
| Fig. 2A | Sliding window detection workflow with confidence trace and peak detection |
| Fig. 2B | Example detection in cerebellar GC recording |
| Fig. 3A-C | Benchmarking shows miniML superior in precision and recall vs. 5 methods |
| Fig. 3-S1 | miniML performance robust to threshold; other methods show precision-recall trade-off |

---

## Reference Count
74 references cited in the paper.
