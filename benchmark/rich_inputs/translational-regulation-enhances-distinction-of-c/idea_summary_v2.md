## Working title
Translational Regulation Enhances Cell-Type Distinction Between Neurons and Glia in the Drosophila Brain

## Core question
Does translational regulation amplify the distinction between neuronal and glial proteomes beyond what is evident from transcriptional differences alone, and what molecular mechanisms drive cell-type-specific translation?

## Motivation / gap
- Single-cell transcriptomics has catalogued mRNA differences between cell types, but proteomic diversity driven by translational regulation remains largely unexplored
- Translational efficiency (TE) can differ dramatically across genes, but cell-type-specific TE profiles are poorly characterized
- Neuronal genes like ion channels and neurotransmitter receptors are expressed at mRNA level in glia but may be translationally suppressed
- The role of 5' leader sequences and upstream ORFs (uORFs) in cell-type-specific translational control is unclear
- Technical challenges in performing Ribo-seq on genetically defined cell types in intact brains have limited progress

## Core contribution (bullet form)
- Performed cell-type-specific Ribo-seq and RNA-seq in Drosophila neurons (nSyb-GAL4) and glia (repo-GAL4) using FLAG-tagged ribosome immunoprecipitation, revealing substantial post-transcriptional regulation
- Identified 161 differentially translated transcripts (DTTs) with >10-fold higher TE in neurons than glia, enriched for ion channels and neurotransmitter receptors
- Found that ribosome footprints on DTTs show remarkable 5' leader bias in glia, with footprint accumulation at upstream AUG codons
- TE variability spans >20-fold between 5th and 95th percentiles in whole-head Ribo-seq (R^2 = 0.664 between mRNA and ribosome footprints)
- Demonstrated via transgenic Rh1-Venus reporters that small uORFs in the 5' leader confer selective translational suppression in glia
- KEGG pathway enrichment reveals low-TE genes enriched for neuroactive ligand-receptor interaction and calcium signaling

## Method in brief
Ribo-seq and RNA-seq were performed on Drosophila fly heads. For cell-type specificity, FLAG-tagged RpL3 (ribosomal protein L3) was expressed under nSyb-GAL4 (neurons) or repo-GAL4 (glia), followed by anti-FLAG immunoprecipitation to isolate cell-type-specific ribosomes. RNase I digestion generated ribosome-protected footprints. Translational efficiency was computed as ribosome footprints on CDS (TPM) divided by mRNA level (TPM). The 21-nt and 32-nt footprint fragments were analyzed separately to capture different ribosome states.

Footprint distribution on 5' leaders was analyzed to detect upstream AUG-mediated ribosome stalling. For 161 DTTs showing >10x neuron/glia TE ratio, meta-gene analysis around start codons revealed biased footprint accumulation in the 5' leader in glia. Transgenic reporter strains (UAS-Rh1-Venus with wild-type and mutated 5' leader) were used to test whether uORFs in the 5' leader sequence are sufficient to confer glial translational suppression.

## Target venue
eLife
