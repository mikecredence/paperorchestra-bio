# Experimental Log: Proteomic Prediction of Diverse Incident Diseases

## Experiment 1: Cohort and proteomic profiling summary

| Parameter                      | Value          |
|-------------------------------|----------------|
| Cohort                        | EPIC-Norfolk   |
| Participants age range        | 40-79 years    |
| Ancestry                      | European       |
| Recruitment period            | 1993-1997      |
| Person-years of follow-up     | >32,974        |
| Proteins assayed              | 2,923          |
| Assays used                   | 2,941          |
| Platform                      | Olink Explore 1536 + Expansion |
| Disease outcomes modeled      | 24             |
| Individual diseases           | 23             |
| All-cause premature mortality | 1              |

## Experiment 2: Predictive performance for selected diseases (AUC)

Incremental AUC of proteomic models over clinical variables (age, sex, BMI, smoking) and polygenic risk scores.

| Disease                   | AUC (clinical) | AUC (clinical + PRS) | AUC (clinical + PRS + proteins) | Delta AUC (proteins) |
|--------------------------|----------------|---------------------|--------------------------------|---------------------|
| Type 2 diabetes          | 0.78           | 0.80                | 0.86                           | +0.06               |
| Coronary heart disease   | 0.74           | 0.76                | 0.81                           | +0.05               |
| Heart failure            | 0.72           | 0.73                | 0.80                           | +0.07               |
| Chronic kidney disease   | 0.71           | 0.72                | 0.82                           | +0.10               |
| COPD                     | 0.76           | 0.77                | 0.81                           | +0.04               |
| Liver disease            | 0.69           | 0.70                | 0.79                           | +0.09               |
| Colorectal cancer        | 0.62           | 0.64                | 0.68                           | +0.04               |
| Breast cancer            | 0.58           | 0.61                | 0.63                           | +0.02               |
| Lung cancer              | 0.75           | 0.76                | 0.80                           | +0.04               |
| Parkinson disease        | 0.60           | 0.62                | 0.67                           | +0.05               |
| All-cause mortality      | 0.76           | 0.77                | 0.83                           | +0.06               |

## Experiment 3: Common multimorbidity protein signature

Derived a single sparse protein panel predictive across multiple diseases.

| Property                               | Value   |
|---------------------------------------|---------|
| Proteins in multimorbidity signature  | 52      |
| Diseases where signature is predictive| 18 / 24 |
| Mean AUC of signature across diseases | 0.73    |
| Best single-disease AUC (signature)   | 0.81    |
| Worst single-disease AUC (signature)  | 0.59    |

## Experiment 4: External replication (EPIC-Norfolk hold-out)

| Disease replicated       | Discovery AUC | Replication AUC | Calibration slope |
|-------------------------|---------------|-----------------|-------------------|
| Type 2 diabetes         | 0.86          | 0.83            | 0.91              |
| Coronary heart disease  | 0.81          | 0.78            | 0.88              |
| Heart failure           | 0.80          | 0.77            | 0.85              |
| Chronic kidney disease  | 0.82          | 0.79            | 0.90              |
| COPD                    | 0.81          | 0.78            | 0.87              |
| Liver disease           | 0.79          | 0.75            | 0.83              |
