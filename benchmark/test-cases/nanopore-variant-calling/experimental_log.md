# Experimental Log: Nanopore Bacterial Variant Calling Benchmark

## Variant Callers Under Test

| Caller | Version | Type | Category |
|--------|---------|------|----------|
| Clair3 | v1.0.5 | SNP + indel | Deep learning |
| DeepVariant | v1.6.0 | SNP + indel | Deep learning |
| Medaka | v1.11.3 | SNP + indel | Deep learning (own alignment via minimap2) |
| NanoCaller | v3.4.1 | SNP + indel | Deep learning |
| BCFtools | v1.19 | SNP + indel | Traditional (pileup-based) |
| FreeBayes | v1.3.7 | SNP + indel | Traditional (haplotype-based) |
| Longshot | v0.4.5 | SNP only | Traditional (haplotype-aware) |

## Illumina Baseline
- Caller: Snippy
- Used as the reference standard for ONT comparison

## Bacterial Species (14 total)

| Species | GC Content Range | Genome Size Range |
|---------|-----------------|-------------------|
| Campylobacter jejuni | ~30% | ~1.6 Mbp |
| Campylobacter lari | ~30% | ~1.5 Mbp |
| Escherichia coli | ~50% | ~5.0 Mbp |
| Klebsiella pneumoniae | ~57% | ~5.5 Mbp |
| Klebsiella variicola | ~57% | ~5.5 Mbp |
| Listeria ivanovii | ~37% | ~2.9 Mbp |
| Listeria monocytogenes | ~38% | ~2.9 Mbp |
| Listeria welshimeri | ~36% | ~2.8 Mbp |
| Mycobacterium tuberculosis | ~66% | ~4.4 Mbp |
| Salmonella enterica | ~52% | ~4.8 Mbp |
| Staphylococcus aureus | ~33% | ~2.8 Mbp |
| Streptococcus dysgalactiae | ~39% | ~2.1 Mbp |
| Streptococcus pyogenes | ~39% | ~1.8 Mbp |
| Vibrio parahaemolyticus | ~45% | ~5.2 Mbp |

- GC content spans 30-66% across species
- ANI between sample pairs targeted at ~99.5% for truthset generation
- Truthset variant counts ranged from 2,102 SNPs (M. tuberculosis) to 57,887 SNPs (V. parahaemolyticus)
- Insertions per sample: 57-280
- Deletions per sample: 63-304

## ONT Basecalling Models and Read Types

### Read quality (median read identity)

| Basecalling Model | Read Type | Median Identity | Quality Score |
|-------------------|-----------|-----------------|---------------|
| sup | Duplex | 99.93% | Q32 |
| hac | Duplex | 99.79% | Q27 |
| sup | Simplex | 99.26% | Q21 |
| hac | Simplex | 98.31% | Q18 |
| fast | Simplex | 94.09% | Q12 |

- Basecalling performed with Dorado
- Duplex reads available only for hac and sup models

---

## Results: SNP F1 Scores (median across 14 species)

### Sup basecalling model

| Caller | Simplex F1 | Duplex F1 |
|--------|-----------|-----------|
| Clair3 | 99.99% | ~99.99% |
| DeepVariant | 99.99% | ~99.99% |
| Medaka | High (DL tier) | High (DL tier) |
| NanoCaller | High (DL tier) | High (DL tier) |
| BCFtools | Matches Illumina | Matches Illumina |
| FreeBayes | Matches Illumina | Matches Illumina |
| Longshot | Matches Illumina | Matches Illumina |
| **Illumina (Snippy)** | **99.45%** | -- |

### Hac basecalling model
- Deep learning callers (Clair3, DeepVariant): match or surpass Illumina for SNPs
- Traditional callers (BCFtools, FreeBayes, Longshot): match or slightly exceed Illumina for SNPs

### Fast basecalling model
- All ONT variant callers have lower F1 than Illumina
- Best case: SNP parity with Illumina only for the top-performing caller
- Order of magnitude worse than hac/sup for deep learning callers

---

## Results: Indel F1 Scores (median across 14 species)

### Sup basecalling model

| Caller | Simplex F1 | Duplex F1 |
|--------|-----------|-----------|
| Clair3 | 99.53% | 99.20% |
| DeepVariant | 99.61% | 99.22% |
| FreeBayes | Matches Illumina | -- |
| BCFtools | Reduced accuracy | Reduced accuracy |
| **Illumina (Snippy)** | **95.76%** | -- |

