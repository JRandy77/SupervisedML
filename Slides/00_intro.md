---
marp: true
theme: micm_theme
paginate: true
---

# Introduction to Supervised Machine Learning

### QLS–MiCM Workshop

**Instructor:** [Your Name]  
**Duration:** 4 hours total  
**Section:** Introduction (~15 minutes)

---

## Workshop Overview

1. Introduction & Motivation  
2. Linear Regression  
3. Regularization  
4. Feature Engineering & Nonlinearity  
5. MLPs for Tabular Data  
6. Training Mechanics & Evaluation  
7. Mini Hackathon

---

## Why Machine Learning in Medicine?

- We generate **massive amounts of biomedical data**
  - Clinical measures, omics, imaging, EHRs  
- ML can:
  - **Predict** outcomes (e.g., risk, response)
  - **Identify** patterns and biomarkers
  - **Support** clinical decisions

---

## What Is Supervised Learning?

We have:
- **Features (X)** -> age, BMI, gene expression  
- **Labels (y)** -> blood pressure, disease status  

Goal:
> Learn a function that maps X -> y  
> and generalizes to unseen data

---

## Two Core Tasks

| Task | Example | Output |
|------|----------|---------|
| **Regression** | Predict blood pressure | Continuous |
| **Classification** | Predict disease yes/no | Categorical |

---

## The Supervised ML Workflow

Data -> Preprocess -> Split -> Train -> Evaluate -> Interpret




- Clean data  
- Train/test split  
- Fit model  
- Evaluate on unseen data  
- Interpret results

---

## Data–Model–Evaluation Triangle



     Data
    /   \
Model ----- Evaluation




- Data quality defines limits  
- Model choice shapes behavior  
- Evaluation builds trust

---

## Responsible ML in Biomedicine

- Watch for **bias** in datasets  
- Maintain **privacy and consent**  
- Strive for **interpretability**  

Ethics is part of technical quality.

---

## Tools for This Workshop

- **Python + Jupyter Notebooks**  
- **scikit-learn**, **pandas**, **matplotlib**  
- Example datasets: `Exercises/data/`  
- Hands-on exercises: `Exercises/notebooks/`

---

## By the End of Today

You’ll be able to:
- Explain supervised learning basics  
- Build simple regression & classification models  
- Understand regularization & nonlinearity  
- Evaluate and interpret model performance

---

## Let's Get Started 🚀

Open your notebook:  
**`00_intro_and_data_exploration.ipynb`**

We’ll explore our first dataset together!

---