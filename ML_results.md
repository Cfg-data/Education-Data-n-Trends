# Machine Learning Results and Usage

## ML Models using scikit-learn

### Classification Models:

- **Logistic Regression**  
  `sklearn.linear_model.LogisticRegression`
  
- **K-Nearest Neighbors (KNN)**  
  `sklearn.neighbors.KNeighborsClassifier`
  
- **Support Vector Machine (SVM) - Classification**  
  `sklearn.svm.SVC`
  
- **Naive Bayes Classifiers**  
  - `GaussianNB`: `sklearn.naive_bayes.GaussianNB`  
  - `MultinomialNB`: `sklearn.naive_bayes.MultinomialNB`  
  - `BernoulliNB`: `sklearn.naive_bayes.BernoulliNB`
  
- **Decision Trees**  
  `sklearn.tree.DecisionTreeClassifier`
  
- **Random Forest Classifier**  
  `sklearn.ensemble.RandomForestClassifier`
  
- **Gradient Boosting Classifier**  
  `sklearn.ensemble.GradientBoostingClassifier`
  
- **AdaBoost Classifier**  
  `sklearn.ensemble.AdaBoostClassifier`
  
- **Linear Discriminant Analysis (LDA)**  
  `sklearn.discriminant_analysis.LinearDiscriminantAnalysis`
  
- **Quadratic Discriminant Analysis (QDA)**  
  `sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis`
  
- **Extra Trees Classifier**  
  `sklearn.ensemble.ExtraTreesClassifier`

### Regression Models:

- **Linear Regression**  
  `sklearn.linear_model.LinearRegression`
  
- **Ridge Regression**  
  `sklearn.linear_model.Ridge`
  
- **Lasso Regression**  
  `sklearn.linear_model.Lasso`
  
- **ElasticNet Regression**  
  `sklearn.linear_model.ElasticNet`
  
- **K-Nearest Neighbors (KNN) - Regression**  
  `sklearn.neighbors.KNeighborsRegressor`
  
- **Support Vector Machine (SVM) - Regression**  
  `sklearn.svm.SVR`
  
- **Decision Trees - Regression**  
  `sklearn.tree.DecisionTreeRegressor`
  
- **Random Forest Regressor**  
  `sklearn.ensemble.RandomForestRegressor`
  
- **Gradient Boosting Regressor**  
  `sklearn.ensemble.GradientBoostingRegressor`
  
- **AdaBoost Regressor**  
  `sklearn.ensemble.AdaBoostRegressor`
  
- **Linear Support Vector Regressor**  
  `sklearn.svm.SVR`
  
- **Extra Trees Regressor**  
  `sklearn.ensemble.ExtraTreesRegressor`
  
- **Huber Regressor**  
  `sklearn.linear_model.HuberRegressor`

### Other Models:

- **Bayesian Ridge Regression**  
  `sklearn.linear_model.BayesianRidge`
  
- **RANSAC Regressor**  
  `sklearn.linear_model.RANSACRegressor`

---

## First Tests Using KNN

## KNN Classifier:

#### Train-test split: 50 / 50  
- KNN Classifier Accuracy (MinMaxScaler): 35.71%  
- KNN Classifier Accuracy (StandardScaler): 28.57%

#### Train-test split: 60 / 40  
- KNN Classifier Accuracy (MinMaxScaler): 46.67%  
- KNN Classifier Accuracy (StandardScaler): 35.56%

#### Train-test split: 70 / 30  
- KNN Classifier Accuracy (MinMaxScaler): 52.94%  
- KNN Classifier Accuracy (StandardScaler): 38.24%

#### Train-test split: 80 / 19  
- KNN Classifier Accuracy (MinMaxScaler): 30.43%  
- KNN Classifier Accuracy (StandardScaler): 26.09%

---

## KNN Regressor:

#### Train-test split: 50 / 50  
- KNN Regressor MSE (MinMaxScaler): 16.97  
- KNN Regressor MSE (StandardScaler): 17.07

#### Train-test split: 60 / 40  
- KNN Regressor MSE (MinMaxScaler): 17.93  
- KNN Regressor MSE (StandardScaler): 16.68

#### Train-test split: 70 / 30  
- KNN Regressor MSE (MinMaxScaler): 19.39  
- KNN Regressor MSE (StandardScaler): 19.42

