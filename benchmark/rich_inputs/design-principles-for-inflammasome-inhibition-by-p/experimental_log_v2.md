# Experimental Log

> Pre-writing data tables and observations for the POP-inflammasome inhibition study.

---

## Datasets and Structural Resources

| Resource | PDB ID | Description | Use |
|----------|--------|-------------|-----|
| ASCPYD filament | 3j63 | Cryo-EM structure of ASC pyrin domain filament | Honeycomb template for Rosetta |
| AIM2PYD filament (tagless) | 7k3r | Cryo-EM structure, hexameric base | Honeycomb template for AIM2 |
| AIM2PYD filament (GFP-tagged) | 6mb2 | Cryo-EM structure, pentameric base | Template for IFI16PYD homology model |
| NLRP3PYD filament | 7pdz | Cryo-EM structure | Honeycomb template for NLRP3 |
| NLRP6PYD filament | 6ncv | Cryo-EM structure | Honeycomb template for NLRP6 |
| POP1 crystal structure | 4qob | X-ray crystal structure | Used directly in Rosetta |
| POP2 homology model | Based on 7pdz | Modeled on monomeric NLRP3PYD | Used in Rosetta |
| POP3 homology model | Based on 7k3r | Modeled on AIM2PYD monomer | Used in Rosetta |

---

## Methods and Baselines

| Assay | Readout | Key Parameters |
|-------|---------|----------------|
| Rosetta InterfaceAnalyzer | Interface energy (delta-G, REU) | 6 interface types per honeycomb |
| FRET polymerization | Donor/acceptor fluorescence ratio over time | MBP-PYD + TEVp trigger, increasing POP |
| Fluorescence anisotropy (FA) | Anisotropy change over time | Labeled PYD filament + POP titration |
| Cell-based imaging (HEK293T) | Filament count per field (mCherry puncta) | 300 ng PYD-mCherry + 600/1200 ng POP-eGFP |
| Negative-stain EM (nsEM) | Filament/aggregate morphology | 20-100 uM protein, TEVp 5 uM for 30 min |
| SEC (Superdex 75) | Elution profile, monodispersity | Monomeric POP peaks collected |

---

## Experiment 1: Rosetta Interface Energy Analysis of Homotypic PYD Filaments

Each PYD filament has six unique interface types (1a, 1b, 2a, 2b, 3a, 3b). The Rosetta analysis showed symmetric energy landscapes for homotypic assemblies (i.e., Type 1a and 1b contribute similar delta-G values).

| PYD Filament | Type 1a/1b (REU) | Type 2a/2b (REU) | Type 3a/3b (REU) | Sum Top Half (REU) | Sum Bottom Half (REU) |
|-------------|------------------|------------------|------------------|--------------------|-----------------------|
| ASCPYD | -22.1 / -22.1 | -10.5 / -10.5 | -6.8 / -6.8 | -39.4 | -39.4 |
| AIM2PYD | Symmetric | Symmetric | Symmetric | Favorable | Favorable |
| IFI16PYD (6mb2 model) | More favorable | More favorable | More favorable | Better than 7k3r model | Better than 7k3r model |
| IFI16PYD (7k3r model) | Less favorable | Less favorable | Less favorable | Largely unfavorable | Largely unfavorable |
| NLRP3PYD | Symmetric | Symmetric | Symmetric | Favorable | Favorable |
| NLRP6PYD | Symmetric | Symmetric | Symmetric | Favorable | Favorable |

Note: The IFI16PYD filament structure is unknown; homology model based on 6mb2 (pentameric base) produced more favorable delta-G values than the 7k3r-based model.

---

## Experiment 2: Rosetta Interface Analysis of POP-PYD Interactions

For each target PYD filament, the center protomer was replaced with POP1, POP2, or POP3. Delta-delta-G (ddG) values were computed at each interface.

| Interaction | Favorable Interfaces (ddG <= 3.5) | Unfavorable Interfaces (ddG >= 10.0) | Net Assessment |
|-------------|-----------------------------------|--------------------------------------|----------------|
| POP1 - ASCPYD | Few | Multiple | Poor inhibitor predicted |
| POP2 - ASCPYD | Multiple (especially bottom half) | Some | Good inhibitor predicted |
| POP3 - ASCPYD | Multiple (especially bottom half) | Some | Good inhibitor predicted |
| POP1 - AIM2PYD | Several | Fewer | Moderate inhibitor predicted |
| POP2 - AIM2PYD | Several | Moderate | Moderate inhibitor predicted |
| POP3 - AIM2PYD | Several | Moderate | Moderate inhibitor predicted |
| POP1 - IFI16PYD | Several | Fewer | Moderate inhibitor predicted |
| POP2 - IFI16PYD | Several | Moderate | Moderate inhibitor predicted |
| POP3 - IFI16PYD | Several | Moderate | Moderate inhibitor predicted |
| POP1 - NLRP3PYD | Several | Fewer | Moderate inhibitor predicted |
| POP2 - NLRP3PYD | Several | Moderate | Moderate inhibitor predicted |
| POP1 - NLRP6PYD | Several | Fewer | Moderate inhibitor predicted |
| POP3 - NLRP6PYD | Several | Fewer | Good inhibitor predicted |

