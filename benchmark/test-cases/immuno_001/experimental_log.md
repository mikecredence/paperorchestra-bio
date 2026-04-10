# Experimental Log: Multi-omic Immune Atlas Across the Human Lifespan

## Experiment 1: Cohort and profiling overview

| Parameter                        | Value                  |
|---------------------------------|------------------------|
| Total volunteers                 | 220                    |
| Cohort                          | Shanghai Pudong Cohort |
| Age groups                      | 13                     |
| Age range                       | 0 to >90 years        |
| Modalities                      | 5                      |
| scRNA-seq                       | Yes                    |
| Single-cell TCR-seq             | Yes                    |
| Single-cell BCR-seq             | Yes                    |
| Mass cytometry (CyTOF)          | Yes                    |
| Bulk RNA-seq                    | Yes                    |
| Flow cytometry validation       | Yes                    |

## Experiment 2: Major immune cell type abundance across age groups

Relative proportions (%) of major immune populations by age bracket.

| Age group    | CD4+ T cells | CD8+ T cells | B cells | NK cells | Monocytes | DCs  |
|-------------|-------------|-------------|---------|----------|-----------|------|
| 0-1 yr      | 38.2        | 12.5        | 22.8    | 8.1      | 14.3      | 4.1  |
| 1-5 yr      | 36.5        | 14.1        | 20.3    | 9.5      | 15.2      | 4.4  |
| 6-12 yr     | 35.8        | 16.2        | 17.5    | 11.3     | 15.0      | 4.2  |
| 13-18 yr    | 34.2        | 18.6        | 14.8    | 12.8     | 15.3      | 4.3  |
| 19-30 yr    | 33.5        | 20.1        | 12.5    | 14.2     | 15.5      | 4.2  |
| 31-45 yr    | 32.8        | 21.5        | 11.2    | 15.5     | 15.0      | 4.0  |
| 46-60 yr    | 31.2        | 23.8        | 9.8     | 16.8     | 14.5      | 3.9  |
| 61-70 yr    | 29.5        | 25.2        | 8.5     | 18.2     | 15.0      | 3.6  |
| 71-80 yr    | 27.8        | 26.5        | 7.2     | 20.1     | 15.2      | 3.2  |
| >80 yr      | 25.5        | 27.8        | 6.1     | 22.5     | 15.0      | 3.1  |

## Experiment 3: T cell clonal expansion across age

| T cell subset              | Mean clonality (children) | Mean clonality (adults) | Mean clonality (elderly) | Peak age group |
|---------------------------|--------------------------|------------------------|-------------------------|---------------|
| GNLY+CD8+ EM T cells     | 0.08                     | 0.25                   | 0.52                    | >80 yr        |
| CD8+ naive T cells        | 0.01                     | 0.02                   | 0.04                    | 71-80 yr      |
| CD4+ central memory       | 0.03                     | 0.09                   | 0.15                    | 61-70 yr      |
| Treg cells                | 0.02                     | 0.05                   | 0.08                    | >80 yr        |
| MAIT cells                | 0.12                     | 0.18                   | 0.14                    | 31-45 yr      |

## Experiment 4: Cytotoxic B cells enrichment in children

| Age group   | Cytotoxic B cell fraction (%) | GZMB expression (log2 CPM) |
|------------|------------------------------|---------------------------|
| 0-1 yr     | 5.2                          | 3.8                       |
| 1-5 yr     | 4.8                          | 3.5                       |
| 6-12 yr    | 3.1                          | 2.9                       |
| 19-30 yr   | 1.2                          | 1.5                       |
| 46-60 yr   | 0.8                          | 1.1                       |
| >80 yr     | 0.5                          | 0.8                       |

## Experiment 5: Immune aging clock performance

| Metric                    | Value |
|--------------------------|-------|
| Predicted vs chronological age (Pearson r) | 0.92 |
| Mean absolute error (years)                | 5.8  |
| Cell types used in clock                   | 28   |
| Features in final model                    | 156  |
