# Experimental Log: A prefrontal network model operating near steady and oscillatory states links spike desynchronization and synaptic deficits in schizophrenia

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsSummary of experimental resultsIn this section we summarize main experimental findings reported previously by our group (Zick et al., 2018).
- In that study, spike trains of ensembles of single neurons were recorded simultaneously from PFC of monkeys while they performed the dot-pattern expectancy (DPX) task, a task that measures specific deficits in cognitive control in schizophrenia (Jones et al., 2010).
- Figure 1 shows the population average pairwise correlation between spike trains of neurons recorded in drug-naïve (black) and drug (magenta) conditions.
- The strength of spike correlation was quantified by the ratio between the observed frequency of synchronous spikes (2ms resolution) and the frequency expected if the spike trains were uncorrelated (we subtracted 1 from this ratio so that correlation value is zero for uncorrelated, positive for corre
- The frequency of spike synchrony was determined from activity observed during a short (100 ms-long) window that was slid across time of task performance.
- Figure 1a shows that spike synchrony obtained from trials aligned to the cue onset (time 0) remained relatively weak and unchanged during the cue and delay periods, until the probe onset, in both drug-naïve and drug conditions.
- Because the instant of response after probe presentation varied from trial to trial, to appreciate the time course of synchrony after delay period immediately preceding the response, in Fig.1b we aligned trials to response time (time 0).
- It is seen that spike synchrony started to increase sharply about 200ms before the motor response in the drug-naïve condition.
- We term this effect as NMDAR blockage induced desynchronization of spiking activity.biorxiv;2022.06.10.495666v1/FIG1F1fig1Figure 1.Population average spike synchrony between spike trains of neuron pairs recorded during the DPX task as a function of timePlots are shown for drug-naïve (black) and drug
- Spike synchrony was measured with 2 ms resolution, and its temporal modulation was estimated with 100 ms resolution.
- a: Trials are aligned to the cue onset (t = 0 ms); in all trials, the cue was presented until t = 1,000 ms, followed by a 1,000 ms delay period, after which the probe was presented at t = 2,000 ms.
- The numbers of contributing neuron pairs for drug-naïve and drug conditions are 978 and 368, respectively.
- b: Trials are aligned to the time of motor response (t = 0 ms) to show the temporal modulation of synchrony during the last 600 ms immediately preceding the response.
- The numbers of contributing neuron pairs for drug-naïve and drug conditions are 1,246 and 434, respectively.Network model and theoretical frameworkTo understand the phenomenon of drug-induced desynchronization of spiking activity and the role played by various components of synaptic currents, we con
- The asynchronous state is stable when λ < 0; in this case small perturbations of firing rates cause exponentially damped oscillation of network activity.
- The case λ = 0 corresponds to the onset of instability of the asynchronous state and the emergence of sustained sinusoidal oscillations of population average firing rates with frequency ω; in the oscillatory regime spike trains remain sparse and irregular but at each oscillation cycle a random subse
- Lastly, when λ >0, small fluctuations in the stationary rates develop oscillatory instability with the amplitude of oscillations growing exponentially in time; however, higher order terms neglected in linear analysis can eventually saturate the instability growth (Brunel and Hakim, 1999), resulting 
- Figure 2a shows a state diagram of the system for which external spike rate is set to νX = 5 Hz, the rates of excitatory and inhibitory populations are set to , , and the NMDA current balance is fixed at INMDA/IGABA = 0.2.
- The asynchronous stationary state corresponds to the region where λ < 0, whereas the synchronous oscillation state is realized in the region where λ >0.
- The asynchronous and synchronous states are separated by a “critical” or instability line on which λ = 0 (shown in white color in Fig.
- The oscillation frequency on the critical line, fntwrk = ω/2π, as a function of the balance between the recurrent AMPA and GABA currents, IAMPA/IGABA, is shown in Fig.
- 2b.biorxiv;2022.06.10.495666v1/FIG2F2fig2Figure 2.Characteristics of the system predicted by the linear stability analysisParameters are as follows: prescribed firing rates of excitatory and inhibitory populations are 5 Hz and 20 Hz, respectively; external input spike rate is 5 Hz; and the balance b
- a: State diagram in the (IAMPA/IGABA, IX,E/Iθ,E) parameter plane showing color coded value of the rate of instability growth λ: in the region of the parameter space where λ <0 the asynchronous state is stable, whereas the region where λ >0 corresponds to the synchronous oscillation state.
- The two regimes are separated by a critical line on which λ = 0.
- b: Network oscillation frequency that develops on the critical line as a function of the balance between AMPA component of recurrent excitation and inhibition.Figure supplement 1.
- 2–figure supplement 1b).Integration of DPX task context and drug condition into the modelTo study spike synchrony in asynchronous and synchronous networks in the context of the DPX task performed in drug-naïve and drug conditions (Zick et al., 2018), we make two assumptions regarding neural and syna
- 2a was obtained exactly for these values of the above listed parameters.
- For synchronous regime, we look for a network on the critical line (λ = 0, white line in Fig.
- 2a), at the onset of oscillatory instability with a frequency in the γ-band (a frequency band associated with the LFPs recorded from prefrontal areas (Bastos et al., 2018; Lundqvist et al., 2016)).
- 2a located at  corresponds to such a network with oscillation frequency  (cf.
- In the following, we refer to this network as the critical state primary network.Correspondingly, for the asynchronous regime, we need to select a network that is far from the critical line and deep in the region of stable network dynamics (λ < 0).
- 2a located at  is an example of such a network.
- Both networks comprise N = 5,000 neurons, of which NE = 4,000 are excitatory and NI = 1,000 inhibitory.
- Neurons are connected randomly with a probability p = 0.2.
- Figure 3 illustrate the behavior of simulated networks with synaptic conductance parameters corresponding to the steady and critical primary networks indicated by the red and blue asterisks, respectively, in the state diagram presented in Fig.
- The dynamic behavior is shown at the level of individual cell activity (spike rasters, top of panels in Fig.3), as well as whole population activity (bottom of panels in Fig.3).biorxiv;2022.06.10.495666v1/FIG3F3fig3Figure 3.Simulations of networks composed of 4,000 excitatory and 1,000 inhibitory ne
- a1, b1, a2, b2: Top, spike rasters (sorted by rate) of 200 excitatory (red) and 50 inhibitory (blue) neurons.
- Bottom, time-varying activity (1ms resolution) of excitatory (red) and inhibitory (blue) populations.
- a1, a2: External input spike rate νX = 5 Hz.
- Excitatory and inhibitory neurons display average firing rates of, respectively, 5.2 Hz and 20 Hz (a1), and 5.5 Hz and 21 Hz (a2).
- b1, b2: In these simulations νX was increased by 5%.
- Excitatory and inhibitory neurons display average firing rates of, respectively, 7.8 Hz and 26 Hz (b1), and 15 Hz and 42 Hz (b2).Figure supplement 1.
- 3 panels a1 and a2 external spike rate νX was fixed at the level of  chosen for the primary networks.
- It is seen that excitatory and inhibitory neurons exhibit highly irregular firing with average rates, νE and νI, about 5.2 Hz and 20 Hz in the steady state primary network (Fig.
- 3a1) and 5.5 Hz and 21 Hz in the critical state primary network (Fig.
- 3a1 demonstrates that population activity of the steady state primary network is rather stationary in time, whereas activity of the critical primary network shown in Fig.
- 3a2 exhibits signs of developing of oscillatory instability (compare Fig.3–figure supplement 1a1 vs Fig.3–figure supplement 1a2).
- Correspondingly, the behavior of the simulated critical state primary network exhibits similarity with the boundary regime on which the asynchronous stationary state destabilizes and oscillatory behavior of the population activity emerges.Panels b1 and b2 in Fig.
- 3 demonstrate results of simulations in which external spike rate νX was increased by 5% relative to the rate  used in simulations illustrated in Fig.
- 3b1), the firing rates of excitatory and inhibitory neurons increase with the external drive.
- However, the regime of network dynamics qualitatively does not change and remains asynchronous (compare Fig.3–figure supplement 1a1 vs Fig.3–figure supplement 1b1).
- It is seen that while individual neurons continue to fire irregularly, population activity now clearly exhibits oscillatory behavior, indicating that the network is in synchronous irregular regime in which the average firing frequency of neurons is low, about 20 Hz, compared to the frequency of netw
- This frequency is close to the theoretically predicted network frequency of 58 Hz near the onset of oscillation.Thus, direct simulations confirm that analytically derived network parameters for both steady and critical primary networks provide the anticipated regimes of network dynamics.To facilitat
- In the context of the DPX task performed in drug-naïve and drug conditions studied in (Zick et al., 2018) and with the purpose of elucidating the mechanism of drug-induced desynchronization of spiking activity, we investigated how temporal correlations depend on the strength of external drive and th
- Conductances for excitatory and inhibitory neurons were scaled with the same factor and, therefore, their relative values  and  are the same; in the following we drop the E,I designation.Figure 4 displays correlation of spiking activity (panels a1, a2, c1, c2) and synchrony (0-lag correlation, panel
- 4 panels a2, c2), and with increasing external drive or NMDAR conductance spike synchrony could be modulated from relatively weak to rather strong (Fig.
- 4 panels b2, d2).biorxiv;2022.06.10.495666v1/FIG4F4fig4Figure 4.Spiking activity correlation and synchrony computed from spike trains of simulated networksConductance parameters are solutions of mean field equations for the steady state primary network (a1, b1, c1, d1) and the critical state primary
- For the steady state network correlation and synchrony are weak and insensitive to the modulation of external input spike rate νX (a1, b1) and NMDAR conductance gNMDA (c1, d1).
- In contrast, for the critical state network spike correlation depends strongly on the external spike rate (a2) and NMDAR conductance (c2) and the degree of spike synchrony could be modulated from relatively weak to strong (b2, d2).
- Results shown in (c1, d1, c2, d2) are obtained from simulations in which νX is increased by 5%.
- The numbers next to color-coded markers for spike correlation plots show the normalized magnitudes of external input spike rates, , (a1, a2) and NMDAR conductance, , (c1, c2).Circuit mechanisms of spike synchronization modulationWhat are the network mechanisms of external drive and NMDA conductance 
- For both steady and critical state primary networks, stability is investigated in the vicinity of the standard values of the external input spike rate and NMDAR conductances corresponding to the respective networks.Figure 5 illustrates state diagrams in the  plane in the neighborhood of the steady (
- 2a, the critical line (λ = 0) separating the asynchronous stationary (λ < 0) and synchronous oscillatory (λ > 0) states is shown in white color.
- 5B) state primary networks in these parameter planes.
- 5a) do not change the network state; these modulations have no impact on the spike correlation and the strength of synchrony (cf.
- 5a insets).biorxiv;2022.06.10.495666v1/FIG5F5fig5Figure 5.Network state diagrams in the  planeThe critical line (λ = 0, white line) separates the parameter plane into regions of asynchronous stationary (λ < 0) and synchronous oscillatory (λ > 0) regimes.
- These insets display the same plots for spike synchrony that are shown in panels b1 and b2 (bottom insets in a and b, correspondingly) and d1 and d2 (right insets in a and b, correspondingly) in Fig.
- 4.In contrast, the modulations of νX and gNMDA in the critical state primary network (Fig.
- 5b) induce transitions between the network states.
- 5b) the system crosses the boundary between asynchronous and synchronous regimes and the network state changes from stationary to oscillatory; this transition is accompanied by a sharp increase in spike synchrony (cf.
- 5b) causes the system to cross the boundary again, and the network state changes now from oscillatory to stationary; this transition is accompanied by a sharp decrease in spike synchrony (cf.
- 5b right inset).Thus, this analysis reveals that networks that are close to the boundary between asynchronous and synchronous regimes, in contrast to asynchronous networks that are far from this boundary, have a rich dynamic behavior.
- 1b, spiking activity observed in monkey PFC in the DPX task (Zick et al., 2018) remains practically desynchronized after probe presentation for about 200 ms but it begins to increase sharply about 200 ms before the motor response.
- 6 temporal correlations of spiking activity during the 200 ms period following probe presentation (Fig.
- 6a1) and during the 200 ms period preceding the motor response (Fig.
- 6b1) in drug-naïve (black) and drug (magenta) conditions.
- 6b1).biorxiv;2022.06.10.495666v1/FIG6F6fig6Figure 6.Direct comparison of the effects of blocking of NMDAR in primate PFC and in the prefrontal circuit modela1, b1: Plots show population average temporal correlations between spiking activity of neuron pairs recorded from PFC during the 200ms period i
- In the drug-naïve condition (black line), population activity during the pre-response period develops characteristics of synchronous oscillation with a frequency of ~55 Hz (peaks at time lags ±18 ms, blue arrows, b1).
- Administration of a drug blocking NMDAR (magenta line) desynchronizes neuronal activity during the pre-response period (b1).
- a2, b2, c: Temporal correlations (a2, b2) computed from spike trains of simulated networks corresponding to four conditions shown in the  state plane (c) by bold dots and arrow heads: initial probe (, a2) and pre-response (, b2) periods for drug-naive (, black line) and drug (, magenta line) conditi
- The critical line (λ = 0, white line in panel c) separates the parameter plane into regions of asynchronous stationary (λ < 0) and synchronous oscillation (λ > 0) regimes.
- The locus of the blue asterisk corresponds to the critical state primary network in this plane.The presence of strong spike synchrony (0 ms lag) together with the correlation peaks at ±18 ms lags in the pre-response period (Fig.
- 6b1), and the absence of these characteristics in the initial probe period (Fig.
- 6a1) suggest that after probe presentation but before motor response network dynamics switches from the asynchronous stationary state to the synchronous oscillation state with a γ-frequency around 55 Hz.
- We start by recalling that in the framework of our approach: 1) the pre-response afferent signals, which we assume are received by PFC neurons before the monkey’s response, are modeled as an increase in the external spike rate from its background level νX and 2) the effect of drug administration is 
- 6c, black arrow crosses the boundary between the regimes).
- The oscillation frequency is about 50 Hz, which is manifested in the temporal correlations of spiking activity as a sharp increase in synchrony and appearance of peaks at ±20 ms lags (cf.
- 6 a1 vs a2 and b1 vs b2, black line).In the drug condition, setting NMDAR conductance to zero prevents the circuit model from switching to the synchronous regime in response to an increase in the external spike rate νX (cf.
- 6c, magenta arrow does not cross the boundary between the regimes).
- 6b2, magenta vs black line), similar to the desynchronizing effect of NMDAR antagonist administration on spiking activity in monkey PFC (Fig.
- 6 b1, magenta vs black line).In summary, this analysis suggests that because the prefrontal network model operates close to the boundary between asynchronous stationary and synchronous oscillatory regimes it has a considerable capacity to accurately capture experimentally observed aspects of spike s
- 2–figure supplement 1b), and that the characteristic features of the (IAMPA/IGABA, IX,E/Iθ,E) state diagram qualitatively remain unchanged when this balance is varied (Fig.
- 6c depend on the  balance.Figure 7 shows state diagrams in the  plane obtained for several  balance values.
- When the balance is shifted toward stronger inhibition (, Fig.7a), the critical line becomes too steep: in the drug condition, blocking NMDA current may not necessarily lead to spike desynchronization because the external spike modulation could trigger the network to switch to the synchronous regime
- 7c), the critical line becomes too flat: in the drug-naïve condition the external spike modulation may not be able to produce strong enough synchrony because the system would be too close to the critical line, and not shift deep enough into the region of the synchronous regime (cf.
- 7c).biorxiv;2022.06.10.495666v1/FIG7F7fig7Figure 7.State diagrams in the  plane obtained for several values of the balance between the NMDA and GABA currentsNotations are the same as in Fig.