#### Train-test split: 80 / 19  
- KNN Regressor MSE (MinMaxScaler): 24.90  
- KNN Regressor MSE (StandardScaler): 24.75

## **KNN Classifier - Performance**

### **Train-Test Split: 70/30 (Best Split)**
- **Scaler Used**: MinMaxScaler
- **KNN Classifier Accuracy**: 52.94%

### **Classification Report:**
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 2005  | 0.67      | 0.50   | 0.57     | 8       |
| 2010  | 0.47      | 0.70   | 0.56     | 10      |
| 2015  | 0.67      | 0.33   | 0.44     | 12      |
| 2021  | 1.00      | 0.67   | 0.80     | 3       |
| 2022  | 0.20      | 1.00   | 0.33     | 1       |

- **Overall Accuracy**: 53%
- **Macro Average**: 
  - Precision: 0.60
  - Recall: 0.64
  - F1-Score: 0.54
- **Weighted Average**: 
  - Precision: 0.62
  - Recall: 0.53
  - F1-Score: 0.54

---

## **KNN Regressor - Performance**

### **Train-Test Split: 60/40 (Best Split)**
- **Scaler Used**: StandardScaler
- **KNN Regressor Mean Squared Error**: 16.68
- **KNN Regressor Mean Absolute Error**: 3.14
- **KNN Regressor R-Squared**: 0.34
- **Accuracy (within tolerance of 0.1)**: 2.22%

---

### KNN Classifier:

#### KNN Classifier with StandardScaler - Classification Report:
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 8     | 0.00      | 0.00   | 0.00     | 0       |
| 40    | 0.00      | 0.00   | 0.00     | 2       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 112   | 0.00      | 0.00   | 0.00     | 0       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.20      | 1.00   | 0.33     | 1       |
| 196   | 0.33      | 1.00   | 0.50     | 1       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 276   | 0.00      | 0.00   | 0.00     | 0       |
| 344   | 1.00      | 1.00   | 1.00     | 1       |
| 348   | 0.00      | 0.00   | 0.00     | 1       |
| 352   | 1.00      | 1.00   | 1.00     | 1       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 410   | 0.00      | 0.00   | 0.00     | 1       |
| 428   | 0.00      | 0.00   | 0.00     | 0       |
| 440   | 0.00      | 0.00   | 0.00     | 2       |
| 446   | 0.00      | 0.00   | 0.00     | 1       |
| 484   | 0.00      | 0.00   | 0.00     | 2       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 0.00      | 0.00   | 0.00     | 3       |
| 642   | 0.00      | 0.00   | 0.00     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 703   | 0.00      | 0.00   | 0.00     | 2       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.00      | 0.00   | 0.00     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |

- **Accuracy**: 14.71%
- **Macro Average**:
  - Precision: 0.11
  - Recall: 0.16
  - F1-Score: 0.12
- **Weighted Average**:
  - Precision: 0.10
  - Recall: 0.15
  - F1-Score: 0.11

#### KNN Classifier with MinMaxScaler - Classification Report:
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 40    | 0.00      | 0.00   | 0.00     | 2       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 112   | 0.00      | 0.00   | 0.00     | 0       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.00      | 0.00   | 0.00     | 1       |
| 196   | 1.00      | 1.00   | 1.00     | 1       |
| 203   | 0.00      | 0.00   | 0.00     | 0       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 344   | 0.00      | 0.00   | 0.00     | 1       |
| 348   | 0.00      | 0.00   | 0.00     | 1       |
| 352   | 1.00      | 1.00   | 1.00     | 1       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 410   | 0.00      | 0.00   | 0.00     | 1       |
| 428   | 0.00      | 0.00   | 0.00     | 0       |
| 440   | 0.00      | 0.00   | 0.00     | 2       |
| 446   | 0.00      | 0.00   | 0.00     | 1       |
| 484   | 0.00      | 0.00   | 0.00     | 2       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 554   | 0.00      | 0.00   | 0.00     | 0       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 0.00      | 0.00   | 0.00     | 3       |
| 642   | 0.00      | 0.00   | 0.00     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 703   | 0.00      | 0.00   | 0.00     | 2       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.00      | 0.00   | 0.00     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |

- **Accuracy**: 8.82%
- **Macro Average**:
  - Precision: 0.09
  - Recall: 0.09
  - F1-Score: 0.09
- **Weighted Average**:
  - Precision: 0.09
  - Recall: 0.09
  - F1-Score: 0.09

---

