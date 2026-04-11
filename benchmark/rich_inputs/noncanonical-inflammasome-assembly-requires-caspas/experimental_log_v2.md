# Experimental Log: Noncanonical Inflammasome Assembly

## Datasets and Model Systems

| System | Cell Type | Genotype | Delivery Method | Purpose |
|--------|-----------|----------|----------------|---------|
| Primary BMDMs | Murine bone marrow-derived macrophages | Casp11-/- (C57BL/6 background) | Lentiviral transduction | Physiological LPS-induced speck assay |
| HEK293T | Human embryonic kidney | Wild-type | Transient transfection (PEI) | Ectopic expression / mechanistic dissection |

## Constructs Generated

| Construct | Tag | Backbone | Key Mutation | Purpose |
|-----------|-----|----------|-------------|---------|
| Casp11 WT-mCherry | C-terminal mCherry | pTwist Lenti-SFFV-WPRE | None | Reporter for WT speck formation |
| Casp11 C254A-mCherry | C-terminal mCherry | pTwist Lenti-SFFV-WPRE | C254A (catalytic dead) | Test catalytic activity requirement |
| Casp11 D285A-mCherry | C-terminal mCherry | pReceiver-M56 | D285A (non-cleavable IDL) | Test autoprocessing requirement |
| Casp11 C254A/D285A-mCherry | C-terminal mCherry | pReceiver-M56 | C254A + D285A | Double mutant control |
| TEV-D285A-mCherry | C-terminal mCherry | pTwist Lenti-SFFV-WPRE | D285A + TEV site at IDL | Exogenous cleavage rescue |
| TEV-C254A/D285A-mCherry | C-terminal mCherry | pTwist Lenti-SFFV-WPRE | C254A + D285A + TEV site | Negative control for TEV rescue |
| Untagged Casp11 WT | None | pReceiver-M56 | None | Trans-processing donor |
| Untagged Casp11 C254A | None | pReceiver-M56 | C254A | Catalytic-dead donor |
| Untagged Casp11 D285A | None | pReceiver-M56 | D285A | Non-cleavable donor |

## Experiment 1: LPS-Induced Speck Formation in BMDMs (Figure 1)

### Protocol
- Casp11-/- BMDMs transduced with Casp11 WT-mCherry or C254A-mCherry via lentivirus
- Primed with Pam3CSK4 for 4 h
- Transfected with LPS from S. enterica serovar Minnesota at increasing doses
- Fixed at 6 h post-LPS transfection for microscopy; 16 h for LDH/western

### Cytotoxicity by LDH Release (Fig 1B)

| LPS Dose (ug/mL) | WT-mCherry LDH (% cytotoxicity) | C254A-mCherry LDH (% cytotoxicity) | Empty Vector LDH (% cytotoxicity) |
|-------------------|---------------------------------|-------------------------------------|-------------------------------------|
| 0 | ~5 | ~5 | ~5 |
| 0.5 | ~20 | ~5 | ~5 |
| 1.0 | ~35 | ~5 | ~5 |
| 2.0 | ~50 | ~5 | ~5 |
| 5.0 | ~65 | ~5 | ~5 |

- WT-mCherry restores dose-dependent pyroptosis in Casp11-/- BMDMs
- C254A-mCherry shows no cytotoxicity at any LPS dose tested

### GSDMD Cleavage by Western Blot (Fig 1C)
- WT-mCherry: full-length GSDMD band diminishes and cleaved GSDMD-NT appears in a dose-dependent manner upon LPS transfection
- C254A-mCherry: no GSDMD cleavage detected at any dose
- Both constructs express at comparable levels by anti-mCherry blot; C254A slightly higher expression

### Speck Formation Quantification (Fig 1D-E)

| LPS Dose (ug/mL) | WT-mCherry Speck (% of mCherry+ cells) | C254A-mCherry Speck (% of mCherry+ cells) |
|-------------------|-----------------------------------------|---------------------------------------------|
| 0 | ~0 | ~0 |
| 0.5 | ~8 | ~0 |
| 1.0 | ~15 | ~0 |
| 2.0 | ~25 | ~0 |
| 5.0 | ~35 | ~0 |

- Fig 1D: WT-mCherry cells show large perinuclear mCherry specks after LPS; C254A-mCherry remains entirely diffuse
- Fig 1E: dose-response curve for WT follows non-linear regression (Log2, 3-parameter); C254A is flat at baseline
- Key finding: CARD-LPS binding alone is NOT sufficient for speck formation; catalytic activity at C254 is essential

## Experiment 2: Spontaneous Speck Formation in HEK293T (Figure 2)