Fig. 1 shows honeycomb sideview diagrams for each PYD filament with corresponding POP replacements. The key finding is that both favorable and unfavorable interactions between POPs and PYDs are necessary for effective recognition and inhibition.

Fig. 1 Supplement 2 shows the specific favorable (ddG <= 3.5, blue dots) and unfavorable (ddG >= 10.0, red dots) interactions between ASCPYD and each POP.

---

## Experiment 3: Cell-Based Inhibition of ASCPYD Filament Assembly

HEK293T cells were co-transfected with ASCPYD-mCherry (300 ng) and POP-eGFP or eGFP control at two doses (600 ng and 1200 ng). Filament formation was quantified as relative filament count.

| Condition | POP Dose (ng plasmid) | Relative ASCPYD Filaments | Significant Inhibition? |
|-----------|----------------------|--------------------------|------------------------|
| eGFP control | 600 | 1.0 (reference) | N/A |
| eGFP control | 1200 | 1.0 (reference) | N/A |
| POP1-eGFP | 600 | ~1.0 | No |
| POP1-eGFP | 1200 | ~1.0 | No |
| POP2-eGFP | 600 | Reduced | Yes |
| POP2-eGFP | 1200 | Further reduced | Yes |
| POP3-eGFP | 600 | Reduced | Yes |
| POP3-eGFP | 1200 | Further reduced | Yes |

Fig. 2A shows representative fluorescent microscopy images. POP1-eGFP does not reduce ASCPYD-mCherry filament puncta (crimson), while POP2/POP3 clearly reduce them.

Fig. 2B: Quantification with N >= 4 replicates confirms POP1 fails to inhibit ASCPYD assembly in cells. POP2 and POP3 show dose-dependent inhibition.

---

## Experiment 4: Cell-Based Inhibition with Full-Length ASC

| Condition | POP Dose (ng) | Relative ASCFL Filaments | Notes |
|-----------|--------------|--------------------------|-------|
| eGFP control | 1200 | 1.0 (reference) | Full-length ASC-mCherry (300 ng) |
| POP1-eGFP | 1200 | ~1.0 | No inhibition |
| POP2-eGFP | 1200 | Reduced | Inhibits ASCFL |
| POP3-eGFP | 1200 | Reduced | Inhibits ASCFL |

Fig. 2C: Representative images of HEK293T cells with full-length ASC-mCherry confirm the PYD-only results.

---

## Experiment 5: FRET/FA Polymerization Kinetics for ASC Inhibition

FRET-labeled MBP-ASCPYD was triggered by TEVp, monitored over time. Polymerization half-times (t1/2) were measured with increasing POP concentrations.

| POP | Effect on ASC Nucleation | Effect on ASC Elongation | IC50 for ASC |
|-----|--------------------------|--------------------------|--------------|
| POP1 | Minimal lag prolongation | Minimal | Poor inhibitor (high IC50) |
| POP2 | Prolonged lag (nucleation suppressed) | Moderate | Effective inhibitor |
| POP3 | Prolonged lag (nucleation suppressed) | Moderate | Effective inhibitor |

Fig. 2E: Time courses show POP2 and POP3 markedly prolong the lag phase of ASCPYD polymerization, consistent with nucleation inhibition. POP1 has minimal effect.

---

## Experiment 6: Recombinant POP Characterization

| Protein | Purification | SEC Behavior | nsEM at High Concentration |
|---------|-------------|-------------|---------------------------|
| POP1 (untagged) | Ni-NTA + SEC (Superdex 75) | Monomeric peak collected | 100 uM: no filaments, no aggregates |
| MBP-POP2 | Ni-NTA + SEC (Superdex 75) | Monomeric MBP-POP2 peak | 20 uM after TEVp: no filaments |
| MBP-POP3 | Ni-NTA + SEC (Superdex 75) | Monomeric MBP-POP3 peak | 20 uM after TEVp: no filaments |

Fig. 2 Supplement 1A: SEC profiles confirm monomeric states. Fig. 2 Supplement 1B: nsEM images at high concentrations show POPs do not form filaments, confirming they inhibit without co-assembling.

Storage buffer: 40 mM HEPES-NaOH pH 7.4, 400 mM NaCl, 2 mM DTT, 0.5 mM EDTA, 10% glycerol. Proteins stored at -80C.

