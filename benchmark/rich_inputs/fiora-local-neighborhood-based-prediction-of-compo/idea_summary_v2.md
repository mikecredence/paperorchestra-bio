## Working title

Fiora: Predicting tandem mass spectra via local neighborhood-aware graph neural networks modeling individual bond dissociations

## Core question

Can modeling individual bond dissociation events and their local molecular neighborhood with graph neural networks substantially improve the accuracy of in silico tandem mass spectra prediction compared to existing fragmentation algorithms?

## Motivation / gap

- Non-targeted metabolomics is limited by incomplete spectral reference libraries; the vast majority of MS/MS spectra from experiments remain unannotated ("dark matter")
- In silico methods for compound identification achieved only ~34% recall in the 2016 CASMI challenge and below 30% in the 2022 CASMI challenge
- Existing fragmentation algorithms either use combinatorial bond-breaking (CFM-ID) with fixed energy levels or global molecular embeddings (ICEBERG) that may miss local structural context
- No existing tool simultaneously predicts MS/MS spectra, retention time (RT), and collision cross section (CCS) from molecular structure
- Accurate spectral prediction at arbitrary collision energies and for both positive/negative ionization modes remains a challenge
- Rapid prediction speed is needed for large-scale library expansion and rescoring of putative identifications

## Core contribution (bullet form)

- Developed Fiora, an open-source GNN-based fragmentation algorithm that models fragment ions as consequences of single bond breaks, learning local molecular neighborhood via graph convolutions
- Outperforms state-of-the-art algorithms (ICEBERG and CFM-ID) in median cosine similarity on NIST 2017 test set, MS-Dial test set, and CASMI 2016/2022 challenge compounds
- Achieves high prediction quality with as few as 3-6 graph convolution layers, demonstrating that short-range structural context is sufficient for strong performance
- Predicts spectra at arbitrary continuous collision energies and for both positive and negative ionization modes in a single unified model; merging multi-CE predictions improves accuracy vs single-CE prediction
- Additionally predicts retention time and collision cross section using the same molecular graph embeddings
- Provides significant speed improvements via GPU acceleration, enabling rapid large-scale spectral library expansion

## Method in brief

Fiora represents each molecule as a graph with atoms as nodes and bonds as edges. A graph neural network (GCN or RGCN) performs multiple convolutions to aggregate local neighborhood information into hidden representations of each bond. Fragment ions are modeled as the direct consequence of removing a single edge from the molecular graph. For each bond, the model predicts abundance values for all possible fragment ions (including up to 4 hydrogen rearrangements), extending the break tendency concept introduced by Allen et al. (2015). A precursor stability parameter is also predicted. These are combined via a softmax function to compute fragment probabilities: P(f) = exp(theta_f) / (exp(sigma) + sum(exp(theta_f'))), where theta_f are fragment abundance values and sigma is precursor stability.

The fragment ion space F(G) is constructed as all subgraph pairs arising from single edge removal, combined with hydrogen loss variants (0 to 4 H losses). The MS/MS spectrum is reconstructed from exact fragment ion m/z values and predicted probabilities. Covariates including ionization mode, collision energy, instrument type, and molecular weight are incorporated at the intensity prediction level. The same molecular graph embeddings are used for auxiliary property prediction of RT and CCS via dedicated neural network submodules.

Training uses merged spectral libraries from NIST (2017) and MS-Dial with 10% validation and 10% test splits. Evaluation is performed on held-out test data as well as independent CASMI 2016 and 2022 challenge datasets. Performance is measured by cosine similarity between predicted and experimental spectra, stratified by Tanimoto structural similarity to training data, compound superclass, and peak intensity coverage.

## Target venue

Nature Communications
