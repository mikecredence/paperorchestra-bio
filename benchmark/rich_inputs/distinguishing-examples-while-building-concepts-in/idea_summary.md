# Idea Summary: Distinguishing examples while building concepts in hippocampal and artificial networks

## Working title
Distinguishing examples while building concepts in hippocampal and artificial networks

## Core question
AbstractThe hippocampal subfield CA3 is thought to function as an autoassociative network that stores experiences as memories. Information from these experiences arrives via the entorhinal cortex (EC), which projects to CA3 directly as well as indirectly through the dentate gyrus (DG). DG sparsifies and decorrelates the information before also projecting to CA3. The computational purpose for receiving two encodings of the same sensory information has not been firmly established. We model CA3 as 

## Motivation / gap
- IntroductionThe hippocampus is believed to underlie our ability to form episodic memories, through which we can recount personally experienced events from our daily lives (Scoville and Milner, 1957).
- In particular, the subfield CA3 is thought to provide this capability as an autoassociative network (McNaughton and Morris, 1987; O’Reilly and Rudy, 2001; Rolls and Kesner, 2006).
- Its pyramidal cells contain abundant recurrent connections exhibiting spike-timing-dependent plasticity (Bi and Poo, 1998; Mishra et al., 2016).
- These features allow networks to perform pattern completion and recover stored patterns of neural activity from noisy cues.
- Sensory information to be stored as memories arrives to CA3 via the entorhinal cortex (EC), which serves as the major gateway between hippocampus and neocortex (Fig.

## Core contribution (bullet form)
Extracted from abstract:
AbstractThe hippocampal subfield CA3 is thought to function as an autoassociative network that stores experiences as memories. Information from these experiences arrives via the entorhinal cortex (EC), which projects to CA3 directly as well as indirectly through the dentate gyrus (DG). DG sparsifies and decorrelates the information before also projecting to CA3. The computational purpose for receiving two encodings of the same sensory information has not been firmly established. We model CA3 as a Hopfield-like network that stores both correlated and decorrelated encodings and retrieves them at low and high inhibitory tone, respectively. As more memories are stored, the dense, correlated encodings merge along shared features while the sparse, decorrelated encodings remain distinct. In this way, the model learns to transition between concept and example representations by controlling inhibitory tone. To experimentally test for the presence of these complementary encodings, we analyze the theta-modulated tuning of place cells in rat CA3. In accordance with our model’s prediction, these neurons exhibit more precise spatial tuning and encode more detailed task features during theta phases with sparser activity. Finally, we generalize the model beyond hippocampal architecture and find that feedforward neural networks trained in multitask learning benefit from a novel loss term that promotes hybrid encoding using correlated and decorrelated representations. Thus, the complementary encodings that we have found in CA3 can provide broad computational advantages for solving complex tasks.

## Method in brief
MethodsTransformation of memories along hippocampal pathwaysBinary autoencoder from images to ECOur memories are 256 images from each of the sneaker, trouser, and coat classes in the FashionMNIST dataset (Xiao et al., 2017). We train a fully connected linear autoencoder on these images with three hidden layers of sizes 128, 1024, and 128. Batch normalization is applied to each hidden layer, followed by a rectified linear unit (ReLU) nonlinearity for the first and third hidden layers and a sigmoid nonlinearity for the output layer. Activations in the middle hidden layer are binarized by a Heaviside step function with gradients backpropagated by the straight-through estimator (Bengio et al., 2013). The loss function is



where iμν is the image with pixel values between 0 and 1,  is its reconstruction,  represents the binary activations of the middle hidden layer with NEC = 1024 units indexed by i, and aEC = 0.1 is its desired density (Fig. 2C). Sparsification with strength λ = 10 is achieved by computing the Kullback-Leibler (KL) divergence between the hidden layer density and aEC (Le et al., 2011). Training is performed over 150 epochs with batch size 64 using the Adam optimizer with learning rate 10−3 and weight decay 10−5.Binary feedforward networks from EC to CA3To propagate patterns from EC to DG, from DG to MF inputs, and from EC to PP inputs, we compute



where  and  are presynaptic and postsynaptic patterns, Wij is the connectivity matrix, and θ is a threshold. Each p

## Target venue
Nature Communications