### KNN Regressor:

#### KNN Regressor with StandardScaler - Report:
- **Mean Squared Error (MSE)**: 16.68
- **Mean Absolute Error (MAE)**: 3.14
- **R-squared**: 0.34
- **Accuracy (within tolerance of 0.1)**: 2.22%

#### KNN Regressor with MinMaxScaler - Report:
- **Mean Squared Error (MSE)**: 17.93
- **Mean Absolute Error (MAE)**: 3.32
- **R-squared**: 0.29
- **Accuracy (within tolerance of 0.1)**: 2.22%

---

# Hyperparameter Tuning Results

## KNN Classifier with StandardScaler

### Best Hyperparameters:
- **Metric:** Manhattan
- **n_neighbors:** 5
- **Weights:** Distance

### Classification Report:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 8     | 0.00      | 0.00   | 0.00     | 1       |
| 40    | 0.00      | 0.00   | 0.00     | 3       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.00      | 0.00   | 0.00     | 1       |
| 196   | 0.00      | 0.00   | 0.00     | 2       |
| 203   | 0.00      | 0.00   | 0.00     | 1       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 268   | 0.00      | 0.00   | 0.00     | 1       |
| 276   | 0.00      | 0.00   | 0.00     | 1       |
| 344   | 0.00      | 0.00   | 0.00     | 1       |
| 348   | 1.00      | 1.00   | 1.00     | 1       |
| 352   | 1.00      | 1.00   | 1.00     | 2       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 392   | 0.00      | 0.00   | 0.00     | 0       |
| 410   | 0.50      | 1.00   | 0.67     | 1       |
| 428   | 0.50      | 1.00   | 0.67     | 1       |
| 440   | 0.00      | 0.00   | 0.00     | 3       |
| 446   | 0.00      | 0.00   | 0.00     | 2       |
| 470   | 0.00      | 0.00   | 0.00     | 0       |
| 484   | 0.00      | 0.00   | 0.00     | 2       |
| 498   | 0.00      | 0.00   | 0.00     | 0       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 554   | 0.00      | 0.00   | 0.00     | 0       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 1.00      | 0.33   | 0.50     | 3       |
| 642   | 0.00      | 0.00   | 0.00     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 688   | 0.00      | 0.00   | 0.00     | 0       |
| 703   | 0.00      | 0.00   | 0.00     | 3       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.50      | 1.00   | 0.67     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |
| 840   | 0.00      | 0.00   | 0.00     | 0       |

### Accuracy:
- **Accuracy:** 17.78%

---

## KNN Classifier with MinMaxScaler

### Best Hyperparameters:
- **Metric:** Euclidean
- **n_neighbors:** 7
- **Weights:** Distance

### Accuracy:
- **Accuracy:** 0.00% (indicating poor performance)

---

## KNN Regressor with StandardScaler

### Report:
- **Mean Squared Error (MSE):** 16.68
- **Mean Absolute Error (MAE):** 3.14
- **R-squared:** 0.34
- **Accuracy (within tolerance of 0.1):** 2.22%

---

## KNN Regressor with MinMaxScaler

### Report:
- **Mean Squared Error (MSE):** 17.93
- **Mean Absolute Error (MAE):** 3.32
- **R-squared:** 0.29
- **Accuracy (within tolerance of 0.1):** 0.00%

---

## KNN Classifier with SMOTE

### Best Hyperparameters for KNN with SMOTE:
- **Metric:** Manhattan
- **n_neighbors:** 3
- **Weights:** Distance

---

### KNN Classifier with StandardScaler and SMOTE - Classification Report:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 8     | 0.00      | 0.00   | 0.00     | 1       |
| 40    | 0.00      | 0.00   | 0.00     | 3       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 112   | 0.00      | 0.00   | 0.00     | 0       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.00      | 0.00   | 0.00     | 1       |
| 196   | 0.00      | 0.00   | 0.00     | 2       |
| 203   | 0.00      | 0.00   | 0.00     | 1       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 268   | 0.00      | 0.00   | 0.00     | 1       |
| 276   | 0.00      | 0.00   | 0.00     | 1       |
| 344   | 0.25      | 1.00   | 0.40     | 1       |
| 348   | 0.17      | 1.00   | 0.29     | 1       |
| 352   | 0.00      | 0.00   | 0.00     | 2       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 410   | 0.00      | 0.00   | 0.00     | 1       |
| 428   | 0.00      | 0.00   | 0.00     | 1       |
| 440   | 0.00      | 0.00   | 0.00     | 3       |
| 442   | 0.00      | 0.00   | 0.00     | 0       |
| 446   | 0.00      | 0.00   | 0.00     | 2       |
| 470   | 0.00      | 0.00   | 0.00     | 0       |
| 484   | 0.00      | 0.00   | 0.00     | 2       |
| 498   | 0.00      | 0.00   | 0.00     | 0       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 554   | 0.00      | 0.00   | 0.00     | 0       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 0.00      | 0.00   | 0.00     | 3       |
| 642   | 0.00      | 0.00   | 0.00     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 703   | 0.00      | 0.00   | 0.00     | 3       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.33      | 1.00   | 0.50     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |

