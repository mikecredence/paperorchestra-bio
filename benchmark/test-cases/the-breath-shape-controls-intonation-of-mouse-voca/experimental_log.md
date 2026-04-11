# Experimental Log: The breath shape controls intonation of mouse vocalizations

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- ResultsVocalizations are produced by a program coupled to breathingIt is possible that the ten murine ultrasonic vocalizations (USVs) defined by unique pitch patterns (‘syllable types’; Grimsley et al., 2011) are formed by distinct breaths or as substructures nested in a common breath.
- Prior work has suggested the latter (Sirotin et al., 2014).
- Male mice in the chamber were exposed to fresh female urine and robustly sniffed and vocalized for the first 5-10 minutes of the recording at a peak rate of about 4 events per second (n = 6) (Fig.
- A vocalization was classified as a narrow-band sound in the 40-120 kHz ultrasonic frequency range during a single breath (Fig.
- The instantaneous frequency of vocalization breaths was typically between 5-10 Hz (mean: 7.5 Hz) (Fig.
- 1C) and mostly occurred during episodes of rapid sniffs (8.5 - 10 Hz) (Fig.
- 1A and B), as previously reported (Sirotin et al., 2014, Castellucci et al., 2018).
- 1C) with subtly larger inspiratory and perhaps expiratory airflow despite similar durations of each phase (Fig.
- This led us to hypothesize that a distinct sub-program is activated within a breath to generate a vocalization.biorxiv;2023.10.16.562597v2/FIG1F1fig1Figure 1.The full repertoire of vocalizations occurs within a normal appearing breath.A, Male mice exposed to female urine produce ultrasonic vocalizat
- Exposure to female urine at time 0, n=6 mice.
- C, Left, histogram of the instantaneous frequency of breaths with and without USVs from n=6 animals.
- Right, bar graph of mean ± SEM of Ti, Te, and the ratio for n=6.
- p-values 0.40, 0.18, and 0.25; paired t-test.
- p-values 0.01, 0.27; paired t-test.
- F, Bar graph (mean ±SEM) of the percent of total USVs for each type from n=6 mice.The adult murine lexicon is composed of at least 10 USV syllable types that are defined by different, but stereotyped, patterns of pitch.
- Most breaths contain a single syllable (88%), which we define as a continuous USV event (Fig.
- 1F and S2-3), however, on some occasions, we observed 2 (8%) or 3 (4%) syllables separated by >20 ms within a single breath (Fig.
- This structure mirrors that described in neonatal cries (Wei et al., 2022).
- A pre-trained convolutional neural network (CNN) was used to classify USVs into different types based on changes in pitch (Fonseca et al., 2021), and the on- and offset of each vocalization was overlayed upon the corresponding breath airflow (Fig.
- S1), and the most common tended to start near the onset of exhalation and ended shortly there-after (like the up frequency modulated, step down, flat, and short types) (Fig.
- The bias of USV timing by the breath, combined with the USV modulation of breath length demonstrate these programs are independent but reciprocally coupled.biorxiv;2023.10.16.562597v2/FIGS1F6figs1Figure Supplemental 1.USV onset and offset during expiration.Left, raster plot of USV onset and offset t
- Below, the average expiratory length for n=6 animals.
- Note, while onset is biased to early expiration, vocalizations can begin throughout and even in late expiration.biorxiv;2023.10.16.562597v2/FIGS2F7figs2Figure Supplemental 2.Representative example of the most common USV types and the onset and offset times during expiration.Representative examples f
- S1.biorxiv;2023.10.16.562597v2/FIGS3F8figs3Figure Supplemental 3.Representative example of the many USV types and the onset and offset times during expiration.Representative examples for the remaining USV types and the representation of the onset and offset as Fig.
- Note, more complex vocalizations have onset and offset times that occur later in expiration.biorxiv;2023.10.16.562597v2/FIGS4F9figs4Figure Supplemental 4.Raster plot of USV on- and offset plotted upon the breathing rhythm.Raster plot of 1850 USVs aligned by the beginning of expiration with the sound
- Note that breaths after ∼1200 have late onset during expiration and delay the onset of the subsequent inspiration.Two mechanisms create the changes in pitch patternFluctuations in airflow speed through the larynx produce changes in the sound’s pitch.
- For example, augmenting airflow through the explanted rodent larynx increases pitch (Mahrt et al., 2016).
- We proposed two potential mechanisms that could contribute to how the laryngeal airflow is modulated to form the distinct USV types in the murine lexicon: one based on the swiftness of exhalation pushing air through the larynx (model 1), and the other based on the diameter of the laryngeal opening (
- On the other hand (model 2), a narrowed larynx increases pitch by speeding local airflow while simultaneously impeding the overall expiratory airflow measured by plethysmography; we call this negative intonation.
- Down or up frequency modulated (fm) USVs served as simple USV examples and we found that these were positively or negatively correlated, respectively (median r = 0.62 and −0.46, Fig.
- These distinguishing features are consistent with the sounds being produced by separate mechanisms to alter pitch, positive and negative intonation.biorxiv;2023.10.16.562597v2/FIG2F2fig2Figure 2.The ten types of USVs are produced by at least two mechanisms that modulate airflow.A, Left, example of t
- Note, the change in pitch mirrors airflow (annotated as “+”), consistent with the ‘breath modulation’ called model 1.
- Box and whisker plot of n=40 down fm correlation coefficients (r).
- B-D, Representative expiratory airflow and pitch, box and whisker plot of all r values, and onset / offset for complex (n=165), up fm (n = 589), and two step (n=61) vocalizations represented as in A.
- * = p < 0.05, one-way ANOVA with Sidak’s post-hoc test.Between these mechanisms, most syllable types displayed positive intonation.
- Five of the other eight USV syllable types had positively shifted intonation, the complex, step down, chevron, two step, and multi (median r = 0.31, 0.28, 0.32, 0.19, and 0.24 respectively) (Fig.
- In particular, the mirrored oscillations in the breath expiratory airflow and pitch during a complex vocalization best illustrated the positively coupled relationship (model 1, Fig.
- S5).biorxiv;2023.10.16.562597v2/FIGS5F10figs5Figure Supplemental 5.Correlation coefficient and onset / offset time for six USVs.Box and whisker plot of correlation coefficients (r) for step down (n=293), flat (n=337), short (n=168), chevron (n=99), multi (n=58), and step up (n=40) USVs.
- * = p < 0.05, one-way ANOVA with Sidak’s post-hoc test.The two step and step up USVs (median r = 0.19 and −0.03) appeared to have a portion of the pitch pattern correlated with the expiratory airflow, while the other part(s) were un- or anti-correlated (e.g., the two step, Fig.
- For example, step up syllables could be negative to negative (20%), negative to positive (20%), or positive to positive (60%) intonations.Across all USV types, we found that the relationship between airflow and pitch is relative rather than absolute which is expected since the relationship is determ
- In summary, these results establish an important positive connection between the breath expiratory airflow to modulate pitch (model 1).
- S2-3), we anticipated that USVs with positive intonation would have a coordinated re-activation of the diaphragm and laryngeal muscles later in expiration, while the up fm would only have laryngeal activity at expiration onset.EMG activity during basal breathing displayed the three phases of the bre
- The airflow measured by plethysmography had a ∼10ms lag when compared to the EMG activities (blue and red arrows, Fig.
- Like airflow, the sound followed EMG activity by ∼10ms.
- More than 10 mice were studied and, unsurprisingly, given the invasiveness of the EMGs only three produced robust signals and the number of acquired vocalizations varied from tens to thousands between these mice (n=70, 1482, 2819).
- The analysis below is from a single animal that had the clearest EMG signals, but the same results and relationships were observed in all three animals.biorxiv;2023.10.16.562597v2/FIG3F3fig3Figure 3.Ectopic activation of inspiratory and laryngeal muscles corresponds to changes in vocalization pitch.
- Note, blue and red arrows / lines indicate the ∼10ms offset of the peak EMG activity and airflow / sound measurements.
- C, Representative sound, airflow, diaphragm and laryngeal EMGs during the expiration of a down fm (n = 23 annotated), complex (n = 43 annotated), and up fm USV (n = 29 annotated).
- Model 1 – breath control: inspiratory and laryngeal muscles have alternating activity throughout the sound / expiration and a r > 0 for pitch vs expiratory airflow.
- Model 2 – laryngeal only: laryngeal but not diaphragm activity occurs during the sound and produces a r < 0 for pitch vs expiratory airflow.To study positive intonation, we analyzed the down fm and complex USVs.
- 3C) and the following laryngeal activity persisted during the sound.
- Complex USVs had an average of 1.5 cycles per expiration, the interval between diaphragm bursts was 43 ± 14 ms, and the laryngeal activity occurred at 69 ± 12% through this diaphragm-to-diaphragm interval.
- Also, in ∼19% of the complex USVs, sound, laryngeal, and diaphragm activity co-occurred, suggesting that other mechanisms contribute to the diversity of sounds.Up fm represents negative intonation, and correspondingly, the activity of the muscles distinct from the positively intonated types.
- 3C).In summary, these EMG studies of the key inspiratory muscle and larynx serve to reflect the core components of the breathing central pattern generator (CPG) that produce inspiration and post-inspiration.
- The novel finding that the endogenous pattern of the breathing CPG is re-engaged within an adult vocal breath, a ‘mini-breath’, mimics the rhythmic syllables of the neonatal vocalizations patterned by the intermediate Reticular Oscillator (iRO;Wei et al., 2022).
- The iRO is molecularly defined in the neonate by the co-expression of Preproenkephalin (Penk) and Vesicular glutamate transporter 2 (Vglut2) and is anatomically localized to the medullary ventral intermediate Reticular Formation (iRT) directly medial to the compact nucleus ambiguus (Wei et al., 2022
- First, we generated triple transgenic mice that label Penk+Vglut2+ neurons and the derived lineages with tdTomato (Penk-Cre; Vglut2-Flp; Ai65) (Fig.
- And second, we stereotaxically injected the iRO region of Penk-Cre; Vglut2-Flp mice with a Cre and Flp dependent reporter adeno-associated virus (AAV CreONFlpON-ChR2::YFP) (Fig.
- Consistent with the definition of the iRO in neonatal mice, tdTomato+ and YFP+ Penk+Vglut2+ neurons were found in the iRT adjacent to the compact nucleus ambiguus (Fig.
- These results demonstrate that the ventrolateral medulla of adult mice contains neurons with the molecular and anatomical identity of the iRO.biorxiv;2023.10.16.562597v2/FIG4F4fig4Figure 4.Anatomically and molecularly defined iRO neurons form a brainstem phonatory circuit.A, Labeling of Penk+Vglut2+
- B, Bilateral stereotaxic injection of AAV CreONFlpON-ChR2::EYFP into the iRO anatomical region of Penk-Cre;Vglut2-Flp adult mice.
- Arrowheads label neuron soma quantified right (n=3).
- F, Unilateral retrograde AAV CreON-EYP (AAVrg) stereotaxic injection into the iRO region in Vglut2- Cre adults (n=3).
- G, Model schematic of the iRO as a central component of the brainstem phonation circuit to convert a vocalization “go” cue from the PAG into a motor pattern.Neonatal iRO neurons are presynaptic to the kernel of breathing, the pacemaker for inspiration (preBötzinger Complex, preBötC) (Smith et al., 1
- We traced the YFP+ axons of Penk+Vglut2+ neurons (Penk-Cre; Vglut2-Flp and AAV CreONFlpON-ChR2::YFP) and found they elaborated within the nucleus ambiguus (NA) and retroambiguus (RAm) where laryngeal premotor and motor neurons localize (Fig.
- 4A, D), the breathing pacemaker (Fig.
- 4E), and the hypoglossal (tongue) motor nucleus (Fig.
- The projection patterns of these Penk+Vglut2+ neurons provide additional evidence that these adult neurons maintain the same connectivity properties as the neonatal iRO neurons, indicating they can control the key elements for vocalization: the breath airflow and larynx.In adult mice, vocalizations 
- To assess if the iRO region is positioned downstream of the ventrolateral PAG, we unilaterally injected Vglut2-Cre mice with a CreON-ChR2::YFP expressing retrograde traveling AAV (AAVrg) (Fig.
- 4G).Ectopic activation of the putative iRO induced vocalizationIf these labeled Penk+Vglut2+ neurons are indeed the iRO, we anticipated that ectopic activation would induce vocalization.
- First, we generated Penk-Cre;Vglut2-Flp;CreONFlpON-ReaChR triple transgenic mice which express the red-shifted Channel Rhodopsin in Penk+;Vglut2+ neurons and the derived lineage (ReaChR mice) and second, we stereotaxically injected the AAV CreONFlpON-Channel Rhodopsin2::YFP (ChR2) into the iRO regio
- In both experimental regimes, ectopic light activation of the Penk+Vglut2+ neurons induced bouts of vocalizations where the breathing rate was entrained by the frequency of stimulation (Fig.
- 5B and S6B), and the amplitudes of all elicited breaths were significantly increased (Fig.
- Some AAV-ChR2 mice showed previously described broad band harmonic vocalizations (like Grimsley et al., 2011), while others did not vocalize (n=5/9), likely due to incomplete labeling.
- Additionally, the ReaChR animals without vocalizations were found to have “off target” optic fiber implants (n=2/6).
- Taken together, these data are consistent with the notion that the iRO is sufficient to induce phonation via control of both breath airflow and laryngeal opening, just as it does in neonatal cries.biorxiv;2023.10.16.562597v2/FIGS6F11figs6Figure Supplemental 6.Optogenetic modulation of breathing and 
- B, Percent of stimulation bouts and breaths within each bout that contain USVs or broad band vocalizations in Penk-Cre;Vglut2-Flp;ReaChR and Penk-Cre;Vglut2-Flp virally injected mice.
- ReaChR with iRO optic fiber implantation, n=6.
- iRO stereotaxic viral injection: Penk-Cre;Vglut2-Flp, n=9; Oprm1-Cre;Vglut2-Flp, n=4; Penk-Cre, n=4; Tac1-Cre, n=5, Vgat-Cre, n=4.
- PreBötC stereotaxic viral injection: Vglut2-Cre, n=4.
- I, Bar graph of average ± standard deviation and average for each animal (circle) for the instantaneous breathing frequency before and during the optogenetic laser pulse (10 Hz).
- * p<0.05; *** p<0.001; **** p<0.0001; two-way ANOVA with Sidak’s post-hoc test.
- * p<0.05; ** p<0.01; two-way ANOVA with Sidak’s post-hoc test.
- Genotypes and injection sites as in C-H.biorxiv;2023.10.16.562597v2/FIG5F5fig5Figure 5.Ectopic activation of the iRO evokes airflow correlated USV types and switches the relationship of the anti-correlated types.A, Optogenetic activation of the iRO region in Penk-Cre;Vglut2-Flp;CreONFlpON-ReaChR mic
- **** p-value< 0.001; two-way ANOVA with Sidak’s post-hoc test, p > 0.05 for all other types.
- D, Box and whisker plot of the correlation coefficient between breathing airflow and pitch (r) for all opto evoked (n=395) and endogenous (n=1850) USVs and all opto evoked and endogenous vocalizations without down fm (n=143 and 1810) from n=4 opto and n=6 endogenous mice.
- **** p-value < 0.001; Mann-Whitney test.
- Right, box and whisker plot of correlation coefficients (r) for each optogenetically evoked and endogenous up fm USV (n=15 vs.
- box and whisker plot of correlation coefficients (r) for each optogenetically evoked and endogenous step up USV (n=15 vs.
- G, r value box and whisker plots for the remaining optogenetically evoked USV types (down fm n=242 vs.
- 99 from n=4 opto and 6 endogenous mice.
- E-G, Two-way ANOVA with Sidak’s post-hoc test for two way comparisons was used; all p-values >0.05.
- First, to ensure that just stimulation of breathing is insufficient to elicit vocalization, we optogenetically excited the glutamatergic preBötC neurons (Vglut2-Cre with AAV CreON-ChR2).
- And second, to determine if the ability to elicit vocalizations was generalizable to other neural types in the iRO anatomical region, we activated Penk+, µ-opioid receptor+Vglut2+, Tachykinin 1+, and Vesicular GABA transporter+ neurons and found that vocalizations were never induced upon light stimu
- In summary, these data functionally demonstrate the existence of Penk+Vglut2+ iRO neurons in adult mice and their ability to create vocalizations by modulating both breathing and presumably the larynx.Excitation of the iRO evoked nearly the entire murine lexiconAbove, we described that one mechanism
- We hypothesized that this property stems from the iRO’s capacity to control breathing, and so we made the following predictions: 1) that the USVs evoked after stimulation would be biased to those with an endogenous positive correlation between airflow and pitch (like the down fm and step down), and 

## Tables

### 

## Figure Descriptions

### Figure 1.
The full repertoire of vocalizations occurs within a normal appearing breath.A, Male mice exposed to female urine produce ultrasonic vocalizations (USV) at about 75 kilohertz (top) that coincide with the expiratory airflow (E, arbitrary units) of the breath cycle (bottom). Red box indicates the leng

### Figure Supplemental 1.
USV onset and offset during expiration.Left, raster plot of USV onset and offset times (ms) aligned to the beginning of expiration (onset, black and offset, red) for 1850 events. Below, the average expiratory length for n=6 animals. Right, histogram of the onset for each vocalization during a normal

### Figure Supplemental 2.
Representative example of the most common USV types and the onset and offset times during expiration.Representative examples for each if the most common USV types and the representation of the onset and offset as Fig. S1.

### Figure Supplemental 3.
Representative example of the many USV types and the onset and offset times during expiration.Representative examples for the remaining USV types and the representation of the onset and offset as Fig. S1. Note, more complex vocalizations have onset and offset times that occur later in expiration.

### Figure Supplemental 4.
Raster plot of USV on- and offset plotted upon the breathing rhythm.Raster plot of 1850 USVs aligned by the beginning of expiration with the sound onset and offset annotated by dots. The breath airflow is represented the gradient from blue to gray, where inspiration is blue, and expiration is gray. 

### Figure 2.
The ten types of USVs are produced by at least two mechanisms that modulate airflow.A, Left, example of the expiratory airflow and pitch for a down frequency modulated (fm) USV. Middle, magnification of airflow and sound. The scale of airflow is not displayed. The time of breath airflow from expirat

### Figure Supplemental 5.
Correlation coefficient and onset / offset time for six USVs.Box and whisker plot of correlation coefficients (r) for step down (n=293), flat (n=337), short (n=168), chevron (n=99), multi (n=58), and step up (n=40) USVs. * = p < 0.05, one-way ANOVA with Sidak’s post-hoc test.

### Figure 3.
Ectopic activation of inspiratory and laryngeal muscles corresponds to changes in vocalization pitch.A, Activity of the diaphragm (inspiratory) and laryngeal (thyroarytenoid and cricothyroid) muscles were recorded in vivo by electromyography (EMG) simultaneously with breathing and USVs. Right, examp

### Figure 4.
Anatomically and molecularly defined iRO neurons form a brainstem phonatory circuit.A, Labeling of Penk+Vglut2+ neurons in the iRO anatomical region in adult Penk- Cre;Vglut2-Flp;Ai65 mice (CreONFlpON-tdTomato) (observed in n=5 mice). The iRO region is defined as medial to the compact nucleus ambigu

### Figure Supplemental 6.
Optogenetic modulation of breathing and USVs for different molecularly defined cell types in the iRO anatomical region.A, Representative example of the change in breathing and ultrasonic vocalizations during a single light stimulation bout (blue box, 10 Hz) in Penk-Cre;Vglut2-Flp mice stereotaxicall

### Figure 5.
Ectopic activation of the iRO evokes airflow correlated USV types and switches the relationship of the anti-correlated types.A, Optogenetic activation of the iRO region in Penk-Cre;Vglut2-Flp;CreONFlpON-ReaChR mice evokes USVs (blue box, 5 Hz stimulation). USVs occur during, or shortly after laser o

## References
Total references in published paper: 46

### Key References (from published paper)
- Opioids depress breathing through two small brainstem sites (, 2020)
- Functions of the larynx and production of sounds. Handbook of mammalian vocalization – an integrativ (, 2009)
- The temporal organization of mouse ultrasonic vocalizations (, 2018)
- Vocalization frequency and duration are coded in separate hindbrain nuclei (, 2011)
- Flexible scaling and persistence of social vocal communication (, 2021)
- A suite of transgenic driver and reporter mouse lines with enhanced brain-cell-type targeting and fu (, 2018)
- The control of vocal pitch in human laryngeal motor cortex (, 2018)
- Structure and oscillatory function of the vocal folds. Handbook of mammalian vocalization – an integ (, 2009)
- Targeting cells with single vectors using multiple-feature boolean logic (, 2014)
- Analysis of ultrasonic vocalizations from mice using computer vision and machine learning (, 2021)
- Peripheral motor dynamics of song production in the zebra finch (, 2004)
- Development of social vocalizations in mice (, 2011)
- Neuronal networks involved in the generation of vocalization (, 2009a)
- Localization of the central pattern generator for vocalization (, 2009b)
- Anatomical characterization of cre driver mice for neural circuit mapping and manipulation (, 2014)
- Vertebrate sound production and acoustic communication (, 2016)
- Dual-channel circuit mapping reveals sensorimotor convergence in the primary motor cortex (, 2015)
- Ultrasonic output from the excised rat larynx (, 2010)
- Neural pathways underlying vocal control (, 2002)
- Generation, coordination, and evolution of neural circuits for vocal communication (, 2020)
- Laryngeal activity for production of ultrasonic vocalizations in rats. Handbook of mammalian vocaliz (, 2018)
- Interplay between mammalian ultrasonic vocalizations and respiration. Neuronal networks involved in  (, 2018)
- Divergent brainstem opioidergic pathways that coordinate breathing with pain and emotions (, 2022)
- Mice produce ultrasonic vocalizations by intra-laryngeal planar impinging jets (, 2016)
- Transgenic mice for intersectional targeting of neural sensors and effectors with high specificity a (, 2015)
- Central pattern generators and the control of rhythmic movements (, 2001)
- Neuromodulation of neuronal circuits: back to the future (, 2012)
- Circuit and synaptic organization of forebrain-to-midbrain pathways that promote and suppress vocali (, 2020)
- Brainstem control of vocalization and its coordination with respiration (, 2024)
- Singing with reduced air sac volume causes uniform decrease in airflow and sound amplitude in the ze (, 2008)

## Ground Truth Reference
- Figures: 11
- Tables: 1
- References: 46