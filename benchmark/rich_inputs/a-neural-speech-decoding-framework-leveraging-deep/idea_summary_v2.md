# Idea Summary

## Working title
A Neural Speech Decoding Framework Leveraging Deep Learning and Speech Synthesis

## Core question
Can a two-stage deep learning framework -- combining an ECoG decoder with a differentiable speech synthesizer guided by interpretable speech parameters -- reliably decode natural-sounding speech from cortical signals across a large cohort, including with causal (real-time-compatible) architectures and right-hemisphere electrode coverage?

## Motivation / gap
- Decoding speech from neural signals is essential for brain-computer interfaces restoring communication in patients with neurological deficits, but remains highly challenging
- Training data for neural-to-speech decoding is extremely limited in duration, while deep learning models require substantial data
- Speech production varies in rate, intonation, and pitch even within a single speaker producing the same word, complicating latent representations
- Prior approaches vary widely: linear models achieve about 0.6 PCC but with limited naturalness; deep models using articulatory representations sound robotic; generative approaches (WaveNet, GANs) produce natural sound but with limited accuracy
- Most previous methods use non-causal operations (using future neural signals), which is incompatible with real-time BCI deployment that requires causal-only processing
- Very little open-source code is available for replication and comparison of decoding approaches
- Prior work has focused on left-hemisphere decoding, with limited evidence for right-hemisphere speech decoding

## Core contribution (bullet form)
- Developed a novel two-stage framework: an ECoG Decoder that maps cortical signals to interpretable speech parameters (pitch, voicing, formant frequencies) paired with a differentiable Speech Synthesizer that converts parameters to spectrograms
- Achieved mean PCC of 0.804 (non-causal) / 0.798 (causal) with 3D ResNet across N=48 participants, with SWIN transformer closely following at 0.793/0.796
- Demonstrated that causal models achieve comparable performance to non-causal models (no significant difference for ResNet), enabling real-time BCI applications
- Successfully decoded speech from both left (n=32) and right (n=16) hemisphere electrode placements with no significant PCC difference
- Performed occlusion analysis identifying cortical regions contributing to decoding; non-causal models rely more on STG (auditory feedback), while causal models shift contribution to motor areas
- Released open-source code for the full pipeline including preprocessing and visualization tools

## Method in brief
The framework consists of two main components. First, a Speech Encoder and differentiable Speech Synthesizer form an audio-to-audio auto-encoder. The Speech Encoder extracts interpretable speech parameters (fundamental frequency F0, voicing, 6 formant frequencies with amplitudes, and noise parameters) from spectrograms via temporal convolution layers and channel MLPs. The Speech Synthesizer is a fully differentiable module that generates spectrograms by combining a voiced pathway (harmonic excitation filtered through 6 formant filters) with an unvoiced noise pathway. This auto-encoder is pre-trained on each participant's speech to establish reference speech parameters.

Second, the ECoG Decoder replaces the Speech Encoder at inference time, mapping ECoG signals directly to the same speech parameter space. Three architectures were compared: 3D ResNet (convolutional), LSTM (recurrent), and SWIN (transformer). The ResNet uses spatiotemporal convolutional layers with residual connections and pooling, followed by transposed convolutions for upsampling. Training uses the pre-trained speech parameters as guidance targets, enabling effective learning from limited neural-speech paired data.

Data came from 48 epilepsy surgery patients with implanted ECoG grids (5 hybrid-density with 128 electrodes, 43 low-density with 64 electrodes). Each participant performed 5 speech tasks (Auditory Repetition, Auditory Naming, Sentence Completion, Word Reading, Picture Naming) producing 50 unique words across 400 total trials. Models were trained per-participant using 350 trials (80%) and tested on 50 held-out trials (20%). ECoG signals were sampled at 2048 Hz, downsampled to 512 Hz, and preprocessed with artifact rejection and high-gamma band extraction.

## Target venue
Nature Machine Intelligence
