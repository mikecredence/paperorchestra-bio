# Experimental Log -- Benchmarking Variant Callers on Bacterial ONT Data

## 2024-01-15 -- Experimental design

| Parameter | Value |
|---|---|
| Bacterial species | 14 (diverse) |
| Sequencing platforms | ONT (high-accuracy chemistry), Illumina |
| Gold standard | Reference genomes with projected strain variations |
| Variant types | SNPs and indels |

## 2024-02-01 -- Variant caller inventory

| Caller | Type | Platform support |
|---|---|---|
| Clair3 | Deep learning | ONT |
| DeepVariant | Deep learning | ONT, Illumina |
| Medaka | Deep learning / neural network | ONT |
| FreeBayes | Traditional (Bayesian) | ONT, Illumina |
| bcftools mpileup | Traditional (pileup) | ONT, Illumina |
| GATK HaplotypeCaller | Traditional (assembly-based) | Illumina |

## 2024-03-01 -- SNP calling accuracy (across 14 species)

| Caller | Platform | Mean Precision | Mean Recall | Mean F1 |
|---|---|---|---|---|
| Clair3 | ONT | >0.99 | >0.99 | >0.99 |
| DeepVariant | ONT | >0.98 | >0.98 | >0.98 |
| Medaka | ONT | >0.97 | >0.96 | >0.96 |
| GATK | Illumina | >0.98 | >0.97 | >0.97 |
| FreeBayes | Illumina | >0.97 | >0.96 | >0.96 |
| bcftools | ONT | >0.95 | >0.93 | >0.94 |

Clair3 on ONT provides the most accurate SNP calls overall, surpassing Illumina-based methods.

## 2024-03-15 -- Indel calling accuracy (across 14 species)

| Caller | Platform | Mean Precision | Mean Recall | Mean F1 |
|---|---|---|---|---|
| Clair3 | ONT | >0.97 | >0.96 | >0.96 |
| DeepVariant | ONT | >0.95 | >0.94 | >0.94 |
| Medaka | ONT | >0.93 | >0.91 | >0.92 |
| GATK | Illumina | >0.94 | >0.93 | >0.93 |
| FreeBayes | Illumina | >0.92 | >0.90 | >0.91 |

Deep-learning ONT callers outperform Illumina-based callers even for indels.

## 2024-04-01 -- Homopolymer analysis

| Chemistry | Homopolymer indel error rate | Notes |
|---|---|---|
| ONT (old chemistry, R9) | Elevated | Known limitation |
| ONT (high-accuracy, R10/SUP) | Absent / negligible | Major improvement |
| Illumina | Low (but short-read limitations) | Structural/repeat issues remain |

High-accuracy ONT chemistry eliminates the traditional homopolymer-induced indel problem.

## 2024-04-05 -- Error analysis (false and missed calls)

| Error source | ONT (deep learning) | Illumina |
|---|---|---|
| Homopolymer regions | Minimal | Low |
| Repetitive regions | Low | Moderate (short-read mapping ambiguity) |
| Low-complexity regions | Low | Moderate |
| Structural variant boundaries | Moderate | Moderate-High |

Short-read limitations (mapping ambiguity in repeats) are a larger source of error than ONT-specific issues with modern chemistry.

## Summary

Clair3 on ONT high-accuracy data provides the best variant calling accuracy for bacteria across 14 species, outperforming both traditional ONT methods and Illumina. Homopolymer errors are no longer an issue with modern ONT chemistry.
