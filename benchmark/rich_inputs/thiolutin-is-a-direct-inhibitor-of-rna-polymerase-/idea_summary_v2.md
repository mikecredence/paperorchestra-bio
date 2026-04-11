# Idea Summary

## Working title
Resolving the mode of action of thiolutin: complex in vivo effects but direct RNA Polymerase II inhibition in vitro

## Core question
Does thiolutin directly inhibit RNA Polymerase II, and if so, what cofactors and conditions are required for this activity? More broadly, what cellular pathways modulate thiolutin sensitivity in yeast?

## Motivation / gap
- Thiolutin is a dithiolopyrrolone natural product widely used as a transcription inhibitor for mRNA stability studies, yet its mechanism of action remains unresolved
- Recent work showed that reduced thiolutin/holomycin chelate Zn2+, and concluded that RNAP inhibition is indirect (via metalloprotein inhibition), directly contradicting classic in vitro studies that showed thiolutin can inhibit partially purified polymerases
- Nobody has systematically screened for genetic modifiers of thiolutin sensitivity in yeast, which could reveal the relevant cellular pathways
- The connection between thiolutin and oxidative stress (redox cycling, thioredoxin oxidation) has been proposed but not genetically dissected
- Thiolutin interacts with multiple metals (not just Zn2+), but the role of Mn2+ and Cu2+ has been largely overlooked
- The specific reductants needed for thiolutin activation in vivo are unclear -- glutathione was initially thought to be inert, but more recent data suggests it can reduce dithiolopyrrolones at physiological concentrations
- In vivo Pol II occupancy changes after thiolutin treatment have not been systematically profiled by genomics approaches

## Core contribution (bullet form)
- Three independent genetic screens (UV mutagenesis/forward genetics, manual Variomics, high-throughput Bar-seq of Variomics + deletion libraries) identify mutants in multidrug resistance, oxidative stress, metal homeostasis, and proteasome pathways that alter thiolutin sensitivity in S. cerevisiae
- Genetic evidence that thiolutin oxidizes thioredoxins (Trx1/Trx2) in vivo: trx1-delta trx2-delta double deletion confers resistance and suppresses trr1-delta hypersensitivity
- Demonstration that thiolutin induces oxidative stress partly through redox cycling, depleting total glutathione and inducing nuclear localization of the redox-sensitive Yap1 transcription factor
- Discovery that Mn2+ is a required cofactor: thiolutin plus DTT plus Mn2+ together (but not any pair alone) directly inhibit Pol II transcription initiation in vitro using purified components
- Characterization of a novel inhibition mode: thiolutin must bind Pol II before template DNA (clamp-inhibitor-like behavior), and excess DTT abrogates inhibition; when initiation block is bypassed on bubble templates, pause-prone defective elongation is observed
- Genome-wide Pol II ChIP-seq after thiolutin treatment shows widespread occupancy changes, with the largest effects at ribosomal protein genes and stress-responsive genes consistent with Tor pathway inhibition rather than specific transcription targeting

## Method in brief
The genetic approach combined three complementary screens in S. cerevisiae. A forward genetic screen used UV mutagenesis of a wild-type strain followed by selection on 10 ug/mL thiolutin plates, with causal mutations identified by bulk segregant analysis and whole-genome sequencing. In parallel, a Variomics library (random gene-specific mutants on CEN plasmids, covering nearly all yeast genes) was screened both manually (plating on thiolutin) and by high-throughput Bar-seq, where changes in barcode abundance after ~20 generations of growth in thiolutin (3 ug/mL for haploid non-essential, 4 ug/mL for diploid essential libraries) quantified fitness effects. Deletion libraries (plasmid-free versions of the Variomics strains selected on 5-FOA) were also screened by Bar-seq in liquid culture. Three biological replicates were performed for each high-throughput screen, and fitness scores from uptag and downtag barcodes showed excellent correlation.

For in vitro transcription assays, fully purified 12-subunit yeast Pol II was used with ssDNA or dsDNA templates and radiolabeled (32P-UTP) NTPs. Transcribed RNA was resolved on 10% polyacrylamide gels. Key conditions tested included thiolutin alone, thiolutin + DTT, thiolutin + Mn2+ (as MnCl2), and thiolutin + DTT + Mn2+ at various concentrations. Order-of-addition experiments tested whether thiolutin needed to be added before or after template DNA. Elongation was assessed using a transcription bubble template that bypasses the initiation requirement.

In vivo validation included Yap1-EGFP nuclear relocalization imaging (quantifying nuclear/cytoplasmic fluorescence ratios), glutathione depletion assays (measuring reduced GSH and total glutathione), plate growth assays with serial dilutions for dozens of mutant strains, Tecan plate reader growth curves for doubling time measurements, and Pol II ChIP-seq to profile genome-wide occupancy changes after thiolutin treatment.

## Target venue
Nucleic Acids Research
