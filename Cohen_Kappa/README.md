# Cohen Kappa Examination

## Sampling Dataset

1. To check the quality of EduNER, we sampled a batch of sudataset and invited different raters to annotate it again. 

- samping dataset:
  - sentences: 672
  - words: 41511
- entities summary:
  | label | ALG | COF | CON | COU | CRN | DAT | FRM | LOC | ORG | PER | PLO | TER | THE | TOO |
  | :---- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
  | count | 8   | 5   | 386 | 75  | 47  | 187 | 29  | 7   | 94  | 597 | 45  | 965 | 48  | 390 |

## Cohen's Kappa Result

============== Cohen's Kappa summary =======================

 Cohen Kappa and Weighted Kappa correlation coefficients 
 and confidence boundaries

|                  | lower | estimate | upper |
| :--------------- | ----- | -------- | ----- |
| unweighted kappa | 0.78  | 0.78     | 0.79  |
| weighted kappa   | 0.66  | 0.82     | 0.98  |

Number of words = 41511 

============== Cohen's Kappa summary =======================

## Explanation

Cohen's kappa reference sheet

| Cohen's kappa Coefficient | Strength of agreement |
| :------------------------ | :-------------------- |
| < 0.20                    | Slight                |
| 0.21 - 0.40               | Fair                  |
| 0.41 - 0.60               | Moderate              |
| 0.61 - 0.80               | Substantial           |
| 0.81 - 1.00               | Almost perfect        |

Our Cohen's kappa is 0.78, which indicates that the sampling dataset has a good quality.