### Accuracy:
- **Accuracy:** 8.89%

# Hyperparameter Tuning Results for KNN with RandomOverSampler

## Best Hyperparameters:
- **Metric:** Manhattan
- **n_neighbors:** 3
- **Weights:** Distance

---

## KNN Classifier with RandomOverSampler

### Classification Report:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 8     | 0.00      | 0.00   | 0.00     | 1       |
| 40    | 0.00      | 0.00   | 0.00     | 3       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.00      | 0.00   | 0.00     | 1       |
| 196   | 0.00      | 0.00   | 0.00     | 2       |
| 203   | 1.00      | 1.00   | 1.00     | 1       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 268   | 0.00      | 0.00   | 0.00     | 1       |
| 276   | 0.00      | 0.00   | 0.00     | 1       |
| 344   | 0.00      | 0.00   | 0.00     | 1       |
| 348   | 0.17      | 1.00   | 0.29     | 1       |
| 352   | 1.00      | 1.00   | 1.00     | 2       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 392   | 0.00      | 0.00   | 0.00     | 0       |
| 410   | 0.50      | 1.00   | 0.67     | 1       |
| 428   | 0.25      | 1.00   | 0.40     | 1       |
| 440   | 0.00      | 0.00   | 0.00     | 3       |
| 442   | 0.00      | 0.00   | 0.00     | 0       |
| 446   | 0.00      | 0.00   | 0.00     | 2       |
| 484   | 1.00      | 1.00   | 1.00     | 2       |
| 498   | 0.00      | 0.00   | 0.00     | 0       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 1.00      | 0.33   | 0.50     | 3       |
| 642   | 1.00      | 0.50   | 0.67     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 688   | 0.00      | 0.00   | 0.00     | 0       |
| 703   | 1.00      | 0.33   | 0.50     | 3       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.00      | 0.00   | 0.00     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |
| 840   | 0.00      | 0.00   | 0.00     | 0       |

### Accuracy:
- **Accuracy:** 26.67%

## KNN Classifier with StandardScaler

### Classification Report:
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 8     | 0.00      | 0.00   | 0.00     | 1       |
| 40    | 0.00      | 0.00   | 0.00     | 3       |
| 56    | 1.00      | 1.00   | 1.00     | 1       |
| 100   | 0.00      | 0.00   | 0.00     | 1       |
| 124   | 0.00      | 0.00   | 0.00     | 1       |
| 191   | 0.00      | 0.00   | 0.00     | 1       |
| 196   | 0.00      | 0.00   | 0.00     | 2       |
| 203   | 0.00      | 0.00   | 0.00     | 1       |
| 233   | 0.00      | 0.00   | 0.00     | 1       |
| 246   | 0.00      | 0.00   | 0.00     | 1       |
| 268   | 0.00      | 0.00   | 0.00     | 1       |
| 276   | 0.00      | 0.00   | 0.00     | 1       |
| 344   | 0.00      | 0.00   | 0.00     | 1       |
| 348   | 1.00      | 1.00   | 1.00     | 1       |
| 352   | 1.00      | 1.00   | 1.00     | 2       |
| 372   | 0.00      | 0.00   | 0.00     | 2       |
| 380   | 0.00      | 0.00   | 0.00     | 1       |
| 392   | 0.00      | 0.00   | 0.00     | 0       |
| 410   | 0.50      | 1.00   | 0.67     | 1       |
| 428   | 0.50      | 1.00   | 0.67     | 1       |
| 440   | 0.00      | 0.00   | 0.00     | 3       |
| 446   | 0.00      | 0.00   | 0.00     | 2       |
| 470   | 0.00      | 0.00   | 0.00     | 0       |
| 484   | 0.00      | 0.00   | 0.00     | 2       |
| 498   | 0.00      | 0.00   | 0.00     | 0       |
| 528   | 0.00      | 0.00   | 0.00     | 1       |
| 554   | 0.00      | 0.00   | 0.00     | 0       |
| 578   | 0.00      | 0.00   | 0.00     | 1       |
| 616   | 0.00      | 0.00   | 0.00     | 2       |
| 620   | 1.00      | 0.33   | 0.50     | 3       |
| 642   | 0.00      | 0.00   | 0.00     | 2       |
| 674   | 0.00      | 0.00   | 0.00     | 1       |
| 688   | 0.00      | 0.00   | 0.00     | 0       |
| 703   | 0.00      | 0.00   | 0.00     | 3       |
| 705   | 0.00      | 0.00   | 0.00     | 0       |
| 724   | 0.50      | 1.00   | 0.67     | 1       |
| 752   | 0.00      | 0.00   | 0.00     | 0       |
| 826   | 0.00      | 0.00   | 0.00     | 0       |
| 840   | 0.00      | 0.00   | 0.00     | 0       |

