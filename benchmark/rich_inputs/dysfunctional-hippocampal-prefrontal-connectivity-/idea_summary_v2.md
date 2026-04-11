# Idea Summary

## Working title
Dysfunctional hippocampal-prefrontal network underlies a multidimensional neuropsychiatric phenotype following early-life seizure

## Core question
How do early-life seizures (ELS) produce dissociable long-term cognitive and sensorimotor impairments in adulthood, and what are the specific HPC-PFC circuit dysfunctions -- at the synaptic plasticity, oscillatory, and neurochemical levels -- that underlie each behavioral domain?

## Motivation / gap
- Children experiencing early-life seizures face heightened risk for epilepsy, cognitive impairment, ASD, ADHD, and psychiatric symptoms, but the pathophysiological mechanisms linking ELS to this multimorbidity spectrum are unclear
- ELS rodent models show behavioral alterations without severe neuronal loss, suggesting functional rather than structural circuit-level disruption
- The HPC-PFC circuit is implicated in both cognitive and sensorimotor processing and may serve as a common substrate for neurodevelopmental and psychiatric disorders
- Prior studies reported reduced hippocampal LTP after ELS, but the relationship between synaptic plasticity changes and specific behavioral domains has not been dissected
- No comprehensive study has characterized HPC-PFC network dynamics across multiple brain states (active behavior, NREM, REM, quiet wake) following ELS
- The association between specific neurobiological alterations (LTP, neuroinflammation, dopamine) and separate behavioral dimensions within the ELS phenotype remains unknown

## Core contribution (bullet form)
- Demonstrated that ELS in rats produces dissociable cognitive (working memory) and sensorimotor (hyperlocomotion, impaired PPI, psychostimulant sensitivity) impairments in adulthood despite no neuronal loss (NeuN immunohistochemistry in CA1 and PL)
- Found that cognitive deficits associate with aberrantly increased HPC-PFC LTP in a U-shaped dose-response relationship, while sensorimotor alterations associate with heightened neuroinflammation (GFAP expression) and altered dopamine neurotransmission
- Showed ELS rats display impaired HPC-PFC theta-gamma coupling during active behavior (reduced amplitude-amplitude correlation) and diminished theta coherence during REM sleep
- Discovered an abnormal brain state during active behavior in ELS rats resembling REM sleep oscillatory dynamics, identified through state-space analysis
- Used canonical correlation analysis (CCA) and machine learning classification (SVM, random forest) to demonstrate that the collective pattern of oscillatory alterations accurately distinguishes ELS from control animals

## Method in brief
Early-life status epilepticus was induced at postnatal day 11-12 in male Wistar rats using lithium chloride (127 mg/kg, i.p.) followed by methylscopolamine (1 mg/kg) and pilocarpine (80 mg/kg, s.c.), producing a 2-hour SE terminated by diazepam (5 mg/kg). Four cohorts totaling 17 litters were used: cohort 1 for acute SE electrophysiology (n=5 ELS), cohort 2 for behavioral tests (CTRL n=11, ELS n=14), synaptic plasticity (CTRL n=7, ELS n=7), and immunohistochemistry (CTRL n=9, ELS n=11), cohort 3 for freely moving HPC-PFC recordings (CTRL n=6, ELS n=9), and cohort 4 for psychostimulant sensitization (CTRL n=15, ELS n=14) and neurochemistry (CTRL n=8, ELS n=9).

Behavioral testing included radial arm maze working memory (21 days, training/test phases 30 min apart), open field locomotion, acoustic startle response, prepulse inhibition (PPI at 3 intensities), and amphetamine sensitization. Synaptic plasticity was assessed via in vivo HPC-PFC LTP with high-frequency stimulation of the ventral hippocampus while recording field postsynaptic potentials in the prelimbic cortex. Immunohistochemistry targeted NeuN (neuronal loss), parvalbumin (inhibitory interneurons), mGluR5, and GFAP (astroglia/inflammation) in CA1 and prelimbic cortex. Neurochemical quantification measured dopamine and metabolites in prefrontal cortex and striatum.

For electrophysiology in freely moving animals, chronic recordings from HPC and PFC were obtained across 24-hour sessions. Sleep-wake states were classified using spectrograms, EMG, and theta/delta ratios. Analyses included power spectral density, theta-gamma amplitude-amplitude correlation, HPC-PFC theta coherence, phase-amplitude coupling, and state-space mapping. Canonical correlation analysis linked multivariate neurobiological measures to behavioral dimensions, and machine learning classifiers (SVM, random forest) were trained on oscillatory features to distinguish ELS from control animals.

## Target venue
eLife
