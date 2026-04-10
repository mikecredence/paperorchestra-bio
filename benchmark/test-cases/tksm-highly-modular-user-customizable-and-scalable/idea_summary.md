## Working title

TKSM: Highly Modular, User-Customizable, and Scalable Transcriptomic Sequencing Long-Read Simulator

## Core question

Can we build a long-read transcriptomic sequencing simulator that is truly modular -- where each RNA processing and library preparation step is an independent, composable software module -- to enable flexible benchmarking of LR analysis tools?

## Motivation / gap

- Long-read transcriptomic sequencing is increasingly used for isoform detection, gene fusion analysis, and other RNA tasks
- Existing LR simulators mimic sequencing noise and target specific library protocols but lack modularity
- Key library preparation steps like PCR amplification are missing from current simulators
- Adapting existing tools to new or changing protocols (e.g., single-cell LR) is difficult
- Lack of abundant gold-standard datasets hinders rigorous benchmarking of LR analysis tools

## Core contribution

- TKSM: a modular, scalable long-read simulator where each RNA modification step is an independent software module
- Users can assemble custom simulation pipelines from any combination of TKSM modules
- Explicit modeling of library preparation steps including PCR
- Supports new and changing library protocols (e.g., single-cell long reads)
- Enables creation of gold-standard datasets for benchmarking transcriptomic tools

## Method in brief

Software engineering approach: each step in the RNA-to-reads pipeline (transcription, fragmentation, PCR, adapter ligation, sequencing error) implemented as a standalone module with defined input/output interfaces. Modules are composable via a pipeline configuration. Validation against real long-read datasets (ONT, PacBio). Benchmarking downstream tools (isoform detection, fusion detection) on TKSM-simulated data vs. real data.

## Target venue

Bioinformatics
