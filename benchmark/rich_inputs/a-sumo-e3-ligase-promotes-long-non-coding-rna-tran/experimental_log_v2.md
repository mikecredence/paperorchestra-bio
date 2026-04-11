# Experimental Log: SUMO E3 Ligase Ema2 and lncRNA Transcription in Tetrahymena

## Strains and Growth Conditions

| Parameter | Value |
|-----------|-------|
| Organism | Tetrahymena thermophila |
| Wild-type strains | B2086, CU427, CU428 |
| MIC-defective star strains | B*VI, B*VII |
| Growth medium | SPP with 2% proteose peptone |
| Growth temperature | 30 degrees C |
| Conjugation induction | Wash growing cells (~5-7 x 10^5/mL), pre-starve 12-24 hr, mix two mating types in 10 mM Tris pH 7.5 at 30 degrees C |

## Antibodies Used

| Antibody | Target | Source | Dilution (IF) | Dilution (WB) |
|----------|--------|--------|---------------|---------------|
| Anti-H3K27me3 | Histone 3 K27 trimethylation | Millipore 07-449 | 1:1000 | 1:10000 |
| Anti-HA HA11 | HA epitope tag | Covance clone 6B12 | 1:1000 | 1:10000 |
| Anti-H3K9me3 | Histone 3 K9 trimethylation | Active Motif 39162 | 1:1000 | 1:10000 |
| Anti-GST | GST tag | BD Biosciences 554805 | -- | 1:10000 |
| Anti-His | His tag | Proteintech 66005-1-Ig | -- | 1:10000 |
| Anti-long dsRNA J2 | Long double-stranded RNA | Jena Bioscience RNT-SCI-10010200 | 1:1000 | -- |
| Anti-alpha-tubulin 12G10 | Tubulin loading control | DSHB, U of Iowa | -- | 1:10000 |
| Anti-Rpb3 | RNAPII subunit Rpb3 | Previously described | 1:1000 | 1:10000 |
| Anti-Smt3 | SUMO protein | Gift, previously described | -- | 1:10000 |

## Experiment 1: Ema2 Expression and Localization (Fig 1)

### EMA2 mRNA Expression Profile (Fig 1A)

| Growth/Stage Condition | EMA2 mRNA Expression |
|-----------------------|---------------------|
| Growing cells (low density) | Undetectable |
| Growing cells (medium density) | Undetectable |
| Growing cells (high density) | Undetectable |
| Starved cells (0-24 hr) | Undetectable |
| Conjugation 0 hpm | Begins to appear |
| Conjugation 3-6 hpm | High expression |
| Conjugation 8-12 hpm | Present |
| Conjugation/post-conjugation 14-18 hpm | Declining |

- Data source: microarray expression data from Miao et al., 2009

### Ema2-HA Protein Localization (Fig 1B)

| Time Point | Ema2-HA Location | Notes |
|------------|-----------------|-------|
| Vegetative (Vg) | Not detectable | No expression in growing cells |
| 3 hpm | Parental MAC | First appearance during conjugation |
| 6 hpm | Parental MAC | Continued localization |
| 8 hpm | New MAC (appeared), parental MAC (disappeared) | Localization switch coincides with new MAC development |
| 12 hpm | New MAC (fading) | Signal diminishing |
| 14 hpm | New MAC (fading) | Signal further reduced |

- Localization switch from parental to new MAC is reminiscent of Twi1 (Piwi protein) and PRC2

## Experiment 2: DNA Elimination Assay (Fig 2)

### FISH with Tlr1 Probes at 36 hpm

| Genotype | Tlr1 Signal in MIC | Tlr1 Signal in New MAC | Interpretation |
|----------|-------------------|-----------------------|----------------|
| Wild-type (WT) | Detected | Not detected | DNA elimination completed |
| EMA2 somatic KO | Detected | Detected (reduced vs. TWI1 KO) | DNA elimination partially blocked |
| TWI1 KO | Detected | Detected (strong) | DNA elimination completely blocked |

### FISH Signal Intensity Comparison (Fig 2B)

| Genotype Cross | Relative Tlr1 FISH Intensity in New MAC |
|---------------|----------------------------------------|
| WT | Absent (elimination complete) |
| EMA2 KO | Present but lower than TWI1 KO |
| TWI1 KO | Strong (complete elimination block) |

### Progeny Viability

| Genotype | Viable Sexual Progeny? |
|----------|----------------------|
| WT | Yes |
| EMA2 KO | No -- consistent with DNA elimination requirement for viability |

## Experiment 3: Target-Directed scnRNA Degradation (TDSD) (Fig 3)

### scnRNA Northern Blot with Mi-9 Probe (MDS-complementary) (Fig 3A)

| Genotype | 3 hpm | 4.5 hpm | 6 hpm | Trend |
|----------|-------|---------|-------|-------|
| WT | Present | Reduced | Strongly reduced | Progressive TDSD occurring |
| EMA2 KO | Present | Persists | Persists | TDSD blocked -- MDS-complementary scnRNAs not degraded |

