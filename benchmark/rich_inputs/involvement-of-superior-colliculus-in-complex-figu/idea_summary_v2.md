## Working title

Superficial superior colliculus is causally involved in complex figure detection and encodes figure-ground signals in mice

## Core question

Is the superficial superior colliculus (sSC) of mice causally involved in detecting figures defined by complex features (contrast, orientation, phase) on textured backgrounds, and do sSC neurons encode figure-ground information in a behaviorally relevant manner?

## Motivation / gap

- Object detection is a core visual function, traditionally attributed to visual cortex (V1); however, mice can still detect simple stimuli after V1 silencing/ablation, likely mediated by SC
- SC involvement has been demonstrated for detecting isolated stimuli and simple changes, but not for detecting figures on complex, non-homogeneous backgrounds
- Recent work showed mouse sSC encodes visual features of complex objects independently of V1 input, but the behavioral relevance of this encoding was unknown
- Existing models of texture-defined figure detection focus exclusively on cortical circuits (V1 figure-ground modulation, higher area feedback), leaving SC out of the picture
- Prior SC inhibition/ablation studies typically targeted deeper layers or were unilateral; bilateral sSC-specific manipulations are rare

## Core contribution (bullet form)

- Optogenetic inhibition of bilateral sSC (N=8 GAD2-Cre mice, ChR2 in inhibitory neurons) significantly decreased performance on all three figure detection tasks: contrast, orientation, and phase
- Inhibition was most effective at early latencies (0-100 ms after stimulus onset), with effects diminishing at later time points (100-200 ms)
- sSC visually evoked responses were reduced by 33% on average during optogenetic inhibition (p < 0.001), though silencing was not complete
- Neural recordings (5 C57BL/6J mice) showed sSC neurons respond more strongly to figure elements than identical ground elements for contrast and orientation tasks
- Linear SVM decoder could discriminate figure vs. ground from sSC population activity above chance for all three tasks including phase
- Figure-ground discriminability (d-prime) was significantly higher on correct trials than error trials, linking sSC activity to behavioral decisions
- A small group of putative multisensory neurons at slightly deeper locations showed task-related responses peaking later (~700 ms), after lick spout presentation but before licking

## Method in brief

For optogenetic experiments, 8 GAD2-Cre mice received bilateral injections of Cre-dependent ChR2 (ssAAV-9/2-hEF1a-dlox-hChR2(H134R)_mCherry, titer 5.4e12) into sSC, followed by optic fiber implantation. Blue laser light activated inhibitory neurons, suppressing overall sSC activity. Mice performed a two-alternative forced choice figure detection task (left vs. right figure position, reported by licking a Y-shaped spout). Three task variants used figures differing from background by contrast, orientation, or phase. Inhibition was applied at different latencies (0-200 ms) after stimulus onset, with response allowed from 200 ms. A blue LED flashed at random intervals above the head to prevent behavioral cueing by the laser. Mice ran 100-250 trials per session over 2-5 months.

For electrophysiology, 5 C57BL/6J mice were implanted with silicon probes (Neuropixels or 32-channel linear arrays) targeting sSC. Neurons were classified by receptive field location relative to the figure: inside the figure, on the figure edge, or outside. Population responses were compared between figure and ground conditions using cluster-based permutation tests. A linear SVM classifier with a 50 ms sliding window (10 ms steps) decoded figure vs. ground identity. Behavioral relevance was assessed by comparing figure-ground discriminability (d-prime from ROC analysis) between hit and error trials. The response window was 500 ms before lick response was allowed.

## Target venue

eLife
