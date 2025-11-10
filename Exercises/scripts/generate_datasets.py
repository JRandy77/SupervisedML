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
    sodium = rng.normal(3, 0.8, n)             # mmol/L equivalent
    exercise_minutes = rng.normal(150, 60, n)  # minutes per week
    sex = rng.integers(0, 2, n)                # 0 = female, 1 = male

    # derived variable: weight correlated with BMI
    weight = bmi * 1.8 + rng.normal(0, 5, n)

    # base model
    sbp = (
        90
        + 0.5 * age
        + 1.8 * bmi
        + 4.0 * sodium
        - 0.05 * exercise_minutes       # protective effect: more exercise, lower BP
    )

    # interaction: stronger BMI effect for males
    sbp += 1.2 * bmi * sex

    # add noise
    sbp += rng.normal(0, 5, n)

    df = pd.DataFrame(
        {
            "age": age,
            "bmi": bmi,
            "sodium": sodium,
            "exercise_minutes": exercise_minutes,
            "weight": weight,
            "sex": sex,
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

import numpy as np
import pandas as pd
import numpy as np
import pandas as pd

def generate_cvd(
    n=1000,
    random_state=0,
    target_prevalence=0.5,
    max_iter=30,
    tol=0.01,
):
    """
    Nonlinear cardio-ish simulator that auto-tunes the intercept so the
    final prevalence is near `target_prevalence` (e.g. 0.5 for ~balanced).
    """
    rng = np.random.default_rng(random_state)

    # ---------- 1. simulate features ----------
    age = rng.normal(50, 12, n).clip(20, 90)
    chol = rng.normal(200, 30, n).clip(120, 320)
    bp = rng.normal(120, 15, n).clip(80, 200)
    bmi = rng.normal(27, 4, n).clip(16, 45)
    smoker = rng.binomial(1, 0.25, n)
    sex_male = rng.binomial(1, 0.5, n)

    # nonlinear pieces (no intercept yet)
    age_centered = (age - 50) / 10.0
    age_term = 0.4 * age_centered + 0.25 * (age_centered ** 2)
    bmi_term = 0.08 * (bmi - 27) + 0.03 * np.maximum(bmi - 32, 0)
    bp_term = 0.04 * (bp - 120)
    chol_term = 0.03 * (chol - 180) / 10.0
    interaction_term = 0.002 * (chol - 200) * (bp - 120)
    smoker_term = 0.8 * smoker + 0.3 * smoker * (age > 55)
    sex_term = 0.3 * sex_male

    base_logit = (
        age_term
        + bmi_term
        + bp_term
        + chol_term
        + interaction_term
        + smoker_term
        + sex_term
    )

    # ---------- 2. find an intercept that hits the prevalence ----------
    # simple 1D search over intercept
    low, high = -6.0, 2.0  # wide-ish range
    intercept = 0.0

    for _ in range(max_iter):
        intercept = (low + high) / 2
        prob = 1 / (1 + np.exp(-(intercept + base_logit)))
        prevalence = prob.mean()

        if abs(prevalence - target_prevalence) < tol:
            break

        if prevalence > target_prevalence:
            # too many positives -> make intercept more negative
            high = intercept
        else:
            # too few positives -> make intercept bigger
            low = intercept

    # finalize labels
    prob = 1 / (1 + np.exp(-(intercept + base_logit)))
    y = rng.binomial(1, prob)

    df = pd.DataFrame({
        "age": age,
        "chol": chol,
        "bp": bp,
        "bmi": bmi,
        "smoker": smoker,
        "sex_male": sex_male,
        "CVD": y,
    })
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
