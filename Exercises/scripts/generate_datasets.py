#!/usr/bin/env python3
"""
Generate synthetic medical tabular datasets for the MiCM supervised ML workshop.
Writes CSV files into Exercises/data/.

Datasets:
- bp.csv
- omics.csv
- drug_response.csv
- cvd.csv
- clinical_risk.csv
"""

import os
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def generate_bp(n=200, random_state=0):
    rng = np.random.default_rng(random_state)
    age = rng.normal(50, 10, n)
    bmi = rng.normal(27, 4, n)
    sodium = rng.normal(3, 0.8, n)
    weight = bmi * 1.8 + rng.normal(0, 5, n)
    sbp = 90 + 0.5 * age + 1.8 * bmi + 4 * sodium + rng.normal(0, 5, n)
    df = pd.DataFrame(
        {
            "age": age,
            "bmi": bmi,
            "sodium": sodium,
            "weight": weight,
            "sbp": sbp,
        }
    )
    return df


def generate_omics(n_samples=80, n_features=300, n_informative=10, random_state=0):
    X, y, coef = make_regression(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=n_informative,
        noise=10.0,
        coef=True,
        random_state=random_state,
    )
    cols = [f"gene_{i}" for i in range(n_features)]
    df = pd.DataFrame(X, columns=cols)
    df["inflammation_index"] = y
    return df


def generate_drug_response(n=150, random_state=0):
    rng = np.random.default_rng(random_state)
    dose = np.linspace(0, 10, n)
    effect = 50 / (1 + np.exp(-(dose - 5))) + rng.normal(0, 2, n)
    df = pd.DataFrame({"dose": dose, "effect": effect})
    return df


def generate_cvd(n=400, random_state=0):
    rng = np.random.default_rng(random_state)
    age = rng.normal(50, 12, n)
    chol = rng.normal(200, 30, n)
    bp = rng.normal(120, 15, n)
    logit = (
        -10
        + 0.05 * age
        + 0.03 * (chol - 180)
        + 0.04 * (bp - 120)
        + 0.001 * (chol - 200) * (bp - 120)
    )
    prob = 1 / (1 + np.exp(-logit))
    y = rng.binomial(1, prob)
    df = pd.DataFrame({"age": age, "chol": chol, "bp": bp, "CVD": y})
    return df


def generate_clinical_risk(n=500, random_state=0):
    rng = np.random.default_rng(random_state)
    age = rng.normal(45, 12, n)
    bmi = rng.normal(28, 6, n)
    glucose = rng.normal(100, 25, n)
    bp = rng.normal(120, 15, n)
    sex = rng.choice(["M", "F"], n)
    logit = (
        -12
        + 0.06 * age
        + 0.05 * bmi
        + 0.07 * (glucose - 100)
        + 0.02 * (bmi * glucose / 100)
    )
    prob = 1 / (1 + np.exp(-logit))
    y = rng.binomial(1, prob)
    df = pd.DataFrame(
        {
            "age": age,
            "bmi": bmi,
            "glucose": glucose,
            "bp": bp,
            "sex": sex,
            "diabetes": y,
        }
    )
    return df


def main():
    ensure_data_dir()

    bp = generate_bp()
    bp.to_csv(os.path.join(DATA_DIR, "bp.csv"), index=False)

    omics = generate_omics()
    omics.to_csv(os.path.join(DATA_DIR, "omics.csv"), index=False)

    drug = generate_drug_response()
    drug.to_csv(os.path.join(DATA_DIR, "drug_response.csv"), index=False)

    cvd = generate_cvd()
    cvd.to_csv(os.path.join(DATA_DIR, "cvd.csv"), index=False)

    cr = generate_clinical_risk()
    cr.to_csv(os.path.join(DATA_DIR, "clinical_risk.csv"), index=False)

    print("Datasets generated in:", DATA_DIR)


if __name__ == "__main__":
    main()