---

## Experiment 7: Inhibition of ALR (AIM2/IFI16) PYD Filament Assembly

### Cell-based (HEK293T)

| Target PYD | POP | Dose (ng) | Relative Filaments | N |
|-----------|-----|-----------|-------------------|---|
| AIM2PYD-mCherry (300 ng) | eGFP control | 1200 | 1.0 | >= 4 |
| AIM2PYD-mCherry | POP1-eGFP | 600 | Reduced | >= 4 |
| AIM2PYD-mCherry | POP1-eGFP | 1200 | Further reduced | >= 4 |
| AIM2PYD-mCherry | POP2-eGFP | 600 | Reduced | >= 4 |
| AIM2PYD-mCherry | POP2-eGFP | 1200 | Further reduced | >= 4 |
| AIM2PYD-mCherry | POP3-eGFP | 600 | Reduced | >= 4 |
| AIM2PYD-mCherry | POP3-eGFP | 1200 | Further reduced | >= 4 |
| IFI16PYD-mCherry (300 ng) | eGFP control | 1200 | 1.0 | >= 4 |
| IFI16PYD-mCherry | POP1-eGFP | 1200 | Reduced | >= 4 |
| IFI16PYD-mCherry | POP2-eGFP | 1200 | Reduced | >= 4 |
| IFI16PYD-mCherry | POP3-eGFP | 1200 | Reduced | >= 4 |

Fig. 3A: All three POPs reduce AIM2PYD-mCherry filaments in HEK293T cells. Fig. 3B: Quantification confirms dose-dependent inhibition by all POPs.

Fig. 3C-D: Similar results with IFI16PYD. All three POPs inhibit IFI16PYD filament formation.

### Biochemical (FRET/FA)

| POP | Effect on AIM2PYD Polymerization | Mechanism |
|-----|----------------------------------|-----------|
| POP1 | Inhibits elongation | Reduces rate but minimal lag extension |
| POP2 | Inhibits elongation | Reduces rate and some lag extension |
| POP3 | Inhibits elongation | Reduces rate; also some nucleation effect |

Fig. 3E: Polymerization time courses show POPs primarily inhibit elongation of AIM2PYD filaments.

---

## Experiment 8: Effect of dsDNA Activating Ligand on POP Inhibition of ALRs

| Condition | POP Required for Inhibition | Observation |
|-----------|----------------------------|-------------|
| AIM2PYD alone (no dsDNA) | Lower POP concentration | Easier to inhibit |
| AIM2PYD + dsDNA | Higher POP concentration | Excess POP needed |
| IFI16PYD alone (no dsDNA) | Lower POP concentration | Easier to inhibit |
| IFI16PYD + dsDNA | Higher POP concentration | Excess POP needed |

Fig. 3 Supplement 2: In the presence of activating dsDNA ligand, more POP is required to achieve equivalent inhibition, consistent with the model that POPs compete with the assembly-promoting effect of the ligand.

---

## Experiment 9: Inhibition of NLRP PYD Filament Assembly

### Cell-based (HEK293T)

| Target PYD | POP | Dose (ng) | Relative Filaments | N |
|-----------|-----|-----------|-------------------|---|
| NLRP3PYD-mCherry (600 ng) | eGFP control | 1200 | 1.0 | >= 4 |
| NLRP3PYD-mCherry | POP1-eGFP | 600 | Reduced | >= 4 |
| NLRP3PYD-mCherry | POP1-eGFP | 1200 | Further reduced | >= 4 |
| NLRP3PYD-mCherry | POP2-eGFP | 600 | Reduced | >= 4 |
| NLRP3PYD-mCherry | POP2-eGFP | 1200 | Further reduced | >= 4 |
| NLRP3PYD-mCherry | POP3-eGFP | 600 | Minimal effect | >= 4 |
| NLRP3PYD-mCherry | POP3-eGFP | 1200 | Minimal effect | >= 4 |
| NLRP6PYD-mCherry (300 ng) | eGFP control | 1200 | 1.0 | >= 4 |
| NLRP6PYD-mCherry | POP1-eGFP | 1200 | Reduced | >= 4 |
| NLRP6PYD-mCherry | POP2-eGFP | 1200 | Reduced | >= 4 |
| NLRP6PYD-mCherry | POP3-eGFP | 1200 | Reduced | >= 4 |

Fig. 4A-B: POP1 and POP2 inhibit NLRP3PYD filament assembly while POP3 shows minimal effect.

Fig. 4C-D: All three POPs can inhibit NLRP6PYD filament formation.

### Biochemical (FRET/FA)

