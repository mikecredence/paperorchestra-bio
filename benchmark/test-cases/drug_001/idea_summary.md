## Working title

SE(3)-equivariant ternary complex prediction towards target protein degradation (DeepTernary)

## Core question

Can a deep learning model with SE(3)-equivariant architecture accurately and rapidly predict three-dimensional structures of PROTAC- and molecular glue-induced ternary complexes for targeted protein degradation?

## Motivation / gap

- Targeted protein degradation (TPD) via PROTACs and molecular glues requires formation of a ternary complex between an E3 ligase, a degrader molecule, and a target protein
- Predicting ternary complex structures is critical for rational degrader design but remains extremely challenging
- Existing methods (RosettaDock, FRODock, BOTCP, PRosettaC, AlphaFold3) are either slow, inaccurate, or both
- No existing approach jointly captures the SE(3)-equivariant nature of molecular interactions in ternary complexes with an end-to-end learned framework
- A large curated training dataset for ternary complex structures was previously unavailable

## Core contribution

- Present DeepTernary, an end-to-end SE(3)-equivariant deep learning model using a GNN encoder with intra-graph and ternary inter-graph attention
- Introduce a query-based Pocket Points Decoder that extracts 3D binding structures from learned ternary embeddings
- Curate TernaryDB, a large-scale ternary complex dataset from PDB for training
- Achieve DockQ scores of 0.65 (PROTAC) and 0.23 (molecular glue) with inference in 1-7 seconds per complex
- Demonstrate that buried surface area from predicted structures correlates with experimental degradation potency

## Method in brief

DeepTernary employs an SE(3)-equivariant graph neural network with intra-graph and ternary inter-graph attention mechanisms. Given binary structures of E3 ligase-degrader and target-degrader pairs, the model predicts the ternary complex configuration. A novel query-based Pocket Points Decoder extracts the final 3D structure from learned embeddings. The model is trained on TernaryDB, a curated dataset from PDB with known PROTAC/molecular glue complexes excluded from training. Evaluation uses DockQ scores and RMSD.

## Target venue

Nature Communications
