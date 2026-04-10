# Experimental Log: DeepTernary -- SE(3)-Equivariant Ternary Complex Prediction

## Experiment 1: PROTAC benchmark performance

Evaluated DeepTernary against existing methods on PROTAC ternary complex benchmark.

| Method       | DockQ (mean) | % Acceptable (DockQ > 0.23) | % Medium (DockQ > 0.49) | Avg time/complex |
|-------------|-------------|----------------------------|------------------------|-----------------|
| DeepTernary | 0.65        | 78%                        | 55%                    | ~7 s            |
| PRosettaC   | 0.38        | 52%                        | 28%                    | ~30 min         |
| AlphaFold3  | 0.42        | 58%                        | 32%                    | ~5 min          |
| Chai-1      | 0.35        | 48%                        | 24%                    | ~3 min          |
| BOTCP       | 0.30        | 42%                        | 18%                    | ~45 min         |
| FRODock     | 0.25        | 35%                        | 15%                    | ~20 min         |

## Experiment 2: Molecular glue/degrader (MG(D)) benchmark

| Method       | DockQ (mean) | % Acceptable | Avg time/complex |
|-------------|-------------|-------------|-----------------|
| DeepTernary | 0.23        | 45%         | ~1 s            |
| PRosettaC   | 0.15        | 30%         | ~30 min         |
| AlphaFold3  | 0.18        | 35%         | ~5 min          |

## Experiment 3: Ranking quality across seeds

Assessed prediction reliability using 40 random seeds per target.

| Metric                            | Value |
|-----------------------------------|-------|
| Avg rank of best acceptable pose  | 4.06  |
| Seeds evaluated per target        | 40    |
| Targets with acceptable in top-5  | 82%   |
| Targets with acceptable in top-10 | 91%   |

## Experiment 4: Buried surface area vs degradation potency

| E3 ligase | N targets | Pearson r (BSA vs DC50) | Spearman rho |
|-----------|----------|------------------------|-------------|
| CRBN      | 18       | 0.62                   | 0.58        |
| VHL       | 14       | 0.71                   | 0.65        |
| IAP       | 8        | 0.55                   | 0.50        |
| Combined  | 40       | 0.64                   | 0.59        |

## Experiment 5: TernaryDB dataset statistics

| Property                    | Count  |
|----------------------------|--------|
| Total ternary complexes    | 4,520  |
| After filtering PROTAC/MG  | 4,182  |
| Training set               | 3,346  |
| Validation set             | 418    |
| Test set                   | 418    |
