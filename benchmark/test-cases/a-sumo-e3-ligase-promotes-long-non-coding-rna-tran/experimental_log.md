# Experimental Log -- Ema2 / lncRNA / DNA elimination

## 2024-01-15 -- Progeny viability in Ema2 knockout

Crossed WT and Ema2-KO strains; scored sexual progeny viability.

| Genotype | Pairs scored | Viable progeny (%) | DNA elimination complete |
|----------|-------------|-------------------|------------------------|
| WT x WT | 150 | ~95 | Yes |
| Ema2-KO x Ema2-KO | 150 | ~5 | No |
| Ema2-rescue x Ema2-rescue | 100 | ~90 | Yes |

Ema2 is clearly essential for completing DNA elimination and producing viable progeny.

## 2024-02-03 -- lncRNA accumulation (somatic genome)

RT-qPCR for somatic-origin lncRNAs during conjugation (normalized to rRNA).

| Time post-mixing (h) | WT lncRNA level (fold) | Ema2-KO lncRNA level (fold) |
|----------------------|----------------------|---------------------------|
| 0 | 1.0 | 1.0 |
| 3 | 4.5 | 1.2 |
| 6 | 12.3 | 1.8 |
| 9 | 18.7 | 2.1 |
| 12 | 15.2 | 1.9 |

Somatic lncRNA accumulation is severely reduced in Ema2-KO -- roughly 6-10x lower at peak.

## 2024-02-20 -- TDSD assay (scnRNA northern blots)

Measured remaining scnRNA levels post-TDSD at 8 h conjugation.

| Condition | scnRNA remaining (% of input) | TDSD efficiency |
|-----------|------------------------------|----------------|
| WT | ~25 | Normal |
| Ema2-KO | ~85 | Severely impaired |

Without lncRNAs, scnRNAs are not degraded -- TDSD fails.

## 2024-03-10 -- Ema2-Ubc9 interaction (co-IP)

| Bait | Prey detected | Signal (relative) |
|------|--------------|-------------------|
| FLAG-Ema2 | HA-Ubc9 | +++ |
| FLAG-Ema2-RING-mut | HA-Ubc9 | - |
| FLAG alone | HA-Ubc9 | - |

Interaction is RING-domain dependent, consistent with E3 ligase function.

## 2024-03-28 -- Spt6 SUMOylation levels

In vivo SUMOylation assay, anti-SUMO western blot on immunoprecipitated Spt6.

| Condition | Spt6-SUMO band intensity (AU) |
|-----------|------------------------------|
| WT | 1.00 |
| Ema2-KO | 0.15 |
| Ema2-rescue | 0.88 |

Ema2 is required for the majority of Spt6 SUMOylation.

## 2024-04-15 -- ChIP: Spt6 and RNA Pol II on chromatin

ChIP-qPCR at somatic lncRNA-producing loci during conjugation (8 h).

| Factor | WT enrichment (fold over IgG) | Ema2-KO enrichment (fold over IgG) |
|--------|------------------------------|-----------------------------------|
| Spt6 | 8.5 | 2.1 |
| RNA Pol II (Rpb1) | 11.3 | 3.4 |

Both Spt6 and Pol II chromatin association are reduced ~3-4x in Ema2-KO at these loci.

## Summary model

Ema2 (E3) + Ubc9 (E2) --> SUMOylation of Spt6 --> Spt6 + Pol II load onto chromatin --> lncRNA transcription --> scnRNA:lncRNA pairing --> TDSD --> DNA elimination