### Key indel findings
- Deep learning callers substantially outperform Illumina for indels
- BCFtools shows reduced indel accuracy across all models and read types
- FreeBayes matches Illumina indel performance but does not exceed it
- Longshot does not call indels (SNP-only tool)

---

## Results: Depth Subsampling Analysis

### At 10x ONT sup simplex depth
- Clair3 and DeepVariant achieved F1 scores consistent with or better than full-depth Illumina for both SNPs and indels

### At 5x depth
- Duplex sup: SNP precision remained above Illumina for all methods except NanoCaller
- F1 scores generally lower than Illumina at this depth
- BCFtools surprisingly produced SNP F1 on par with Illumina on duplex sup reads at 5x

### Recommended minimum depth
- 25x for clinical and public health applications
- 10x sufficient to match Illumina accuracy with Clair3/DeepVariant on sup data

---

## Results: Error Mode Analysis

### Variant-dense regions (Illumina weakness)
- Illumina showed bimodal distribution of false negatives
- Second peak at 20 variants per 100 bp window
- Illumina errors driven by short-read alignment failures in variant-dense regions
- Clair3 showed no bimodal distribution and few missed or false calls at this density

### Impact of masking repetitive regions on F1
- Illumina: F1 increased from 99.3% to 99.7% (+0.4%) when repetitive regions masked
- Clair3 (100x simplex sup): F1 increased by only +0.003% when masking repetitive regions
- Demonstrates ONT long reads are minimally affected by repetitive region complexity

### Homopolymer error analysis

#### Clair3 false positive indels (sup model)
- Total: 8 false positive indels
- 5 were homopolymer-related errors
- 3 were within 1-2 bases of a similar insertion

#### Clair3 (fast model)
- Frequently miscalculated homopolymer lengths by 1-2 bp
- Equal number of non-homopolymeric false indel calls

#### DeepVariant (sup model)
- 8 out of 11 false positive indels were homopolymer-related

---

## Results: Runtime and Computational Resources

### Runtime (seconds per megabase, at 100x depth)

| Caller | Median s/Mbp | Estimated Time (4 Mbp genome) |
|--------|-------------|-------------------------------|
| Clair3 | 0.86 | <6 min |
| DeepVariant | 5.7 | ~38 min |
| FreeBayes | Variable (max 597) | Up to 2.75 days |
| Basecalling (GPU, sup) | 0.77 | ~5 min |

### Memory usage

| Caller | Median RAM |
|--------|-----------|
| Clair3 | 1.6 GB |
| DeepVariant | 8 GB |
| All methods | <8 GB (laptop compatible) |

### Key runtime findings
- Clair3 is the most practical for clinical deployment: best accuracy + fastest runtime + lowest memory
- FreeBayes has highly variable runtime, with worst case reaching 2.75 days for a single 4 Mbp genome
- All callers run within laptop-level memory constraints (<8 GB)
- GPU basecalling (sup model) adds only ~5 min for a typical 4 Mbp bacterial genome at 100x

---

## Summary: Overall Caller Rankings

### SNP calling (sup simplex, full depth)
1. Clair3 (F1 99.99%)
2. DeepVariant (F1 99.99%)
3. Medaka / NanoCaller (high DL tier)
4. BCFtools / FreeBayes / Longshot (~Illumina level, 99.45%)
5. Illumina baseline (99.45%)

### Indel calling (sup simplex, full depth)
1. DeepVariant (F1 99.61%)
2. Clair3 (F1 99.53%)
3. FreeBayes (~Illumina level)
4. Illumina baseline (95.76%)
5. BCFtools (reduced accuracy)

### Best overall recommendation
- Clair3 with sup simplex reads: best balance of accuracy, speed, and resources
- Minimum acceptable: hac basecalling model (fast model is below Illumina)
- Minimum recommended depth: 25x for clinical use, 10x sufficient for surveillance

---

## Reproducibility
- Code available at: github.com/mbhall88/NanoVarBench
- All raw sequencing data deposited in public repositories

## Ground Truth Reference
- bioRxiv DOI: 10.1101/2024.03.15.585313
- Published: eLife, DOI 10.7554/eLife.98300
