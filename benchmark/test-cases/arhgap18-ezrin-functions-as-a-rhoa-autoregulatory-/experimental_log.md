# Experimental Log -- ARHGAP18-Ezrin RhoA autoregulation in microvilli

## 2024-01-12 -- ARHGAP18 localization

Confocal imaging of GFP-ARHGAP18 in Jeg-3 cells, co-stained with ezrin and myosin-2B.

| Marker | Microvillar colocalization (Pearson r) | Terminal web colocalization (Pearson r) |
|--------|---------------------------------------|---------------------------------------|
| ARHGAP18 vs Ezrin | 0.88 | 0.15 |
| ARHGAP18 vs Myosin-2B | 0.12 | 0.10 |
| Ezrin vs Myosin-2B | 0.08 | 0.05 |

ARHGAP18 strongly colocalizes with ezrin in microvilli but not with terminal web myosin-2.

## 2024-02-01 -- ARHGAP18 binding requires active (phospho-)ezrin

GST-pulldown with ARHGAP18 and ezrin variants.

| Ezrin construct | Binding to ARHGAP18 | Notes |
|----------------|--------------------|----- |
| WT ezrin (inactive/closed) | - | Dormant conformation |
| T567D ezrin (phosphomimetic, active) | +++ | Open/active conformation |
| T567A ezrin (phospho-dead) | - | Cannot be activated |
| Ezrin FERM domain alone | ++ | Active-like |

Interaction is specific to the active (open) conformation of ezrin.

## 2024-02-18 -- ARHGAP18 RhoGAP activity enhancement by ezrin

In vitro GTP hydrolysis assay (recombinant RhoA loaded with GTP).

| Condition | GTP hydrolysis rate (nmol/min) | Fold over basal |
|-----------|-------------------------------|-----------------|
| RhoA alone | 0.5 | 1.0x |
| RhoA + ARHGAP18 | 2.8 | 5.6x |
| RhoA + ARHGAP18 + ezrin-T567D | 6.2 | 12.4x |
| RhoA + ARHGAP18 + ezrin-T567A | 2.9 | 5.8x |
| RhoA + ARHGAP18-GAP-dead | 0.6 | 1.2x |

Active ezrin roughly doubles ARHGAP18's GAP activity, supporting the autoregulatory model.

## 2024-03-05 -- ARHGAP18 knockdown phenotype

CRISPR ARHGAP18-KO in Caco-2 cells, quantified by SIM imaging.

| Phenotype metric | WT | ARHGAP18-KO | p-value |
|-----------------|-----|-------------|---------|
| Microvilli per cell (apical) | 85 +/- 12 | 62 +/- 18 | <0.001 |
| Microvillar length (um) | 1.4 +/- 0.3 | 1.1 +/- 0.5 | <0.01 |
| Myosin-2 in microvilli (% cells) | 3 | 45 | <0.0001 |
| Terminal web organization score | 4.2 / 5 | 2.1 / 5 | <0.001 |

Loss of ARHGAP18 causes aberrant myosin-2 assembly inside microvilli and disrupts the terminal web boundary.

## 2024-03-22 -- RhoA activity measurement (FRET biosensor)

Apical RhoA-GTP levels measured by FRET in live cells.

| Compartment | WT RhoA-GTP (FRET ratio) | ARHGAP18-KO RhoA-GTP (FRET ratio) |
|-------------|-------------------------|-----------------------------------|
| Microvilli | 0.35 | 0.58 |
| Terminal web | 0.52 | 0.50 |
| Sub-apical cytoplasm | 0.20 | 0.22 |

RhoA activity is specifically elevated in microvilli upon ARHGAP18 loss, consistent with the local GAP model.
