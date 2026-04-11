# Experimental Log: A Neural Speech Decoding Framework Leveraging Deep Learning and Speech Synthesis

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsDataWe employed our speech decoding framework across N=48 participants who consented to complete a series of speech tasks (see Methods Section: Datasets and Experiments).
- ECoG data were obtained from five participants with hybrid-density(HB) sampling (clinical-research grid) and 43 participants with low-density(LD) sampling (standard clinical grid), who took part in five speech tasks: Auditory Repetition (AR), Auditory Naming (AN), Sentence Completion (SC), Word Read
- We provided 50 repeated unique words (400 total trials per participant), all of which were analyzed locked to the onset of speech production.
- We trained a model for each participant using 80% of available data for this participant and evaluated the model on the remaining 20% of data (with the exception of the more stringent word-level cross-validation).Speech Decoding Performance and CausalityWe first aimed to directly compare decoding pe
- Our results show that ResNet outperforms the other models providing the highest Pearson correlation coefficient (PCC) across N=48 participants (mean PCC=0.804, 0.798 for noncausal, causal respectively) but closely followed by SWIN (mean PCC=0.793, 0.796 for non-causal, causal respectively) shown in 
- We find the same conclusion when evaluating three models using STOI+ [23], shown in Supplementary Fig.
- Previous reports typically employed non-causal models [5, 8, 10, 17], that could potentially use neural signals related to auditory and speech feedback, unavailable in realtime applications.
- 2a compares the decoding results of our models’ causal and non-causal versions.
- The causal ResNet model (PCC=0.798) achieved performance comparable to that of the non-causal model (PCC=0.804) with no significant differences between the two (Wilcoxon signed-rank test p = 0.1022).
- The same was true for the causal SWIN model (PCC=0.796) and its non-causal (PCC=0.793) counterpart (Wilcoxon signed-rank test p = 0.2794).
- In contrast, the performance of the causal LSTM model (PCC=0.713) was significantly inferior to that of its non-causal (PCC=0.757) version (Wilcoxon signed-rank test p = 0.0007).
- However, we did not find significant differences between causal ResNet and causal SWIN performance (Wilcoxon signed-rank test p = 0.1413).
- Since the ResNet and SWIN models had the highest performance and were on par with each other and their causal counterparts, we chose to focus further analyses on these causal models, which we believe are best suited for prosthetic applications.To ensure our framework can generalize well to unseen wo
- 2b demonstrate that performance on the held-out words is comparable to our standard trial-based held-out approach (i.e., Fig.
- For each parameter, we calculate the PCC between the decoded time series and the reference sequence showing an average PCC of 0.834 (voice weight, Fig.
- 2f), 0.827 (first formant f1, Fig.
- 2f), 0.895 (second formant f2, Fig.
- The fact that both non-causal and causal models could yield reasonable decoding results is encouraging.biorxiv;2023.09.16.558028v1/FIG2F2fig2Fig.
- 2Decoding performance comparing the original and decoded spectrograms across non-causal and causal models.a, Performance of ResNet, SWIN, and LSTM models with non-causal and causal operations across all participants (n=48; 43 low-density ECoG grids and 5 hybrid density grids).
- b, A stringent cross-validation showing the Causal ResNet model performance on unseen words during training from 5-folds where we ensured the training and validation sets in each fold do not overlap in unique words.
- The performance across all five validation folds is comparable to our trial-based validation and denoted for comparison as ResNet (identical to the ResNet causal model in 2a).
- (f) Decoded (dashed) and reference (solid) parameters for pitch (f0) and the first two formants (f1 and f2) are shown for the eight words as well as the PCC across participants (boxplots to the right).
- All boxplots represent the median, 25th and 75th quantiles across participants, and the yellow error bars denote the mean and standard error of the mean (across participants).biorxiv;2023.09.16.558028v1/FIG3F3fig3Fig.
- 3Comparison of decoding PCC under different settings of the 3D ResNet and 3D SWIN models.a, Comparison between left and right hemisphere participants, using causal models.
- No statistically significant differences in PCC exist between left (n=32) and right (n=16) hemisphere participants.
- b, An example hybrid density ECoG array, with a total of 128 electrodes.
- The 64 electrodes marked in red correspond to a low-density placement.
- The remaining 64 green electrodes, combined with red electrodes, reflect a hybrid density placement.
- c, Comparison between causal ResNet and causal SWIN models for the same participant across participants with hybrid-density (HB, n=5) or low-density (LD, n=43) ECoG grids.
- There are no statistically significant differences for 4 out of 5 participants.Left vs Right Hemisphere Decoding and Effect of Electrode DensityMost speech decoding studies focused on the language and speech-dominant left hemisphere ([24]).
- However, many patients who suffer damage to the left hemisphere are unable to speak ([25]), and right hemisphere decoding could serve as a valuable clinical target.
- For both our ResNet and SWIN decoders, we found robust speech decoding from the right hemisphere (ResNet PCC=0.790, SWIN PCC=0.781), which were not significantly different from the left (Fig.
- 3a, ResNet Wilcoxon rank-sum test, p=0.312; SWIN Wilcoxon rank-sum test, p=0.325).
- S1b, ResNet Wilcoxon rank-sum test, p=0.108; SWIN Wilcoxon rank-sum test, p=0.092).
- Next, we assessed the impact of the electrode sampling density for speech decoding, as many previous reports employ higher-density grids (0.4 mm) with more closely spaced contacts than typical clinical grids (1 cm).
- 3b), which had typical low density (i.e., LD) electrode sampling as well as additional electrodes interleaved.
- 3c), with a slight advantage in STOI+, shown in Supplementary Fig.
- 3d) suggest that decoding results were not significantly different from each other (with the exception of Participant 2), including our evaluation of STOI+ (Fig.
- Together, these results suggest that our models can learn speech representations well from both the high and low spatial sampling of the cortex with the exciting finding of robust speech decoding from the right hemisphere.biorxiv;2023.09.16.558028v1/FIG4F4fig4Fig.
- 4We visualize the contribution of each cortical location to the decoding result by both causal or non-causal decoding models through an occlusion analysis.The contribution of each electrode region in each participant is projected onto the standardized Montreal Neurological Institute (MNI) brain anat
- 4 show similar contribution values for both ResNet and SWIN models.

## Figure Descriptions

### Fig. 1
The proposed neural speech decoding framework.The upper part shows the ECoG-to-speech decoding pipeline. The ECoG Decoder generates time-varying speech parameters from ECoG signals. The Speech Synthesizer generates spectrograms from the speech parameters. A separate spectrogram inversion algorithm c

### Fig. 2
Decoding performance comparing the original and decoded spectrograms across non-causal and causal models.a, Performance of ResNet, SWIN, and LSTM models with non-causal and causal operations across all participants (n=48; 43 low-density ECoG grids and 5 hybrid density grids). The Pearson Correlation

### Fig. 3
Comparison of decoding PCC under different settings of the 3D ResNet and 3D SWIN models.a, Comparison between left and right hemisphere participants, using causal models. No statistically significant differences in PCC exist between left (n=32) and right (n=16) hemisphere participants. b, An example

### Fig. 4
We visualize the contribution of each cortical location to the decoding result by both causal or non-causal decoding models through an occlusion analysis.The contribution of each electrode region in each participant is projected onto the standardized Montreal Neurological Institute (MNI) brain anato

### Fig. 5
Differentiable Speech Synthesizer architecture.Our Speech synthesizer generates the spectrogram at time t by combining a voice component and an unvoice component based on a set of speech parameters at t. The upper part represents the voice pathway, which generates the voice component by passing a ha

### Fig. 6
Speech Encoder and ECoG Decoder.a, Speech Encoder architecture. We input a spectrogram into a network of temporal convolution layers and channel MLPs that produce speech parameters. b, ECoG Decoder architecture using the 3D ResNet architecture. We first use several temporal and spatial convolutional

## References
Total references in published paper: 48

### Key References (from published paper)
- Biosignal-based spoken communication: A survey. IEEE/ACM Transactions on Audio (, 2017)
- The current state of electrocorticography-based brain–computer interfaces (, 2020)
- Brain-computer interface: applications to speech decoding and synthesis to augment communication (, 2022)
- Real-time decoding of question-and-answer speech dialogue using human cortical activity (, 2019)
- Neuroprosthesis for decoding speech in a paralyzed person with anarthria (, 2021)
- Automatic speech recognition from neural signals: a focused review (, 2016)
- The potential for a speech brain– computer interface using chronic electrocorticography (, 2019)
- Speech synthesis from ecog using densely connected 3d convolutional neural networks (, 2019)
- Brain2char: a deep architecture for decoding text from brain recordings (, 2020)
- Machine translation of cortical activity to text with an encoder–decoder framework (, 2020)
- Stimulus speech decoding from human cortex with generative adversarial network transfer learning (, 2020)
- Impact of vocal effort variability on automatic speech recognition (, 2012)
- Automatic speech recognition and speech variability: A review (, 2007)
- Decoding spectrotemporal features of overt and covert speech from the human cortex (, 2014)
- Real-time synthesis of imagined speech processes from minimally invasive recordings of neural activi (, 2021)
- Speech synthesis from neural decoding of spoken sentences (, 2019)
- Generating natural, intelligible speech from brain activity in motor, premotor, and inferior frontal (, 2019)
- Deep residual learning for image recognition (, 2016)
- Swin transformer: Hierarchical vision transformer using shifted windows (, 2021)
- Long short-term memory (, 1997)
- Intelligibility prediction for speech mixed with white gaussian noise at low signal-to-noise ratios (, 2021)
- The cortical organization of speech processing (, 2007)
- Chronic apraxia of speech and broca’s area (, 2013)
- Distributed feedforward and feedback processing across perisylvian cortex supports human speech (, 2021)
- Differential representation of articulatory gestures and phonemes in precentral and inferior frontal (, 2018)
- Brain-to-text: decoding spoken phrases from phone representations in the brain (, 2015)
- Synthesizing speech from intracranial depth electrodes using an encoder-decoder framework (, 2021)
- Towards closed-loop speech synthesis from stereotactic eeg: A unit selection approach (, 2022)
- Spectral modeling synthesis: A sound analysis/synthesis system based on a deterministic plus stochas (, 1990)
- Sensory–motor transformations for speech occur bilaterally (, 2014)

## Ground Truth Reference
- Figures: 6
- Tables: 0
- References: 48