# Experimental Log: DEBBIES Dataset

## Dataset overview

| Property | Value |
|---|---|
| Number of species | 185 |
| Taxonomic scope | Ectotherms |
| Number of traits | 8 |
| Model framework | DEB-IPM |

## Trait definitions

| Trait | Description | Units |
|---|---|---|
| Length at birth | Size at hatching/birth | cm |
| Length at puberty | Size at reproductive maturity | cm |
| Maximum length | Asymptotic or max observed size | cm |
| Max reproduction rate | Peak reproductive output | offspring/time |
| Energy allocation fraction | Fraction to respiration vs reproduction | dimensionless |
| Von Bertalanffy growth rate | Somatic growth rate parameter | 1/time |
| Mortality rate (juvenile) | Age-specific mortality before maturity | 1/time |
| Mortality rate (adult) | Age-specific mortality after maturity | 1/time |

## Technical validation: observed vs. predicted

| Demographic quantity | Correlation (obs vs pred) | Notes |
|---|---|---|
| Longevity | Satisfactory agreement | Across all 185 species |
| Generation time | Satisfactory agreement | Validated cross-taxonomically |
| Age at maturity | Satisfactory agreement | Good coverage of data-deficient spp. |

## Comparison with existing datasets

| Feature | DEBBIES | Existing datasets |
|---|---|---|
| Cross-taxonomic comparisons | Easy (standardized DEB traits) | Difficult (heterogeneous definitions) |
| Data-deficient species | Included (185 spp.) | Often excluded |
| Population forecasts (novel conditions) | Supported via DEB-IPM | Limited or not supported |

## Notes

- 2024-01-10: Compiled trait data for 185 species from DEB parameter databases and literature.
- 2024-02-05: DEB-IPM parameterization complete; demographic quantities computed.
- 2024-02-18: Validation against observed longevity and generation time shows satisfactory fit across taxa.
- Next step: link demographic outputs to IUCN conservation status for applied analysis.
