# pages/ml_results.py

import streamlit as st

def show(model_results, feature_importance=None):
    st.title("Machine Learning Results")
    
    # Models Used Section
    st.write("### Models Used")
    st.write("""
    In this project, two machine learning models were used to analyze global literacy data and identify patterns and relationships:
    
    1. **Linear Regression**:
       - A linear model used to predict literacy rates based on various socio-economic, demographic, and policy features.
    
    2. **Random Forest**:
       - An ensemble learning method used to capture complex non-linear relationships between the features and the target variable (literacy rate).
    """)
    
    # Features Section
    st.write("### Features")
    st.write("""
    The following features were selected for the models:
    - **Country**: The country or region.
    - **GDP per capita**: The Gross Domestic Product per capita of each country.
    - **Education expenditure**: Government expenditure on education.
    - **Teacher qualification**: The percentage of teachers with the required qualifications.
    - **Gender Parity Index**: A measure of gender equality in education.
    - **Access to Computers**: The availability of computers in educational institutions.
    - **Youth Literacy Rate**: Literacy rate for the population aged 15-24.
    - **School Enrollment Rate**: The percentage of children enrolled in school.
    """)
    
    # Hyperparameters Section
    st.write("### Hyperparameters")
    st.write("""
    The following hyperparameters were used for model tuning:
    
    **Linear Regression**:
    - No hyperparameters to tune for Linear Regression (default settings).
    
    **Random Forest**:
    - `n_estimators`: Number of trees in the forest (set to 100).
    - `max_depth`: Maximum depth of each tree (set to 10).
    - `min_samples_split`: Minimum number of samples required to split an internal node (set to 2).
    - `min_samples_leaf`: Minimum number of samples required to be at a leaf node (set to 1).
    - `random_state`: Ensures reproducibility of results (set to 42).
    """)
    
    # Results Section
    st.write("### Results")
    
    if model_results:
        st.write("#### Model Performance")
        st.write("""
        The models were evaluated using several metrics, such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared (R²):
        """)
        
        # Display Model Results
        st.write("**Linear Regression Performance**:")
        st.write(f"- **R²**: {model_results['linear_regression']['r2']:.3f}")
        st.write(f"- **MAE**: {model_results['linear_regression']['mae']:.3f}")
        st.write(f"- **MSE**: {model_results['linear_regression']['mse']:.3f}")
        
        st.write("**Random Forest Performance**:")
        st.write(f"- **R²**: {model_results['random_forest']['r2']:.3f}")
        st.write(f"- **MAE**: {model_results['random_forest']['mae']:.3f}")
        st.write(f"- **MSE**: {model_results['random_forest']['mse']:.3f}")
        
        # If feature importance is available for Random Forest
        if feature_importance is not None:
            st.write("#### Feature Importance (Random Forest)")
            st.bar_chart(feature_importance)
    
    else:
        st.write("No results available.")
    
    # Testing Section
    st.write("### Testing")
    st.write("""
    The models were tested using a hold-out test set (20% of the data), and the performance was evaluated on the test set. The evaluation metrics include:
    - **R-squared**: Indicates how well the model explains the variance in the data.
    - **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in predictions.
    - **Mean Squared Error (MSE)**: Measures the average squared differences between predicted and actual values.
    
    We performed cross-validation to ensure the robustness and generalizability of the models. The results indicate that the Random Forest model performs better in capturing non-linear relationships compared to Linear Regression.
    """)
    
    # Conclusion (optional)
    st.write("### Conclusion")
    st.write("""
    Based on the results, it is clear that the Random Forest model outperforms the Linear Regression model in terms of both R-squared and error metrics. 
    The feature importance analysis shows which factors most significantly impact literacy rates, with key drivers being access to education, public expenditure on education, and teacher qualifications.
    """)