### Protocol
- HEK293T transfected with WT-mCherry or C254A-mCherry using PEI
- Imaged by fluorescence microscopy 18 h post-transfection
- Specks quantified as % mCherry-positive cells with at least one speck

### Speck Quantification (Fig 2A-B)

| Construct | Speck Formation (% of mCherry+ cells) | N (biological replicates) |
|-----------|----------------------------------------|---------------------------|
| WT-mCherry | ~40-50 | 3 |
| C254A-mCherry | ~2-5 | 3 |

- Fig 2A: WT-mCherry forms bright specks spontaneously upon overexpression; C254A remains diffuse
- Fig 2B: Quantification confirms a large and significant difference between WT and C254A

### Western Blot Analysis (Fig 2C-D)
- Fig 2C: WT-mCherry is processed (cleaved bands visible) while C254A-mCherry remains full-length only
- Fig 2D: WT-mCherry appears in a high-molecular-weight complex by non-reducing SDS-PAGE; C254A does not

### Blue Native PAGE (Fig 2E-F)
- Fig 2E: WT-mCherry assembles into complexes >1 MDa; C254A-mCherry remains as monomer/dimer
- Fig 2F: quantification of high-MW complex signal confirms WT >> C254A

## Experiment 3: IDL Cleavage Requirement -- D285A Mutant (Figure 3)

### Speck Quantification (Fig 3A-B)

| Construct | Speck Formation (% of mCherry+ cells) |
|-----------|----------------------------------------|
| WT-mCherry | ~40-50 |
| D285A-mCherry | ~2-5 |

- The non-cleavable D285A mutant phenocopies the catalytic-dead C254A in failing to form specks
- Autoprocessing at the IDL is necessary for higher-order oligomerization

### Cleavage-Only vs Catalytic Activity (Fig 3C-D)
- Fig 3C: Schematic of constructs -- testing whether blocking only cleavage (D285A) vs blocking catalysis (C254A) gives the same phenotype
- Fig 3D: Both single mutants and the double mutant C254A/D285A fail to form specks, confirming that physical cleavage at D285 is required in addition to catalytic activity

## Experiment 4: Trans-Rescue by Co-Transfection with WT Casp11 (Figure 4)

### Protocol
- Fixed dose of tagged C254A-mCherry co-transfected with increasing doses of untagged WT Casp11
- Specks scored in mCherry channel only (tracks the catalytically dead reporter)

### Trans-Rescue Speck Data (Fig 4B-D)

| Untagged WT Dose (relative) | C254A-mCherry Speck (%) | WT-mCherry Speck (control, %) |
|-----------------------------|-------------------------|-------------------------------|
| 0 | ~2 | ~45 |
| 0.25x | ~10 | ~45 |
| 0.5x | ~18 | ~48 |
| 1.0x | ~25 | ~50 |
| 2.0x | ~30 | ~50 |

- Untagged WT Casp11 rescues C254A-mCherry speck formation in a dose-dependent manner
- This rescue could be via trans-cleavage of C254A at D285, or via WT oligomers nucleating C254A incorporation

### Double Mutant Not Rescued (Fig 4E-F)

| Untagged WT Dose (relative) | C254A/D285A-mCherry Speck (%) |
|-----------------------------|-------------------------------|
| 0 | ~2 |
| 0.25x | ~2 |
| 0.5x | ~3 |
| 1.0x | ~3 |
| 2.0x | ~3 |

- The C254A/D285A double mutant is NOT rescued by co-expression of WT Casp11
- This means the rescue of C254A requires cleavage at D285 on the tagged molecule itself
- Critically, this rules out a simple nucleation/co-recruitment model and points to cis-autoprocessing as essential

## Experiment 5: Cis vs Trans Processing Dissection (Figure 5)

### Protocol
- Fixed dose of C254A-mCherry co-transfected with increasing doses of untagged WT, C254A, or D285A

### Processing and Speck Rescue (Fig 5B-D)

| Untagged Co-Transfectant | C254A-mCherry Processing? | C254A-mCherry Speck Rescue? |
|--------------------------|---------------------------|----------------------------|
| WT Casp11 | Yes (cleaved bands appear) | Yes (dose-dependent) |
| C254A Casp11 | No | No |
| D285A Casp11 | Yes (cleaved bands appear) | Yes (dose-dependent) |

- Untagged WT rescues both processing and speck formation of C254A-mCherry
- Untagged D285A (which is catalytically active but itself non-cleavable) also rescues C254A-mCherry processing and specks
- Untagged C254A (catalytically dead) cannot rescue
- This means the catalytic activity of the untagged partner cleaves C254A-mCherry in trans at D285, but the resulting processed C254A-mCherry then assembles into specks through cis-dependent conformational changes

## Experiment 6: TEV Protease Rescue (Figure 3E-G or related)

