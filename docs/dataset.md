# Dataset: Default of Credit Card Clients

## Overview

- Subject: default payments of credit card clients in Taiwan, with monthly data from April to September 2005.
- Task: binary classification. Predict whether a client defaults on the payment next month.
- Size: 30,000 clients, 23 features and 1 target. No missing values.

## Source and license

- Page: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients
- Creator: I-Cheng Yeh. Donated to the UCI Machine Learning Repository on 25 January 2016.
- License: Creative Commons Attribution 4.0 International (CC BY 4.0).
- Dataset citation: Yeh, I. (2009). *Default of Credit Card Clients* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H
- Introductory paper: Yeh, I. & Lien, Che-hui (2009). "The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients." *Expert Systems with Applications*.

## Variables

All amounts are in NT dollars (New Taiwan dollars). The monthly columns cover April to September 2005.

| UCI name | Column in file | Description |
|----------|----------------|-------------|
| - | ID | Record identifier |
| X1 | LIMIT_BAL | Amount of given credit (individual and family/supplementary credit) |
| X2 | SEX | Gender: 1 = male, 2 = female |
| X3 | EDUCATION | 1 = graduate school, 2 = university, 3 = high school, 4 = others |
| X4 | MARRIAGE | 1 = married, 2 = single, 3 = others |
| X5 | AGE | Age in years |
| X6-X11 | PAY_0, PAY_2 ... PAY_6 | Repayment status per month, from September to April |
| X12-X17 | BILL_AMT1 ... BILL_AMT6 | Bill statement amount per month, from September to April |
| X18-X23 | PAY_AMT1 ... PAY_AMT6 | Amount of previous payment per month, from September to April |
| Y | default payment next month | Target: 1 = default, 0 = no default |

### Repayment status codes (PAY_*)

Documented codes: -1 = paid duly, 1 = payment delay of one month, 2 = delay of two months, and so on up to 8, and 9 = delay of nine months or more. The page does not define the code 0.

### Months

The page states the months for the first, second and last columns of each group (September, August and April). The months in between are inferred from the column order: PAY_0, BILL_AMT1 and PAY_AMT1 are September, and PAY_6, BILL_AMT6 and PAY_AMT6 are April.

## Notes on the file

- The page offers a ZIP archive that contains one Excel file (`default of credit card clients.xls`). In this project it is stored as `data/raw/default_of_credit_card_clients.xls`.
- The first row holds the labels X1 to X23 and Y. The real column names are in the second row, so the file is read with `header=1`.
- The column names in the file differ from the UCI names. There is no `PAY_1`; the first repayment column is called `PAY_0`.

## Observations from our analysis

These points come from `notebooks/01_data_overview.ipynb`. They are not part of the UCI documentation.

- 35 duplicated rows (excluding ID).
- Target imbalance: 6,636 defaults (22.12%) vs 23,364 non-defaults (77.88%).
- EDUCATION contains the undocumented codes 0, 5 and 6 (14, 280 and 51 rows).
- MARRIAGE contains the undocumented code 0 (54 rows).
- PAY_* columns contain the undocumented codes -2 and 0. The documented code 9 never appears.
- BILL_AMT columns contain negative values (between 590 and 688 rows per column).
- PAY_AMT and BILL_AMT columns are strongly right-skewed with large outliers.

## Sensitive attributes

SEX, EDUCATION, MARRIAGE and AGE are personal demographic attributes. Their use in a credit risk model should be considered carefully (fairness).