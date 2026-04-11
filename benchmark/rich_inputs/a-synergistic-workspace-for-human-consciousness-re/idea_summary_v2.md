## Working title

A synergistic global workspace revealed by integrated information decomposition: bridging Global Neuronal Workspace Theory and Integrated Information Theory through network science and information-theoretic analysis of human fMRI

## Core question

How is the human brain's information-processing architecture functionally organized in terms of synergistic and redundant interactions, and does a "synergistic workspace" that integrates information from specialized modules support consciousness -- as evidenced by its breakdown during anesthesia and disorders of consciousness?

## Motivation / gap

- Two leading theories of consciousness -- Global Neuronal Workspace Theory (GNWT) and Integrated Information Theory (IIT) -- both emphasize information integration but differ on its specific role and neural mechanisms
- No prior work had formally connected synergy (information produced by the whole beyond the parts) with the concept of a global neuronal workspace
- The distinct functional roles of the default mode network (DMN) and fronto-parietal/executive control network (FPN) within a potential workspace architecture were not well characterized from an information-theoretic perspective
- The relationship between integrated information (Phi) and consciousness had been studied, but without resolving Phi into its synergistic vs. redundant components
- It was unclear whether loss of consciousness (anesthesia, disorders of consciousness) specifically disrupts synergistic integration within a workspace, or merely reduces overall brain activity

## Core contribution (bullet form)

- Proposed the SAPHIRE (Synergy-Phi-Redundancy) neurocognitive architecture that decomposes brain information processing into three stages: (i) gathering via synergistic gateway regions, (ii) integration within a synergistic workspace, and (iii) broadcasting via redundant broadcaster regions
- Demonstrated using HCP resting-state fMRI (454-ROI augmented Schaefer atlas) that workspace gateways correspond to the default mode network (DMN) and broadcasters correspond to the executive control/fronto-parietal network (FPN)
- Used Integrated Information Decomposition to resolve Phi into synergistic and redundant components, showing that workspace regions are characterized by high synergy-to-redundancy ratios
- Showed that loss of consciousness under propofol anesthesia (n=16 healthy volunteers, Ramsay score 5) is associated with diminished integrated information within the synergistic workspace
- Replicated the finding in disorders of consciousness (DOC) patients, showing similar reorganization of cortical integrated information
- Demonstrated that recovery from anesthesia restores the workspace's ability to integrate information, and that the overlap between anesthesia-induced and DOC-induced changes specifically involves synergistic workspace gateway regions

## Method in brief

The study uses Integrated Information Decomposition (PhiID), which decomposes the mutual information between two neural sources (X, Y) across time into atoms of redundancy, unique information, and synergy -- yielding a 4x4 decomposition. This framework enables computation of synergistic and redundant components of integrated information (Phi). Whole-minus-sum Phi can be negative when persistent redundancy dominates, but the decomposition separates out synergistic Phi (always non-negative) as the key measure. Synergistic interactions were computed for all pairs of regions in a 454-ROI parcellation, yielding synergy and redundancy matrices.

Network science methods were then applied to these matrices. Gateways were defined as regions with high participation coefficient in the synergy network (connecting across multiple modules) and high within-module degree in the redundancy network (well-connected locally). Broadcasters were defined as regions with high within-module degree in the synergy network and high participation coefficient in the redundancy network (distributing information widely). This operationalization captures the three-stage processing model: gateways collect diverse synergistic information, the workspace integrates it, and broadcasters redundantly distribute the integrated output.

Empirical validation used three datasets: (1) HCP resting-state fMRI for identifying the architecture, (2) propofol anesthesia data (n=16, awake vs. deep anesthesia at Ramsay 5, plus post-recovery) collected at Robarts Research Institute, and (3) disorders of consciousness patient data. Network-based statistic (NBS) analyses identified regions with significant changes in integrated information between conscious and unconscious states. The overlap between anesthesia and DOC effects was mapped onto the synergistic workspace to test whether consciousness specifically depends on workspace integration.

## Target venue

eLife
