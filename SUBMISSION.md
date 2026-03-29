# Lab 5 - Submission

Zrobiłem lab 5 o DVC i MLflow.

## Co się zrobiło

**DVC (versioning danych):**
- Pobrałem dataset z Ames housing
- Dodałem do DVC, żeby śledzić wersje
- Skonfigurował remote storage

**MLflow (experiment tracking):**
- Wytrenowałem 5 sklearn modeli (autologging)
- Wytrenowałem neural network z PyTorcha (manual logging)
- Wszystko zalogowało się automatycznie do MLflow

## Wyniki

Gradient Boosting najlepszy z R² = 0.899. Reszta modeli:
- Random Forest: 0.875
- Ridge: 0.828
- KNN: 0.747
- Decision Tree: 0.682
- PyTorch: 0.725

## Jak uruchomić

1. `uv sync` - instalacja dependencji
2. `mlflow ui --port 5001` - start MLflow serwera
3. Noteook: LAB_INSTRUCTION_2_MLFLOW.ipynb - wszystkie komórki wytrenowane

## Co jest w submisjii

- LAB_INSTRUCTION_2_MLFLOW.ipynb - notebook z wszystkim
- .gitignore - updated
- README.md - info o labie
- Kod do czyszczenia danych: ames_data_cleaning.py

Git repo: https://github.com/KarolK94-sys/Lab-5---versioning-experiment-tracking

Wszystko działa.
   - Both approaches tracked in MLflow for comparison

2. **Why use cross-validation in MLflow tracking?**
   - Assesses generalization across data folds
   - Identifies problematic subsets (Fold 3 showed R² = 0.32)
   - Provides confidence intervals (mean ± std)
   - Critical for model robustness assessment

3. **How does DVC metadata enhance experiment tracking?**
   - Creates immutable link between data version and results
   - Enables reproducibility even if data changes
   - Facilitates compliance and auditing
   - Supports team collaboration with data synchronization

4. **What could improve neural network performance?**
   - Alternative architectures (different depth/width)
   - Regularization tuning (L1/L2 vs dropout)
   - Learning rate scheduling
   - Ensemble combining sklearn + PyTorch predictions

---

## MLflow Dashboard Access

### View Experiments at: http://localhost:5001

**Navigation:**
1. **Scikit-learn Experiment**
   - Path: Experiments → `ames-housing-autolog`
   - Contains: 5 model runs with autologged parameters and metrics
   - Compare: Sort by RMSE or R² to identify best model

2. **PyTorch Experiment**
   - Path: Experiments → `pytorch-housing-manual`
   - Contains: Neural network with CV scores and DVC metadata
   - View: Training configuration and fold-wise performance

---

## How to Reproduce

### Prerequisites:
```bash
pip install uv
```

### Setup:
```bash
# 1. Clone repository
git clone https://github.com/KarolK94-sys/Lab-5---versioning-experiment-tracking.git
cd lab05

# 2. Sync dependencies
uv sync

# 3. Pull DVC data
.venv/Scripts/activate  # or source .venv/bin/activate on Linux/Mac
dvc pull

# 4. Start MLflow server (in one terminal)
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlflow-artifacts \
  --port 5001

# 5. Run notebook (in another terminal)
jupyter notebook LAB_INSTRUCTION_2_MLFLOW.ipynb
```

---

## Repository Structure

```
lab05/
├── .dvc/                              # DVC configuration
│   ├── config                         # DVC remote configuration
│   └── .gitignore                     # DVC gitignore
├── data/
│   ├── ames_data_2006_2008.parquet   # Main dataset (tracked by DVC)
│   ├── ames_data_2006_2008.parquet.dvc # DVC metadata
│   ├── ames_description.txt          # Data description
│   ├── ames_description.txt.dvc      # DVC metadata
│   └── .gitignore                    # Git ignore for data files
├── remote_data/                       # Local DVC remote storage
├── mlflow-artifacts/                  # MLflow artifacts directory
├── mlruns/                           # MLflow experiments directory
├── .gitignore                        # Git ignore rules
├── LAB_INSTRUCTION_1_DVC.md          # DVC instructions
├── LAB_INSTRUCTION_2_MLFLOW.ipynb    # ⭐ COMPLETED NOTEBOOK
├── LAB_INSTRUCTION_2_MLFLOW.md       # MLflow reference
├── ames_data_cleaning.py             # Data cleaning script
├── ames_inspect_data.py              # Data inspection script
├── pyproject.toml                    # Project dependencies
├── uv.lock                           # Locked dependencies
└── SUBMISSION.md                     # This file
```

---

## Notebook: LAB_INSTRUCTION_2_MLFLOW.ipynb

### Sections with Completed Exercises:

1. **Section 1**: MLflow Setup (Connection verification) ✅
2. **Section 2**: Data Preparation ✅
   - Dataset loading and temporal split
   - Feature engineering with proper handling of missing values
   - Training samples: 1319 | Test samples: 622 | Features: 209

3. **Section 2.2**: Scikit-learn Autologging ✅
   - 5 models trained with automatic metric logging
   - **Exercise 1 Analysis**: Results comparison and best model identification
   - Custom CV metrics logged alongside autologged parameters

4. **Section 2.3**: DVC Integration ✅
   - Reading and logging DVC metadata in MLflow
   - Data version linked to experiment for reproducibility

5. **Section 3**: PyTorch Manual Logging ✅
   - Neural network implementation with custom metrics
   - **Exercise 2 Analysis**: Detailed Q&A on manual logging vs autologging
   - 5-fold cross-validation with fold-wise performance tracking

6. **MLflow Results & Screenshots**: Documentation ✅
   - How to view experiments in MLflow dashboard
   - Expected results summary with comparison tables
   - Access instructions for results

7. **Lab Completion Summary**: ✅
   - Learning objectives achieved
   - Technical implementation details
   - Reproduction instructions
   - Lessons learned

---

## Key Technologies

- **Python 3.11.14** - Programming language
- **DVC** - Data version control
- **MLflow** - Experiment tracking
- **Git** - Source control
- **Scikit-learn 1.7.0** - Machine learning library
- **PyTorch** - Deep learning framework
- **Pandas** - Data manipulation
- **Jupyter** - Interactive notebook

---

## Validation Checklist

- ✅ All DVC exercises completed
- ✅ All MLflow exercises completed
- ✅ Code comments and markdown explanations provided
- ✅ Results analyzed and interpreted
- ✅ Questions answered comprehensively
- ✅ Git history clean with descriptive commits
- ✅ GitHub repository updated
- ✅ Fully reproducible setup instructions provided
- ✅ Notebook saved with all outputs

---

## Additional Resources

- **DVC Documentation**: https://dvc.org/doc
- **MLflow Documentation**: https://mlflow.org/docs
- **Ames Housing Dataset**: https://www.openintro.org/book/statdata/?data=ames
- **GitHub Repository**: https://github.com/KarolK94-sys/Lab-5---versioning-experiment-tracking

---

## Author

**Student**: Karol Kempski  
**Email**: karol.kempski@example.com  
**Date**: March 29, 2026  
**Course**: MLOps - AGH University

---

**Submission Ready**: All tasks completed with full documentation and analysis. ✅
