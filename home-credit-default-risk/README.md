# Home Credit Default Risk Analysis

This project is a beginner-friendly analysis of the Kaggle Home Credit Default Risk dataset.

## Project Goal

The goal of this notebook is not to build a complex model first. Instead, the focus is to:

- understand the data structure and target variable
- analyze missing values and feature types
- explore key numerical and categorical variables
- compare grouped default rates
- summarize a clear high-risk customer profile from a credit-risk perspective

## Main Notebook

- [home_credit_risk_analysis.ipynb](./home_credit_risk_analysis.ipynb)

## Current Scope

The analysis currently focuses on:

- `application_train.csv`
- `HomeCredit_columns_description.csv`

Key variables discussed in the notebook include:

- `AMT_INCOME_TOTAL`
- `AMT_CREDIT`
- `AMT_ANNUITY`
- `ANNUITY_INCOME_RATIO`
- `NAME_INCOME_TYPE`
- `NAME_EDUCATION_TYPE`
- `NAME_FAMILY_STATUS`
- `NAME_HOUSING_TYPE`

## Main Findings

- The target is imbalanced, with high-risk customers forming a minority of the sample.
- Some housing-related features have high missingness and should be interpreted carefully.
- Absolute income, credit amount, and annuity provide some signal, but their standalone explanatory power is limited.
- `ANNUITY_INCOME_RATIO` is more informative because it captures repayment burden relative to income.
- Education level, income source, family status, and housing type all show meaningful differences in default risk.

## Dataset Note

The raw Kaggle CSV files are large, so they are not intended to be uploaded to GitHub with this project.

If you want to run the notebook locally, place the required dataset files in this folder:

- `application_train.csv`
- `HomeCredit_columns_description.csv`

You can download the full dataset from the Kaggle Home Credit Default Risk competition page.

## Project Style

This notebook is designed as a learning project:

- beginner-friendly
- analysis-first
- focused on explanation and business interpretation
- not optimized for leaderboard performance
