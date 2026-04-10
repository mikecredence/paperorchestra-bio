# Experimental Log -- Museum specimen long-read genome assembly

## 2024-01-12 -- DNA extraction quality from ethanol-preserved specimens

Fragment size distribution assessed by pulsed-field gel and Femto Pulse.

| Specimen | Collection year | Preservation | Median fragment size (kb) | Total DNA yield (ug) |
|----------|----------------|-------------|--------------------------|---------------------|
| Maned sloth (Bradypus torquatus) | 1998 | Ethanol | 12.5 | 8.2 |
| Land snail (Cornu aspersum) | 2005 | Ethanol | 8.3 | 2.1 |
| Millipede (Glomeris marginata) | 2010 | Ethanol | 15.2 | 0.4 |
| Beetle (Carabus sp.) | 2002 | Ethanol | 10.8 | 1.5 |
| Springtail (Folsomia candida) | 2015 | Ethanol | 18.0 | 0.15 |

Museum samples retain kilobase-sized DNA suitable for long-read sequencing.

## 2024-02-05 -- Amplification-free vs amplified assembly comparison (land snail)

| Protocol | Contig N50 (Mb) | Total assembly (Gb) | BUSCO complete (%) | Misassemblies |
|----------|----------------|--------------------|--------------------|--------------|
| Amplification-free (ONT) | 2.8 | 3.2 | 91.5 | 12 |
| Standard PCR amplification | 0.4 | 2.8 | 78.2 | 45 |
| Modified polymerase amplification | 2.1 | 3.1 | 89.8 | 18 |

Amplification-free yields the most contiguous assembly; modified polymerase is a strong alternative for low-input samples.

## 2024-02-28 -- Maned sloth genome assembly (modified amplification protocol)

| Metric | Value |
|--------|-------|
| Genome size (assembled) | 3.1 Gb |
| Contig N50 | 5.2 Mb |
| Scaffold N50 | 18.4 Mb |
| BUSCO completeness (mammalia_odb10) | 93.2% |
| Coverage | 35x |
| Previous protocol size limit | 500 Mb |

Successfully assembled a 3.1 Gb genome, breaking the previous 500 Mb ceiling for amplification-based museum protocols.

## 2024-03-18 -- Tiny organism assemblies (millimeter-scale)

| Organism | Body size (mm) | Genome size (Mb) | Protocol | Contig N50 (Mb) | BUSCO (%) |
|----------|---------------|------------------|----------|----------------|----------|
| Springtail | ~1.5 | 220 | Amp-free | 1.8 | 94.1 |
| Mite (Acarus siro) | ~0.5 | 85 | Modified amp | 0.9 | 88.5 |
| Beetle larva | ~3.0 | 350 | Modified amp | 2.5 | 91.3 |
| Millipede | ~15.0 | 180 | Amp-free | 3.2 | 95.0 |

The protocol works for millimeter-scale organisms that are extremely difficult to sequence with standard approaches.

## 2024-04-05 -- Protocol comparison: PCR bias assessment

GC-coverage deviation (lower is better) across assembly windows.

| Protocol | Mean GC deviation (%) | Coverage CV | Dropout regions |
|----------|-----------------------|------------|----------------|
| Standard PCR | 8.5 | 0.42 | 128 |
| Modified polymerase | 2.1 | 0.18 | 15 |
| Amplification-free | 1.2 | 0.12 | 5 |

The alternative polymerase dramatically reduces GC bias compared to standard PCR, approaching amplification-free quality.
