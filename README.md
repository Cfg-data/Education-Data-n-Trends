# Educational Data Analysis Project

## Navigation

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App](#streamlit-app)

---

## Project Overview

This project involves analyzing educational data collected from the United Nations Data (UNDATA). The data covers various aspects of education, including gender ratios, public expenditure, access to computers, and teaching staff in different regions and countries. The datasets provided are from the *Statistical Yearbook* and are crucial for understanding trends and disparities in global education systems.

# EDA Results Summary

For a detailed view of the complete EDA results, please visit [Full EDA Results](https://github.com/Cfg-data/final-project/blob/master/EDA_results.md).

---

## Education Trends (2005-2022)

- **Primary Education**: Enrollment ratios for both males and females were nearly universal in 2005 but have slightly declined by 2022. Both female and male enrollment ratios were close to 98%, signaling stable access to primary education.
- **Secondary Education**: Enrollment at the lower and upper secondary levels has decreased significantly over the years. The gender disparity is notable in upper secondary education, where females initially had higher enrollment but saw a sharp drop by 2022, with males having slightly higher rates by the end.
- **Regional Disparities**: Developed countries, especially in Europe and North America, generally maintained strong enrollment, while lower-income or politically unstable regions faced challenges, particularly at the secondary education level.

## Public Expenditure Insights

- **Staff Compensation**: Mexico (85.5%) and Belgium (83.6%) dedicate a significant share of their public expenditure to staff compensation, emphasizing a focus on salaries and benefits in the public sector.
- **Capital Expenditure**: Countries like Japan (13%) and Norway (12.3%) invest heavily in capital expenditures, suggesting a focus on long-term infrastructure development and public assets. Some countries like San Marino report 0% in this category, which may reflect unique expenditure patterns.
- **Current Expenditure**: Finland (32.85%) and Sweden (29.77%) allocate substantial portions of their budgets to other current expenditures, pointing to a robust funding model for public services beyond salaries.

## Regional Variations in Expenditure

- **High Expenditure on Staff Compensation**: Mexico and Belgium stand out with high percentages of public expenditure dedicated to staff compensation, indicating a larger portion of the public budget directed towards public sector employees.
- **Infrastructure Investment**: Japan and Norway prioritize capital expenditure, which indicates significant investments in public infrastructure and future development.
- **Operational Costs**: Finland, Sweden, and Romania show a larger share of spending on operational expenses beyond staff compensation, reflecting broad public service investments.

## Overall Conclusions

- **Education**: Global education trends show near-universal primary education enrollment, but secondary education faces challenges, with gender disparities increasing at the upper secondary level.
- **Public Expenditure**: The focus of public expenditure varies across regions. Countries like Mexico and Belgium emphasize staff compensation, while Japan and Norway prioritize infrastructure investment. Finland and Sweden lead in operational expenditure, ensuring robust public services.

This comprehensive comparison of education trends and public expenditure highlights diverse priorities and challenges faced by different regions, offering insights into both educational access and government spending patterns.

## Teacher Data (2005-2022) Summary

- **Primary Level Teachers**: Teacher numbers at the primary level fluctuated significantly, starting with none reported in **2005**, then sharply increasing to **48.38** by **2010**, followed by a drop to **11.64** in **2015**, and recovering to **55.42** in **2022**.
  
- **Lower Secondary Level Teachers**: Similar trends were observed at the lower secondary level, with no teachers in **2005**, an increase to **18.06** in **2010**, a drop to zero in **2015**, and a partial recovery to **13.17** in **2022**.

- **Upper Secondary Level Teachers**: No teachers were reported at the upper secondary level in **2005** and **2010**, but by **2022**, the number reached **10.75**, showing recovery.

- **Teachers with Minimum Required Qualifications**: 
  - The percentage of qualified teachers at the **primary level** increased from **18.80%** in **2005** to **52.17%** in **2022**.
  - For the **lower secondary level**, the qualification rate rose from **8.96%** in **2005** to **24.20%** in **2022**.
  - At the **upper secondary level**, the qualification rate increased from **9.10%** in **2005** to **32.92%** in **2022**, indicating progress in teacher qualification.

### Key Observations:
1. **Teacher Numbers Fluctuation**: Teacher numbers across all levels fluctuated significantly, with sharp increases around **2010**, drops in **2015**, and recovery in **2022**.
2. **Improved Qualifications**: The percentage of teachers with minimum required qualifications steadily improved across all education levels, especially at the primary and upper secondary levels.
3. **Data Gaps and Anomalies**: The lack of teachers reported in **2005** and **2010** raises questions about either data collection issues or temporary disruptions in the education system during these years.

This data highlights both progress in teacher qualifications and the instability in the number of teachers across various education levels over the years.

# ML Results Summary

For a detailed view of the complete ML results, please visit [Full ML Results](https://github.com/Cfg-data/final-project/blob/master/ML_results.md).

## First Tests Using KNN

### KNN Classifier:

The accuracy for the KNN Classifier improves as the train-test split increases, with **MinMaxScaler** consistently outperforming **StandardScaler** as the training set grows.

#### Best performance for Classifier:
- The **70/30 split with MinMaxScaler** yields the highest accuracy (52.94%), indicating the best balance between training and testing data.

---

### KNN Regressor:

For the KNN Regressor, the **mean squared error (MSE)** decreases with a larger training set, with **StandardScaler** outperforming **MinMaxScaler** in most cases.

#### Best performance for Regressor:
- The **60/40 split with StandardScaler** gives the lowest MSE (16.68), suggesting the best performance for regression tasks.

---

## Conclusion and Recommendations:

### KNN Classifier:
- **Best Train-Test Split**: 70/30 split
- **Best Scaler**: MinMaxScaler  
  The **70/30 split with MinMaxScaler** provides the highest accuracy, making it the best choice for classification tasks.

### KNN Regressor:
- **Best Train-Test Split**: 60/40 split
- **Best Scaler**: StandardScaler  
  The **60/40 split with StandardScaler** gives the lowest MSE, making it the best choice for regression tasks.

---

## Summary:
- For **classification tasks**, the **70/30 split with MinMaxScaler** is optimal.
- For **regression tasks**, the **60/40 split with StandardScaler** offers the best performance.

## Collected Datasets

The following datasets have been collected from UNDATA:

1. **[Ratio of Girls to Boys in Education](https://data.un.org/_Docs/SYB/CSV/SYB67_319_202411_Ratio%20of%20girls%20to%20boys%20in%20education.csv)**
   - Dataset ID: SYB67_319_202411
   - Description: This dataset provides the ratio of girls to boys in education across different countries and regions.

2. **[Public Expenditure on Education and Access to Computers](https://data.un.org/_Docs/SYB/CSV/SYB67_245_202411_Public%20expenditure%20on%20education%20and%20access%20to%20computers.csv)**
   - Dataset ID: SYB67_245_202411
   - Description: This dataset presents the public expenditure on education, along with data on the availability of computers in educational institutions.

3. **[Teaching Staff in Education](https://data.un.org/_Docs/SYB/CSV/SYB67_323_202411_Teaching%20Staff%20in%20education.csv)**
   - Dataset ID: SYB67_323_202411
   - Description: This dataset outlines the number of teaching staff in the education sector across various countries and regions.

4. **[Education Statistics](https://data.un.org/_Docs/SYB/CSV/SYB67_309_202411_Education.csv)**
   - Dataset ID: SYB67_309_202411
   - Description: This dataset provides a comprehensive overview of various education-related statistics, such as enrollment rates, graduation rates, and literacy rates.

## Additional Datasets

### Literacy Rates:
- **[Youth Literacy Rate, Population 15-24 Years (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24)**  
  Identified as UNdata_Export_20241213_140703208 in the files.
- **[Youth Literacy Rate, Population 15-24 Years, Gender Parity Index (GPI)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24_GPI)**  
  Identified as UNdata_Export_20241213_140708283 in the files.

## Project Progress

### Handling Data:
1. Change column names.
2. Drop rows with index 0 (which contained all the column names).
3. Look for null values.
4. Describe data by Region Code and Value.
5. Get all unique values.
6. Fill null values with mode in the "Footnotes" column.
7. Gather further data.
8. Change and normalize format.
9. Filter dataset for the regions needed.
10. Group only for the years with the largest amount of data for the largest number of countries kept.
11. Repeat step 10 for the regions.
12. Rename the files.
13. Load files into a Jupyter notebook, run a correlation matrix for each variable, making sure all NaN values are filled with 0.
14. Run several figures for the various variables by year, mostly bar plots and violin plots (disregarding 0 values using Seaborn and Plotly).

---

### Preliminary EDA:
1. Started EDA with **EDA_countries** Jupyter notebook.
2. Placed all the formatted CSV dataframes.
3. Merged dataframes.
4. Created a preliminary correlation matrix.
5. Proceeded with analysis and description of relevant columns into a summary table.
6. Output the summary table into a CSV file.
7. Created violin and box plots.
8. Made more visualizations using Seaborn and Matplotlib.
9. Created a line plot for enrollment trends.
10. Moved on to more complex EDA.

---

### Complex EDA:
(All of the relevant results are available in [Full EDA Results](https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/EDA_results.md))

1. Created a new EDA notebook: **full_analytics**.
2. Loaded only the merged CSV and checked for data types, null values, and duplicates.
3. Made a summary table and a categorical summary.
4. Plotted all the enrollment trend lines and one congregated clean plot with all of them together.
5. Made a trend table and interpreted the results.
6. Created a bar chart for staff compensation as expenditure data.
7. Created two more charts with better views of the relevant data.
8. Made a comparison of expenditure data by country (region).
9. Plotted a new correlation matrix for the countries being analyzed.
10. Created a histogram for teacher distribution by education level.
11. Made line plots for teacher distribution by level and year, and also for qualifications.
12. Created a table to iterate on the data for the analytics file.
13. Made an enrollment ratio plot.
14. Plotted a graph to detect outliers.
15. Created aggregate tables (only kept one in the file).
16. Made comparison scatter plots between expenditure and enrollment ratios, using only the aggregate data.
17. Created a missing data matrix.

---

### MySQL Progress:
1. Database creation in Python connector attempted but unsuccessful.
2. Proceeded to create the database in MySQL Workbench directly.
3. Proceeding with each .csv file.
4. Creating a table for countries and for years separately, to relate all tables to each other.
5. Aggregating data from existing tables into a full table with only the chosen list of countries.

---

### Machine Learning Models:
1. Make a list of models and run regressor and classifier versions whenever possible.
2. Decide a target variable.
3. Start running various models test by test.
4. Implement features into the models that run better.
5. Run both types of KNN.
6. Try multiple splits.
7. Get a confusion matrix.
8. Choose the splits to continue with and scaling types.
9. Apply grid search.
10. Apply SMOTE to KNN classifier.
11. Use random oversampler.
12. Use class weights.
13. Try again with KNN regressor.
14. Arrive at no conclusion.
15. Try regression ensemble models.
16. Attempt random forest regressor.
17. Attempt stacking regressor.

---

### Streamlit App Development:
1. Decide on a schematic.
2. Create a Jupyter notebook for function aggregation and to keep things organized.
3. Make the folders.
4. Start creating functions.
5. Test app.
6. Create pages.
7. Test multiple times at every step.
8. Keep proceeding with EDA.
9. Decide to make an md file to make it easier to import information into the EDA page.
10. Make an EDA page.
11. Import information in phases.
12. Test between phases.

## License

This project is based on publicly available data from UNDATA. Please refer to the [UN Data Usage Policy](https://data.un.org/Usage.aspx) for licensing and attribution information.

## Folder Structure

The project is organized into the following folders:

- **`working_notebooks`**: Notebooks that contain work in progress and are not organized.
  - **`unused_notebooks`**
- **`usable_notebooks`**: Organized notebooks that present findings in an organized manner.
  - **`correlations`**
  - **`plots`**
  - **`barfigures`**
  - **`full_analysis`**
- **`data`**: Collects the data used for the project separate folders:
  - **`raw`**:
    - `literacy_rates`
    - `unused_data`
      - `enrollment_data`
      - `government_expenditure`
  - **`cleaned`**
  - **`filtered`**
  - **`merged`**
    - `variables`
    - `years_vars`
    - `final`
- **`mysql_scripts`**: Collects MySQL scripts and tables created for the project directly in MySQL Workbench.
- **`app_files`**: Contains all the files that pertain to the Streamlit app written for the project.
- **`tableau`**: Tableau visualizations created for the project in PDF form for ease of reading.
- **`slides`**: Presentation PDF for ease of view.

## Streamlit App

The Streamlit app is structured as follows:

- **`app_files/`**: Main folder containing app-related files.
  - **`app.py`**: Main script to run the Streamlit app.
  - **`data_loader.py`**: Handles data loading and processing.
  - **`pages/`**: Contains individual pages of the app.
    - **`opener.py`**: Page that confirms data has been loaded and presents project details.
    - **`introduction.py`**: Provides project introduction and overview.
    - **`ml_results.py`**: Displays machine learning results and findings.
  - **`utils_/`**: Folder for utility functions.
    - **`display.py`**: Helper functions for displaying data.

This app allows users to explore different aspects of the education data, verify the results of the machine learning models run for the project, and analyze trends in education. Navigation buttons within the app enable users to seamlessly switch between sections.