## Figure Descriptions

### Figure 1.
Population average spike synchrony between spike trains of neuron pairs recorded during the DPX task as a function of timePlots are shown for drug-naïve (black) and drug (magenta) conditions. Spike synchrony was measured with 2 ms resolution, and its temporal modulation was estimated with 100 ms res

### Figure 2.
Characteristics of the system predicted by the linear stability analysisParameters are as follows: prescribed firing rates of excitatory and inhibitory populations are 5 Hz and 20 Hz, respectively; external input spike rate is 5 Hz; and the balance between NMDA and GABA currents is fixed at 0.2. a: 

### Figure 3.
Simulations of networks composed of 4,000 excitatory and 1,000 inhibitory neurons connected randomly with probability 0.2Conductance parameters are solutions of mean field equations for the steady state primary network (a1, b1) and the critical state primary network (a2, b2) corresponding to the red

### Figure 4.
Spiking activity correlation and synchrony computed from spike trains of simulated networksConductance parameters are solutions of mean field equations for the steady state primary network (a1, b1, c1, d1) and the critical state primary network (a2, b2, c2, d2) corresponding to the red and blue aste

### Figure 5.
Network state diagrams in the  planeThe critical line (λ = 0, white line) separates the parameter plane into regions of asynchronous stationary (λ < 0) and synchronous oscillatory (λ > 0) regimes. Asterisks correspond to the steady (a) and critical (b) state primary networks in these planes. Color-c

