Use the paper-builder skill to write a submission-ready LaTeX manuscript.
Target venue: eLife

## Idea Summary

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


## Experimental Log

# Experimental Log: Translational Regulation in Drosophila Brain

## Whole-Head Ribo-seq Overview (Fig 1)

### Footprint Distribution

| Region | % of Ribosome Footprints |
|--------|------------------------|
| Annotated CDS | 96.2% |
| 5' UTR | ~2-3% |
| 3' UTR | ~1% |
| Periodicity | Clear 3-nt codon-wise pattern |
| Footprint length analyzed | 21-nt (standard), 32-nt (initiation) |

### Transcriptome-Translatome Correlation (Fig 1C)

| Metric | Value |
|--------|-------|
| Squared Pearson correlation (R^2) | 0.664 |
| Interpretation | Substantial post-transcriptional regulation (mRNA and footprints do not match) |
| Genes analyzed | 9,611 with >= 1 read in both Ribo-seq and RNA-seq |

### Example Genes: Contrasting TE (Fig 1D-F)

| Gene | Product | mRNA Level | Footprints | TE |
|------|---------|-----------|------------|-----|
| Shaker (Sh) | Voltage-gated K+ channel | Moderate | Low | Low |
| Trehalase (Treh) | Trehalose hydrolase | Moderate (similar to Sh) | High | High |

### TE Distribution (Fig 1G)

| Metric | Value |
|--------|-------|
| Genes plotted | 9,611 |
| Bin size | 0.2 (log2 units) |
| TE variability | >20-fold between 5th and 95th percentiles |
| Distribution shape | Approximately log-normal |

### KEGG Pathway Enrichment by TE (Fig 1H, iPAGE analysis)

| TE Level | Enriched Pathways | P-value Threshold |
|----------|------------------|------------------|
| Low TE | Neuroactive ligand-receptor interaction | < 0.0005 |
| Low TE | Calcium signaling pathway | < 0.0005 |
| High TE | Metabolic pathways | < 0.0005 |

### GO Term Analysis of TE (Fig 1I)

