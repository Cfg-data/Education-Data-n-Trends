# pages/ml_results.py

import streamlit as st

def show(model_results, feature_importance=None):
    # ML Models using scikit-learn Section
    st.write("### ML Models using scikit-learn")

    st.write("""
    #### Classification Models:

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
    
    #### Regression Models:

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

    #### Other Models:

    - **Bayesian Ridge Regression**  
      `sklearn.linear_model.BayesianRidge`
  
    - **RANSAC Regressor**  
      `sklearn.linear_model.RANSACRegressor`
    """)

    # First Tests Using KNN Section
    st.write("### First Tests Using KNN")

    st.write("""
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

    ### Best performance for Classifier:
    - The **70/30 split with MinMaxScaler** (52.94% accuracy) yields the highest accuracy, suggesting this is the best balance between having enough data for training and testing.
    - **MinMaxScaler** consistently performs better than **StandardScaler**, especially as the training size increases.

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

    ### Best performance for Regressor:
    - The **60/40 split with StandardScaler** (MSE = 16.68) gives the lowest MSE, suggesting the best performance for regression tasks.
    - **StandardScaler** tends to give better results than **MinMaxScaler**, especially when the train-test split is 60/40.

    ---

    ## Summary:
    - For **classification tasks**, the **70/30 split with MinMaxScaler** is optimal.
    - For **regression tasks**, the **60/40 split with StandardScaler** offers the best performance.
    """)

    # KNN Model Evaluation Results Section
    st.write("### KNN Model Evaluation Results")

    st.write("""
    ## KNN Classifier - Performance

    ### Train-Test Split: 70/30 (Best Split)
    - Scaler Used: MinMaxScaler
    - Accuracy: 52.94%

    #### Classification Report:
    | Class | Precision | Recall | F1-Score | Support |
    |-------|-----------|--------|----------|---------|
    | 2005  | 0.67      | 0.50   | 0.57     | 8       |
    | 2010  | 0.47      | 0.70   | 0.56     | 10      |
    | 2015  | 0.67      | 0.33   | 0.44     | 12      |
    | 2021  | 1.00      | 0.67   | 0.80     | 3       |
    | 2022  | 0.20      | 1.00   | 0.33     | 1       |

    Overall Accuracy: 53%
    Macro Average: 
    - Precision: 0.60
    - Recall: 0.64
    - F1-Score: 0.54
    Weighted Average: 
    - Precision: 0.62
    - Recall: 0.53
    - F1-Score: 0.54

    ### Interpretation:
    - The **KNN Classifier** shows mixed performance across different classes. While it performs well for certain classes like 2021 (perfect precision of 1.00), its recall for others, particularly 2015, is low.
    - The overall accuracy is 53%, showing improvement over earlier splits.
    - Model refinement is needed through tuning hyperparameters or handling class imbalance.

    ---

    ## KNN Regressor - Performance

    ### Train-Test Split: 60/40 (Best Split)
    - Scaler Used: StandardScaler
    - Mean Squared Error: 16.68
    - Mean Absolute Error: 3.14
    - R-Squared: 0.34

    ### Interpretation:
    - MSE of 16.68 suggests moderate prediction errors.
    - R-Squared value of 0.34 indicates the model explains 34% of the variance in the data.
    - Further tuning can improve accuracy and reduce error.

    ---

    ## Recommendations:
    - **Classification Tasks**: Use **70/30 split with MinMaxScaler**.
    - **Regression Tasks**: Use **60/40 split with StandardScaler**.
    - Focus on advanced techniques like SMOTE for class imbalance and explore alternative models like Gradient Boosting for regression.
    """)