### scnRNA Size and Abundance (Fig 3B)

| Genotype | scnRNA (~26-31 nt) | Observation |
|----------|-------------------|-------------|
| WT | Normal biogenesis, then selective degradation of MDS-matching scnRNAs | TDSD functional |
| EMA2 KO | Normal biogenesis, but MDS-matching scnRNAs persist | TDSD defective |
| EMA2 rescue (HA-tagged) | Restored TDSD | Confirms Ema2 is the responsible factor |

### H3K27me3 Heterochromatin Mark (Fig 3C)

| Genotype | H3K27me3 in New MAC | Interpretation |
|----------|--------------------|--------------------|
| WT | Present (marks IES regions for elimination) | Normal heterochromatin formation |
| EMA2 KO | Reduced or absent | Downstream heterochromatin formation impaired |

## Experiment 4: Ema2 as a SUMO E3 Ligase (Fig 4)

### SP-RING Domain Comparison (Fig 4A)

| Organism | Protein | Domain | Conserved Residues |
|----------|---------|--------|-------------------|
| Tetrahymena | Ema2 | SP-RING | Conserved Cys and His for Zn binding (yellow highlighted) |
| S. cerevisiae | MMS21 | SP-RING | Conserved |
| S. cerevisiae | SIZ1 | SP-RING | Conserved |
| D. melanogaster | Su(var)2-10 | SP-RING | Conserved |
| H. sapiens | PIAS1 | SP-RING | Conserved |

### In Vitro Interaction Assay (Fig 4B)

| Protein Combination | Interaction with His-Ubc9? |
|--------------------|-----------------------------|
| GST alone | No |
| GST-Ema2 | Yes -- direct physical interaction with Ubc9 (SUMO E2) |

### SUMOylation Enhancement

| Condition | SUMOylation Activity |
|-----------|---------------------|
| E1 + E2 (Ubc9) alone | Basal SUMOylation |
| E1 + E2 + Ema2 | Enhanced SUMOylation (E3 ligase activity confirmed) |

## Experiment 5: Ema2-Dependent SUMOylation of Spt6 (Fig 5)

### His-Smt3 Pulldown + Mass Spectrometry (Fig 5A)

| Comparison | Method | Readout |
|------------|--------|---------|
| WT cross vs. EMA2 KO cross | Ni-NTA pulldown of His-Smt3 conjugates at 6 hpm | Label-free quantification (LFQ) intensities |
| Metric | Log2 of LFQ intensity ratio (WT/KO) for each protein | |

| Protein | Ema2-Dependent SUMOylation? | Evidence |
|---------|----------------------------|----------|
| Spt6 | Yes -- reduced SUMOylation in EMA2 KO | Higher LFQ intensity in WT vs. KO |
| Other proteins | Not detected at significant level | May be masked by Ema2-independent SUMOylation or degradation |

### Spt6 Slower-Migrating Species (Fig EV2)

| Condition | Spt6-HA Bands on Western Blot |
|-----------|-------------------------------|
| Vegetative | Single band |
| 0 hpm | Single band |
| 4.5 hpm | Slower migrating species appear |
| 6 hpm | Slower migrating species present |
| No-tag control | No signal |

- Slower migrating bands consistent with SUMOylated forms of Spt6

## Experiment 6: lncRNA Accumulation (Fig 6)

### RT-PCR Assay Design (Fig 6A, left)

| Feature | Detail |
|---------|--------|
| Primer design | Spanning MDS-IES junctions |
| Detected transcript types | lncRNAs that read through IES boundaries |
| Not detected | Processed mRNAs (which lack IES sequences) |
| Control | Genomic DNA PCR with same primers (Fig EV3) |

### RT-PCR Results at 6 hpm (Fig 6A, right)

| lncRNA Region | WT | EMA2 KO |
|---------------|-----|---------|
| MDS-IES junction products | Detected (bands present) | Not detected or strongly reduced |

### dsRNA Immunofluorescence (J2 antibody) (Fig 6)

| Genotype | dsRNA Signal in Parental MAC | Interpretation |
|----------|------------------------------|----------------|
| WT | Present (strong) | lncRNAs accumulating, forming dsRNA with complementary transcripts or scnRNAs |
| EMA2 KO | Absent or strongly reduced | lncRNA transcription or accumulation impaired |

### Genomic DNA Controls (Fig EV3)

| Genotype | Genomic PCR Products |
|----------|---------------------|
| WT | All loci present |
| EMA2 KO | All loci present (confirming loss of lncRNA is not due to genomic deletion) |

## Experiment 7: Chromatin Association of Spt6 and RNAPII (Fig 7)

### Spt6-HA Chromatin Immunofluorescence