| GO Term | Median TE | vs "All" Group |
|---------|-----------|----------------|
| Ion channels | Low | *** (P < 0.001, Dunn's test) |
| Neurotransmitter receptors | Low | *** (P < 0.001) |
| All genes | Reference | -- |
| Metabolic enzymes | High | ns (P > 0.05) |

## Cell-Type-Specific Ribo-seq (Fig 2)

### Experimental Setup

| Parameter | Value |
|-----------|-------|
| Neuron driver | nSyb-GAL4 (BDSC #39171) |
| Glia driver | repo-GAL4 (BDSC #7415) |
| Tagged protein | RpL3::FLAG (BDSC #77132) |
| IP antibody | Anti-FLAG M2 (Sigma F1804) |
| Beads | Dynabeads M-280 anti-mouse IgG |
| Elution | 3xFLAG peptide |
| Fly age | 4-8 days, mixed gender |
| Heads per replicate | ~500 |

### Differential Translation (MA-plot, Fig 2B)

| Category | Count | Definition |
|----------|-------|-----------|
| Differentially translated transcripts (DTTs) | 161 | >10x higher TE in neurons vs glia |
| Direction | Neuron-enriched translation | Neuronal genes preferentially translated |
| Enriched functions | Ion channels, neurotransmitter receptors | -- |

### Cell-Type TE Comparison (Fig 2)

| Gene Category | TE in Neurons | TE in Glia | Ratio |
|--------------|--------------|-----------|-------|
| Ion channels | High | Low | >10x for many |
| Neurotransmitter receptors | High | Low | >10x for many |
| Housekeeping genes | Similar | Similar | ~1x |
| Glial-specific genes | Lower | Higher | <1x |

## 5' Leader Ribosome Stalling in Glia (Fig 3)

### Meta-Gene Analysis of 161 DTTs (Fig 3A)

| Cell Type | Footprint Distribution Around Start Codon |
|-----------|-------------------------------------------|
| Neurons | Most footprints on CDS (after start codon) |
| Glia | Remarkable accumulation of footprints on 5' leader (before start codon) |
| Genome-wide control | Normal distribution for comparison |

Normalized by total footprints; 7,933 genes with TPM > 1 in both neuron and glia RNA-seq considered.

### 5' Leader Characteristics of DTTs

| Feature | DTTs vs All Genes |
|---------|------------------|
| 5' leader length | Relatively long |
| Number of upstream AUGs | Higher |
| uORF content | Enriched for small uORFs |

## Upstream AUG Ribosome Accumulation (Fig 4)

### 32-nt Footprint Analysis (Initiation-Associated)

| Analysis | Finding |
|----------|---------|
| Meta-gene around upstream AUG (glia, Fig 4A) | Peak of 32-nt footprints at upstream AUG codons |
| Meta-gene around annotated start (glia, Fig 4B) | Normal initiation pattern |
| Footprint accumulation on 5' leader (Fig 4C) | Enriched at upstream AUG positions in glia |
| Footprint accumulation on CDS (Fig 4D) | Normal distribution |

Footprint accumulation defined as ribosome footprints on each codon normalized by average of surrounding (-50 to +50) region.

## Transgenic Reporter Validation (Fig 5)

### Rh1-Venus Reporter System

| Construct | 5' Leader | Expression in Neurons | Expression in Glia |
|-----------|-----------|----------------------|-------------------|
| UAS-Rh1-Venus (wild-type 5' leader) | Contains uORFs | High | Low (suppressed) |
| UAS-m-Rh1-Venus (mutated 5' leader) | uORFs removed | High | Higher (de-repressed) |

### Rh1 Endogenous Data (Fig 5A-C)

| Metric | Value |
|--------|-------|
| Rh1-RA CDS Ribo-seq reads | Available in dataset |
| Neuron vs glia ribosome distribution | Footprint ratio on 5' leader much higher in glia |
| 6-base uORFs identified | Multiple consecutive start/stop codon pairs in 5' leader |

Fig 5B: Ribosome distribution on Rh1-RA showing footprint accumulation on 5' leader uORFs specifically in glia (blue) not neurons (green).
Fig 5C: Ratio of ribosome density on 5' leader vs CDS is higher in glia.

### Reporter Quantification

| Measurement | Rh1-Venus (WT 5' leader) | m-Rh1-Venus (mutated) |
|-------------|-------------------------|----------------------|
| Neuron expression | High | High (similar) |
| Glia expression | Low | Increased |
| Interpretation | uORFs suppress translation selectively in glia |

## Additional Observations

### Ribosome Stall at Initiation Codon (Fig 3 - supplement 1)

| Observation | Detail |
|-------------|--------|
| Specific transcripts | Remarkable stall at annotated start codon |
| Cell-type specificity | Observed in neurons but not whole heads |
| Gene identity | Transcripts massively expressed in fat bodies, less in nervous system |

### Molecular Machinery for uORF-Mediated Regulation

| Factor | Neuron vs Glia Expression |
|--------|--------------------------|
| eIF1 | Higher in neurons |
| eIF2alpha kinases | Higher in neurons |
| DENR/MCT1 | Higher in neurons |
| Interpretation | These factors facilitate main ORF translation past uORFs; enrichment in neurons may explain preferential neuronal translation |

## Fly Strains Used

| Strain | BDSC # | Purpose |
|--------|--------|---------|
| Canton-S | -- | Wild-type |
| nSyb-GAL4 (GMR57C10) | #39171 | Pan-neuronal driver |
| repo-GAL4 | #7415 | Pan-glial driver |
| tubulin-GAL4 | #5138 | Ubiquitous driver |
| MB010B | #68293 | Mushroom body driver |
| UAS-RpL3::FLAG | #77132 | Tagged ribosome |
| UAS-Rh1-Venus | Custom | WT 5' leader reporter |
| UAS-m-Rh1-Venus | Custom | Mutated 5' leader reporter |
| UASz-GFP | Gift | Control |

## Technical Parameters

| Parameter | Value |
|-----------|-------|
| RNase | RNase I from E. coli |
| Ribosome run-off prevention | Cycloheximide + chloramphenicol |
| Lysis | Multi-beads Shocker pulverization |
| DNase | Turbo DNase |
| IP incubation | 4C, 1 hour with rotation |
| Washes | 4x with lysis buffer |
| Elution | 3xFLAG peptide (100 ug/ml) |

## Key Figure Observations

- Fig 1A: Schematic of whole-head Ribo-seq and RNA-seq workflow
- Fig 1B: Meta-genome ribosome distribution shows 3-nt periodicity
- Fig 1C: Scatter plot of mRNA vs footprints (R^2 = 0.664) with neuronal genes highlighted
- Fig 1G: TE histogram shows >20-fold variability
- Fig 1H: iPAGE analysis shows neuron-related pathways enriched at low TE
- Fig 2A: Cell-type-specific Ribo-seq schematic with FLAG-IP
- Fig 2B: MA-plot showing differentially translated genes
- Fig 3A: Meta-gene plots revealing 5' leader footprint bias in glia
- Fig 4A: 32-nt footprint accumulation at upstream AUGs in glia
- Fig 5: Rh1-Venus reporter confirms uORF-mediated glial translational suppression

