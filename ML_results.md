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

The accuracy for the KNN Classifier seems to improve as the train-test split gets larger (with a larger training set). The results indicate the following trend for **MinMaxScaler** and **StandardScaler**:

- **50/50 split**: 35.71% (MinMax) vs. 28.57% (StandardScaler)
- **60/40 split**: 46.67% (MinMax) vs. 35.56% (StandardScaler)
- **70/30 split**: 52.94% (MinMax) vs. 38.24% (StandardScaler)
- **80/20 split**: 30.43% (MinMax) vs. 26.09% (StandardScaler)

### Best performance for Classifier:
- The **70/30 split with MinMaxScaler** (52.94% accuracy) yields the highest accuracy, suggesting this is the best balance between having enough data for training and testing.
- **MinMaxScaler** consistently performs better than **StandardScaler**, especially as the training size increases.

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

For KNN Regressor, the mean squared error (MSE) decreases with a larger training set, with the following observations:

- **50/50 split**: 16.97 (MinMax) vs. 17.07 (StandardScaler)
- **60/40 split**: 17.93 (MinMax) vs. 16.68 (StandardScaler)
- **70/30 split**: 19.39 (MinMax) vs. 19.42 (StandardScaler)
- **80/20 split**: 24.90 (MinMax) vs. 24.75 (StandardScaler)

### Best performance for Regressor:
- The **60/40 split with StandardScaler** (MSE = 16.68) gives the lowest MSE, suggesting the best performance for regression tasks.
- **StandardScaler** tends to give better results than **MinMaxScaler**, especially when the train-test split is 60/40.

---

## Conclusion and Recommendations:

### KNN Classifier:
- **Best Train-Test Split**: 70/30 split
- **Best Scaler**: MinMaxScaler  
  The 70/30 split with **MinMaxScaler** provides the highest accuracy (52.94%), suggesting it strikes the best balance between training size and model performance for classification tasks.

### KNN Regressor:
- **Best Train-Test Split**: 60/40 split
- **Best Scaler**: StandardScaler  
  The 60/40 split with **StandardScaler** gives the lowest MSE (16.68), making it the best option for regression tasks.

---

## Summary:
- For **classification tasks**, the **70/30 split with MinMaxScaler** is optimal.
- For **regression tasks**, the **60/40 split with StandardScaler** offers the best performance.

# KNN Model Evaluation Results

## 1. **KNN Classifier - Performance**

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

### **Interpretation of Classifier Performance:**
- The **KNN Classifier** shows mixed performance across different classes, with significant imbalances in precision and recall. While it performs well for certain classes like 2021 (perfect precision of 1.00), its recall for other classes, particularly 2015, is low.
- The overall accuracy is 53%, which, while not exceptional, is an improvement over earlier attempts (35.71% with 50/50 split). The **MinMaxScaler** still outperforms the **StandardScaler**.
- The model needs further refinement, potentially through tuning hyperparameters or using more advanced techniques such as oversampling for imbalanced classes.

---

## 2. **KNN Regressor - Performance**

### **Train-Test Split: 60/40 (Best Split)**
- **Scaler Used**: StandardScaler
- **KNN Regressor Mean Squared Error**: 16.68
- **KNN Regressor Mean Absolute Error**: 3.14
- **KNN Regressor R-Squared**: 0.34
- **Accuracy (within tolerance of 0.1)**: 2.22%

### **Interpretation of Regressor Performance:**
- The **KNN Regressor** shows decent results with a Mean Squared Error (MSE) of 16.68, which suggests moderate prediction errors.
- The **R-Squared value of 0.34** indicates that the model explains about 34% of the variance in the data, which is modest. 
- The **accuracy within a tolerance of 0.1** is low at 2.22%, meaning that the predictions are not closely aligned with the true values within this margin.
- These results imply that while the regressor is functioning reasonably well, it can likely benefit from improvements such as feature engineering or tuning the model's hyperparameters to reduce error further.

---

## 3. **Summary and Conclusions**

### **KNN Classifier Results:**
- The **best train-test split** for classification tasks is **70/30** with the **MinMaxScaler**, achieving the highest accuracy of **52.94%**.
- The **classification report** shows varying performance across different classes, with precision and recall issues, particularly for certain classes like 2015 and 2022.
- Further improvements can be made with better handling of class imbalances or tuning the model.

### **KNN Regressor Results:**
- The **best train-test split** for regression tasks is **60/40** with the **StandardScaler**, achieving the lowest MSE of **16.68**.
- The **R-squared value** of **0.34** indicates that the model has a moderate ability to explain the variance, but there is room for improvement in predictive accuracy.
- The accuracy within a tolerance of 0.1 (2.22%) is very low, which suggests that further tuning and improvements are required for more accurate predictions.

### **Final Recommendations:**
- For **classification** tasks, the **70/30 split** with **MinMaxScaler** is optimal, but further class imbalance handling may be necessary to improve recall and precision for underperforming classes.
- For **regression** tasks, the **60/40 split** with **StandardScaler** should be maintained, but more tuning is needed to reduce the error metrics and increase model accuracy.

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

## Summary of Findings:

### KNN Classifier:
- **StandardScaler**: Accuracy is 14.71%, and the model struggles with most classes, particularly those with few instances. Some classes have perfect precision and recall, but these are rare and likely indicate overfitting.
- **MinMaxScaler**: Accuracy is reduced to 8.82%, indicating that MinMaxScaler does not improve the model's performance significantly. The model continues to underperform across most classes.

### KNN Regressor:
- **StandardScaler**: Shows moderate performance with a reasonable MSE of 16.68 and an R-squared of 0.34, but the accuracy within a tolerance of 0.1 is very low at 2.22%.
- **MinMaxScaler**: Performs slightly worse than StandardScaler, with a higher MSE of 17.93 and a lower R-squared of 0.29, suggesting that MinMaxScaler may not be suitable for this regression task.

### Final Recommendations:
- **For Classification**: The KNN model struggles with both StandardScaler and MinMaxScaler. Data preprocessing, such as handling class imbalance, and hyperparameter tuning are recommended for improving performance.
- **For Regression**: The KNN Regressor with StandardScaler performs slightly better than with MinMaxScaler. Further model tuning and possibly exploring alternative regression models may help achieve better results.