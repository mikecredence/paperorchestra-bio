# Idea Summary

## Working title
Digital Telomere Measurement by Long-Read Sequencing Distinguishes Healthy Aging from Disease

## Core question
Can nanopore long-read sequencing provide high-resolution digital measurements of individual telomere lengths, and can these telomere length distributions distinguish healthy aging from telomere biology disorders (TBDs)?

## Motivation / gap
- Existing telomere measurement methods (TRF Southern blot, flow-FISH, qPCR) only provide coarse mean estimates or relative quantifications of total telomeric content
- PCR-based methods (STELA, TeSLA) preferentially amplify the shortest telomeres and are limited by polymerase processivity
- TRF systematically overestimates mean telomere length by up to several thousand base pairs
- Flow-FISH overestimates by roughly 1500 bp on average and is largely restricted to mean estimation in peripheral blood leukocytes
- No existing method captures the full distribution of individual intact telomere lengths at base-pair resolution
- The structure of the telomere length distribution (not just the mean) may carry clinically important information, but this has been inaccessible
- It is unclear whether telomere length can serve as a predictive biomarker of aging given the innate variability between individuals of similar age

## Core contribution (bullet form)
- Developed a nanopore sequencing preparation and bioinformatic pipeline (Telometer) that measures individual intact telomeres with a maximal precision of 30-40 base pairs
- Demonstrated telomere-enriched library preparation achieves several thousand-fold enrichment of telomeric reads without significantly impacting telomere length distributions
- Showed that mean/median telomere length in peripheral blood leukocytes decreases by approximately 24 bp per year in a cross-section of 14 healthy donors aged 18-77, matching prior TRF-based estimates
- Discovered that the third quartile telomere length decreases more steeply with age than the first quartile, indicating preferential loss of longer telomeres during aging
- Demonstrated pronounced accumulation of short telomeres in patients with RTEL1 mutations and other TBD genotypes, correlating with phenotypic severity
- Trained a binary classification model (machine learning) that distinguishes healthy individuals from those with TBDs, achieving high accuracy

## Method in brief
The pipeline begins with either whole-genome or telomere-enriched nanopore (ONT) sequencing library preparation. For enrichment, a custom oligonucleotide complementary to both the telomeric 3-prime overhang and the ONT sequencing adapter is used alongside restriction digestion of genomic DNA. Telomere-containing reads are identified by aligning telomeric repeats to the chromosomal termini of the T2T human genome assembly. Each telomere spans from the terminal repeat at the chromosome end to the final two consecutive repeats preceding the subtelomeric sequence.

The bioinformatic pipeline, Telometer, measures each telomere individually and can be applied generically to any human whole-genome long-read sequencing data from ONT or PacBio. Digital mean telomere length was validated against gold-standard TRF Southern blot and flow-FISH, showing high correlation. Bootstrapping analysis showed the standard error of measurement decays exponentially with additional reads, reaching 30-40 bp maximal precision. For clinical classification, a machine learning binary classifier was trained on features from the telomere length distribution to separate healthy individuals from TBD patients.

## Target venue
Nature Communications
