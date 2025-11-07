# McGill Initiative in Computational Medicine
## Introduction to Supervised Machine Learning (Tabular Data)

This repository contains the full materials for the MiCM Workshop: Introduction to Supervised Machine Learning, designed to teach fundamental supervised learning concepts through hands-on, medically themed exercises (simulated) using tabular data.

## Workshop Overview
**Audience:** Researchers, trainees, students interested in supervised learning  
**Duration:** ~4 hours + breaks  
**Focus:** Regression, classification, regularization, nonlinearity, and MLPs for medical tabular data  
**Tools:** Python, pandas, scikit-learn, and matplotlib  

The workshop consists of:
- Guided exercises implemented in Jupyter notebooks  
- Synthetic medical datasets that simulate realistic relationships  
- A final mini-hackathon applying all learned concepts  

## Repository Structure
```
QLS-MiCM_Introduction_to_supervised_machine_learning-main/
│
├── Outline/
│   └── workshop_outline.md
│
├── Slides/
│   ├── 00_intro.md
│   ├── 01_linear_regression.md
│   ├── 02_regularization.md
│   ├── 03_nonlinearity.md
│   ├── 04_mlp.md
│   ├── 05_training_eval.md
│   └── 06_hackathon.md
│
└── Exercises/
    ├── data/
    ├── scripts/
    │   └── generate_datasets.py
    ├── workshop_utils.py
    └── notebooks/
        ├── 00_intro_and_data_exploration.ipynb
        ├── 01_linear_regression_medical.ipynb
        ├── 02_regularization_high_dim_medical.ipynb
        ├── 03_feature_engineering_and_nonlinearity.ipynb
        ├── 04_mlp_for_tabular_medical.ipynb
        ├── 05_training_mechanics_and_eval.ipynb
        └── 06_hackathon_template.ipynb
```

## Installation and Setup
### 1. Clone or Download
```bash
git clone https://github.com/<your-org>/QLS-MiCM_Introduction_to_supervised_machine_learning.git
cd QLS-MiCM_Introduction_to_supervised_machine_learning-main
```

### 2. Create Environment
**Using conda:**
```bash
conda create -n micm-ml python=3.10 -y
conda activate micm-ml
```
**Using venv:**
```bash
python -m venv micm-ml
source micm-ml/bin/activate  # Windows: micm-ml\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Datasets
```bash
cd Exercises/scripts
python generate_datasets.py
```

This creates five datasets inside `Exercises/data/`.

### 5. Launch Jupyter
```bash
jupyter lab
```
or
```bash
jupyter notebook
```

Then open the notebooks in `Exercises/notebooks/`.

## Dependencies
See `requirements.txt` for exact versions.  
Core dependencies include:
- numpy
- pandas
- scikit-learn
- matplotlib
- jupyter

## License
This material is for educational purposes within the McGill Initiative in Computational Medicine (MiCM).

## Generative AI declaration
Generative AI (ChatGPT5) was used in the making of this workshop. All tutorials and text have been human validated / adjusted, primarily adding structure to the content.
