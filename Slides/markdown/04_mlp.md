---
marp: true
theme: micm_theme
paginate: true
---

# MLP for Tabular Medical Data
QLS–MiCM Workshop

---

## Linear vs. Logistic Regression

**Linear regression**
- predicts a *continuous* value.
- output can be any real number.
- model:
  - $\hat{y} = X\beta$


**Logistic regression**
- predicts a *probability* (0–1).
- uses the sigmoid function.
  - $\hat{p} = \sigma(X\beta)$
- ideal for classification tasks.

**Key idea:**
Logistic = linear model **passed through a probability link function**.


---

## Why Compare MLPs to Linear Models? 

Tabular data often has:

- few features.
- moderate sample size.
- mostly linear or monotonic relationships.

**Logistic regression is often hard to beat.**
MLPs help **only if** the data contain meaningful **nonlinear and/or interaction patterns**.

This exercise tests that idea.

---

## What an MLP Can Learn 

A multilayer perceptron can model:

- nonlinear boundaries.
- interactions between features.
- complex patterns missed by linear models.

But can also:

- overfit easily.
- require tuning (activation, layers, regularization).
- fail when data is simple or small.

You will explore both outcomes.

---

## The Baseline: Logistic Regression

Logistic regression is:

- linear.
- stable.
- interpretable.
- often the best model.

---

## What You Will Change in the MLP

You will experiment with:

### 🔧 **Architecture**
- number of layers `(e.g., (8,), (32,16), (100,100))`
- number of neurons.

### 🔧 **Activation Functions**
- `relu`.
- `tanh`.
- avoid `identity` for hidden layers

### 🔧 **Regularization**
- adjust `alpha`.
- understand it acts like L2 weight decay.

### 🔧 **Training Settings**
- increase `max_iter`.
- add `random_state=42`.

Goal:.
**Can you make the MLP outperform logistic regression?**

---

## How You Will Evaluate

Using `classification_report`:

- **Accuracy** - correctness.
- **Precision** - false-alarm.
- **Recall** - disease-detection.
- **F1-score** - balance of precision + recall.

Key question:.
**Does added model complexity improve clinically meaningful metrics?**

