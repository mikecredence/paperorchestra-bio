{
  "statistical_sentences": [
    "On both targets, we discover hits, including seven novel hits (14% hit rate) to KLHDC2 and four novel hits (44% hit rate) to NaV1.7 with single digit micromolar binding affinities.",
    "Results of other methods are obtained from Ref 28; c, Mean ROC enrichments at 0.5% (empty bar), 1% (patterned bar), 2% (solid bar) false positive rates, results are averaged over three independent runs and averaged over targets.",
    "Results of other methods are obtained from Ref 73\u201375, the same color scheme is used as in subpanel b; d, CASF2016 docking power, the docking success rates of the top ten methods are shown. e, CASF2016 screening power, the top 1% enrichment factors of the top ten methods are shown. f, CASF2016 screening power, the success rates of the top ten methods are shown.",
    "Even when a cutoff of 0.6 Tanimoto similarity for ligands and a sequence identity of 30% for proteins were used, it is likely that the contamination of these validation benchmarks still occurred.",
    "The second metric is the success rate of placing the best binder among the 1%, 5% or 10% top-ranked ligands over all target proteins in the dataset.",
    "In Fig. 1e and Fig. S4, the top 1% enrichment factor from RosettaGenFF-VS (EF1%=16.72) outperforms the second-best method (EF1%=11.9) by a significant margin.",
    "Similarly, Fig. 1f and Fig. S5 illustrates that RosettaGenFF-VS excels in identifying the best binding small molecule within the top 1/5/10% ranking molecules, surpassing all other methods.",
    "Notably, RosettaVS outperforms the second-best method by a factor of two (0.5/1.0% ROC enrichment), achieving state-of-the-art performance in early ROC enrichment, further highlighting the effectiveness of RosettaVS.",
    "We set out to identify compounds that can anchor to the diglycine-binding site of KLHDC2, which has recently been suggested as a promising PROTACs E3 platform for targeted protein degradation.33,34We used the OpenVS platform and VSX mode in RosettaVS to screen the Enamine-REAL library against the target protein structure, which contains approximately 5.5 billion purchasable small molecules with 80% synthesis success rate.",
    "Approximately 6 million compounds (0.11%) from the Enamine REAL library were subjected to docking.We took the top-ranked 1000 compounds and filtered out compounds with low predicted solubility, unsatisfied hydrogen bonds in the bound conformation, and followed by similarity clustering to reduce the redundancy in ligand structures.",
    "Approximately 4.5 million compounds (0.11%) from the ZINC22 library were subjected to docking.We first clustered the top 100,000 ranked small molecules, then applied filters on the top 1000 cluster representative molecules.",
    "IC50 values of better than 10 \u03bcM were observed for four compounds, translating to a hit rate of 44.4% (Fig. S17).",
    "Notably, compound Z8739902234 is state dependent (Fig. S18, left panel) and has moderate selectivity for hNaV1.7 versus hNaV1.5 and hERG channels (Fig. S18, right panel).biorxiv;2024.03.28.587262v1/FIG4F4fig4Fig. 4Deep learning accelerated virtual screening finds novel Nav1.7 binders.a, 2D structures of the best two compounds discovered from the initial virtual screening. b, Concentration-response curves and inactivated-state IC50 values (in \u00b5M, mean, 95% CI) for Z8739902234 (1.32, 1.14 - 1.55) and Z8739905023 (2.23, 2.14 - 2.46). c, Exemplary current traces showing that Z8739902234 and Z8739905023 inhibit the inactivated state of NaV1.7. d, Docked structure of Z8739902234 and Z8739905023.",
    "Fig. 4: Deep learning accelerated virtual screening finds novel Nav1.7 binders.a, 2D structures of the best two compounds discovered from the initial virtual screening. b, Concentration-response curves and inactivated-state IC50 values (in \u00b5M, mean, 95% CI) for Z8739902234 (1.32, 1.14 - 1.55) and Z8739905023 (2.23, 2.14 - 2.46). c, Exemplary current traces showing that Z8739902234 and Z8739905023 inhibit the inactivated state of NaV1.7. d, Docked structure of Z8739902234 and Z8739905023.",
    "Fig. S4: CASF2016 screening power top 1% enrichment factor results of all the methods.",
    "The success rate of including the best binder in the top 1/5/10% ranked molecules.",
    "The success rate of ranking the best protein target among the top 1/5/10% of all the targets given the ligand.",
    "Fig. S8: Success rate of identifying the best-affinity ligand among top 1% ranked ligands for each protein target in the CASF2016 forward screening power test on three subsets.",
    "In both cases, VSH predicted a better docking pose and ranked the ligand among top 1% due to predicted movement in receptor sidechains.",
    "IC50 (in \u00b5M, mean, 95% CI) for inactivated state: 1.32, 1.14 - 1.55; resting state: 13.1, 12.78 - 13.45.",
    "IC50 (in \u00b5M, mean, 95% CI)."
  ],
  "methods_sentences": [
    "While several compounds showed detectable activity in displacing the degron peptide, compound 29 (C29) stood out with the best IC50 of \u223c 3 \u03bcM (Fig. 2a, c).",
    "Compound Z8739902234 demonstrated the highest potency with IC50 = 1.3 \u03bcM for NaV1.7 in an inactivated state-dependent manner (Fig. 4 and Fig. S18).",
    "IC50 values of better than 10 \u03bcM were observed for four compounds, translating to a hit rate of 44.4% (Fig. S17)."
  ],
  "table_count": 0
}