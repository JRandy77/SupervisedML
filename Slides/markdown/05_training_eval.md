---
marp: true
theme: micm_theme
paginate: true
---

# Training Mechanics & Evaluation.
QLS–MiCM Workshop

---

## Why Evaluation Matters

Medical ML adds challenges:

- small datasets.
- class imbalance.
- noisy predictors.
- high stakes (false negatives matter).

**Accuracy alone is misleading.**.
We need richer, more reliable evaluation methods.

---

## Cross-Validation for Model Selection

GridSearchCV:

- splits training data into folds.
- trains several models with different hyperparameters.
- selects the model with the best mean CV performance.
- avoids tuning on the test set

Core principle:.
**Hyperparameters must be chosen using only training data.**

---

## What We Tune in This Exercise 

### 🔧 Architecture.
- `hidden_layer_sizes`: (32,), (64,), (32,16)

### 🔧 Regularization.
- `alpha` → L2 penalty controlling model complexity

### 🔧 Training Settings.
- `max_iter`.
- `random_state` (reproducibility).
- optional: `early_stopping=True` to reduce overfitting + speed up training

The goal is to observe **how each change affects test performance**.

---

## Evaluation Metrics

From `classification_report`:

- **Accuracy**.
.- overall correctness; can be misleading with imbalance.
- **Precision**.
.- among predicted positives, how many are correct?.
- **Recall (Sensitivity)**.
.- of true positives, how many were detected?.
- **F1-score**.
.- harmonic mean of precision + recall; balances both.

Medical importance:
**Low recall = missed disease cases.**

---

## ROC AUC

If the model supports probabilities:

- ROC AUC measures ranking quality.
- threshold-independent.
- widely used in medical risk assessment.

High AUC means:
**Model gives higher scores to true positives more often.**

---

## Practical Training Notes

- Use `stratify=y` in train/test split to preserve class ratios.
- Use `n_jobs=-1` to speed up grid search.
- Watch for `ConvergenceWarning` -> increase `max_iter`.
- Don’t build huge grids — slow and prone to overfitting CV folds.
