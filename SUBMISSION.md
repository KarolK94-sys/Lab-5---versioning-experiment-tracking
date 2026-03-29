# Lab 5 - Data Versioning & Experiment Tracking - SUBMISSION

## Overview
This submission contains the completed Lab 5 for the MLOps course at AGH. The lab focuses on:
1. **Data Versioning** using DVC (Data Version Control)
2. **Experiment Tracking** using MLflow
3. **Reproducibility** through Git + DVC + MLflow integration

## Completion Status: ✅ COMPLETE

All exercises and tasks have been successfully completed and documented.

---

## Lab 5 Part 1: Data Versioning (DVC)

### Completed Tasks:
- ✅ DVC initialization in Git repository
- ✅ Dataset download (Ames housing 2006-2008 data)
- ✅ Data tracking with `dvc add`
- ✅ Remote storage configuration (local_remote)
- ✅ **Exercise 1**: DVC remote setup, .gitignore configuration
- ✅ **Exercise 2**: Data cleaning pipeline with version tracking
- ✅ Data versioning demonstration (rollback capabilities)

### Key Files:
- `data/ames_data_2006_2008.parquet.dvc` - DVC tracking metadata
- `data/ames_description.txt.dvc` - Data description tracking
- `.dvc/config` - DVC remote configuration
- `remote_data/` - Local remote storage

### Results:
- Raw dataset: 186.5 KB
- Tracked datasets: 2 versions (original + cleaned)
- Remote storage: Successfully synchronized
- Git history: Clean with descriptive commits

---

## Lab 5 Part 2: Experiment Tracking (MLflow)

### Completed Tasks:
- ✅ MLflow server setup
- ✅ **Exercise 1**: Scikit-learn autologging
  - 5 models trained and logged automatically
  - Models: Ridge, Decision Tree, KNN, Random Forest, Gradient Boosting
  - Best model: Gradient Boosting (R² = 0.899)

- ✅ **Exercise 2**: PyTorch manual logging
  - Neural network with 5-fold cross-validation
  - DVC metadata integration
  - Manual metric logging (RMSE, MAE, R², CV scores)
  - Configuration management with dict merging

### Exercise Analysis:

#### Exercise 1: Scikit-learn Autologging Results
```
Model Rankings by Test R² Score:
1. Gradient Boosting    R² = 0.899  RMSE = $24,001   MAE = $15,253  ⭐ BEST
2. Random Forest        R² = 0.875  RMSE = $26,708   MAE = $16,202
3. Ridge Regression     R² = 0.828  RMSE = $31,348   MAE = $17,303
4. K-Nearest Neighbors  R² = 0.747  RMSE = $37,972   MAE = $25,638
5. Decision Tree        R² = 0.682  RMSE = $42,569   MAE = $25,638
```

**Key Insights:**
- Gradient Boosting shows best generalization
- Linear model (Ridge) outperforms simple trees
- Tree-based ensemble methods dominate
- MLflow autologging captured all metrics automatically

#### Exercise 2: PyTorch Manual Logging Results
```
Model: PyTorch Neural Network
Architecture: 2 hidden layers (128 units), Dropout 0.1
Test Set Performance:
  - R² Score: 0.725
  - RMSE: $39,641.82
  - MAE: $20,857.78

Cross-Validation Performance (5-folds):
  - R² Mean: 0.642 ± 0.203
  - Fold 1: R² = 0.706
  - Fold 2: R² = 0.856 (best)
  - Fold 3: R² = 0.320 (problematic)
  - Fold 4: R² = 0.505
  - Fold 5: R² = 0.824

DVC Integration:
  - Data hash: 7f045b7f24d1af6daf02a075a188432d
  - File size: 186512 bytes
  - Logged in MLflow for reproducibility
```

**Questions Answered:**

1. **How does manual logging differ from autologging?**
   - Autologging: Automatic, requires minimal code (sklearn-specific)
   - Manual: Full control, custom training loops, framework-agnostic
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