| POP | Effect on NLRP3PYD | Effect on NLRP6PYD |
|-----|--------------------|--------------------|
| POP1 | Inhibits elongation | Inhibits elongation |
| POP2 | Inhibits elongation | Inhibits elongation |
| POP3 | Weak/no effect | Inhibits elongation |

Fig. 4E: Polymerization kinetics confirm the cell-based observations for NLRP PYDs.

---

## Experiment 10: Summary of POP Target Specificity and Inhibition Modes

| POP | Primary Target(s) | Inhibition Mechanism | Secondary Target(s) |
|-----|-------------------|---------------------|---------------------|
| POP1 | AIM2, IFI16, NLRP3, NLRP6 | Elongation inhibition of receptor PYDs | Not ASC |
| POP2 | ASC (nucleation) | Nucleation suppression | AIM2, IFI16, NLRP3, NLRP6 (elongation) |
| POP3 | ASC (nucleation) | Nucleation suppression | AIM2, NLRP6 (elongation) |

Fig. 5: Summary cartoon showing refined target specificity. Solid red lines = most likely primary targets. Solid gray lines = additional direct targets. Dotted gray lines = other possible targets.

---

## Key Mechanistic Observations

| Feature | POPs | COPs (for comparison) |
|---------|------|-----------------------|
| Inhibition without co-assembly | Yes, POPs do not co-assemble | No, COPs co-assemble into CARD filaments |
| Stoichiometry required | Super-stoichiometric (excess POP needed) | Sub-stoichiometric |
| Nucleation vs. elongation | POP2/3 suppress nucleation of ASC; all POPs inhibit elongation of receptors | COPs inhibit caspase-1 assembly |
| Effect of activating ligand | Requires more POP when ligand present (dsDNA for AIM2/IFI16) | N/A |

---

## Sequence Analysis

Fig. 1 Supplement 1 (A-C): Amino acid sequence alignments of POPs with their most similar PYDs. POP1 shares partial homology with ASCPYD, POP2 with NLRP3PYD, and POP3 with AIM2PYD. Despite these homologies, target specificity is not dictated by sequence similarity alone.

| POP | Most Similar PYD by Sequence | Actual Primary Target |
|-----|-----------------------------|-----------------------|
| POP1 | ASCPYD | NOT ASC; instead upstream receptors |
| POP2 | NLRP3PYD | ASC nucleation + receptor elongation |
| POP3 | AIM2PYD | ASC nucleation + AIM2/NLRP6 elongation |

---

## Expression and Cell Culture Parameters

| Parameter | Value |
|-----------|-------|
| Cell line | HEK293T (ATCC CRL-11268) |
| Seeding density | 0.1 x 10^6 per well (12-well plate) |
| Transfection | Lipofectamine 2000, at 70% confluence |
| Fixation | 4% paraformaldehyde, 16h post-transfection |
| Cover glass | 20 mm round |
| Imaging | Cytation 5 multi-functional reader (BioTek) |
| Analysis software | Gen5 (BioTek) |
| E. coli strain | BL21 Rosetta2DE3 |
| Affinity purification | Ni2+-NTA |
| SEC column | Superdex 75 (Cytiva) |

---

## Protein Constructs and Vectors

| Protein | Vector | Tag | Notes |
|---------|--------|-----|-------|
| POP1 | pET21b | None (untagged) | Expressed in E. coli |
| POP2 | pET28b | N-terminal His6-MBP + TEVp site | Cleaved for assays |
| POP3 | pET28b | N-terminal His6-MBP + TEVp site | Cleaved for assays |
| PYDs (cell assay) | pCMV6 | C-terminal mCherry | For imaging |
| POPs (cell assay) | pCMV6 | C-terminal eGFP | For imaging |

---

## Rosetta Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Software | Rosetta InterfaceAnalyzer |
| Filament model | Honeycomb sideview (7 protomers) |
| Interface types | 6 (Type 1a, 1b, 2a, 2b, 3a, 3b) |
| Favorable ddG threshold | <= 3.5 REU |
| Unfavorable ddG threshold | >= 10.0 REU |
| IFI16 special threshold | >= 5.0 or positive delta-G (weaker intrinsic energies) |

---

## Overall Conclusions from Data

1. POP1 does NOT directly inhibit ASC, contrary to the previous model. Instead, POP1 targets upstream receptor PYD filaments.
2. POP2 and POP3 suppress the nucleation step of ASC filament assembly (seen as prolonged lag phases in kinetic assays).
3. All three POPs can inhibit elongation of various receptor PYD filaments, revealing intrinsic target redundancy.
4. The combination of favorable and unfavorable Rosetta interface energies at the six contact surfaces predicts inhibition effectiveness.
5. Super-stoichiometric POP concentrations are needed, especially when activating ligands are present, which is rationalized as allowing inflammasome function while still providing regulation.