### Protocol
- TEV cleavage site engineered into the IDL of D285A-mCherry (replacing the native cleavage sequence)
- Co-transfection with TEV protease expression plasmid

### TEV Rescue Results

| Construct | TEV Protease | Processing? | Speck Formation? |
|-----------|-------------|-------------|------------------|
| TEV-D285A-mCherry | - | No | No |
| TEV-D285A-mCherry | + | Yes | Yes (~30-40%) |
| TEV-C254A/D285A-mCherry | - | No | No |
| TEV-C254A/D285A-mCherry | + | Yes | Yes (~25-35%) |

- Exogenous TEV protease cleavage at the engineered IDL site is sufficient to induce speck formation
- Even the catalytically dead TEV-C254A/D285A can be rescued by TEV, confirming that it is the physical act of cleavage, not ongoing catalytic activity, that enables oligomerization
- This is the key experiment distinguishing between "catalytic activity needed continuously" vs "cleavage is the activating event"

## Summary of Key Comparisons Across All Experiments

| Construct | Catalytic Activity | IDL Cleavable | Forms Specks (BMDMs) | Forms Specks (HEK293T) | Rescued by WT | Rescued by TEV |
|-----------|-------------------|---------------|---------------------|----------------------|---------------|----------------|
| WT | Yes | Yes | Yes | Yes | N/A | N/A |
| C254A | No | Yes | No | No | Yes | N/A |
| D285A | Yes | No | N/D | No | N/D | N/A |
| C254A/D285A | No | No | N/D | No | No | N/A |
| TEV-D285A | Yes | No (native); Yes (TEV) | N/D | No without TEV; Yes with TEV | N/D | Yes |
| TEV-C254A/D285A | No | No (native); Yes (TEV) | N/D | No without TEV; Yes with TEV | N/D | Yes |

## Experimental Conditions and Reagents

| Parameter | Detail |
|-----------|--------|
| BMDM differentiation | 30% L929-conditioned DMEM, 7 days |
| Priming agent | Pam3CSK4, 4 h |
| LPS source | S. enterica serovar Minnesota |
| LPS delivery | Lipofectamine/FuGENE transfection |
| Microscopy fixation time | 6 h post-LPS |
| LDH assay time | 16 h post-LPS |
| HEK293T imaging time | 18 h post-transfection |
| Transfection reagent (HEK293T) | PEI, 1:1 w/w DNA:PEI ratio |
| Lentiviral packaging | pVSV-G + psPAX2 |
| Microscopy | Confocal fluorescence, Hoechst nuclear stain |
| Western blot targets | mCherry, GSDMD, beta-actin (loading control) |
| Mutagenesis kit | Q5 SDM Kit (NEB #E0554S) |
| TEV consensus sequence | ENLYFQ/G |

## Proposed Mechanistic Model

| Step | Event | Evidence |
|------|-------|----------|
| 1 | LPS binds Casp11 CARD | Published (Shi et al., 2014) |
| 2 | LPS-bound Casp11 dimerizes | Published (Ross et al., 2018) |
| 3 | Dimerization activates catalytic activity | Published (proximity-induced activation) |
| 4 | Catalytic activity mediates intra-molecular autoprocessing at D285 (IDL) | This study: C254A and D285A both block specks |
| 5 | Processed Casp11 undergoes conformational change enabling higher-order oligomerization | This study: TEV rescue of catalytic-dead mutants |
| 6 | Oligomeric SMOC (speck) forms | This study: direct visualization by microscopy |
| 7 | SMOC-assembled Casp11 cleaves GSDMD | Published + this study |
| 8 | GSDMD-NT pores trigger pyroptosis | Published |

## Observations from Figures (Summary)

- Fig 1D: WT-mCherry shows bright perinuclear specks in BMDMs after LPS; C254A remains diffuse throughout the cytoplasm at all doses
- Fig 1E: dose-response curve for speck formation parallels the dose-response for LDH release
- Fig 2A: HEK293T overexpression of WT-mCherry produces specks spontaneously (no LPS needed), while C254A does not
- Fig 2E: Blue native PAGE reveals WT assembles into complexes exceeding 1 MDa
- Fig 3: D285A phenocopies C254A in HEK293T -- no specks, confirming cleavage is independently required
- Fig 4: Untagged WT rescues C254A-mCherry specks dose-dependently, but cannot rescue the double mutant C254A/D285A
- Fig 5: D285A untagged (catalytically active, self-non-cleavable) rescues C254A-mCherry, proving trans-cleavage occurs and the resulting cis-processed molecule can oligomerize
- TEV experiments: physical cleavage alone, delivered by an orthogonal protease, is sufficient for speck assembly even in the complete absence of Casp11 catalytic activity
