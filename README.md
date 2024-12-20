# Educational Data Analysis Project

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App Structure](#streamlit-app-structure)

---

## Project Overview

This project involves analyzing educational data collected from the United Nations Data (UNDATA). The data covers various aspects of education, including gender ratios, public expenditure, access to computers, and teaching staff in different regions and countries. The datasets provided are from the *Statistical Yearbook* and are crucial for understanding trends and disparities in global education systems.

### Supporting Materials
- **Presentation**: [Made using Canva](https://education-data-and-trends-full.my.canva.site/)
- **Kanban Board**: [Used for organization](https://trello.com/b/JQXi189u/kanban-board-final-project)
- **Daily Task Planner Board**: [Used to keep on top of time management](https://trello.com/b/MKJuGmnZ/final-project-daily-task-planner)
- **Application**: [Created using Streamlit to present findings](https://educationstudy.streamlit.app)

# EDA Results Summary

For a detailed view of the complete EDA results, please visit [Full EDA Results](https://github.com/Cfg-data/final-project/blob/master/EDA_results.md).

---

### **1. Year**
- **Span**: 2005–2022, with an average focus year of 2012.96.
- **Context**: Concentration in high-income countries, reflecting trends shaped by events like the 2008 global financial crisis.

### **2. Region/Country/Area**
- **High-Income Coverage**: Strong data for countries like the U.S., Germany, and Japan.
- **Data Gaps**: Sparse data from Albania, Moldova, and Montenegro.
- **Frequency Leaders**: High reporting in China, U.S., India, and Russia.

### **3. Staff Compensation (% of Public Expenditure)**
- **Average**: 50.77%, higher in developed economies.
- **Outliers**: Some developing nations report 0%, indicating reporting gaps or alternative funding.

### **4. Access to Computers by Education Level**
- **Disparities**: 
  - Primary: 44.6% access.
  - Lower Secondary: 33.3%.
  - Upper Secondary: 34.1%.
- **Digital Divide**: High-income nations offer near-universal access; gaps persist in developing regions.

### **5. Capital Expenditure (% of Total Public Education Spending)**
- **Low Average**: 6.09%, with a focus on operational costs over infrastructure.
- **Regional Variance**: Higher in developed nations; limited in smaller economies.

### **6. Other Current Expenditures**
- **Average**: 17.08%, reflecting operational cost allocations outside staff compensation.

### **7. Gross Enrollment Ratios (GER)**
- **Primary and Secondary**: Near-universal GER in developed nations; challenges in developing regions.
- **Gender Trends**: Slight male advantage in early levels, with upper secondary education showing parity.

### **8. Ratio of Girls to Boys**
- **Parity**: Near-equal ratios across levels, with slight advantages for girls in upper secondary in developed regions.

### **9. Teachers by Education Level**
- **Shortages**: Noticeable in lower secondary and upper secondary levels, particularly in under-resourced areas.

### **10. Teacher Qualifications**
- **Regional Disparities**: Higher qualification standards in developed countries, with gaps in developing nations.

### **Key Trends**
1. Digital inequality persists.
2. Focus remains on operational costs over infrastructure.
3. Teacher availability and qualifications vary significantly.
4. Gender parity is largely achieved in enrollment.
5. Significant disparities exist between developed and developing regions.

# ML Results Summary

For a detailed view of the complete ML results, please visit [Full ML Results](https://github.com/Cfg-data/final-project/blob/master/ML_results.md).

## **KNN Model Performance**
### Classifier
- **Best Setup**: 70/30 split, MinMaxScaler, 52.94% accuracy.
- **Challenges**: Struggles with class imbalances, low recall and F1-scores.

### Regressor
- **Best Setup**: 60/40 split, StandardScaler, MSE of 16.68.
- **Insights**: R-squared of 0.34; improvements needed in predictive accuracy.

## **Advanced Models**
- **Random Forest vs. Stacked Regressor**:
  - Both achieve **R-squared = 0.47**.
  - **MSE**: 13.41 (Random Forest), 13.26 (Stacked Regressor).
  - Accuracy within tight tolerance: 0%.

## **Improvement Recommendations**
1. **For Classification**:
   - Address imbalances using techniques like SMOTE.
   - Explore advanced classifiers (e.g., Gradient Boosting).
2. **For Regression**:
   - Improve feature engineering and try models like LightGBM.
3. **For Ensemble Models**:
   - Optimize hyperparameters and base model diversity.

## **Final Suggestions**
- Focus on balancing datasets for classification models.
- Refine regression models with advanced methodologies and robust cross-validation.

# Policy Recommendations

**Caveat:** Mock UN recommendations created by Ceci for this project as per the analysis done.

For a detailed view of the complete Recommendations, please visit [Full Recommendations](https://github.com/Cfg-data/final-project/blob/master/recommendations_page.md).

## 1. Enhance Educational Data Reporting and Accessibility
- Standardize data collection and reporting systems across countries.
- Encourage international organizations to support low-income regions with data reporting.

## 2. Invest in Teacher Training and Professional Development
- Focus on improving teacher training, especially in developing regions.
- Promote international partnerships to share best practices and provide financial incentives for teachers.

## 3. Address the Digital Divide through Technology Investment
- Promote universal access to digital tools and infrastructure in secondary education.
- Collaborate with the private sector to support digital literacy programs.

## 4. Promote Gender Parity in Secondary and Upper Secondary Education
- Strengthen initiatives to reduce gender disparities in secondary education.
- Implement scholarships, mentorship, and gender-sensitive policies to support female students.

## 5. Address Teacher Shortages in Low-Income and Conflict-Affected Regions
- Increase teacher recruitment and professional development in underserved areas.
- Provide targeted support through international partnerships.

## 6. Promote Balanced Investment in Education Infrastructure
- Allocate balanced public education expenditure toward both current costs and long-term infrastructure investments.
- Urge international financial institutions to prioritize infrastructure in low- and middle-income countries.

## 7. Support Long-Term Strategic Planning for Education Systems
- Advocate for sustainable education policies focusing on teacher quality, gender equality, and infrastructure.
- Align national education plans with global frameworks such as the SDGs and Education 2030 Agenda.

## 8. Facilitate International Collaboration and Knowledge Sharing
- Foster global partnerships for knowledge exchange to address common educational challenges.
- Support multilateral platforms for sharing research and scaling successful initiatives.

## 9. Develop Targeted Programs for Vulnerable Regions
- Implement region-specific programs for areas affected by economic instability, conflict, or political challenges.
- Mobilize funding for mobile schools, digital learning platforms, and community-based education solutions.

## 10. Enhance International Investment in Education
- Urge increased financing for education in low-income and conflict-affected regions.
- Support innovative financing mechanisms like education bonds and public-private partnerships.

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

## License

This project is based on publicly available data from UNDATA. Please refer to the [UN Data Usage Policy](https://data.un.org/Usage.aspx) for licensing and attribution information.

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

---

### Presentation Construction:
1. Look at available models.
2. Narrow down search.
3. Choose a color scheme and vector theme.
4. Pick one model.
5. Start presentation.
6. Decide on a title.
7. Make notes on progress time and steps (this whole list).
8. Decide what presentation must include.
9. Plot what to say, when to say it, and where to insert the information.
10. Decide main steps.
11. Finish presentation.

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
- **`slides`**: Presentation PDF for ease of view.

## Streamlit App Structure

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