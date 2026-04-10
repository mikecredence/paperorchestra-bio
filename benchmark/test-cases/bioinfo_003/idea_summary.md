## Working title

Long-read sequencing and genome assembly from natural history museum collection samples

## Core question

Can natural history museum collections, with ethanol-preserved specimens containing partially degraded DNA, be used for high-quality long-read genome assembly?

## Motivation / gap

- Museum collections harbor millions of preserved biological samples, largely untapped for long-read sequencing
- Ethanol-preserved specimens retain kilobase-sized DNA fragments but have been considered unsuitable for long-read technologies
- Existing amplification-based protocols hit a genome size ceiling around 500 Mb due to PCR bias
- Tiny and difficult-to-sequence organisms (millimeter-scale arthropods, molluscs) need accessible genome assembly protocols

## Core contribution

- Demonstrate that amplification-free long-read protocols can yield contiguous genome assemblies from ethanol-preserved museum samples
- Develop a modified amplification-based protocol using an alternative polymerase to overcome PCR bias, assembling the 3.1 Gb maned sloth genome (surpassing the previous 500 Mb limit)
- Show the protocol also improves assemblies for difficult-to-sequence molluscs and arthropods, including millimeter-sized organisms
- Highlight museum collections as valuable, underutilized resources for reference genome efforts

## Method in brief

- Source ethanol-preserved specimens from museum collections
- Extract high-molecular-weight DNA; assess fragment size distributions
- Amplification-free library prep for specimens with sufficient DNA quantity
- Modified amplification protocol with alternative polymerase for low-input or large-genome samples
- Oxford Nanopore and/or PacBio long-read sequencing
- Genome assembly (Flye, Hifiasm, or similar) and quality assessment (BUSCO, contig N50)

## Target venue

Genome Biology