### Accuracy:
- **Accuracy:** 17.78%

### Model Performance Reports

#### Random Forest Regressor - Report:
- **Mean Squared Error (MSE):** 13.41
- **Mean Absolute Error (MAE):** 3.05
- **R-squared (R²):** 0.47
- **Accuracy (within tolerance of 0.1):** 0.00%

#### Stacked Regressor - Report:
- **Mean Squared Error (MSE):** 13.26
- **Mean Absolute Error (MAE):** 3.03
- **R-squared (R²):** 0.47
- **Accuracy (within tolerance of 0.1):** 0.00%

# **Analysis Summary**

## **KNN Classifier and Regressor Performance**

### **Classifier Performance**
- **Best Configuration**: 
  - **Train-Test Split**: 70/30
  - **Scaler**: MinMaxScaler
  - **Accuracy**: 52.94%
- **Key Observations**:
  - The **MinMaxScaler** consistently outperforms the **StandardScaler** across different splits.
  - Classification performance struggles with imbalanced classes, evident from low recall and F1-scores for many classes.
  - Certain rare classes show perfect scores due to overfitting on minority data.

### **Regressor Performance**
- **Best Configuration**:
  - **Train-Test Split**: 60/40
  - **Scaler**: StandardScaler
  - **Mean Squared Error (MSE)**: 16.68
- **Key Observations**:
  - Regression performance improves with larger training sizes, but predictive accuracy within a tight tolerance is very low.
  - **R-squared** value of 0.34 indicates moderate variance explanation, with room for improvement.

---

## **Advanced Model Comparisons**

### **Random Forest Regressor vs. Stacked Regressor**
- **Performance Metrics**:
  - Both achieve **R-squared = 0.47**, explaining 47% of variance.
  - Mean Squared Error (MSE): 13.41 (Random Forest) vs. 13.26 (Stacked Regressor).
  - Accuracy within tolerance (±0.1): 0% for both.
- **Insights**:
  - Stacked Regressor showed marginally better performance but did not significantly outperform the Random Forest.
  - Moderate performance suggests missing important features or needing more complex modeling.

---

## **Techniques for Improvement**

### **For KNN Models**:
1. **Classification**:
   - Address class imbalance using techniques like **SMOTE** or **RandomOverSampler**.
   - Optimize hyperparameters (e.g., neighbors, distance metrics).
   - Explore advanced classifiers like **Random Forests** or **Gradient Boosting**.
2. **Regression**:
   - Improve feature engineering to reduce MSE and enhance R-squared.
   - Consider alternate models like **Gradient Boosting** or **LightGBM** for better non-linear relationship modeling.

### **For Ensemble Models**:
- Optimize hyperparameters for Random Forests and Stacked Regressors (e.g., number of trees, depth).
- Experiment with diverse base models in Stacked Regressor for potential improvements.

---

## **Final Recommendations**
- For **classification**, the **70/30 split with MinMaxScaler** is optimal but requires balancing techniques to handle class imbalance effectively.
- For **regression**, the **60/40 split with StandardScaler** works best; however, switching to advanced models like Gradient Boosting may yield better results.
- Incorporate feature engineering, dimensionality reduction (e.g., PCA), and robust cross-validation to improve all models' performance.