# Idea Summary

## Working title
Distinguishing examples while building concepts in hippocampal and artificial networks

## Core question
How can CA3, which receives both sparse/decorrelated mossy fiber (MF) inputs from the dentate gyrus and dense/correlated perforant path (PP) inputs from the entorhinal cortex, use these complementary encodings to simultaneously maintain distinct episodic memories and build generalizable concept representations?

## Motivation / gap
- CA3 receives two different encodings of the same sensory information (via MF and PP), but the computational purpose for this dual-pathway architecture has not been firmly established
- DG is known to sparsify and decorrelate EC patterns, but how this interacts with the denser PP pathway within the CA3 autoassociative network is poorly understood
- The hippocampus is implicated in both episodic memory (specific experiences) and concept/category learning, yet the circuit-level mechanism enabling both functions is unclear
- Theta oscillations modulate hippocampal activity and have been linked to phase-specific coding properties, but how they relate to switching between example-specific and concept-level representations has not been tested
- Artificial neural networks performing multitask learning lack principled approaches for balancing example discrimination and concept classification

## Core contribution (bullet form)
- Developed a Hopfield-like model of CA3 that stores both sparse/decorrelated MF and dense/correlated PP encodings and retrieves them at high and low inhibitory tone, respectively
- Showed that as memory load increases, dense PP encodings merge along shared features (forming concepts) while sparse MF encodings remain distinct (preserving examples)
- Demonstrated that the model can alternate between example and concept representations via an oscillating threshold mimicking theta rhythm
- Analyzed theta-modulated place cell tuning in rat CA3 and found that sparser theta phases encode finer spatial positions and more detailed task features (e.g., turn direction in a W-maze)
- Generalized the framework to feedforward neural networks, introducing a novel loss term promoting hybrid correlated/decorrelated encoding that improves multitask learning performance on combined digit classification and set identification tasks

## Method in brief
The model begins by encoding FashionMNIST images (sneakers, trousers, coats; 256 examples per concept) through a binary autoencoder into sparse EC representations (NEC = 1024 neurons, 10% density). From EC, two pathways generate CA3 inputs: the PP pathway uses random binary connectivity yielding dense, correlated patterns (aPP = 0.2, correlation ~0.09), while the MF pathway routes through DG (NDG = 8192, aDG = 0.005) to produce very sparse, decorrelated patterns (aMF = 0.02, correlation ~0.01). CA3 (NCA3 = 2048) stores linear combinations of these encodings in a Hopfield-like network, with MF inputs weighted more heavily. A winners-take-all approach converts postsynaptic inputs to binary activity at a specified density.

Retrieval operates by initializing the network to a corrupted stored pattern and running asynchronous updates under either high inhibitory threshold (retrieving sparse MF-like examples) or low threshold (retrieving dense PP-like concepts). An oscillating threshold simulates the theta cycle, causing the network to alternate between example and concept regimes. Pattern completion success is measured by overlap with stored patterns.

For the neural data analysis, publicly available CA3 place cell recordings from rats on linear tracks and W-mazes were partitioned into theta phase bins. Spatial information per spike was computed at each phase, and population sparsity was measured to test the prediction that sparser phases carry more precise spatial tuning. For the machine learning extension, a multilayer perceptron was trained on an augmented MNIST task requiring both digit classification and set identification, with a novel correlation-based loss term encouraging the hidden layer to maintain both correlated and decorrelated representations.

## Target venue
Nature Communications