### Figure 6.
Direct comparison of the effects of blocking of NMDAR in primate PFC and in the prefrontal circuit modela1, b1: Plots show population average temporal correlations between spiking activity of neuron pairs recorded from PFC during the 200ms period immediately following probe presentation (a1) and the

### Figure 7.
State diagrams in the  plane obtained for several values of the balance between the NMDA and GABA currentsNotations are the same as in Fig. 6c. a: ; b: ; c: . Note that the critical line orientation depends on the  balance.

### Figure 2–figure supplement 1.
Dependence of the characteristic features of the network on the balance between the NMDA and GABA currents.a: Critical line separating the asynchronous and synchronous states in the (IAMPA/IGABA, IX,E/Iθ,E) parameter plane is shown for several values of the INMDA/IGABA balance. b: Oscillation freque

### Figure 3–figure supplement 1.
Power spectra of population spiking activity observed in network simulations.a1, b1: Spectra of the steady state network activities shown in Fig. 3a1 and Fig. 3b1, respectively. a2, b2: Spectra of the critical state network activities shown in Fig. 3a2 and Fig. 3b2, respectively. Note that the scale

## References
Total references in published paper: 41

### Key References (from published paper)
- Asynchronous states in networks of pulse-coupled oscillators (, 1993)
- Model of global spontaneous activity and local structured activity during delay periods in the cereb (, 1997)
- Context-processing deficits in schizophrenia: diagnostic specificity, 4-week course, and relationshi (, 2003)
- Laminar recordings in frontal cortex suggest distinct layers for maintenance and control of working  (, 2018)
- Monkey Prefrontal Neurons Reflect Logical Operations for Cognitive Control in a Variant of the AX Co (, 2016)
- Dynamics of sparsely connected networks of excitatory and inhibitory spiking neurons (, 2000)
- Effects of synaptic noise and filtering on the frequency response of spiking neurons (, 2001)
- Fast global oscillations in networks of integrate-and-fire neurons with low firing rates (, 1999)
- Firing frequency of leaky intergrate-and-fire neurons with synaptic current dynamics (, 1998)
- What determines the frequency of fast network oscillations with irregular neural discharges? I. Syna (, 2003)
- Effects of neuromodulation in a cortical network model of object working memory dominated by recurre (, 2001)
- Global disruption in excitation-inhibition balance can cause localized network dysfunction and Schiz (, 2021)
- Synaptic mechanisms and network dynamics underlying spatial working memory in a cortical network mod (, 2000)
- Spike timing-dependent plasticity of neural circuits (, 2004)
- Differential Roles of Mediodorsal Nucleus of the Thalamus and Prefrontal Cortex in Decision-Making a (, 2020)
- Dynamics of the firing probability of noisy integrate-and-fire neurons (, 2002)
- Organizing principles for a diversity of GABAergic interneurons and synapses in the neocortex (, 2000)
- On numerical simulations of integrate-and-fire neural networks (, 1998)
- Distinct Eligibility Traces for LTP and LTD in Cortical Synapses (, 2015)
- Mechanisms generating the time course of dual component excitatory synaptic currents recorded in hip (, 1990)
- Rethinking schizophrenia (, 2010)
- Voltage dependence of NMDA-activated macroscopic conductances predicted by single-channel kinetics (, 1990)
- Schizophrenia (, 2022)
- The dot pattern expectancy task: reliability and replication of deficits in schizophrenia (, 2010)
- Spine dynamics in the brain, mental disorders and artificial neural networks (, 2021)
- Computational study of NMDA conductance and cortical oscillations in schizophrenia (, 2014)
- Cognitive Control Errors in Nonhuman Primates Resembling Those in Schizophrenia Reflect Opposing Eff (, 2020)
- Dynamics of networks of excitatory and inhibitory neurons in response to time-dependent inputs (, 2011)
- A dynamical systems hypothesis of schizophrenia (, 2007)
- Gamma and Beta Bursts Underlie Working Memory (, 2016)

## Ground Truth Reference
- Figures: 9
- Tables: 0
- References: 41