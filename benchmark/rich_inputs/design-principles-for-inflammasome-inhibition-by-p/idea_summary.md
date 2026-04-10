# Idea Summary: Design Principles for Inflammasome Inhibition by Pyrin-Only-Proteins

## Working title
Design Principles for Inflammasome Inhibition by Pyrin-Only-Proteins

## Core question
AbstractInflammasomes are filamentous signaling platforms essential for host defense against various intracellular calamities such as pathogen invasion and genotoxic stresses. However, dysregulated inflammasomes cause an array of human diseases including autoinflammatory disorders and cancer. It was recently identified that endogenous pyrin-only-proteins (POPs) regulate inflammasomes by directly inhibiting their filament assembly. Here, by combining Rosetta in silico, in vitro, and in cellulo me

## Motivation / gap
- IntroductionInflammasomes are filamentous signaling platforms integral to host innate defense against a wide range of intracellular catastrophes, which include ionizing irradiation, genotoxic chemical
- However, persisting inflammasome activities lead to several human maladies including numerous autoinflammatory disorders, cancer, and even severe COVID-19 (Karki et al., 2017; Tartey & Kanneganti, 202
- Thus, understanding how inflammasome assemblies are regulated at the molecular level can provide key insights into developing strategies for preventing and treating various diseases (Broz & Dixit, 201
- For instance, an array of molecular signatures arising from various pathogenic conditions induces the oligomerization of inflammasome receptors, resulting in filament assembly by their pyrin-domains (
- The upstream PYD oligomers then induce the filament assembly by the PYD of the central adaptor ASC (ASCPYD), resulting in oligomerization/filamentation of its CARD (ASC: Apoptosis-associated-speck-for

## Core contribution (bullet form)
Extracted from abstract:
AbstractInflammasomes are filamentous signaling platforms essential for host defense against various intracellular calamities such as pathogen invasion and genotoxic stresses. However, dysregulated inflammasomes cause an array of human diseases including autoinflammatory disorders and cancer. It was recently identified that endogenous pyrin-only-proteins (POPs) regulate inflammasomes by directly inhibiting their filament assembly. Here, by combining Rosetta in silico, in vitro, and in cellulo methods, we investigate the target specificity and inhibition mechanisms of POPs. In contrast to a previous report, we find that POP1 is a poor inhibitor of the central inflammasome adaptor ASC. Instead, POP1 inhibits the assembly of upstream receptor PYD filaments such as those of AIM2, IFI16, NLRP3, and NLRP6. Moreover, not only does POP2 directly suppress the nucleation of ASC, but it can also inhibit the elongation of receptor filaments. In addition to inhibiting the elongation of AIM2 and NLRP6 filaments, POP3 potently suppresses the nucleation of ASC. Our Rosetta analyses and biochemical experiments consistently suggest that a combination of favorable and unfavorable interactions between POPs and PYDs is necessary for effective recognition and inhibition. Together, we reveal the intrinsic target redundancy of POPs and their inhibitory mechanisms.

## Method in brief
Materials and MethodsRosetta SimulationThe InterfaceAnalyzer script in Rosetta was used to determine the interaction energy at individual interfaces of the honeycomb (Matyszewski et al., 2021). We used the cryo-EM structures of ASCPYD (PDB: 3j63; (Lu et al., 2014)), AIM2PYD (PDB: 7k3r; (Matyszewski et al., 2021)), NLRP3PYD (PDB: 7pdz; (Hochheiser, Behrmann, et al., 2022)) and NLRP6PYD (PDB: 6ncv; (Shen et al., 2019)) filaments to generate corresponding honeycombs. Because the structure of the IFI16PYD filament is unknown, we used the eGFP-AIM2PYD filament (PDB: 6mb2; (Lu et al., 2015)) that shows a pentameric filament base as a template; using the untagged AIM2PYD filament (PDB: 7k3r; (Matyszewski et al., 2021)), which shows a hexameric filament base, as a template resulted in largely unfavorable energy scores (Figure 1- Figure Supplement 1C). For POPs, we used the crystal structure of POP1 (PDB: 4qob), and generated homology models of POP2 and POP3 based on monomeric NLRP3PYD (PDB: 7pdz) and AIM2PYD (PDB: 7k3r), respectively.Cell culture and imagingEach protein was cloned into pCMV6 vector containing C-terminal mCherry (inflammasome PYDs) or eGFP (POPs). HEK293T cells (ATCC, CRL-11268) were seeded into 12-well plate (0.1 x 106 per well) with round cover glass (20 mm). eGFP alone or POP-eGFP plasmids (600 ng and 1200 ng) were co-transfected with inflammasome-mCherry plasmids (300 ng) at 70% confluence using lipofectamine 2000 (Invivogen). After 16 hours, cells were washed twi

## Target venue
eLife
