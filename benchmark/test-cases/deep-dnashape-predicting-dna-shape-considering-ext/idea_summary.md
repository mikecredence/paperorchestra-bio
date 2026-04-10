## Working title

Deep DNAshape: A deep learning method for high-throughput prediction of DNA shape features with extended flanking region effects

## Core question

Can a deep learning model accurately predict 3D DNA shape features while accounting for the influence of extended flanking regions, replacing the limitations of current k-mer based approaches?

## Motivation / gap

- Current k-mer based methods for DNA shape prediction ignore the influence of extended flanking regions on shape in a target region
- Molecular simulations and structural biology experiments are too slow for high-throughput shape prediction
- The quantitative impact of distant flanking sequences on DNA shape readout mechanisms is not well characterized
- No existing tool can predict refined DNA shape features for arbitrary-length sequences at scale

## Core contribution

- Deep DNAshape: a deep learning method that predicts DNA shape features accounting for extended flanking regions
- Fundamentally changes k-mer based high-throughput DNA shape prediction paradigm
- Enables refined shape prediction for any length and number of DNA sequences in a high-throughput manner
- Reveals that DNA shape readout mechanisms of a core target are quantitatively affected by flanking regions, including distant positions

## Method in brief

- Train a deep learning model on DNA shape features (minor groove width, roll, propeller twist, helix twist) derived from structural data
- Input: DNA sequence of arbitrary length; output: per-position shape feature predictions incorporating extended flanking context
- Compare predictions against existing k-mer methods (DNAshapeR) and experimental/simulation data
- Demonstrate influence of flanking regions on shape in target regions

## Target venue

Nature Communications
