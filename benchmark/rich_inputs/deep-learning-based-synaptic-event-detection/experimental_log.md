# Experimental Log: A deep learning framework for automated and generalized synaptic event analysis

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- RESULTSminiML enables highly accurate classification of synaptic eventsTo investigate whether an AI model can detect stochastic synaptic events in noisy single-trial time-series data, we designed a deep neural network consisting of CNN, long short-term memory (LSTM), and fully connected dense layers
- The CNN-LSTM model takes a section of a univariate time-series recording as input and outputs a label for that section of data (Figure 1B).
- The trained classifier can then be applied to unseen time-series data to localize events.biorxiv;2023.11.02.565316v3/FIG1F1fig1Figure 1:High performance classification of synaptic events using a deep neural network.(A) Overview of the analysis workflow.
- Data is input to a convolutional network consisting of blocks of 1D convolutional, ReLU, and average pooling layers.
- The final output is a label in the interval [0, 1].
- (E) UMAP representation of the training data as input to the final layer of the model, indicating linear separability of the two event classes after model training.Figure 1—figure supplement 1.
- Visualization of model training.Figure 1 —figure supplement 2.
- Impact of dataset size, class balance, and model architecture on training performance.biorxiv;2023.11.02.565316v3/FIG1S1F10fig1s1Figure 1-figure supplement 1Visualization of model training.(A) Saliency maps (Simonyan et al., 2013) for four example events of the training data.
- Model training greatly improves linear separability of the two labeled event classes.biorxiv;2023.11.02.565316v3/FIG1S2F11fig1s2Figure 1-figure supplement 2Impact of dataset size, class balance, and model architecture on training performance.(A) To test how size of the training dataset impacts model
- (G) Accuracy and F1 score for different model architectures plotted against number of free parameters.
- EarlyStopping was used for all models to prevent overfitting (difference between training and validation accuracy <0.3%).
- ResNet, Residual Neural Network; MLP, multi-layer perceptron.To train the miniML model, we first extracted a large number of synaptic events and corresponding event-free sections from previous voltage-clamp recordings of cerebellar mossy fiber to granule cell (MF–GC) miniature excitatory postsynapti
- In total, the training data comprised ∼30,000 samples that were split into training and validation sets (0.75/0.25).
- Across training epochs, loss decreased and accuracy increased, stabilizing after ∼30 epochs (Figure 1C).
- The model with the highest validation accuracy was selected for further use, achieving 98.4% (SD 0.1, fivefold cross-validation).
- Saliency map analysis (Simonyan et al., 2013) indicated that the AI model mainly relied on the data sections around the peak of synaptic events to discriminate with respect to the labels (Figure 1—figure supplement 1).
- The trained miniML model achieved an area under the receiver operating characteristic (ROC) curve close to 1 (Figure 1D), indicating almost perfect separability of the classes (Figure 1E, Figure 1—figure supplement 1).
- Deep learning typically requires large datasets for training (van der Ploeg et al., 2014).
- However, the performance gain was marginal when exceeding 5,000 samples (<0.2%, Figure 1—figure supplement 2), indicating that relatively small datasets suffice for effective model training (Bailly et al., 2022).
- To apply the trained classifier to detect events in arbitrarily long data, we used a sliding window approach (Figure 2A).
- We used a stride for the sliding window, which reduces the number of inferences needed and speeds up the computation time while maintaining high detection performance (Figure 2—figure supplement 1).
- By reshaping the data into short sections, model inference can be run in batches and employ parallel processing techniques, including graphics processing unit (GPU) computing, resulting in analysis times of a few seconds for minute-long recordings (Figure 2—figure supplement 1).
- To facilitate the use of the method, miniML also includes a graphical user interface (Figure 2—figure supplement 2).biorxiv;2023.11.02.565316v3/FIG2S1F12fig2s1Figure 2-figure supplement 1Fast computation time for event detection using miniML.(A) Detected events and analysis runtime plotted versus st
- Note that runtime can be minimized by using stride sizes up to 5% of the event window size without impacting detection performance.
- (B) Analysis runtime with different computer hardware for a 120-s long recording at 50 kHz sampling (total of 6,000,000 samples).
- GPU computing enables analysis runtimes shorter than 20 s.biorxiv;2023.11.02.565316v3/FIG2S2F13fig2s2Figure 2-figure supplement 2A graphical user interface for miniML.(A) Workflow for synaptic event analysis using miniML.
- The final results can be saved in different formats via the GUI.biorxiv;2023.11.02.565316v3/FIG2F2fig2Figure 2:Applying AI-based classification to robustly detect synaptic events in electrophysiological time-series data.(A) Event detection workflow using a deep learning classifier.
- Dashed line indicates minimum peak height of 0.5, orange circles indicate event localizations.
- (D) Event analysis for the cell shown in (B) (total recording time, 120 s).
- Bottom: Event amplitude histogram.Figure 2—figure supplement 1.
- Fast computation time for event detection using miniML.Figure 2—figure supplement 2.
- A graphical user interface for miniML.Figure 2—figure supplement 3.
- miniML performance on event-free data.biorxiv;2023.11.02.565316v3/FIG2S3F14fig2s3Figure 2-figure supplement 3miniML performance on event-free data.(A) Confidence (top) and raw data with detected events from a MF–GC recording.
- Note that addition of Bicuculline blocks tonic inhibition in cerebellar GCs, causing a reduction in holding current and reduced noise (Kita et al., 2021).The output of the miniML model predicts the label—no event or event—for each time step (i.e., stride) with a numerical value ranging from zero to 
- While 0.5 represents a reasonable minimum peak value, the exact choice is not critical to detection performance (see below).
- Figure 2B illustrates the sliding window approach to detect spontaneous events in time-series data, such as a continuous voltage-clamp recording of spontaneous mEPSCs in a cerebellar GC.
- miniML provided a clear peak for all synaptic events present, without false positives (Figure 2C, Figure 2—figure supplement 3), allowing fast and reliable event quantification (Figure 2D).
- These data demonstrate that a deep learning model can be applied to detect synaptic events in electrophysiological time-series data.AI-based event detection is superior to previous methodsTo benchmark the AI model’s event detection performance, we compared it with commonly used template-based approa
- We also included a Bayesian event detection approach (Merel et al., 2016), SimplyFire (Mori et al., 2024), and the automated event detection routine of MiniAnalysis software (Synaptosoft Inc.).
- To compare synaptic event detection methods, we developed a standardized benchmarking pipeline (Figure 3A).
- We first performed event-free voltage-clamp recordings from mouse cerebellar GCs (in the presence of blockers of inhibitory and excitatory transmission; see Materials and Methods and Figure 2—figure supplement 3).
- We then generated synthetic events with a two-exponential time course and superimposed these on the raw recording to produce ground-truth data (Figure 3B–C).
- Event amplitudes were drawn from a log-normal distribution (Figure 3—figure supplement 1) with varying means to cover the range of SNRs typically observed in recordings of miniature events (2–15 dB, data from n = 170 GC recordings, Figure 3D).
- To measure detection performance, we calculated recall (i.e., sensitivity), precision (fraction of correct identifications) and the F1 score.
- Recall depended on SNR for all methods, with miniML and deconvolution showing the highest values (Figure 3E).
- The precision was highest for miniML, which detected no false positives at any SNR, in contrast to all other methods (Figure 3F).
- When assessing overall performance, miniML provided the highest F1 scores across SNRs (Figure 3G).
- In addition, miniML showed superior results when changing event kinetics, indicating higher robustness to variable event shapes (Figure 3H and Figure 3—figure supplement 1), which may be particularly important in neurons with diverse synaptic inputs due to mixed receptor populations (Lesperance et a
- Bottom: Amplitude histogram of simulated events for a signal-to-noise ratio (SNR) of 10.8 dB.
- (C) Recall, precision and F1 score for five detection methods with simulated events that have a 2× faster decay than in Figure 3.
- (D) Same as in (C), but for events with a 4.5× slower decay time constant.
- (E) Runtime of five different synaptic event detection methods for a 120-s section of data recorded with 50 kHz sampling rate.
- * miniML was run using a GPU, and data were downsampled to 20 kHz for the Bayesian analysis.
- (G) F1 score versus threshold (in % of default threshold value, range 5–195) for different methods.biorxiv;2023.11.02.565316v3/FIG3F3fig3Figure 3:Systematic benchmarking demonstrates that AI-based event detection is superior to previous methods.(A) Scheme of event detection benchmarking.
- Depicted example data have a signal-to-noise ratio (SNR) of 9 dB.
- (D) SNR from mEPSC recordings at MF–GC synapses (n = 170, whiskers cover full range of data).
- (E–G) Recall, precision, and F1 score versus SNR for the six different methods.
- (H) Average F1 score versus event kinetics.
- threshold (in % of default threshold value, range 5–195) for different methods.
- Dashed line indicates true event number.Figure 3>—figure supplement 1.
- Extended benchmarking and threshold dependence of event detection.Conventional event detection methods typically produce a detection trace with a shape identical to the input data and values in an arbitrary range (Figure 3C).
- In contrast, miniML generates output in the interval [0, 1], which can be interpreted as the confidence of event occurrence.
- In our benchmark scenario, miniML and the Bayesian method provided the greatest discrimination from background noise (Figure 3C).
- Intriguingly, miniML’s detection trace peaks did not depend on event amplitudes, setting it apart from other methods (Figure 3—figure supplement 1).
- For template-based methods, recommendations on threshold selection are provided (Clements and Bekkers, 1997; Perńıa-Andrade et al., 2012), but users usually need to adjust this parameter according to their specific data.
- To investigate the threshold dependence of different methods, we systematically varied the threshold and analyzed the number of detected events and the F1 score.
- Notably, miniML’s detection performance remained consistent over a wide range (5–195%, Figure 3I–J and Figure 3—figure supplement 1), with false positives occurring only at the lower threshold limit (5%, corresponding to a cutoff value of 0.025 in the detection trace).
- Conversely, the other detection methods were very sensitive to threshold changes (Figure 3J and Figure 3—figure supplement 1) due to the comparatively low SNR ratio of the output traces (but note that the Bayesian method is only slightly threshold dependent).
- These comparisons underscore that miniML requires no prior knowledge of the exact event shape and is virtually threshold independent, thus enabling reliable event detection.miniML reliably detects spontaneous synaptic events in out-of-sample dataWe trained the miniML model using data from cerebellar
- Comparison with several previous detection methods revealed that miniML detected more events with a waveform that is consistent with mEPSCs (Figure 4D, Figure 4—figure supplement 1).
- We recorded and analyzed data from the mouse calyx of Held synapse (Figure 4E), a large axosomatic synapse in the auditory brainstem that relays rate-coded information over a large bandwidth and with high temporal precision.
- Despite being trained on cerebellar MF–GC data, miniML accurately detected mEPSCs in these recordings (Figure 4F–H).
- To test whether miniML could also detect events with slower kinetics, we applied it to recordings from cerebellar Golgi cells (Figure 4I) (Kita et al., 2021).
- miniML reliably detected synaptic events in these recordings (Figure 4J–L), although event decay kinetics were slower compared to the training data (Golgi cell, 1.83 ms (SD 0.44 ms, n = 10 neurons), GC training data, 0.9 ms).
- We patch-clamped neurons in eight-week-old cultures of predominantly cortical glutamatergic identity (Asadollahi et al., 2023) and recorded spontaneous synaptic events in voltage-clamp (Figure 4M).
- Using miniML on these human iPSC-derived neuron data showed robust detection of synaptic events (Figure 4N–P), which had an average frequency of 0.15 Hz (SD 0.24 Hz, n = 56 neurons).
- miniML also provided higher event detection accuracy than template-based or finite-threshold-based detection methods, which are prone to false positives (Figure 4D,H,L,P, Figure 4—figure supplement 1).biorxiv;2023.11.02.565316v3/FIG4S1F16fig4s1Figure 4-figure supplement 1Event detection in different
- Due to the slower event kinetics, miniML was run with a 1.5× larger window size.
- Example event traces were filtered for display purposes with a 18-samples Hann window.biorxiv;2023.11.02.565316v3/FIG4F4fig4Figure 4:Application of miniML to electrophysiological recordings from diverse synaptic preparations.(A) Schematic and example voltage-clamp recordings from mouse cerebellar GC
- miniML consistently detects spontaneous events in all four preparations and retrieves more events than matched-filtering approaches.Figure 4—figure supplement 1.
- Event detection in different synaptic preparations.Generalization of miniML to diverse event and data types via transfer learningWhile applicable to out of sample data (Figure 4), simulations indicated that larger differences in event kinetics and waveform may ultimately hinder detection when using 
- TL is a powerful technique in machine learning that allows for the transfer of knowledge learned from one task or domain to another (Caruana, 1994; Yosinski et al., 2014).
- TL is widely used with CNNs to take advantage of large pre-trained models and repurpose them to solve new, unseen tasks (Theodoris et al., 2023).
- Importantly, only a part of the network needs to be trained for the novel task, which significantly reduces the number of training samples needed and speeds up training while avoiding overfitting (Yosinski et al., 2014).
- We therefore reasoned that TL based on freezing the convolutional layers during training of our pre-trained network could be used to train a new model to detect events with different shapes and/or kinetics, using a lower number of training samples (Figure 5A).biorxiv;2023.11.02.565316v3/FIG5S1F17fig
- miniML robustly detects events with up to ∼4-fold slower kinetics (dark blue, dashed line indicates 80% recall).
- Data are normalized to MF–GC mEPSCs (dashed line).biorxiv;2023.11.02.565316v3/FIG5F5fig5Figure 5:Transfer learning allows analyzing different types of events with small amounts of training data.(A) Illustration of the transfer learning (TL) approach.
- Indicated subsets of the dataset were split into training and validation sets; lines are averages of fivefold crossvalidation, shaded areas represent 95% CI.
- TL models yield comparable classification performance with reduced training time using only 12.5% of the samples.
- Dashed line represents identity, solid line with shaded area represents linear regression.Figure 5—figure supplement 1.
- Recall depends on event kinetics.Figure 5—figure supplement 2.
- Transfer learning facilitates model training across different datasets.biorxiv;2023.11.02.565316v3/FIG5S2F18fig5s2Figure 5-figure supplement 2Transfer learning facilitates model training across different datasets.(A) Loss and accuracy versus number of training dataset samples for three different dat
- Points are averages of fivefold cross-validation and shaded areas represent 95% CI.
- (B) Average AUC, accuracy, and training time for TL using 500 samples, and full training using 4,000 samples.
- Error bars denote 95% CI.We tested the use of TL for miniML with recordings of miniature excitatory postsynaptic potentials (mEPSPs) in mouse cerebellar GCs.
- Whereas accuracy increased and loss decreased with the number of samples (Figure 5B), TL models performed well with as few as 400 samples.
- Under these conditions, accuracy was only slightly lower than for full training with almost ten times the sample size (median accuracy, 95.4 versus 96.1%; Figure 5C).
- Across different datasets, TL-trained models performed comparably to those trained from scratch (Figure 5—figure supplement 2).
- Recording miniature EPSPs and EPSCs in the same cerebellar GCs (Figure 5D–E) enabled us to compare detection performance via event frequency.
- However, their kinetics were considerably slower due to the charging of the plasma membrane (Figure 5E).
- Remarkably, the average event frequencies were very similar in the two different recording modes (voltage-clamp: 0.49 Hz, SD 0.53 Hz, current-clamp: 0.54 Hz, SD 0.6 Hz, n = 15 for both) and highly correlated across neurons (Figure 5F).
- To evaluate miniML’s performance in such complex scenarios, we analyzed a dataset recorded from principal neurons of the adult zebrafish telencephalon (Rupprecht and Friedrich, 2018).
- We focused on spontaneous excitatory inputs to these neurons, characterized by diverse event shapes and frequencies (Rupprecht and Friedrich, 2018).
- Training via TL (see Materials and Methods) yielded a model that enabled the reliable detection of spontaneous excitatory currents (Figure 6A).
- Analysis of event properties across cells revealed broad distributions of event statistics (Figure 6B), including a large diversity of event rise and decay kinetics (Figure 6B–C).
- We next used the extracted event kinetics features of individual neurons (Figure 6D–H) to demonstrate miniML’s utility in better understanding the diversity of an existing dataset.
- We mapped the recorded neurons to an anatomical reference and plotted decay times as a function of their position but did not find a strong relationship (Figure 6I; correlation with position p>0.05 in all 3 dimensions).
- Consistent with this idea, we observed correlations between decay and rise times across neurons (Figure 6J).
- Furthermore, the distribution of decay times (examples shown in Figure 6H) was broader for neurons with longer decay times (Figure 6K), suggesting a broader distribution of distances from synapses to the cell body.
- Input resistance was negatively correlated with decay times across neurons (Figure 6L), consistent with the hypothesis that diverse event kinetics across neurons are determined by the conditions of synaptic event propagation to the soma and, more specifically, cell size.
- miniML consistently extracted synaptic events across a spectrum of event kinetics, enabling the identification and investigation of key factors determining event kinetics and other event-related properties across neurons.biorxiv;2023.11.02.565316v3/FIG6F6fig6Figure 6.Synaptic event detection for neu
- (B) Extraction of amplitudes, event frequencies, decay times, and rise time for all neurons in the dataset (n = 34).
- (L) Input resistance as a proxy for cell size is negatively correlated with the decay time.miniML robustly detects mEPSC differences upon genetic receptor perturbationWe next applied miniML to analyze data obtained from the Drosophila melanogaster larval neuromuscular junction (NMJ) (Baccino-Calace 
- The TL model was able to reliably detect synaptic events in wild-type (WT) NMJ recordings (Figure 7A–C).
- We next assessed event detection upon deletion of the non-essential glutamate receptor subunit GluRIIA, which causes a strong reduction in mEPSC amplitude and faster kinetics (DiAntonio et al., 1999).
- A separate TL model allowed reliable synaptic event detection in recordings from GluRIIA mutant larvae (Figure 7D–F).
- We observed a 54% reduction in mEPSC amplitude compared to WT (Figure 7G), consistent with previous reports (DiAntonio et al., 1999; Petersen et al., 1997).
- In addition, the event frequency was reduced by 64% (Figure 7H).
- Although event amplitude distributions had a similar shape in both genotypes (Figure 7C and F), small events below the detection limit in GluRIIA synapses may contribute to the observed frequency difference.
- Half decay and rise times were also shorter at GluRIIA than at WT NMJs (−58% and −18%, respectively) (Figure 7I–J), which can be explained by the faster desensitization of the remaining GluRIIB receptors (DiAntonio et al., 1999).
- Thus, miniML can be applied to two-electrode voltage clamp recordings at the Drosophila NMJ and robustly resolves group differences upon genetic receptor perturbation.biorxiv;2023.11.02.565316v3/FIG7F7fig7Figure 7.Event detection at Drosophila neuromuscular synapses upon altered glutamate receptor c
- The mean difference is depicted as a dot (black); the 95% confidence interval is indicated by the ends of the vertical error bar.
- Recent developments of highly sensitive fluorescent probes have enabled the recording of synaptic events using various imaging techniques (Abdelfattah et al., 2023; Aggarwal et al., 2023; Hao et al., 2024; Ralowicz et al., 2024).
- Nevertheless, the waveforms of imaged synaptic release events, voltage changes, or Ca2+ transients closely resemble those used to train miniML.
- Thus, we hypothesized that miniML could also be employed for event detection in fluorescence imaging data.We first used miniML to analyze a previously published dataset (Aggarwal et al., 2023) from rat neuronal cultures expressing the glutamate sensor iGluSnFR3 (Figure 8A–B).
- Given the low sampling rate of the imaging (100 Hz), we upsampled the data by a factor of 10 to match the model’s input shape.
- The TL model was subsequently applied to all detected sites (n = 1524) within the widefield recording (Aggarwal et al., 2023).
- A qualitative assessment of the imaging traces showed excellent event detection, with miniML consistently localizing the iGluSnFR3 fluorescence transients at varying SNRs (Figure 8C).
- The detected optical minis had similar kinetics to those reported in (Aggarwal et al., 2023) (10–90% rise time, median 21.8 ms; half decay time, median 48.7 ms, Figure 8D).
- In addition, analysis of event frequencies across sites revealed a power-law distribution (Figure 8E), consistent with fractal behavior of glutamate release (Lowen et al., 1997).
- Thus, miniML can reliably detect synaptic release events in time-series data from iGluSnFR3 recordings.biorxiv;2023.11.02.565316v3/FIG8F8fig8Figure 8.Optical detection of spontaneous glutamate release events in cultured neurons using iGluSnFR3 and miniML.(A) miniML was applied to recordings from rat
- Data from (Aggarwal et al., 2023).
- (B) Example epifluorescence image of iGluSnFR3-expressing cultured neurons.
- (C) ΔF/F0 traces for the regions shown in (B).
- (E) Top: Histogram with kernel density estimate (solid line) of event amplitudes for n = 1524 ROIs of the example in (B).
- Bottom: Event frequency histogram.To further investigate miniML’s performance in imaging data, we performed simultaneous electrophysiological and fluorescence recordings of mEPSPs in cultured rat hippocampal neurons expressing ASAP5-Kv (Hao et al., 2024) at physiological temperature (Figure 9A–B).
- ASAP5 allows resolving small voltage changes in the mV-range, as illustrated by the close correlation of optical and current-clamp signals (Figure 9C).
- However, event detection is more challenging in voltage imaging data due to the lower SNR compared to electrophysiological recordings (ASAP5: 2.26, SD 0.46; electrophysiology: 4.79, SD 0.74; n = 5 neurons; Figure 9—figure supplement 1).biorxiv;2023.11.02.565316v3/FIG9S1F19fig9s1Figure 9-figure suppl
- (B) Overlay of simultaneous current-clamp and ASAP5 recording.
- (C) Examples of mEPSPs detected in the electrophysiology data that were either detected by miniML in ASAP5 data (orange dots) or missed (blacked dots).
- Line is a linear fit to the data (slope = 0.95 mV/−%ΔF/F0, Pearson correlation coefficient = 0.83).
- (E) Event half decay time (Left) and rise time (Right) for five neurons from electrophysiology (’Ephys’) and ASAP5 data.
- The lower sampling rate of imaging acquisition (400 Hz) vs.
- electrophysiology (10,000 Hz) likely contributes to the slower event kinetics observed in ASAP5 data.biorxiv;2023.11.02.565316v3/FIG9F9fig9Figure 9:Optical detection of mEPSPs in cultured rat hippocampal neurons using ASAP5 and miniML.(A) Event detection in simultaneous recordings of membrane voltag
- (B) Example epifluorescence image of an ASAP5-Kv-expressing cultured rat hippocampal neuron.
- (C) ΔF/F0 trace (Top) and simultaneous current-clamp recording (Bottom) from the neuron shown in (B).
- Bottom: Amplitudes measured in optical and electrophysiological data are highly correlated (Pearson correlation coefficient r = 0.9).
- (F) Comparative analysis of detection performance in ASAP5 data.
- (G) Example ASAP5 recording with detected event positions indicated for different analysis methods (miniML, template matching, deconvolution).
- (H) Precision and Recall of all three detection methods for n = 5 neurons.
- miniML showed highest recall (miniML, 0.38±0.05; template matching, 0.25±0.05 (Cohen’s d, 1.25); deconvolution, 0.09±0.01 (Cohen’s d, 3.87); mean ± SEM) with similar precision (0.93±0.01; 0.95±0.02; 0.8±0.1).
- Bars are median values.Figure 9—figure supplement 1.
- mEPSP detection in ASAP5 recordings.Figure 9—figure supplement 2.
- Methods comparison for event detection in ASAP5 recordings.biorxiv;2023.11.02.565316v3/FIG9S2F20fig9s2Figure 9-figure supplement 2Methods comparison for event detection in ASAP5 recordings.(A) Average waveforms of detected events in ASAP5 data for miniML (n = 101 events), template-matching (n = 82 e
- Data are from the example shown in Figure 9C, shaded areas represent SEM.
- (B) Recall of events in ASAP5 data versus mEPSP amplitude for miniML, template-matching, and deconvolution.
- (C) F1 score for event detection in ASAP5 data was higher using miniML (0.53±0.04, mean ± SEM) than for template-matching (0.39±0.05; Cohen’s d, 1.35) and deconvolution (0.17±0.01; Cohen’s d, 5.1).
- Bars are median values, n = 5 neurons.Photon shot noise and other sources of noise in the imaging setup not only limit the SNR, but can also lead to spurious event detection (Sjulson and Miesenbö ck, 2007; Wilt et al., 2013).We trained separate miniML TL models to detect mEPSPs in optical and curren
- Optical detection yielded events that closely resembled mEPSPs, with slightly slower decay and rise kinetics (Figure 9E, Figure 9—figure supplement 1).
- Analysis of the corresponding amplitudes of mEPSPs and optically detected events confirmed that ASAP5 linearly reports subthreshold voltage changes in neurons (Figure 9E), in line with previous reports (Hao et al., 2024).
- These results demonstrate that miniML can detect optical mEPSPs recorded using ASAP5 under challenging low SNR conditions.
- To provide a more quantitative assessment of detection performance, we compared miniML to established template-based analysis methods (Figure 9F).
- We quantified the detection of events by different methods in imaging data relative to electrophysiology, with threshold settings of the matched-filtering approaches adjusted to achieve ∼90% precision.
- At comparable levels of precision, miniML demonstrated superior recall of mEPSPs compared with template matching or deconvolution (Figure 9G–H).
- Notably, miniML detected ∼40% of mEPSPs in optical data, a substantial improvement over template-based methods (Figure 9H, Figure 9—figure supplement 2).

## Tables

### Table 1.
> Overview of model architecture


## Figure Descriptions

### Figure 1:
High performance classification of synaptic events using a deep neural network.(A) Overview of the analysis workflow. Data segments from electrophysiological recordings are extracted and labeled to train an artificial neural network. The deep learning-based model is then applied to detect events in 

### Figure 1-figure supplement 1
Visualization of model training.(A) Saliency maps (Simonyan et al., 2013) for four example events of the training data. Darker regions indicate discriminative data segments. Data and saliency values are min-max scaled. (B) The miniML model transforms input to enhance separability. Shown is a Uniform

### Figure 1-figure supplement 2
Impact of dataset size, class balance, and model architecture on training performance.(A) To test how size of the training dataset impacts model training, we took random subsamples from the MF–GC dataset and trained miniML models using fivefold cross validation. (B–D) Comparison of loss (B), accurac

### Figure 2-figure supplement 1
Fast computation time for event detection using miniML.(A) Detected events and analysis runtime plotted versus stride. Note that runtime can be minimized by using stride sizes up to 5% of the event window size without impacting detection performance. (B) Analysis runtime with different computer hard

### Figure 2-figure supplement 2
A graphical user interface for miniML.(A) Workflow for synaptic event analysis using miniML. Optional steps include data pre-processing, model selection, and event rejection. (B) Screenshot of the graphical user interface (GUI). Users can use the GUI to load, inspect, and analyze data. After running

### Figure 2:
Applying AI-based classification to robustly detect synaptic events in electrophysiological time-series data.(A) Event detection workflow using a deep learning classifier. Time-series data are reshaped with a window size corresponding to length of the training data and a given stride. Peak detection

### Figure 2-figure supplement 3
miniML performance on event-free data.(A) Confidence (top) and raw data with detected events from a MF–GC recording. Dashed line indicates miniML minimum peak height. (B) Recording from the same cell after addition of blockers of synaptic transmission (NBQX, APV, Bicuculline, Strychnine). miniML doe

### Figure 3-figure supplement 1
Extended benchmarking and threshold dependence of event detection.(A) Example event-free recording (Top) and power density spectrum of the data (Bottom). (B) Top: Data trace from (A) superimposed with simulated synaptic events. Bottom: Amplitude histogram of simulated events for a signal-to-noise ra

### Figure 3:
Systematic benchmarking demonstrates that AI-based event detection is superior to previous methods.(A) Scheme of event detection benchmarking. Six methods are compared using precision and recall metrics. (B) Event-free recordings were superimposed with generated events to create ground-truth data. D

### Figure 4-figure supplement 1
Event detection in different synaptic preparations.(A) Amplitude histogram with kernel-density estimate (light blue line) of miniML-detected events for the mouse granule cell recording shown in Figure 4. (B) Detected events for miniML and matched-filtering approaches. Color-coded representative exam

### Figure 4:
Application of miniML to electrophysiological recordings from diverse synaptic preparations.(A) Schematic and example voltage-clamp recordings from mouse cerebellar GCs. Orange circles mark detected events. (B) Representative individual mEPSC events detected by miniML. (C) All detected events from (

### Figure 5-figure supplement 1
Recall depends on event kinetics.(A) Recall versus event kinetics for the MF–GC model. Kinetics (i.e., rise and decay time constants) of simulated events were changed as indicated. miniML robustly detects events with up to ∼4-fold slower kinetics (dark blue, dashed line indicates 80% recall). Resamp

### Figure 5:
Transfer learning allows analyzing different types of events with small amounts of training data.(A) Illustration of the transfer learning (TL) approach. The convolutional layers of a trained miniML model are frozen before retraining with new, smaller datasets. (B) Comparison of TL and full training

### Figure 5-figure supplement 2
Transfer learning facilitates model training across different datasets.(A) Loss and accuracy versus number of training dataset samples for three different datasets (mouse MF–GC mEPSPs, Drosophila NMJ mEPSCs, zebrafish (ZF) spontaneous EPSCs). Dashed lines indicate transfer learning (TL), whereas sol

### Figure 6.
Synaptic event detection for neurons in a full-brain explant preparation of adult zebrafish.(A) Application of TL to facilitate event detection for EPSC recordings. (B) Extraction of amplitudes, event frequencies, decay times, and rise time for all neurons in the dataset (n = 34). (C) Typical (mean)

### Figure 7.
Event detection at Drosophila neuromuscular synapses upon altered glutamate receptor composition.(A) Two-electrode voltage-clamp recordings from wild-type (WT) Drosophila NMJs were analyzed using miniML with transfer learning. (B) Left: Example voltage-clamp recording with detected events highlighte

### Figure 8.
Optical detection of spontaneous glutamate release events in cultured neurons using iGluSnFR3 and miniML.(A) miniML was applied to recordings from rat primary culture neurons expressing iGluSnFR3. Data from (Aggarwal et al., 2023). (B) Example epifluorescence image of iGluSnFR3-expressing cultured n

### Figure 9-figure supplement 1
mEPSP detection in ASAP5 recordings.(A) Signal-to-noise ratio (SNR) of mEPSPs in electrophysiology and ASAP5 for five neurons. (B) Overlay of simultaneous current-clamp and ASAP5 recording. Events detected by miniML in both types of recordings are indicated. (C) Examples of mEPSPs detected in the el

### Figure 9:
Optical detection of mEPSPs in cultured rat hippocampal neurons using ASAP5 and miniML.(A) Event detection in simultaneous recordings of membrane voltage using electrophysiology and ASAP5 voltage imaging. (B) Example epifluorescence image of an ASAP5-Kv-expressing cultured rat hippocampal neuron. (C

### Figure 9-figure supplement 2
Methods comparison for event detection in ASAP5 recordings.(A) Average waveforms of detected events in ASAP5 data for miniML (n = 101 events), template-matching (n = 82 events), and deconvolution (n = 15 events). Data are from the example shown in Figure 9C, shaded areas represent SEM. (B) Recall of

## References
Total references in published paper: 74

### Key References (from published paper)
- Synaptic computation (, 2004)
- Sensitivity optimization of a rhodopsin-based fluorescent voltage indicator (, 2023)
- Glutamate indicators with improved activation kinetics and localization for imaging synaptic transmi (, 2023)
- Role of aberrant spontaneous neurotransmission in snap25- associated encephalopathies (, 2021)
- Automatic detection of spontaneous synaptic responses in central neurons (, 1994)
- Postsynaptic dysfunction is associated with spatial and object recognition memory loss in a natural  (, 2012)
- Pathogenic SCN2A variants cause early-stage dysfunction in patient-derived neurons (, 2023)
- Win–win data sharing in neuroscience (, 2017)
- The e3 ligase thin controls homeostatic plasticity through neurotransmitter release repression (, 2022)
- Effects of dataset size and interactions on the prediction performance of logistic regression and de (, 2022)
- Miniature neurotransmission is required to maintain drosophila synaptic structures during ageing (, 2021)
- Local connectivity and synaptic dynamics in mouse and human neocortex (, 2022)
- Detection of spontaneous synaptic events with an optimally scaled template (, 1997)
- Rapid and sustained homeostatic control of presynaptic exocytosis at a central synapse (, 2019)
- DeepCINAC: A deep-learning-based python toolbox for inferring calcium imaging neuronal activity base (, 2020)
- Glutamate receptor expression regulates quantal size and quantal content at the Drosophila neuromusc (, 1999)
- Long-term recurrent convolutional networks for visual recognition and description (, 2017)
- A positively tuned voltage indicator for extended electrical recordings in the brain (, 2023)
- Deep learning for time series classification: A review (, 2019)
- Big data from small data: Data-sharing in the ’long tail’ of neuroscience (, 2014)
- A fast and responsive voltage indicator with enhanced sensitivity for unitary synaptic events (, 2024)
- Moving beyond p values: Data analysis with estimation graphics (, 2019)
- Structure and function of a neocortical synapse (, 2021)
- AMPARs and synaptic plasticity: The last 25 years (, 2013)
- Automated detection and localization of synaptic vesicles in electron microscopy images (, 2022)
- Batch normalization: Accelerating deep network training by reducing internal covariate shift (, 2015)
- Developing a brain atlas through deep learning (, 2019)
- Auxiliary proteins are the predominant determinants of differ- ential efficacy of clinical candidate (, 2020)
- A combined deep CNN-LSTM network for the detection of novel coronavirus (COVID-19) using x-ray image (, 2020)
- Quantal components of unitary EPSCs at the mossy fibre synapse on CA3 pyramidal cells of rat hippoca (, 1993)

## Ground Truth Reference
- Figures: 20
- Tables: 1
- References: 74