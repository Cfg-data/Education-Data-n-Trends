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