# Experimental Log: ScopeDTI -- Semi-Inductive Drug-Target Interaction Prediction

## Experiment 1: Classification performance (semi-inductive split)

Evaluated SCOPE against baseline models using semi-inductive new compound split.

| Model         | BindingDB AUROC | BindingDB AUPRC | Human AUROC | Human AUPRC | KIBA AUROC | KIBA AUPRC |
|--------------|----------------|-----------------|-------------|-------------|-----------|-----------|
| SCOPE (ours) | 0.923          | 0.918           | 0.942       | 0.938       | 0.896     | 0.882     |
| DrugBAN      | 0.871          | 0.862           | 0.905       | 0.897       | 0.854     | 0.838     |
| MolTrans     | 0.856          | 0.843           | 0.889       | 0.878       | 0.841     | 0.822     |
| GraphDTA     | 0.848          | 0.835           | 0.876       | 0.862       | 0.832     | 0.815     |
| DeepDTA      | 0.831          | 0.818           | 0.862       | 0.848       | 0.818     | 0.798     |
| DeepConv-DTI | 0.820          | 0.805           | 0.851       | 0.835       | 0.805     | 0.782     |

## Experiment 2: Performance across split types on SCOPE dataset

| Split type       | AUROC | AUPRC | Accuracy | Sensitivity | Specificity |
|-----------------|-------|-------|----------|-------------|-------------|
| Transductive    | 0.961 | 0.955 | 0.912    | 0.895       | 0.928       |
| Semi-inductive  | 0.935 | 0.928 | 0.886    | 0.871       | 0.902       |
| Fully inductive | 0.878 | 0.865 | 0.821    | 0.798       | 0.843       |

## Experiment 3: Dataset scale comparison

| Dataset        | Positive pairs | Negative pairs | Total    | Unique drugs | Unique proteins |
|---------------|---------------|---------------|----------|-------------|----------------|
| Human (orig)  | 3,369         | 3,369         | 6,738    | 2,726       | 852            |
| BindingDB     | 15,843        | 15,843        | 31,686   | 10,665      | 1,413          |
| KIBA          | 12,068        | 12,068        | 24,136   | 2,111       | 229            |
| SCOPE dataset | 342,510       | 342,510       | 685,020  | 98,234      | 4,815          |

## Experiment 4: Ablation study on SCOPE dataset (semi-inductive)

| Variant                     | AUROC         | AUPRC         |
|----------------------------|--------------|--------------|
| Full SCOPE model            | 0.935        | 0.928        |
| w/o 3D protein repr.        | 0.908 (-0.027)| 0.899 (-0.029)|
| w/o 3D compound repr.       | 0.914 (-0.021)| 0.906 (-0.022)|
| w/o bilinear attention      | 0.901 (-0.034)| 0.892 (-0.036)|
| w/o bias filtering          | 0.918 (-0.017)| 0.910 (-0.018)|

## Experiment 5: Experimental validation

| Prediction rank | Validated | Confirmed binding | Confirmation rate |
|----------------|-----------|-------------------|-------------------|
| Top 50         | 50        | 38                | 76%               |
| Top 100        | 100       | 65                | 65%               |
| Top 200        | 200       | 112               | 56%               |