| Cross | Spt6-HA Signal on Chromatin | Time Point |
|-------|----------------------------|------------|
| WT cross | Strong chromatin association | Mid-conjugation |
| EMA2 KO cross | Reduced chromatin association | Mid-conjugation |

### Rpb3 (RNAPII) Chromatin Immunofluorescence (Fig 7B)

| Cross | Rpb3 Signal on Chromatin | Interpretation |
|-------|--------------------------|----------------|
| WT cross | Strong association | RNAPII engaged in transcription |
| EMA2 KO cross | Majority lost from chromatin | RNAPII disengaged -- transcription impaired |

- Loss of Spt6 and RNAPII from chromatin in EMA2 KO is a temporal event during mid-conjugation
- Spt6 and RNAPII are essential in vegetative cells (Fig EV7), but Ema2 is conjugation-specific

## Experiment 8: SUMOylation-Defective Spt6 Mutant (Fig 8)

| Spt6 Variant | lncRNA Production | DNA Elimination |
|-------------|-------------------|-----------------|
| Wild-type Spt6 | Normal | Normal |
| SUMOylation-defective Spt6 mutant | Normal (not impaired) | Normal |
| EMA2 KO | Impaired | Partially blocked |

- This indicates that Spt6 SUMOylation alone is not sufficient to explain Ema2's role
- Ema2 likely has additional SUMOylation targets beyond Spt6 that are critical for lncRNA transcription

## Experiment 9: Spt6 Localization at Late Conjugation (Fig EV4)

| Cross | Spt6-HA in New MAC at 9 hpm |
|-------|----------------------------|
| WT cross | Present |
| EMA2 KO cross | Reduced |

## Key Molecular Players and Functions

| Protein | Function | Role in DNA Elimination Pathway |
|---------|----------|-------------------------------|
| Ema2 | SUMO E3 ligase (SP-RING domain) | Promotes lncRNA transcription from parental MAC |
| Ubc9 | SUMO E2 conjugating enzyme | Direct interaction partner of Ema2 |
| Smt3 | SUMO protein | Conjugated to target proteins by Ema2/Ubc9 |
| Spt6 | Transcription regulator | SUMOylated by Ema2; promotes RNAPII-chromatin association |
| Rpb3 | RNAPII subunit | Required for lncRNA transcription |
| Twi1 | Piwi protein | Loaded with scnRNAs; mediates TDSD and heterochromatin targeting |
| H3K27me3 | Histone modification | Marks IES regions for elimination in new MAC |
| H3K9me3 | Histone modification | Heterochromatin mark involved in silencing |

## Tetrahymena Genome Parameters

| Parameter | Value |
|-----------|-------|
| MIC genome size | ~200 Mb |
| MAC genome size | ~103 Mb |
| Number of IESs eliminated | ~12,000 |
| DNA eliminated | ~97 Mb (200 - 103) |
| scnRNA size | ~26-31 nt |
| Normal DNA elimination completion | ~14-18 hpm |

## Pathway Summary Table

| Step | Event | Location | Timing |
|------|-------|----------|--------|
| 1 | scnRNA biogenesis from MIC genome | MIC | Early conjugation (meiosis) |
| 2 | scnRNAs loaded onto Twi1 (Piwi) | Cytoplasm | Early conjugation |
| 3 | lncRNA transcription from parental MAC (Ema2-dependent) | Parental MAC | Mid-conjugation (~3-8 hpm) |
| 4 | scnRNAs scan parental MAC lncRNAs | Parental MAC | Mid-conjugation |
| 5 | TDSD: scnRNAs matching MAC sequences degraded | Parental MAC | Mid-conjugation (~3-6 hpm) |
| 6 | Remaining scnRNAs (IES-matching) transferred to new MAC | New MAC | ~8 hpm onward |
| 7 | IES-matching scnRNAs guide H3K27me3/H3K9me3 deposition | New MAC | ~8-14 hpm |
| 8 | Programmed DNA elimination of IESs | New MAC | ~14-18 hpm |

## Genetic Constructs

| Construct | Purpose | Selection |
|-----------|---------|-----------|
| pEMA2-HA-neo3 | C-terminal HA tagging of Ema2 at endogenous locus | 100 ug/mL paromomycin + 1 ug/mL CdCl2 |
| His-SMT3 | His-tagged SUMO for pulldown experiments | -- |
| HA-SMT3 | HA-tagged SUMO for rescue experiments | -- |
| Spt6-HA | HA-tagged Spt6 for localization and interaction studies | -- |

## SMT3 Rescue Experiment (Fig EV1)

| Construct Introduced | SMT3 KO Progeny Survival |
|---------------------|-------------------------|
| His-SMT3 | Viable progeny obtained |
| HA-SMT3 | Viable progeny obtained |
| Empty vector (no SMT3) | No viable progeny |

- Confirms that tagged Smt3 variants retain essential SUMO function

## Reference Count

- Total references cited: 71
