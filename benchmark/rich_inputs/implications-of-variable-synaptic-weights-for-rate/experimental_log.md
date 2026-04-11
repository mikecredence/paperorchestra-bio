# Experimental Log: Implications of variable synaptic weights for rate and temporal coding of cerebellar outputs

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- In order to determine whether this is the case in both young and juvenile age, we recorded the sizes of many individual inputs in young (p10-20, n=74) and juvenile (p23-32, n=83) animals (Fig.
- This approach is shown for three inputs onto the same CbN neuron for a juvenile mouse (P27) (Fig.
- As shown in the individual trials for a small input, stimulation evoked short latency IPSCs (720 pA) in some trials but not others (Fig.
- 1a, upper, black) and failures (Fig.
- 1a, lower) showing that the IPSCs were evoked in a fraction of the trials.
- 1b, 1690 pA) and a large-sized input (Fig.
- 1d), but in juvenile mice there was considerably more variability, primarily because of the presence of many medium and large inputs (Fig.
- 1f; p<0.0001, Kolmogorov–Smirnov test).
- The distribution of input sizes we observed in P10-20 animals was similar to previous studies (P13-29, n=30) (Person and Raman, 2012a), and the skewed distribution of input sizes was only apparent when many individual inputs were characterized in P23-32 mice.biorxiv;2023.05.25.542308v1/FIG1F1fig1Fig
- Example of a small PC-CbN input (P27).
- (top) Responses evoked with the same stimulus intensity are superimposed for 40 trials (grey), and the average of successes (black) and failures (blue) are shown.
- Distribution of input sizes for PC-CbN IPSCs in young mice (P10-P20, n=74).e.
- Distribution of input sizes for PC-CbN IPSCs in juvenile mice (P10-P20, n=83).f.
- The distributions of unitary input sizes in P10-20 animals and P23-32 animals were significantly different (p<0.0001) with a Kolmogorov–Smirnov test.
- The histogram of input sizes in (d, e) were based on new experiments (d, n=44; e, n=39), on (Turecek et al., 2017) (e, n=44), and (Khan and Regehr, 2020) (d, n=30).Using dynamic clamp and simulations to examine the effects of variable input sizesThe variability in the amplitudes of PC to CbN inputs 
- However, it has been shown in several studies that measurement of GABAR single-channel conductance or unitary conductance with high Cl- based internals will result in a 2-3 times bigger value (Bormann et al., 1987; Gjoni et al., 2018; Sakmann et al., 1983).
- Second, we corrected the input sizes for the depression that occurs during physiological activation, which is approximately 40% of the initial size for a wide range of stimulus frequencies (Turecek et al., 2017, 2016).
- The excitatory conductances we used in the dynamic clamp studies were based on previous studies (Najac and Raman, 2017; Wu and Raman, 2017), with a relatively unconstrained frequency to pair with different inhibitory conductances (Methods).The corrected distribution of input sizes used to guide our 
- 1e, Methods) with 16 small (3 nS), 10 medium (10 nS), and 2 large (30 nS) inputs (Fig.
- 2f, grey; total 200 nS, similar to the total conductances used in Person and Raman, 2012).
- The timing and frequency of the inputs were based on PC firing recorded in awake-behaving mice, with each input firing at approximately 80 Hz (Fig.
- 2—figure supplement 1, Methods).
- 2b, red) conductances, which were then summed to generate the total inhibitory conductance arising from all inputs (Fig.
- 2b), that in turn produced large fluctuations in the membrane potential when injected into a CbN neuron (Fig.
- 2b and 2c).biorxiv;2023.05.25.542308v1/FIG2F2fig2Figure 2.Large PC inputs powerfully influence the spike timing of CbN neuron firing.a.
- The corrected distributions of PC-CbN input sizes in juvenile animals (f, red) was approximated with 16 small inputs (3 nS, green), 10 medium inputs (10 nS, blue) and 2 large inputs (30 nS, red).
- Raster plots are shown for the spike times of the 16 small (green), 10 medium (blue), and 2 large (red) inputs used in dynamic clamp experiments.b.
- Different cells (n=6, grey) are shown along with the average cross-correlograms (colored traces).e.
- Summary of the excitation (e), inhibition (i) and half-decay time (t1/2), as defined in the inset for the data in d.
- Cumulative histogram of all recorded inputs from Figure 1 for P23-32 mice corrected for depression and internal solution (red), the simplified input distribution used in dynamic clamp studies in a (grey), and inputs drawn from that distribution that were used in a simulation (black).g.
- Summary of the excitation (e), inhibition (i) and half-decay time (t1/2), for a simulation as defined in the inset for the simulated cell in g (black), and for inputs to 9 other simulated cells with different distributions of inputs (grey).biorxiv;2023.05.25.542308v1/FIG2S1F3fig2s1Figure 2—figure su
- Normalized ISI histograms of 10 PCs recorded in vivo, with their firing rates indicated in the legend.b.
- Example of a lognormal distribution fitting (red) to the ISI histogram of one PC recoded in vivo (black, 83 Hz).
- Similar fittings were performed for the other 9 PCs.d.
- The standard deviation (sd) as a function of the mean of the lognormal distribution fits to the 10 PCs was fitted as a linear function.
- Fits were performed in IGOR Pro to the function exp{−[ln(x⁄x0)/width]2}.
- The values of μ and σ for standard lognormal distribution are computed from x0 and width using equations: .
- The values of mean and sd of the lognormal distribution fits were computed from μ and σ using equations: mean = exp(μ + σ 2/2) and .
- 2d, left), while medium sized inputs strongly reduced CbN neuron spiking (Fig.
- 2d, middle), and large inputs transiently shut down CbN neurons for approximately 2 ms (Fig.
- 2e, middle), as well as the duration of inhibition (Fig.
- 2e, bottom) were all positively correlated with the size of the PC input.
- 2f (red) until the total inhibitory conductance reached 200 nS.
- 2h, black), and for 9 other simulated neurons (Fig.
- 3a) and auto-correlograms (Fig.
- 3b), the three recorded PCs had refractory periods that were correlated with their firing frequency (∼3.5 ms for 49 Hz, ∼2 ms for 83 Hz, and ∼1.5 ms for 122 Hz firing), while the Poisson input did not have a refractory period.
- We then generated inhibitory conductances by convolving spike times with a 20 nS single input conductance.
- To compensate for the differences in input firing frequency, we adjusted the number of the inputs so that the total inhibitory conductances were approximately that same for all cases (12 x 20 nS at 49 Hz, 9 x 20 nS at 83 Hz, 6 x 20 nS at 122 Hz, and 9 x 20 nS for Poisson inputs).
- 3c), and consequently the cross-correlograms showed elevated spiking in the CbN neuron (Fig.
- Thus, the autocorrelations of PC firing led to elevated CbN firing prior to suppression.biorxiv;2023.05.25.542308v1/FIG3F4fig3Figure 3.Autocorrelation of Purkinje cell firing leads to excitation prior to inhibition of CbN neurons.a.
- At 0 ms, all graphs peak at 1 and graphs are truncated to allow better visualization.c.
- Calculated spike-triggered average inhibitory conductances for different cases (12 x 20 nS at 49 Hz, 9 x 20 nS at 83 Hz, 6 x 20 nS at 122 Hz, and 9 x 20 nS for Poisson inputs), with ISIs drawn from the corresponding distributions in a.d.
- The firing rate of CbN neurons was approximately 200 spikes/s for an inhibitory conductance of 30 nS, but as the magnitude of the inhibitory conductance increased the spike rate decreased, and an inhibitory conductance of 65 nS silenced CbN firing (Fig.
- 2—figure supplement 1; Methods).biorxiv;2023.05.25.542308v1/FIG4F5fig4Figure 4.The amplitudes and fluctuations of the total inhibitory conductance both regulate the firing of CbN neurons.a.
- Summary of CbN neuron firing rates (n=7 cells) during constant inhibitory conductances as in a.c.
- Inhibitory conductances with the same average conductance (56 nS) are shown for a constant conductance (far left), and for different cases with the numbers and sizes of inputs varied.d.
- 2f, red), and for the 40 × 5 nS inputs (dashed line).i.
- Simulated CbN firing rates based on 1000 different input distributions randomly drawn from the observed distribution of input sizes (filled grey) and for 40 × 5 nS inputs (open circle) are plotted as a function of the CV of the inhibitory conductance.
- 4c), and the CV became larger (Fig.
- 2f, red) with different CVs and a total conductance value of 200 nS (Fig.
- 4h, solid lines), together with 40 uniform 5 nS PC inputs (Fig.
- 4h, dashed line), were used to generate inhibitory conductances for dynamic clamp experiments.
- Even though the average conductance was the same, the firing rates for the three nonuniform input sizes were higher than for uniform inputs (38, 50, 67 vs.
- We also simulated the firing evoked by 1000 different distributions of PC input sizes drawn from the observed input size distribution with a total conductance size of 200 nS, and observed a broad range of firing rates that depended on the CV of the total inhibitory conductance (Fig.
- 4i and 4j).Different sized inputs reliably transfer a rate codeThe ability of different size PC inputs to convey a rate code to CbN neurons was unclear, given that both the magnitude and variability of total inhibition can influence the firing rates of CbN neurons.
- We addressed this issue using dynamic clamp experiments with small, medium, and large inputs (small: 16 × 3 nS = 48 nS; medium: 10 × 10 nS = 100 nS, and large: 2 × 30 nS = 60 nS), as in Fig.
- We began by varying the firing rates of all small PC inputs from 0 to 160 spikes/s while keeping the firing rates of medium and large inputs constant (Fig.
- 2—figure supplement 1, Methods).
- 5b, left) and decreased the CV (Fig.
- 5c, left) of the total inhibitory conductance, and suppressed the firing rate of CbN neurons (Fig.
- 5e, left, green) and the inhibitory conductance amplitude (Fig.
- 5e, middle, green), and positively correlated with the CV of the inhibitory conductance (Fig.
- 5a, middle) had qualitatively similar effects on the conductance (Fig.
- 5c, middle), and the CbN firing rate (Fig.
- 5e, blue), but had larger effects because of their larger contribution to the inhibitory conductance.
- 5a, right) affected the total conductance (Fig.
- 5b, right) similarly to varying the small and medium inputs but had a very different influence on the CV (Fig.
- 4g), or if the amplitude of the inhibitory conductance amplitude (Fig.
- 4b) is the primary determinant of the CbN firing.
- 5e, middle), but there were differences in the firing rate as a function of CV (Fig.
- Therefore, the ability of a PC input to regulate CbN firing simply depends on its size.biorxiv;2023.05.25.542308v1/FIG5F6fig5Figure 5.PC inputs effectively convey a simple rate code regardless of input size.Dynamic clamp experiments were performed with small (16 × 3 nS, green), medium (10 × 10 nS, b
- The firing rates of either small (left), medium, (middle) or large (right) inputs were varied every 2 s while the firing rates of the other inputs were maintained at 80 spikes/s.b.
- The firing rates of CbN neurons with the conductances in a-c are shown as individual cells (n = 9, grey) and their average (black).e.
- As in f but for simulations for one CbN neuron (black) and other 9 CbN neurons (grey).Simulations allowed us to examine the influences of individual PC inputs with a full range of sizes on the firing rates of CbN neurons.
- 2g-h, but with the firing rates for each input varied between 0 and 160 spikes/s while maintaining the average firing rates of other inputs at 80 Hz (Methods).
- In this example, varying a single 37 nS input from 0 to 160 spikes/s decreased the output firing frequency from 126 spikes/s to 35 spikes/s (Fig.
- 5g, middle), which was not observed for the CbN firing rates vs CV of the total inhibitory conductance (Fig.
- 5h, black) and for 9 other neurons (Fig.
- These simulations, along with the dynamic clamp studies, establish that individual PC inputs can regulate the firing rate of the CbN neuron, and that different sized inputs convey a rate code that depends on the amplitude of total inhibition.Synchrony of uniform or variable sized PC inputsPrevious d
- 6a) and variable sized inputs (Fig.
- 6aii and 6aiii) that resulted in a low baseline firing rate of CbN neurons (25 spikes/s; Fig.
- Synchronizing either 25% or 50% of the uniform inputs (Fig.
- 6ai) increased the variability (Fig.
- 6aiii) of the total inhibitory conductance, which then resulted in a robust increase in the firing rate of CbN neurons (Fig.
- The CbN firing rate increased from the baseline firing rate of 25 spikes/s to 45 spikes/s with 25% synchrony, and 88 spikes/s with 50% synchrony (Fig.
- The increases in CbN firing rate were 1.8-fold higher for 25% synchrony and 3.5-fold higher for 50% synchrony, respectively (Fig.
- 6av).biorxiv;2023.05.25.542308v1/FIG6F7fig6figure 6.The influence of PC synchrony on the firing rates of CbN neurons for uniform and nonuniform sized PC inputs.Dynamic clamp experiments were conducted with either uniform (a) or nonuniform inputs (b) in which the conductance was kept constant, but th
- The extent of synchrony of uniform sized inputs (40 × 5 nS) is varied.ii.
- CbN neuron firing rate with the conductance (average, black; individual cells, n=14, grey).v.
- Similar experiments were performed on the same cells as in a, but for inputs of nonuniform sizes (small: 16 × 3 nS, green; medium: 12 × 8 nS, blue; large: 2 × 30 nS, red).
- Similar plots to c-f, but for simulations with different sized inputs (dark purple, based on a single distribution, light purple based on 9 other different distributions) and uniform inputs (40 × 5 nS, black circles).k.
- Violin plots showing the simulated CbN neuron firing rate with 100 different distributions of different sized inputs (not syn), and the two largest inputs or the two smallest inputs synchronized.l.
- As in k but normalized to the not synchronized firing rate.For nonuniform inputs (small: 16 × 3 nS; medium: 8 × 12 nS; large: 2 × 30 nS), the generated conductance was more variable (Fig.
- 6bii and 6biii), resulting in a higher baseline firing rate of CbN neurons (43 spikes/s; Fig.
- 6biv)), which is similar to Fig.
- Synchronizing 50% of all inputs (small, medium, and large inputs, Fig.
- 6bi, left), increased the variability (Fig.
- 6biii, left) of the conductance, which then elevated the firing of CbN neurons from 43 spikes/s to 91 spikes/s (Fig.
- The firing rates for 50% synchrony with nonuniform and uniform inputs were comparable (Fig.
- 6biv), but because baseline firing rates were higher for nonuniform inputs, their relative increase in CbN firing was much lower (2.1-fold for nonuniform inputs compared to 3.5-fold for uniform inputs, p<0.0001; Fig.
- We also examined the effect of synchronizing 25% or 50% of small or medium inputs (Fig.
- Synchronizing 25% or 50% of either small or medium inputs barely increased the variability and CV of the conductance, and led to minimal increases in the firing of CbN neurons (Fig.
- 6f).Simulations allowed us to explore the effects of a full range of synchrony levels, which would be impractical to test experimentally (Fig.
- We examined uniform inputs (40 × 5 nS) and determined the effect of synchronizing 1, 2, …20 inputs (Fig.
- 2f, red), with a total conductance of 200 nS, and determined the firing rates evoked when we synchronized different combinations of inputs (Fig.
- 6g-j, dark purple: for one distribution of input sizes; light purple: for 9 other distributions of input sizes).
- 6g-j) and dynamic clamp experiments (Fig.
- 6g, dark purple), but much less scatter when the firing rates were plotted as a function of the total amplitude of the synchronized inputs (Fig.
- As shown in simulations, synchronizing the two largest inputs can elevate CbN firing rate by approximately 20%, while synchronizing the two smallest inputs barely changed CbN firing rate (Fig.
- 6k and 6l).We also examined the influence of PC synchrony on the spike timing of CbN neurons in dynamic clamp experiments of Fig.
- For uniform inputs (5 nS), single unsynchronized inputs weakly influenced the spike timing of CbN neurons (Fig.
- 50% synchrony of uniform inputs silenced CbN neurons for several milliseconds, and this was proceeded by a prominent increase in CbN spiking (Fig.
- 2, the influence of individual inputs on the timing of CbN firing depended on the size of the input, and single large inputs could have a very large influence on the timing of CbN spiking (Fig.
- Synchronizing 50% of all nonuniform inputs generated a cross-correlogram similar to that of synchronizing 50% uniform inputs (Fig.
- 7c, top), the amplitude of inhibition (Fig.
- 7c, bottom), and the duration of inhibition (Fig.
- 7d) were dependent on the synchrony amplitude, as was the case for simulations (Fig.
- These findings establish that for nonuniform inputs, the effects of synchrony on CbN spike timing depends on the total size of synchronized inputs.biorxiv;2023.05.25.542308v1/FIG7F8fig7Figure 7.The influence of PC synchrony on the spike timing of CbN neurons for uniform and nonuniform sized PC input
- (top) The cross-correlograms of PC input and CbN neuron spiking for nonsynchronous inputs (left) and 50% synchronous inputs (right) with uniform sized inputs.
- The cross-correlograms of small (green), medium (blue), and large (red) inputs for unsynchronized inputs (left) and 50% synchronous inputs (right, purple) are shown.m.
- As in c but for half-decay time (t1/2).o.

## Tables

### 

## Figure Descriptions

### Figure 1.
The amplitudes of Individual PC to CbN inputs are highly variable.a. Example of a small PC-CbN input (P27). (top) Responses evoked with the same stimulus intensity are superimposed for 40 trials (grey), and the average of successes (black) and failures (blue) are shown. (bottom) IPSCs amplitudes are

### Figure 2.
Large PC inputs powerfully influence the spike timing of CbN neuron firing.a. The corrected distributions of PC-CbN input sizes in juvenile animals (f, red) was approximated with 16 small inputs (3 nS, green), 10 medium inputs (10 nS, blue) and 2 large inputs (30 nS, red). Raster plots are shown for

### Figure 2—figure supplement 1.
ISI histograms of PCs firing used in this study.a. Normalized ISI histograms of 10 PCs recorded in vivo, with their firing rates indicated in the legend.b. As in a but normalized to the peak.c. Example of a lognormal distribution fitting (red) to the ISI histogram of one PC recoded in vivo (black, 8

### Figure 3.
Autocorrelation of Purkinje cell firing leads to excitation prior to inhibition of CbN neurons.a. Interspike interval (ISI) histograms for three different PCs recorded in vivo (left), and for an artificial Poisson input lacking a refractory period (right).b. Autocorrelation functions for the ISI dis

### Figure 4.
The amplitudes and fluctuations of the total inhibitory conductance both regulate the firing of CbN neurons.a. CbN neuron spiking observed for constant inhibitory conductances of the indicated amplitudes.b. Summary of CbN neuron firing rates (n=7 cells) during constant inhibitory conductances as in 

### Figure 5.
PC inputs effectively convey a simple rate code regardless of input size.Dynamic clamp experiments were performed with small (16 × 3 nS, green), medium (10 × 10 nS, blue) and large (2 × 30 nS, red) inputs. a. The firing rates of either small (left), medium, (middle) or large (right) inputs were vari

### figure 6.
The influence of PC synchrony on the firing rates of CbN neurons for uniform and nonuniform sized PC inputs.Dynamic clamp experiments were conducted with either uniform (a) or nonuniform inputs (b) in which the conductance was kept constant, but the synchrony of the inputs was varied.a. i. The exten

### Figure 7.
The influence of PC synchrony on the spike timing of CbN neurons for uniform and nonuniform sized PC inputs.k. (top) The cross-correlograms of PC input and CbN neuron spiking for nonsynchronous inputs (left) and 50% synchronous inputs (right) with uniform sized inputs. Individual cells (grey) and av

## References
Total references in published paper: 62

### Key References (from published paper)
- Robust transmission of rate coding in the inhibitory Purkinje cell to cerebellar nuclei pathway in a (, 2017)
- Polarity of long-term synaptic gain change is related to postsynaptic spike firing at a cerebellar i (, 1998)
- The Cerebellar Cognitive Affective/Schmahmann Syndrome: a Task Force Paper (, 2020)
- Microcircuit Rules Governing Impact of Single Interneurons on Purkinje Cell Output In Vivo (, 2020)
- Discharges of Purkinje cells in the paravermal part of the cerebellar anterior lobe during locomotio (, 1984a)
- Discharges of nucleus interpositus neurones during locomotion in the cat (, 1984b)
- Implications of functional anatomy on information processing in the deep cerebellar nuclei (, 2009)
- Time-invariant feed-forward inhibition of Purkinje cells in the cerebellar cortex in vivo (, 2016)
- MECHANISM OF ANION PERMEATION THROUGH CHANNELS GATED BY GLYCINE AND y-AMINOBUTYRIC ACID IN MOUSE CUL (, 1987)
- Multimodal integration in rostral fastigial nucleus provides an estimate of body movement (, 2009)
- Sensorimotor Integration and Amplification of Reflexive Whisking by Well-Timed Spiking in the Cerebe (, 2018)
- The log-dynamic brain: how skewed distributions affect network operations (, 2014)
- Spatiotemporal firing patterns in the cerebellum (, 2011)
- Binary and analog variation of synapses between cortical pyramidal neurons (, 2022)
- The pathways responsible for excitation and inhibition of fastigial neurones (, 1974)
- The Control of Rate and Timing of Spikes in the Deep Cerebellar Nuclei by Inhibition (, 2000)
- Specific synaptic input strengths determine the computational properties of excitation-inhibition in (, 2018)
- The neuronal code(s) of the cerebellum (, 2013)
- Rate versus synchrony codes for cerebellar control of motor behavior (, 2023)
- Feed-forward recruitment of electrical synapses enhances synchronous spiking in the mouse cerebellar (, 2020)
- Multiplexed coding by cerebellar Purkinje neurons (, 2016)
- Circuitry Underlying Experience-Dependent Plasticity in the Mouse Visual System (, 2020)
- The Cerebellar Cortex (, 2022)
- Functional convergence of on-off direction-selective ganglion cells in the visual thalamus (, 2022)
- Unusually Slow Spike Frequency Adaptation in Deep Cerebellar Nuclei Neurons Preserves Linear Transfo (, 2022)
- Elimination and strengthening of glycinergic/GABAergic connections during tonotopic map formation (, 2003)
- Neuronal integration of synaptic input in the fluctuation-driven regime (, 2004)
- Single-unit activity of cerebellar nuclear cells in the awake genetically dystonic rat (, 1998)
- Organization, Function, and Development of the Mouse Retinogeniculate Synapse (, 2020)
- Functional Convergence at the Retinogeniculate Synapse (, 2017)

## Ground Truth Reference
- Figures: 8
- Tables: 1
- References: 62