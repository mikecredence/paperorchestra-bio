## Working title

A direct cortico-cortical feedforward inhibitory pathway from somatosensory barrel cortex to primary visual cortex mediates tacto-visual integration in the mouse proximity space

## Core question

Do mouse primary somatosensory (SSp-bfd, barrel cortex) and primary visual (VISp) cortices directly interact to support multisensory integration of whisker touch and vision in the shared peripersonal space, and if so, what is the circuit mechanism?

## Motivation / gap

- Multisensory integration was traditionally thought to occur mainly in higher-order association areas, not primary sensory cortices
- Behavioral evidence shows that rodents combine whisker touch and vision for object detection and prey capture, with performance dramatically increasing when both modalities work together
- The 3D spatial relationship between the mouse whisker search space and the visual field covered by VISp was unknown
- While audio-visual cross-modal effects in primary visual cortex had been demonstrated, it was unclear whether tactile input from whiskers could modulate VISp activity
- The specific circuit mechanism (which layers, cell types, and projection patterns) underlying any such tacto-visual interaction in primary cortex was uncharacterized

## Core contribution (bullet form)

- Built a morphologically accurate 3D model of the mouse whisker array via stereo photogrammetry and showed that whisker tips substantially overlap with the visual space covered by VISp, with the overlap fraction increasing from retraction (~lower) to protraction (~higher, p < 0.01 for comparisons)
- Demonstrated that contralateral whisker stimulation suppresses visually evoked activity specifically in a subarea of VISp whose visual space covers the whisker search space (bimodal v+w responses significantly reduced vs. unimodal v-only)
- Identified that cortico-cortical projection neurons from SSp-bfd to VISp originate predominantly from layer 6 of the caudal barrel columns (representing the long caudal whiskers), with postsynaptic targets mainly in layer 2/3 of VISp
- Showed that the cross-modal suppression operates through fast-spiking (FS) interneuron-mediated feedforward inhibition: FS cells receive direct SSp-bfd input and inhibit L2/3 excitatory neurons in VISp
- Developed a recurrent neural network model (coupled VISp and SSp-bfd populations) identifying a gain-dependent inhibition-stabilized network (ISN) regime that explains the suppressive cross-modal effect

## Method in brief

The study combined multiple experimental approaches. Stereo photogrammetry using structured light illumination and two cameras generated 3D point clouds of the mouse head and whisker array (24 large whiskers), which were aligned to a realistic 3D mouse model. Whisker positions were simulated at retraction (-40 deg), intermediate (0 deg), and protraction (+40 deg) positions and mapped against the 3D visual space covered by VISp. Intrinsic signal imaging mapped cortical responses in VISp and SSp-bfd to visual and whisker stimulation under unimodal and bimodal conditions.

Anatomical tracing used brain-wide viral retrograde and anterograde transsynaptic strategies followed by serial two-photon tomography and deep-learning based 3D detection of labeled cells to map projection and postsynaptic neurons between SSp-bfd and VISp. Electrophysiology combined with optogenetics was used to characterize the functional circuit: ChR2 was expressed in SSp-bfd excitatory neurons, and patch-clamp recordings were made from identified excitatory (Cre-negative) and inhibitory Cre-positive neurons in VISp L2/3 to measure postsynaptic currents evoked by optogenetic activation of SSp-bfd axons.

A mathematical network model consisting of coupled recurrent neural networks (each with pyramidal and fast-spiking populations for VISp and SSp-bfd) was constructed to test whether a gain-dependent ISN regime could account for the observed tactile suppression of visual responses. The model explored how tactile input through cross-regional FS cell recruitment shifts the operating point of the VISp circuit into a suppressive regime.

## Target venue

Nature Communications
