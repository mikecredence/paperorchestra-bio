# Idea Summary

## Working title
miniML: A Deep Learning Framework for Automated and Generalized Synaptic Event Analysis

## Core question
Can a supervised deep learning model (CNN-LSTM architecture) reliably detect and quantify spontaneous synaptic events in noisy electrophysiological time-series data, outperforming existing methods and generalizing across diverse preparations, species, and recording modalities?

## Motivation / gap
- Spontaneous synaptic events (miniature EPSCs/EPSPs) carry fundamental information about synaptic function and plasticity, but are difficult to detect due to low signal-to-noise ratio and stochastic occurrence
- Existing detection methods (threshold-based, template matching, deconvolution) suffer from high false positive rates and require extensive manual parameter tuning
- Current approaches involve a trade-off between precision and recall that depends on threshold choice, making results poorly reproducible across labs
- No existing tool generalizes well across different species, synaptic preparations, and recording techniques (electrophysiology vs. optical imaging) without substantial re-parameterization
- Manual event inspection remains common but is subjective, labor-intensive, and incompatible with high-throughput analysis

## Core contribution (bullet form)
- Built miniML, a CNN-LSTM deep learning classifier that achieves near-perfect classification accuracy (AUC close to 1.0) on training data with clear linear separability in UMAP space after model training
- Systematic benchmarking on simulated ground-truth data shows miniML outperforms five existing methods (MiniAnalysis, template matching, deconvolution, finite-difference approaches) in both precision and recall, especially at low SNR
- Detection performance is robust to threshold choice, effectively eliminating the precision-recall trade-off that plagues conventional methods
- Demonstrated generalization across mouse cerebellar granule cells, Calyx of Held, human iPSC-derived neurons, zebrafish, and Drosophila preparations
- Extended the approach to optical time-series data (glutamate sensors, calcium indicators, voltage imaging) via transfer learning with only a few hundred labeled events
- Provided open-source Python implementation with a graphical user interface for community adoption

## Method in brief
miniML uses a deep neural network combining 1D convolutional layers (CNN blocks with ReLU activation and average pooling), a bidirectional LSTM layer, and fully connected dense layers. The model takes a short segment of univariate time-series data as input and outputs a binary label (event vs. no-event) in the interval [0, 1]. Training is supervised using manually labeled segments from electrophysiological recordings. Binary cross-entropy serves as the loss function.

For event detection in continuous recordings, a sliding window approach is used: the time-series is reshaped with a window size matching the training data length and a configurable stride. The model output is treated as a confidence trace, and peak detection (with a configurable minimum peak height threshold) localizes events. Event parameters (amplitude, kinetics, timing) are then extracted from the detected events.

Transfer learning (TL) enables adaptation to new preparations or data types. An existing miniML model is retrained on a small set of labeled events (a few hundred) from the new preparation, updating the model weights to match the new event waveform characteristics. This makes the approach scalable to novel recording conditions, including optical imaging data with different sampling rates and SNR profiles. The model was benchmarked against five existing detection methods using simulated ground-truth data at varying SNR levels.

## Target venue
eLife
