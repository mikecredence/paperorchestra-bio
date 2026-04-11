# Experimental Log: Myelin dystrophy in the aging prefrontal cortex leads to impaired signal transmission and working memory decline: a multiscale computational study

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- RESULTSProgressive demyelination causes CV slowing and AP failures in model neuronsTo simulate myelin alterations in individual neurons, we adapted our multicompartment model tuned to data from rhesus monkey dlPFC (Rumbell et al., 2016) by attaching an axon model that captured nodes and detailed mye
- Myelinated segments included an internode with adjacent juxtaparanodes and paranodes, and tight junctions between the innermost myelin lamella and axolemma (see Methods; Figure 2A-B).
- We applied demyelination and remyelination perturbations to a cohort of 50 young (control) neuron models, with axonal parameters varying within biologically plausible ranges (Table 1; Supplementary Figure 1A-B).
- As such, a ‘fully remyelinated axon’ had all the demyelinated segments subsequently remyelinated, but with fewer lamellae and additional nodes compared to the unperturbed control case, consistent with empirical observations (Peters, 2009).
- The CV in control models varied across the cohort and in response to myelin alterations (Figure 2C; Supplementary Figure 1).
- CV changes and AP failures were more sensitive to variations along some dimensions of the parameter space than to others (e.g., myelinated segment length versus axon diameter), explored further below.biorxiv;2023.08.30.555476v2/FIG2F2fig2Figure 2.Action potential transmission in the single neuron mo
- During demyelination, lamellae were removed from a subset of segments; middle cartoon shows two lamellae remaining, indicating 50% lamellae removed relative to an unperturbed myelinated segment.
- During remyelination, select myelinated segments were replaced with two shorter myelinated segments separated by a new node; bottom cartoon shows remyelination with 50% of lamellae restored relative to unperturbed segments.
- At right are shown membrane potential traces simulated at the initial segment (top, dashed line) and near the distal end of one axon (here, 1.9 cm long) in the unperturbed, demyelinated, and remyelinated cases.
- Demyelinating 75% of segments by removing 50% of their lamellae resulted in a 70% reduction in conduction velocity, and failure of one AP.
- Remyelination of all affected segments with the same 50% of lamellae recovered the failed AP, and 98% of the CV delay relative to the demyelinated case (in one of the 30 simulated trials).
- (C) Distribution of the 50 models of the cohort across two dimensions of parameter space: myelinated segment length and axon diameter.
- Grayscale shade of each model represents the mean CV change across three demyelination conditions: 25, 50, 75% of segments losing lamellae, averaged over 30 randomized trials and lamellae removal conditions.biorxiv;2023.08.30.555476v2/TBL1T1tbl1Table 1Axon parameter ranges for LHS construction.AP pr
- Removing 25% of lamellae had a negligible effect on CV, regardless of how many segments were affected.
- However, when all lamellae were removed, CV slowed drastically – by 38 ± 10% even when just 25% of the segments were demyelinated in this way, and 35 ± 13% of APs failed.
- When 75% of segments lost all their lamellae, CV slowed by 72 ± 8% and 45 ± 13% of APs failed.
- We employed Lasso regression to identify key parameters that contributed to CV changes, since those changes preceded AP failures (Supplementary Figure 2A,C).
- Five of the 12 parameters analyzed contributed to CV changes during demyelination.
- Scale factors for leak and sodium conductance, axoplasm resistance, and tight junction resistance also controlled CV changes during demyelination.biorxiv;2023.08.30.555476v2/FIG3F3fig3Figure 3.Effects of demyelination on CV and AP failures in the single neuron model.(A) Heat maps showing CV change (
- The three blocks from left to right show increasing numbers of demyelinated segments in each axon (25, 50, and 75% of segments respectively), illustrated by cartoons on top.
- Color of each box indicates the mean CV change across 30 trials of each condition, ranging from 0% (no effect) to -100% (AP failure).
- Colors represent the percentages of segments demyelinated, from 10% (light red) to 75% (black).
- Error bars represent mean ± SEM, averaged across all cohort axons and trials.Remyelination leads to partial recovery from CV slowing and AP failuresWe next examined the extent to which remyelination with shorter and thinner segments, occurring after demyelination, restored axonal AP propagation (Fig
- losing all their lamellae (see Methods; Figure 4A-C).
- Most remyelinated models showed CV recovery from 0-100%, except for a few cases in which CV increased relative to the unperturbed models (Supplementary Figure 3A; see Discussion).
- When all demyelinated segments were subsequently remyelinated with sufficient lamellae –and none of the perturbed segments were bare– the CV recovered substantially and almost no AP failed (Figure 4B-C).
- When all demyelinated segments were remyelinated, there was a positive relationship between the initial demyelination rate and the CV recovery: CV recovered more when 75% of the segments were demyelinated (Figure 4B, black lines) than when only 25% were affected.
- This finding is consistent with observations of Scurfield and Latimer (2018), in which axons with more transitions between long (unperturbed) and short (remyelinated) segments had slower CV (Supplementary Figure 4).
- When incomplete remyelination left some segments bare (Figure 4B, colored lines), there was a negative relationship between the initial amount of demyelination and CV recovery: axons with more bare segments had reduced electrical insulation, and therefore recovered less.biorxiv;2023.08.30.555476v2/F
- Top row shows an unperturbed axon with 8 myelinated segments.
- Second row: 50% of segments are completely demyelinated.
- Third row: 25% of the demyelinated segments in second row (1 in total) are remyelinated with two shorter segments, each with 25% of lamellae restored.
- Fourth row: 75% of the demyelinated segments in the second row (3 in total) are remyelinated with two shorter segments, each with 50% of lamellae restored.
- Top row shows an unperturbed axon with 8 myelinated segments.
- Second row: 50% of segments are partially demyelinated (with 50% of lamellae removed).
- Third row: 50% of the demyelinated segments in second row (2 in total) are remyelinated with two shorter segments, each with 50% of lamellae restored.
- In panels B, C, E, and F, the x-axis refers to the percentage of myelin lamellae restored relative to unperturbed segments, starting at 0% (no remyelination).
- Line styles represent the percentage of segments initially demyelinated, from 25% (dashed) to 75% (thick solid).
- Colors represent the extent of remyelination, from 25% (light red) to 100% (black).
- For readability, error bars (representing ± SEM) are shown only for the condition of 50% demyelination of segments.We also simulated remyelination after a milder partial demyelination, where affected segments initially lost only half their lamellae (Figure 4D).
- Overall trends were similar to, but less severe than, those for the complete demyelination case (Figure 4E-F; Supplementary Figure 3B).
- There were also fewer AP failures under partial demyelination conditions, relative to the corresponding complete demyelination cases (Figure 4C vs.
- 4F).Results for the percentage of AP failures (Figure 4C,F) were consistent with those for CV recovery.
- Remyelinating all previously demyelinated segments, even adding just 10% of lamellae, brought AP failure rates down to 14.6 ± 5.1%.
- Remyelinating all affected segments with 75% of lamellae (the maximal amount of remyelination) nearly eliminated AP failures (1.8 ± 1.1%).
- For example, when one eighth of segments were remyelinated with the maximal amount of lamellae and one eighth were left bare, 25.7 ± 11.5% of APs failed across the cohort (Figure 4C, red dashed line and arrow).
- AP failure rates were slightly lower when starting with partial demyelination: 10.6 ± 7.6% of APs failed in the analogous paradigm (Figure 4F, red dashed line and arrow).
- Applying Lasso regression to CV recovery after remyelination (Supplementary Figure 2C,D) found 10 of the 12 parameters contributed significantly; only myelin length and axoplasm resistance were omitted.
- We focused on spatial working memory because the underlying neural network mechanisms have been studied and modeled in detail (e.g., Compte et al., 2000; Hansel and Mato, 2013; Ibañez et al., 2020).
- We built on a previous spiking neural network model that accounts for many experimental findings (Hansel and Mato, 2013).
- It consists of 16,000 excitatory and 4,000 inhibitory integrate-and-fire neurons (see Methods).
- Recurrent excitatory synapses are facilitating, as has been empirically observed in PFC (Hempel et al., 2000; Wang et al., 2006), which promotes robust and reliable persistent activity despite spatial heterogeneities in the connectivity or in the intrinsic properties of the neurons.We first simulate
- The center of the bump encodes the remembered spatial location (Figure 5B,i; Compte et al 2000; Hansel and Mato, 2013).
- Successful trials require a sufficiently strong activity bump throughout the delay period, quantified by the memory strength (Figure 5C, blue line).
- If the memory strength decreases over time (e.g., caused by the demyelination/remyelination conditions discussed below) the memory duration –the period during which the network can retain the stimulus– becomes limited (Figure 5C).
- This leads to trial-to-trial variability in the cue position read out from the network activity, modeling the variability of recalled spatial locations observed empirically (Figure 5B, right panels; Wimmer et al., 2014).
- This memory diffusion increases with the delay duration, consistent with decreasing working memory precision observed experimentally (Figure 5D; Funahashi et al., 1989).
- The bump movement during the delay also has a directed component, i.e., a systematic bias clockwise or counterclockwise away from the cue location, caused by heterogeneities in the network connectivity (Figure 5B, right panels and Figure 5E; Hansel and Mato, 2013).
- However, because of their established relationship with working memory performance, in the following we focus on memory duration, corresponding to complete forgetting, and memory diffusion, corresponding to working memory precision.biorxiv;2023.08.30.555476v2/FIG5F5fig5Figure 5.Action potential fail
- (B) Excitatory neuron activity for a cue stimulus presented at 135° of an (i) unperturbed control network, (ii) a network with demyelination, and (iii) a network with remyelination.
- The points show average spike rates of individual neurons and the solid line the average over 500 nearby neurons.
- (ii) Shows the effect of AP failure probabilities corresponding to demyelination of 25% of the myelinated segments by removing 75% of the myelin lamellae.
- (iii) Corresponds to AP failure probabilities for remyelination of 50% of the demyelinated segments by adding 75% of the myelin lamellae back, after previous partial demyelination of 25% of the segments.
- (C) Memory strength as a function of time and corresponding memory duration (horizontal bars; memory strength ≥ 0.4; see Methods).
- A similar increase of working memory diffusion with demyelination is also observed in networks with overall higher diffusion (Supplementary Figure 5).
- When demyelination is restricted to a part of the network, diffusion only increases in the perturbed zone (Supplementary Figure 7).
- The performance measures in C-E were obtained by averaging across 280 trials and 10 networks, either control (B,i) or perturbed (B, ii-iii).To investigate how myelin alterations affect working memory maintenance, we explored in the network model the same demyelination and remyelination conditions as
- Only unrealistically long delays led to a slight decrease in performance (Supplementary Figure 6).
- For AP failure probabilities matched to the distribution of AP failure probabilities across the cohort of 50 single neurons above, we observed a decay of the activity bump (i.e., reduced memory strength over time) in the network model.
- This can ultimately lead to extinction of the activity bump during the delay period, representing complete forgetting of the remembered stimulus (reduced memory duration; Figure 5B, ii and iii; Figure 5C and Supplementary Figure 10A).
- For a mild reduction of the bump amplitude, memory duration was not affected (Figure 5C, purple line) but memory diffusion increased compared to the control network (Figure 5B, iii and Figure 5D).
- This increase in memory diffusion is consistent with mathematical analysis of firing rate models showing that the bump diffusion depends inversely on the squared bump amplitude (Kilpatrick and Ermentrout, 2013; Esnaola-Acebes et al., 2022).Impact of demyelination and remyelination on working memoryW
- In each of the 10 networks, we set the AP failure rate of the excitatory neurons according to the distribution of failure probabilities of the neurons in the single neuron cohort for the given demyelination or remyelination condition.
- Thus, we took into account the heterogeneity of demyelination and remyelination effects from our single neuron cohort (Figure 3A; Supplementary Figure 3).
- Note that this heterogeneity originates from differences in axon properties, but probabilities of failure for all neurons in the network correspond to the same degree of demyelination (Figure 6).
- We will also consider networks that contain different combinations of axons with either intact or perturbed myelin (Figure 7 and Figure 8).biorxiv;2023.08.30.555476v2/FIG6F6fig6Figure 6.Working memory function in the network model is impaired by demyelination and recovered by sufficient remyelinatio
- Right panel: Same as the middle panel but for partial demyelination (removal of 50% of the myelin lamellae) rather than complete demyelination.
- In all cases, the performance measures were obtained by averaging across the 10 perturbed cohort networks and the 280 trials simulated for each network.
- The average memory duration for the 10 unperturbed, control networks in the cohort (averaged across 280 trials) was 4 seconds, and the average diffusion constant was 0.064 (both values corresponding to the case of 0% of myelin lamellae removed in the left panels of A and B, respectively; not shown).
- Error bars represent mean ± SEM, averaged across all networks and trials.biorxiv;2023.08.30.555476v2/FIG7F7fig7Figure 7.Reduced normal myelin is associated with decreased working memory performance in the network model.(A) Schematic of the quantification of unperturbed, normal myelin sheaths in grou
- Linear regressions show significant positive correlations in both cases (memory duration: r = 0.703, p = 3.86×10-10; diffusion constant: r = -0.802, p = 1.26×10-14).
- Squares: all the demyelinated segments in the perturbed axons had 75% of the myelin lamellae removed.
- Black horizontal bars indicate the percentage of normal sheaths observed in electron microscopy images from young and aged rhesus monkeys dlPFC (Peters and Sethares, 2002).biorxiv;2023.08.30.555476v2/FIG8F8fig8Figure 8.A higher proportion of new myelin sheaths impairs working memory in the network m
- Linear regressions show significant negative correlations in both cases (memory duration: r = -0.852, p = 4.92×10-7; diffusion constant: r = 0.607, p = 0.003).
- The remyelinated axons in the groups have different proportions of segments remyelinated after partial demyelination, by adding 25% of the myelin lamellae back.
- Black horizontal bars indicate the percentage of paranodal profiles observed in electron microscopy images from young and aged rhesus monkeys dlPFC (Peters and Sethares, 2003).Demyelination impairs working memory performance compared to control networksWe found that the memory duration was not affec
- However, when between 55% and 75% of the myelin lamellae were removed, the memory duration began to decrease, depending on the percentage of axonal segments that were demyelinated.
- In this case, increasing the percentage of demyelinated segments from 10% to 50% led to a progressive impairment, whereas an increase to 75% of the segments did not impair memory duration further.
- Finally, in cases where 100% of the myelin lamellae were removed, the memory duration dropped to ≤ 1 s, regardless of the percentage of segments that were demyelinated.
- In a similar trend, memory diffusion increased, that is, working memory became less precise starting when removing between 25% and 50% of the myelin lamellae (Figure 6B; left panel).
- Again, we found a progressive impairment, depending on the percentage of myelin lamellae removed and the percentage of myelinated segments affected, with a ceiling effect when more than 50% of segments were demyelinated.Complete remyelination recovers network functionWe observed that remyelination o
- However, working memory precision is not fully recovered in all these cases, indicated by an increase in the diffusion constant (Figure 6B).
- The performance of control networks was completely recovered only when 75% of the myelin lamellae were added back to the remyelinated segments.
- Thus, despite the new shorter and thinner myelin sheaths compared to the original intact ones, complete remyelination is able to recover control, unperturbed network function.Incomplete remyelination leads to partial recoveryWe studied the effect of incomplete remyelination (remyelination of 25% - 7
- When we remyelinated between 25% - 75% of the previously completely demyelinated segments, we did not observe a significant recovery of the memory duration (Figure 6A; middle panel; memory duration ≲ 1 s in all cases).
- Memory diffusion was partly recovered compared to the complete demyelination case (compare left and middle panels in Figures 6B) when 50% - 75% of the demyelinated segments were remyelinated, but it remained far from the performance of the control network.
- However, when we remyelinated between 25% - 75% of the previously only partially demyelinated segments, both memory duration and memory diffusion were restored closer to the values of the control networks (Figure 6A-B; right panel).Alternative working memory mechanismsWorking memory in our neural ne
- Other mechanisms have been proposed, including that working memory maintenance may rely on activity-silent memory traces (Mongillo et al., 2008; Stokes, 2015; Barbosa et al., 2020).
- We found that AP failures corresponding to demyelination caused working memory errors qualitatively similar to the delay-active network (Supplementary Figure 8).
- On the other hand, increasing propagation delays did not lead to additional working memory errors, unless we include unrealistically high values (uniform distribution in the range of 0 to 100 ms; Supplementary Figure 9).
- That is, we simulated networks with excitatory neurons having AP failure probabilities matched to both neuronal axons with intact and with altered myelin sheaths in different degrees, as likely occurs in the aging brain (Figure 1).Fewer normal myelin sheaths lead to decreased network performanceWe r
- Quantifying the average degree of demyelination in each simulated network allowed us to predict working memory deficits for a degree of demyelination that is within the empirically observed range of 90% to 100% normal myelin (Peters and Sethares, 2002).
- We observed that the performance was impaired – memory duration significantly decreased (Figure 7B), and memory diffusion significantly increased (Figure 7C) – when the percentage of normal sheaths decreased.
- These results are consistent with an experimentally observed increased cognitive impairment in various learning and working memory tasks (including the delayed recognition span task, a spatial working memory task) with an age-related decrease of the percentage of normal sheaths in dlPFC of rhesus mo
- Importantly, our results indicate that myelin alterations alone can account for significant working memory impairment, pointing to demyelination as a key factor in age-related working memory decline.Shorter and thinner myelinated segments impair working memoryTo predict the effects of remyelination 
- Empirical studies have found an age-dependent increase in the percentage of paranodal profiles, indicative of more and shorter myelin sheaths, from 5% in young monkeys to 17% in aged monkeys (Peters and Sethares, 2003).
- Here, we used different proportions of incomplete remyelination as studied in Figure 6 (axons with either 25, 50 or 75% of their segments remyelinated), and we quantified the overall percentage of new myelin sheaths in the networks.
- We simulated networks with up to a 45% of new myelin sheaths and we observed that performance was significantly impaired compared to the young, control networks with intact myelin: memory duration decreased to almost 1s (Figure 8B) and diffusion constant increased (Figure 8C).
- This is consistent with empirical findings showing that cognitive impairment for a cohort of 18 young and aged rhesus monkeys increased with an increase of the percentage of paranodal profiles in the dlPFC (Peters and Sethares, 2003).

## Tables

### Table 1
> Axon parameter ranges for LHS construction.


## Figure Descriptions

### Figure 1.
Electron photomicrographs (transverse sections) depicting age-related alterations in myelinated nerve fibers of area 46 of the rhesus monkey dlPFC.(A) Neuropil from a 10-year-old monkey. Healthy and compact myelin is visible as thick outlines surrounding nerve fibers which have been sectioned at the

### Figure 2.
Action potential transmission in the single neuron model.(A) Cartoon of the model with a close-up view of unperturbed, demyelinated, and remyelinated segments (not to scale). The paranodes, juxtaparanodes, and internodes (shown in different shades of red) were insulated by myelin lamellae, adjacent 

### Figure 3.
Effects of demyelination on CV and AP failures in the single neuron model.(A) Heat maps showing CV change (reduction relative to the CV of the corresponding unperturbed models, measured in %) in response to select demyelination conditions across the 50 cohort axons (see Methods). Axons arranged vert

### Figure 4.
CV recovery in response to remyelination.(A) Cartoons illustrating representative remyelination conditions after select segments were completely demyelinated. Top row shows an unperturbed axon with 8 myelinated segments. Second row: 50% of segments are completely demyelinated. Third row: 25% of the 

### Figure 5.
Action potential failures impair working memory performance in a spiking neural network model.(A) Schematic of the delayed response task. Subjects fixate at the center of a computer screen and need to remember a cue stimulus, presented at one out of eight locations through the delay period, before i

### Figure 6.
Working memory function in the network model is impaired by demyelination and recovered by sufficient remyelination.(A) Memory duration and (B) diffusion constant for simulations of the delayed response task, as in Figure 5, for a systematic exploration of the effect of AP failure probabilities corr

### Figure 7.
Reduced normal myelin is associated with decreased working memory performance in the network model.(A) Schematic of the quantification of unperturbed, normal myelin sheaths in groups of neurons containing intact and demyelinated axons with different proportions of demyelinated segments (see Methods)

### Figure 8.
A higher proportion of new myelin sheaths impairs working memory in the network model.(A) Schematic of the quantification of new myelin sheaths in groups of neurons containing intact and partly remyelinated axons. Vertical purple lines indicate cross sectional planes that model electron microscopy i

## References
Total references in published paper: 103

### Key References (from published paper)
- Neuropsychological and neurophysiological changes in healthy adult humans across the age range (, 1993)
- The node of Ranvier in CNS pathology (, 2014)
- White matter involvement after TBI: Clues to axon and myelin repair capacity (, 2016)
- Subtle paranodal injury slows impulse conduction in a mathematical model of myelinated axons (, 2013)
- Neural evidence for categorical biases in location and orientation representations in a working memo (, 2021)
- Interplay between persistent activity and activity-silent dynamics in the prefrontal cortex underlie (, 2020)
- Single-domain/bound calcium hypothesis of transmitter release and facilitation (, 1996)
- Computer simulation of action potentials and afterpotentials in mammalian myelinated axons: the case (, 1985)
- Age changes in myelinated nerve fibers of the cingulate bundle and corpus callosum in the rhesus mon (, 2010)
- Conduction velocity and spike configuration in myelinated fibres: computed dependence on internode d (, 1977)
- Synchronous oscillatory neural ensembles for rules in the prefrontal cortex (, 2012)
- Age-related alterations to working memory and to pyramidal neurons in the prefrontal cortex of rhesu (, 2022)
- Increased Action Potential Firing Rates of Layer 2/3 Pyramidal Cells in the Prefrontal Cortex are Si (, 2005)
- What is the optimal value of the g-ratio for myelinated fibers in the rat CNS? A theoretical approac (, 2009)
- The Distributed Nature of Working Memory (, 2017)
- Neurochemical changes in the aging brain: A systematic review (, 2019)
- Physiological Dynamics in Demyelinating Diseases: Unraveling Complex Relationships through Computer  (, 2015)
- Synaptic Mechanisms and Network Dynamics Underlying Spatial Working Memory in a Cortical Network Mod (, 2000)
- Temporally irregular mnemonic persistent activity in prefrontal neurons of monkeys during a delayed  (, 2003)
- Different macaque models of cognitive aging exhibit task-dependent behavioral disparities (, 2018)
- Functional consequences of age-related morphologic changes to pyramidal neurons of the rhesus monkey (, 2015)
- The impact of internodal segmentation in biophysical nerve fiber models (, 2014)
- Aging compromises oligodendrocyte precursor cell maturation and efficient remyelination in the monke (, 2022)
- Flexible integration of continuous sensory evidence in perceptual estimation tasks (, 2022)
- Age-related impairment in executive functioning: updating, inhibition, shifting, and access (, 2004)
- Remyelination in the CNS: from biology to therapy (, 2008)
- Mnemonic coding of visual space in the monkey’s dorsolateral prefrontal cortex (, 1989)
- Myelin in the Pathophysiology of Autism Spectrum Disorder (, 2020)
- Metabolic implications of axonal demyelination and its consequences for synchronized network activit (, 2023)
- Working Memory in People with Schizophrenia (, 2023)

## Ground Truth Reference
- Figures: 8
- Tables: 1
- References: 103