# Experimental Log: Design Principles for Inflammasome Inhibition by Pyrin-Only-Proteins

> Extracted from full-text JATS XML (PaperOrchestra-quality inputs)

## Key Results

- sequences vastly differ (Broz & Dixit, 2016; Kagan et al., 2014; Lu & Wu, 2015).
- To elucidate how POPs recognize and regulate the assembly of different PYD filaments, we first implemented Rosetta-based in silico apporach that we had recently developed to define the directionality of the AIM2-ASC inflammasome (Matyszewski et al., 2021).
- Briefly, PYDs assemble into helical filaments in which each protomer provides six unique protein-protein interaction surfaces (e.g., Figure 1A and Figure 1 - Figure Supplement 2A-B, denoted as “Type” 1a/b, 2a/b, and 3a/b) (Lu et al., 2014; Lu & Wu, 2015).
- As we had done before (Matyszewski et al., 2021), we created a honeycomb-like sideview of PYD filaments in which the middle protomer makes all six required contacts for filament assembly (Figure 1 and Figure 1- Figure Supplement 2B).
- We then calculated Rosetta interface energies (ΔGs) for each PYD filament (e.g., Figure 1A, left), and also determined the ΔGs for POP•PYD interactions by replacing the center protomer with each POP (e.g., Figure 1A, three honeycombs on the right).
- Of note, we decided to conduct our in silico and subsequent biochemical experiments on tractable inflammasome components with well-known biological significances such as ASC, AIM2, IFI16, NLRP3, and NLRP6 (Broz & Dixit, 2016; Hochheiser, Behrmann, et al., 2022; Kerur et al., 2011; Lu et al., 2014; L
- The honeycombs were generated based on their respective cryo-EM structures except for IFI16PYD whose filament structure is unknown.
- We generated a homology model of IFI16PYD filament based on the GFP-tagged AIM2 filament (PDB: 6mb2), which produced more favorable ΔGs than the one generated from the tagless-AIM2PYD filament (PDB: 7k3r; Figure 1 -Figure Supplement 2C).We found previously that individual AIM2PYD and ASCPYD filament
- The interface analysis results from other inflammasome PYDs also showed similar symmetric energy landscapes (Figure 1A-E, left), suggesting that bidirectional assembly is universal to all PYD filaments.
- We next noted that the overall ΔGs for individual PYD filaments were significantly more favorable than those from any POP•PYD interactions, which in turn suggested that excess POPs would be necessary to inhibit the assembly of inflammasome PYDs (e.g., the sum of ASCPYD•ASCPYD interactions on the top
- POP1 showed more favorable overall ΔGs for ASCPYD compared to POP2 or POP3 (Figure 1A), seemingly supporting the previous report (and sequency homology) that POP1 is the master regulator of ASC (de Almeida et al., 2015).
- However, although it was reported that POP2 can inhibit ASCPYD more potently than POP1 in vivo (Ratsimandresy et al., 2017), its ΔGs were significantly less favorable (i.e., Figure 1A: POP1•ASCPYD=-24.7 vs.
- POP2•ASC = -0.8 on the top half).
- POP3, on the other hand, appeared to interact with ASC as favorably as POP1 at the bottom interfaces (Figure 1A; ΔG = -34.3 for POP1•ASCPYD vs.
- ΔG =-34.6 for POP3•ASCPYD), suggesting that it could also inhibit the central adaptor.
- For AIM2PYD, all three POPs showed comparable overall ΔGs on the bottom half (Figure 1B), which suggested that each of them could target AIM2.
- IFI16 favored POP3 the most (Figure 1C; e.g., ΔG = -9.6 for POP3•IFI16PYD on the top half); however, the other two POPs still showed more favorable ΔGs than homotypic IFI16PYD•IFI16PYD interactions on at least one individual interface (Figure 1C; e.g., Type 2a for POP1, Type 2b for POP2 and Type 1b 
- These results in turn suggested that not only POP3, but POP1 and POP2 might also recognize IFI16.
- It has been speculated that POPs interfere with the recruitment of ASC by upstream receptors (de Almeida et al., 2015; Devi et al., 2020; Indramohan et al., 2018; Periasamy et al., 2017; Ratsimandresy et al., 2017); however, it remains unknown whether they do so by directly inhibiting NLRPs, which a
- Our Rosetta analyses here suggest that POP1 could interact with NLRP3PYD on the top half (Figure 1D; ΔG = -31.4 for NLRP3PYD•NLRP3PYD vs.
- ΔG =-30.5 for POP1•NLRP3PYD), On the other hand, the interactions between POP2/3 and NLRP3PYD appeared much less favorable (Figure 1D).
- Similar to NLRP3PYD, POP1 again showed more favorable energy scores toward NLRP6PYD than POP2/3 (Figure 1E).
- Overall, although these results appear to rationalize some of the proposed target specificities of POPs (Devi et al., 2020; Indramohan et al., 2018), they also suggest a bit confounding interaction and recognition mechanisms, thus warranting further investigations via biochemical approaches.Mechanis
- When ectopically expressed in HEK293T cells, C-terminally mCherry-tagged ASCPYD forms filaments and full-length ASC (ASCFL) forms puncta (Matyszewski et al., 2021).
- Importantly, HEK293T cells do not contain any endogenous inflammasome components or POPs, providing an ideal cellular system for directly tracking their interactions (de Almeida et al., 2015; Matyszewski et al., 2021; Shi et al., 2016).
- Surprisingly, compared to co-transfecting eGFP alone, POP1-eGFP minimally inhibited the filament assembly of ASCPYD-mCherry (≤ 20% suppression vs.
- By contrast, co-transfecting POP2-eGFP or POP3-eGFP significantly reduced the amount of ASCPYD-mCherry filaments, with POP2 being more effective (Figure 2A-B; note more diffused mCherry signals and reduction in linear filaments in the presence of POP2 and POP3 in Figure 2A).
- Furthermore, POP1 reduced the number of ASCFL puncta by ∼ 30%, yet POP2 and POP3 were again more effective in preventing punctum formation (up to ∼ 80% reduction, Figure 2C- D).
- These results suggest that POP1 may not directly target ASCPYD.
- Moreover, unlike COPs that co-assemble with CARDs into filaments (Lu et al., 2016), our results indicate that POPs suppress filament assembly altogether.biorxiv;2022.08.02.502519v1/FIG2F2fig2Figure 2.POP1 does not directly inhibit ASC.(A) Sample fluorescent microscope images of HEK293T cells co-tran
- Blue: DAPI.(B) The relative amounts of ASCPYD-mCherry filaments (300 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP alone (-) (600 and 120 ng plasmids).
- N ≥ 4.(C) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged ASCFL (300 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green).
- Blue: DAPI.(D) The relative amounts of ASCFL-mCherry puncta (300 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP (-) (600 and 120 ng plasmids).
- n ≥ 4.(E) Time-dependent increase in FRET signals of a donor- and acceptor-labeled ASCPYD (2.5 µM total, black circle) was monitored with increasing concentrations POP1(50 and 150 µM), POP2 (3.3, 6.7, 13.3, 26.7, and 40 µM), or POP3 (3.25, 7.5, 15, 20, and 30 µM); darker shades correspond to increas
- Data shown are representatives of at least three independent measurements (IC50s are average values of these experiments.
- n = 3).(F) nsEM images of ASCPYD filaments (2.5 µM) in the presence and absence of POP1 (150 µM), POP2 (40 µM), or POP3 (30 µM).Our unexpected observations contradict the role of POP1 in directly inhibiting ASC assembly (de Almeida et al., 2015; Devi et al., 2020; Indramohan et al., 2018).
- POP1 behaved as a monomer without forming filaments or higher-order species in our hands (Figure 2- Figure Supplement 1A-B).
- On the other hand, recombinant POP2 and POP3 were prone to aggregation/degradation during purification and required an N-terminal maltose binding protein (MBP) tag to obtain intact proteins (Figure 2- Figure Supplement 1A).
- Cleaving MBP via Tobacco Etch Virus protease (TEVp) indicated that POP2 and POP3 form elongated oligomers with undefined structures (Figure 2- Figure Supplement 1B).We incorporated recombinant POPs into our well-established polymerization assay in which we track the Förster Resonance Energy Transfer
- Of note, our assay displays two distinct phases of filament assembly, namely the rate limiting nucleation (initial lag; double/triple-headed arrows in Figure 2E) followed by elongation (exponential/linear phase; single-headed arrows pointing to the upper righthand corner in Figure 2E (Matyszewski et
- Moreover, the presence of POP1 did not affect the formation of ASCPYD filaments when visualized with nsEM (Figure 2F).
- On the other hand, both POP2 and POP3 significantly prolonged the initial lag phase of ASCPYD polymerization in a dose dependent manner (up to ∼ 15 min delay in nucleation; Figure 2E), while also moderately affecting the elongation phase (≤ 20% reduction in the slope Figure 2E).
- Estimating the polymerization half-times at different POP concentrations indicated that POP2 and POP3 are similarly effective in suppressing the oligomerization of ASCPYD (Figure 2E, IC50s).
- When visualized via nsEM, no ASCPYD filaments were detected in the presence of POP2, and only a few filaments were seen with POP3 (Figure 2F).
- These results suggest that even if ASCPYDs form oligomers (rise in FRET signals in Figure 2E), most of them fail to assemble into intact filaments in the presence of POP2/3.
- Moreover, the complete absence of any ASCPYD filaments in the presence of POP2 is consistent with our cellular experiments in which POP2 was most potent in inhibiting the central adaptor (Figures 2B and 2F).
- Together, our in cellulo and in vitro experiments consistently indicate that POP1 is only marginally effective in directly suppressing the polymerization of ASC.
- We also find that both POP2 and POP3 impede the nucleation of the ASCPYD filament.Re-examining the Rosetta analyses in light of biochemical experimentsOur biochemical experiments indicated that excess POPs are required to inhibit the polymerization of ASC (Figure 2E), which is in agreement with the 
- However, although our in silico analyses suggested that POP1 should interact most favorably with ASCPYD (Figure 1A), our in vitro and in cellulo experiments consistently showed that POP1 is only marginally inhibitory (Figure 2).
- We thus re-examined our Rosetta results in light of our biochemical experimental results, and noted that the interface energy profiles of POP2•ASCPYD and POP3•ASCPYD are different from that of POP1•ASCPYD.
- For instance, all three POPs contain favorable protein•protein interaction surfaces for ASCPYD (ΔΔG = ΔGPYD•PYD- ΔGPOP•PYD ≤ 3.5; arbitrarily determined, marked as blue dots in Figure 2- Figure Supplement 2).
- However, although both POP2 and POP3 show multiple interfaces with significantly unfavorable ΔGs than ASCPYD•ASCPYD interactions, POP1•ASCPYD interfaces lack such negative interactions (ΔΔG ≥ 10.0; marked as red dots in Figure 2-Figure Supplement 2).
- These observations in turn raised the hypothesis that a combination of favorable (recognition) and unfavorable interfaces (repulsion) is necessary for POPs to interfere with the assembly of inflammasome PYDs.Mechanisms of ALR inhibition by POPsWe then set out to test our amended interpretation of Ro
- Here, we noted a mixture of both favorable and unfavorable interactions between all three POPs and both ALRs (Figure 3-Figure Supplement 1A-B), raising the possibility that not only POP3, but the other two POPs might also inhibit the oligomerization of ALRs.
- To test this, we monitored the filament assembly of AIM2PYD- mCherry and IFI16PYD-mCherry in HEK293T cells (Figure 3A-D).
- Compared to co-transfecting with eGFP alone, POP1-eGFP reduced the number of AIM2PYD and IFI16PYD filaments, apparently more effectively than against ASCPYD (Figure 2B vs.
- Figures 3B and 3D; e.g., at 1200 ng POP1, AIM2PYD and IFI16PYD assemblies were inhibited ∼60%, while ASCPYD assembly was suppressed ∼20%).
- On the other hand, co-transfecting POP2 or POP3 essentially obliterated the filament assembly of AIM2PYD and IFI16PYD (Figures 3A-B and 3C-D).
- In our FRET assays tracking AIM2PYD polymerization, all three POPs decreased the slope of the linear phase in a dose dependent manner without significantly affecting the initial lag phase (Figure 3E); recombinant IFI16PYD does not form filaments in our hands (Morrone et al., 2014).
- Our observations indicate that all three POPs can interfere with the elongation of the AIM2PYD filament, with POP3 being most effective (Figure 3E, IC50s).
- Moreover, imaging AIM2PYD filaments using nsEM in the presence of POP1 revealed that the filaments are shorter and fewer, and the presence of POP2/3 abrogated filament formation (Figure 3F).
- As seen from ASCPYD, the dearth of filaments in the presence of POP2/3 in our nsEM and in cellulo experiments (Figure 3B, D and F) indicated that AIM2PYD oligomers rarely progressed into functional filaments (i.e., rise in FRET signals in Figure 3E vs.
- the lack of filaments in Figures 3F).biorxiv;2022.08.02.502519v1/FIG3F3fig3Figure 3.Inhibition of ALR assembly by POPs.(A) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged AIM2PYD (300 ng; crimson) plus eGFP alone or POP-eGFP (1200 ng; green).
- Blue: DAPI.(B) The relative amounts of AIM2PYD-mCherry filaments (300 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP alone (-) (600 and 120 ng plasmids).
- n ≥ 4.(C) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged IFI16PYD (300 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green).
- Blue: DAPI(D) The relative amount of IFI16PYD-mCherry filaments (300 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP alone (-) (600 and 120 ng plasmids).
- N ≥ 4.(E) Time-dependent increase in FRET signals of a donor- and acceptor-labeled AIM2PYD (2.5 µM, black) was monitored with increasing concentrations of POP1 (25, 50, 100 and 150 µM), POP2 (12.5, 25, 50, and 75 µM), or POP3 (7.5, 15, 30, 40, and 50 µM); darker shades correspond to increasing POP c
- Data shown are representatives of at least three independent measurements (IC50s are average values of these experiments.
- n = 3).(F) nsEM images of AIM2PYD filaments (2.5 µM) in the presence and absence of POP1 (100 µM), POP2 (50 µM), or POP3 (40 µM).It is noteworthy that the oligomerization of PYD is important for stable dsDNA binding by ALRs (Morrone et al., 2015; Morrone et al., 2014).
- Conversely, although isolated AIM2PYD can form filaments by mass-action (i.e., high concentrations; (Morrone et al., 2015)), dsDNA provides a one-dimensional diffusion scaffold to facilitate the assembly of full-length ALRs at significantly lower concentrations (Morrone et al., 2015; Morrone et al.,
- AIM2FL forms punctum-like oligomers when transfected in HEK293T cells (Matyszewski et al., 2021), and we found that POP1 slightly reduced the number of AIM2FL puncta, while POP2 and POP3 were more effective (Figure 3- Figure Supplement 1C-D); IFI16FL localizes in the nucleus (Antiochos et al., 2018;
- Consistent with the lack of significant inhibition in cells (Figure 3- Figure Supplement 1 C-D), POP1 failed to interfere with dsDNA- binding/oligomerization of recombinant AIM2FL (Figure 3- Figure Supplement 2A).
- However, POP2 and POP3 still inhibited the dsDNA binding of AIM2, while only POP3 was inhibitory toward the dsDNA binding of recombinant IFI16FL (Figure 3- Figure Supplement 2B).
- Together, our observations indicate that POP3 directly inhibits ALR assembly (elongation in particular for AIM2PYD).
- We also find that POP1 and POP2 can inhibit the assembly of ALR filaments, with POP2 being significantly more effective than the former; the presence of activating ligands can diminish the inhibitory effect of POPs (Figure 3- Figure 3 Supplement 2).
- Furthermore, these results are consistent with our amended interpretation of Rosetta analyses in which a combination of favorable and unfavorable interfaces allow POPs to target and inhibit PYD filament assembly.POP1 likely targets upstream receptors instead of ASCAlthough it has been speculated tha
- Of note, our investigations here revealed that POP1 is ineffective in inhibiting the oligomerization of ASC (Figure 2).
- Moreover, albeit less inhibitory than POP2 or POP3, POP1 was more effective in suppressing the assembly of AIM2PYD and IFI16PYD filaments than that of ASCPYD (Figure 3).
- These observations prompted the new hypothesis that the role of POP1 is to interfere with the assembly of upstream receptors rather than directly inhibiting ASC (i.e., a “decoy” ASC; targeting ASC or multiple upstream receptors would result in the same phenotype).
- Indeed, our Rosetta analyses indicated that POP1 can make a combination of favorable and unfavorable interactions with both NLRP3PYD and NLRP6PYD (Figure 4- Figure Supplement 1).
- Furthermore, POP2 and POP3 also showed favorable and unfavorable interactions with NLRP3 (Figure 4- Figure Supplement 1A); although the ΔGs between NLRP6 and POP2/3 were largely unfavorable, the Type 3a surface showed an energy score that might allow the two POPs to recognize NLRP6 if present at hig
- Of note, NLRP2PYD-mCherry did not form filaments when expressed in HEK293T cells (Figure 4- Figure Supplement 1C), precluding further investigations despite its high sequence similarity to POP2 (Indramohan et al., 2018; Periasamy et al., 2017; Ratsimandresy et al., 2017).
- When co-transfected, POP1 was more effective in suppressing the filament assembly by both NLRP3PYD and NLRP6PYD than that of ASCPYD (Figure 4 A-D).
- For example, with 1200 ng POP1, ASCPYD assembly was only suppressed by ∼20%, but the filament assembly by NLRP3PYD and NLRP6PYD was suppressed 70% and 60%, respectively (Figure 2B vs.
- On the other hand, POP2 was less effective in inhibiting the polymerization of NLRPPYDs than that of ASCPYD (e.g., at 600 ng POP2, ASCPYD assembly was abolished, but the assembly of NLRP3PYD and NLRP6PYD was barely suppressed; Figure 2B vs.
- POP3 was almost equally effective in suppressing the polymerization of NLRPPYDs and ASCPYD, but not nearly as effectively as against ALRs (Figure 4A-D).
- For example, at 600 ng POP3, AIM2PYD assembly was suppressed 70%, but those of ASCPYD and NLRPPYDs were reduced by 40-50%; Figure 3B vs.
- Figures 2B, 4B, and 4D).biorxiv;2022.08.02.502519v1/FIG4F4fig4Figure 4.Inhibition of NLRPPYD assembly by POPs.(A) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged NLRP3PYD (600 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green).
- Blue: DAPI(B) The relative amounts of NLRP3PYD-mCherry filaments (600 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP alone (-) (600 and 120 ng plasmids).
- n ≥ 4.(C) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged NLRP6PYD (300 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green).
- Blue: DAPI(D) The relative amounts of NLRP6PYD-mCherry filaments (300 ng plasmid) in HEK293T cells when co-transfected with POP-eGFP (+) or eGFP alone (-) (600 and 120 ng plasmids).
- n ≥ 4.(E) Time-dependent increase in FRET signals of a donor- and acceptor-labeled NLRP6PYD (2.5 µM, black) was monitored with increasing concentrations of POP1 (25, 50, and 100 µM).
- POP3 (15, 30, and 60 µM); darker color shades correspond to increasing POP concentrations.
- Data shown are representatives of at least three independent measurements (IC50s are average values of these experiments.
- n = 3).(F) nsEM images of NLRP6PYD filaments (5 µM) in the presence and absence of POP1 (100 µM), POP2 (30 µM), or POP3 (30 µM).Next, using FRET-donor and acceptor labeled NLRP6PYDs, we then monitored whether POPs suppress the nucleation and/or elongation (recombinant NLRP3PYD does not auto-assemble
- POP1 predominantly inhibited the elongation of NLRP6PYD filament, and POP2 appeared to interfere with its nucleation.
- Although POP3 mostly reduced the elongation kinetics of NLRP6PYD, it also seemed to interfere with nucleation (Figure 4E).
- Consistent with these observations, the number and length of NLRP6PYD filaments were significantly reduced in the presence of POPs (Figure 4F).
- The lack of filaments (Figure 4F) despite the increase in FRET signals (Figure 4E) again indicate that NLRP6PYD oligomers fail to form intact filaments.
- Together with the results form investigating POP•ALR interactions, our observations are consistent with the idea that POP1 acts as a decoy ASC, interfering with the assembly of upstream PYDs.

## Figure Descriptions

### Figure 1.
Rosetta in silico analyses of putative POP•PYD interactions.(A-E). Rosetta interface energy scores (ΔGs) at individual filament interfaces for homotypic assemblies (left) and putative interactions with POPs (right). Each hexagon represents a PYD or POP monomer. The sum of ΔGs at the top and bottom h

### Figure 2.
POP1 does not directly inhibit ASC.(A) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged ASCPYD (300 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green). Blue: DAPI.(B) The relative amounts of ASCPYD-mCherry filaments (300 ng plasmid) in HEK293T 

### Figure 3.
Inhibition of ALR assembly by POPs.(A) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged AIM2PYD (300 ng; crimson) plus eGFP alone or POP-eGFP (1200 ng; green). Blue: DAPI.(B) The relative amounts of AIM2PYD-mCherry filaments (300 ng plasmid) in HEK293T cells 

### Figure 4.
Inhibition of NLRPPYD assembly by POPs.(A) Sample fluorescent microscope images of HEK293T cells co-transfected with mCherry- tagged NLRP3PYD (600 ng; crimson) plus eGFP alone or eGFP-tagged POPs (1200 ng; green). Blue: DAPI(B) The relative amounts of NLRP3PYD-mCherry filaments (600 ng plasmid) in H

### Figure 5.
Target selection and mode of inhibition of POPs.A cartoon summarizing the refined intrinsic target specificity of POPs. Solid red lines indicate the most likely primary inhibitory targets for each POP. Solid gray lines indicate an additional target that each POP could also directly inhibit. Dotted g

### Figure 1 Supplements 1
(A-C) Amino acid (a.a.) sequence alignments of POPs and their most similar PYDs. See also (de Almeida et al., 2015; Devi et al., 2020; Indramohan et al., 2018; Khare et al., 2014; Ratsimandresy et al., 2017)

### Figure 1 Supplements 2
(A) The “sideview” of the ASCPYD filament (PDB: 3j63). The center magenta protomer makes all six unique contacts with surrounding purple protomers for assembly.(B) The “honeycomb” sideview of the ASCPYD filament (the center protomer and six nearby protomers). Each interface “Type” is labeled, and th

### Figure 2 Supplements 1
(A) Size-exclusion chromatography (SEC; Superdex 75, Cytiva) profiles of recombinant POPs. *: peaks corresponding to monomeric POP1 and MBP-POP2/3 were collected and used in the current study.(B) Negative-stain electron microscopy (nsEM) images of untagged POP1 (100 µM), (MBP)- POP2 (20 µM), and (MB

### Figure 2 Supplements 2
Rosetta interface analysis results showing favorable (ΔΔG ≤ 3.5, blue dots) and unfavorable (ΔΔG ≥ 10.0, red dots) interactions between ASCPYD and POPs.

### Figure 3 Supplements 1
(A-B) Rosetta interface analyses results showing favorable (ΔΔG ≤ 3.5, blue dots) and unfavorable (ΔΔG ≥ 10.0, red dots) interactions between AIM2PYD (A)/ IFI16PYD (B) and POPs. For IFI16, we used ΔΔG ≥ 5.0 or positive ΔGs to identify unfavorable interactions due to the intrinsically weak interface 

### Figure 3 Supplements 2
(A-B) Plots of fraction fluoresceine-amidate (FAM)-labeled 60-bp dsDNA (10 nM) bound to AIM2FL (100 nM, (A)) and IFI16 (200 nM, (B)) with increasing concentrations of POPs. Shown is the average of two independent experiments for each POP.

### Figure 4 Supplements 1
(A-B) Rosetta interface analyses results showing favorable (ΔΔG ≤ 3.5, blue dots) and unfavorable (ΔΔG ≥ 10, red dots) interactions between NLRP3PYD (A)/ NLRP6PYD (B) and POPs. Pink dots indicate interfaces that might allow the recognition between NLRP6PYD and POPs (ΔG ∼9).(C) Sample fluorescent mic

### Figure 5 Supplements 1
(A) A cartoon describing the assembly of inflammasome PYDs in the presence of a basal level of POPs. The more favorable homotypic PYD•PYD interactions would readily outcompete any weak/transient interactions between POPs and PYDs (blue arrows).(B) A cartoon describing a possible reason why POP1 cann

## References
Total references in published paper: 50

### Key References (from published paper)
- NLRP3 cages revealed by full-length mouse NLRP3 structure control pathway activation (, 2021)
- IFI16 filament formation in salivary epithelial cells shapes the anti-IFI16 immune response in Sjogr (, 2018)
- The DNA sensors AIM2 and IFI16 are SLE autoantigens that bind neutrophil extracellular traps (, 2022)
- Crystal structure of NALP3 protein pyrin domain (PYD) and its implications in inflammasome assembly (, 2011)
- Association of Antibodies to Interferon-Inducible Protein-16 With Markers of More Severe Disease in  (, 2016)
- Inflammation-Nature’s Way to Efficiently Respond to All Types of Challenges: Implications for Unders (, 2018)
- Feedback loops shape cellular signals in space and time (, 2008)
- Inflammasomes: mechanism of assembly, regulation and signalling (, 2016)
- Prion-like polymerization underlies signal transduction in antiviral immune defense and inflammasome (, 2014)
- The PYRIN Domain-only Protein POP1 Inhibits Inflammasome Assembly and Ameliorates Inflammatory Disea (, 2015)
- An Update on CARD Only Proteins (COPs) and PYD Only Proteins (POPs) as Inflammasome Regulators (, 2020)
- AIM2 activates the inflammasome and cell death in response to cytoplasmic DNA (, 2009)
- The adaptor ASC has extracellular and ’prionoid’ activities that propagate inflammation (, 2014)
- Structural basis for distinct inflammasome complex assembly by human NLRP1 and CARD8 (, 2021)
- Directionality of PYD filament growth determined by the transition of NLRP3 nucleation seeds to ASC  (, 2022)
- Structure of the NLRP3 decamer bound to the cytokine release inhibitor CRID3 (, 2022)
- AIM2 recognizes cytosolic dsDNA and forms a caspase-1-activating inflammasome with ASC (, 2009)
- COPs and POPs Patrol Inflammasome Activation (, 2018)
- Mitochondrial cardiolipin is required for Nlrp3 inflammasome activation (, 2013)
- SMOCs: supramolecular organizing centres that control innate immunity (, 2014)
- Inflammasomes and Cancer (, 2017)
- IFI16 acts as a nuclear pathogen sensor to induce the inflammasome in response to Kaposi Sarcoma-ass (, 2011)
- The PYRIN domain-only protein POP3 inhibits ALR inflammasomes and regulates responses to infection w (, 2014)
- Acetylation modulates cellular distribution and DNA sensing ability of interferon-inducible protein  (, 2012)
- Molecular basis of caspase-1 polymerization and its inhibition by a new capping mechanism (, 2016)
- Plasticity in PYD assembly revealed by cryo-EM structure of the PYD filament of AIM2 (, 2015)
- Unified polymerization mechanism for the assembly of ASC-dependent inflammasomes (, 2014)
- Structural mechanisms of inflammasome assembly (, 2015)
- Digital signaling network drives the assembly of the AIM2-ASC inflammasome (, 2018)
- Preparation of filamentous proteins for electron microscopy visualization and reconstruction (, 2019)

## Ground Truth Reference
- Figures: 13
- Tables: 0
- References: 50