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

# EDA Results Summary

For a detailed view of the complete EDA results, please visit [Full EDA Results](https://github.com/Cfg-data/final-project/blob/master/EDA_results.md).

---

#### **1. Year**
The dataset spans from **2005 to 2022**, with a concentration of data points around the early 2010s (**average year: 2012.96**). The focus is on mostly high-income countries, suggesting relatively stable education systems during this period, with trends influenced by global events such as the **2008 global financial crisis**. This period likely reflects both stable educational policies and challenges caused by economic disruptions.

#### **2. Region/Country/Area**
- **High-Income Countries**: The dataset includes countries from Western Europe (e.g., Germany, France, Sweden, United Kingdom, United States) and advanced economies in Asia (e.g., Japan, Republic of Korea).
- **Data Gaps**: Some countries (e.g., Albania, Gibraltar, Montenegro, Republic of Moldova) have fewer data points, possibly due to challenges in educational reporting or lower reporting standards.
- **High Reporting Frequency**: Countries like **China** (mainland and Hong Kong), **Russia**, **India**, and the **United States** show higher data frequency, possibly reflecting better data availability and more comprehensive educational statistics systems.

#### **3. All Staff Compensation as % of Total Expenditure in Public Institutions (%)**
- **High Proportion in High-Income Countries**: The average percentage of **staff compensation** across countries is **50.77%**, which is relatively high in developed economies where teacher salaries are a large part of the education budget (e.g., **United States**, **United Kingdom**, **Germany**).
- **Wide Variation**: Some countries, particularly smaller or developing economies (e.g., **Albania**, **Republic of Moldova**), report **0%** staff compensation, which may reflect either alternative funding structures or lack of comprehensive educational expenditure reporting.

#### **4. Basic Access to Computers by Level of Education**
- **Access Gap**: The dataset shows significant disparity in **computer access** by education level:
  - **Primary Level**: 44.6% access
  - **Lower Secondary Level**: 33.3% access
  - **Upper Secondary Level**: 34.1% access
  This digital divide underscores the inequality in technology access, with high-income countries likely offering near-complete access, while others lag, particularly in **Albania** and **Moldova**.

#### **5. Capital Expenditure as % of Total Expenditure in Public Institutions (%)**
- **Low Average Capital Expenditure (6.09%)**: Many countries focus more on operational (current) expenditure rather than on capital expenditure (e.g., infrastructure). 
- **Developed Economies** like **Germany**, **France**, and **United States** are expected to have higher capital expenditure due to larger investments in educational infrastructure, while smaller or lower-income regions like **Moldova** and **Albania** allocate less.

#### **6. Current Expenditure Other Than Staff Compensation**
- **Moderate Share (17.08%)**: Current operational costs (excluding staff compensation) form a significant share of the budget in most regions. High-income countries like the **United States** and **Germany** likely have higher operational costs compared to developing countries that allocate less to infrastructure and resources.

#### **7. Gross Enrollment Ratios (GER) by Education Level**
- **High GERs in Primary and Secondary Education**: Developed countries consistently show near-universal enrollment rates, while some developing countries (e.g., **Republic of Moldova**, **Albania**) might face challenges in ensuring secondary education access for all.
- **Gender Parity**: There is a slight gender imbalance in enrollment at lower secondary and primary levels (favoring boys), but **upper secondary** education shows near-gender parity or a slight advantage for girls, especially in developed countries.

#### **8. Ratio of Girls to Boys in Education**
- **Gender Parity**: The ratio of girls to boys is close to **1** across all education levels. At **upper secondary**, there is a slight trend toward more girls enrolled, reflecting increasing opportunities and better access for girls in many developed countries like **Sweden**, **Finland**, and **Norway**.
- **Gender Imbalance in Some Regions**: Some developing countries or regions with educational disparities may still show lower female enrollment at lower secondary and primary levels.

#### **9. Teachers by Education Level**
- **Disparities in Teacher Availability**: There are significant disparities in teacher numbers across regions. Developed countries like **United States**, **Germany**, and **United Kingdom** report higher teacher availability, while smaller or developing nations (e.g., **Albania**, **Moldova**) show lower numbers, possibly due to underreporting or teacher shortages.
- **Teacher Shortages**: The low mean number of teachers at the **lower secondary** (6.63) and **upper secondary** levels (1.16) reflects a significant shortage, especially in developing regions.

#### **10. Teachers with Minimum Required Qualifications**
- **Qualified Teacher Proportion**: A relatively low percentage of teachers in some countries meet the minimum qualification standards, especially at the **secondary education** levels. This suggests challenges in teacher training, particularly in developing countries.
- **Higher Qualification Standards in Developed Countries**: Countries like **Germany**, **United States**, and **Sweden** likely have higher standards for teacher qualifications, though even in these countries, gaps exist.

---

### **Summary of Key Trends**

1. **Digital Divide**: There is a significant gap in access to computers, with high-income countries having more complete access compared to lower-income regions, particularly in **lower secondary** and **upper secondary** education.
2. **Investment Focus**: Many countries prioritize **current expenditures** (e.g., staff salaries) over **capital expenditures** (e.g., infrastructure), which may impact long-term educational development.
3. **Teacher Availability and Qualification**: Teacher shortages and qualification gaps are evident, particularly at the **secondary education levels**, with developing regions facing the most significant challenges.
4. **Gender Parity**: Generally, there is good **gender parity** in enrollment across all education levels, though females saw a decline in **upper secondary enrollment** compared to males by 2022.
5. **Geographical Inequality**: The dataset shows significant disparities between **high-income countries** and **low-income or smaller regions**. Developed countries tend to have better teacher availability, higher qualification standards, and more consistent enrollment rates.

This analysis highlights the uneven distribution of educational resources, challenges in teacher training and availability, and the ongoing issue of digital inequality in education systems worldwide.

---

### **Trends and Key Observations from Gross Enrollment Ratios (GER)**

#### **Primary Education (Female and Male)**
- **Stable Trend**: Enrollment ratios for both **female** and **male** students in **primary education** remain close to 100% from 2005 to 2022, with a slight decline.
  - **Female GER**: From 102.66% in 2005 to 97.88% in 2022.
  - **Male GER**: From 104% in 2005 to 98.36% in 2022.
- **Interpretation**: Indicates near-universal access to primary education, with a slight decline possibly linked to demographic or policy shifts.

#### **Lower Secondary Education (Female and Male)**
- **Decline in Enrollment**: Both **female** and **male** enrollment at the **lower secondary level** decreased slightly over time.
  - **Female GER**: From 105.93% in 2005 to 88.23% in 2022.
  - **Male GER**: From 105.51% in 2005 to 90.43% in 2022.
- **Interpretation**: The decline suggests challenges in maintaining secondary education enrollment, possibly due to economic, infrastructural, or policy-related factors.

#### **Upper Secondary Education (Female and Male)**
- **Significant Fluctuations**: **Upper secondary enrollment** shows sharp changes.
  - **Female GER**: Peaked at 110% in 2015, then dropped to 92.07% by 2022.
  - **Male GER**: Peaked at 108.24% in 2015, dropping to 93.64% in 2022.
- **Interpretation**: This fluctuation could reflect shifting access or economic influences affecting enrollment at the upper secondary level.

---

### **Gender Parity and Regional Insights**

- **Gender Parity**: **Gender parity** is generally maintained across primary and secondary education, with slight gender imbalances favoring **boys** at lower secondary and **males** maintaining higher enrollment in upper secondary by 2022.
- **Regional Disparities**: **Developed countries** show stable enrollment trends, while **low-income countries** face more significant challenges, particularly in **secondary and upper secondary education**.

---

### **Conclusion**

- **Primary Education**: Near-universal enrollment worldwide, though a slight decline is noted.
- **Secondary Education**: Declining enrollment at the **lower secondary** level and fluctuations at the **upper secondary** level.
- **Gender Trends**: Gender parity exists, but **female enrollment** at the upper secondary level has declined slightly relative to males by 2022.
- **Geographical Disparities**: Developed countries show robust educational systems, while regions with fewer resources struggle to maintain enrollment and teacher availability.

This dataset underscores the importance of addressing **regional disparities**, improving **teacher training**, and addressing the **digital divide** to ensure equitable access to education globally.

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App Structure](#streamlit-app-structure)

# ML Results Summary

For a detailed view of the complete ML results, please visit [Full ML Results](https://github.com/Cfg-data/final-project/blob/master/ML_results.md).

# KNN Classifier Performance:

### Train-Test Split Results:
- The KNN classifier's accuracy increases with larger training datasets, particularly when using **MinMaxScaler**.
- Best performance is observed with a **70/30 split** (52.94% accuracy).
- **MinMaxScaler** consistently outperforms **StandardScaler**, especially with larger training sets.

### Best Performance:
- The highest classifier accuracy of **52.94%** is achieved with the **70/30 split** and **MinMaxScaler**, indicating this configuration provides the best balance for classification tasks.

### Classifier Evaluation:
- The classifier's performance is mixed across different classes, with some classes (e.g., **2021**) showing good precision, while others (e.g., **2015**) have low recall.
- **Overall accuracy** is 53%, suggesting that while the model performs decently, there is room for improvement.
- Further refinements, such as **hyperparameter tuning** or addressing **class imbalances**, are needed.

---

# KNN Regressor Performance:

### Train-Test Split Results:
- The **mean squared error (MSE)** decreases slightly with larger training datasets.
- Best performance is observed with the **60/40 split** and **StandardScaler** (MSE = 16.68).
- **StandardScaler** performs slightly better than **MinMaxScaler** in terms of MSE and other error metrics.

### Best Performance:
- The lowest **MSE** of **16.68** is achieved with the **60/40 split** and **StandardScaler**, making it the best configuration for regression tasks.

### Regressor Evaluation:
- The **KNN regressor** shows a **modest R-squared value of 0.34**, indicating moderate performance.
- However, its **accuracy within a tolerance of 0.1** is low (**2.22%**), suggesting that the model’s predictions are not closely aligned with the true values within this margin.
- Improvements in **feature engineering** or **model tuning** are recommended to enhance predictive accuracy.

---

# Summary of Findings and Recommendations:

### For Classification:
- The best configuration for the **KNN classifier** is the **70/30 split** with **MinMaxScaler**, achieving the highest accuracy (**52.94%**).
- **Class imbalances** affect performance, and further improvements can be made by using techniques like **oversampling** or **tuning the model’s hyperparameters**.

### For Regression:
- The best configuration for the **KNN regressor** is the **60/40 split** with **StandardScaler**, with an **MSE** of **16.68** and an **R-squared** of **0.34**.
- The low accuracy within a tolerance of 0.1 suggests room for further improvement, potentially through **model tuning** or exploring different **regression models**.

---

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App Structure](#streamlit-app-structure)

# Final Recommendations:

### For Classification:
- Focus on improving the handling of **class imbalances** and tuning the model for better **precision** and **recall**.

### For Regression:
- Continue with the **StandardScaler** for the **KNN regressor** but explore **model refinements** and **hyperparameter tuning** to reduce error and improve accuracy.

# Policy Recommendations

**Caveat:** Mock UN recommendations created by Ceci for this project as per the analysis done.

# [Full Recommendations Page](https://github.com/Cfg-data/final-project/blob/master/recommendations_page.md)

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

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App Structure](#streamlit-app-structure)

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

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Collected Datasets](#collected-datasets)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App Structure](#streamlit-app-structure)

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

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Streamlit App Structure](#streamlit-app-structure)

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

- [Project Overview](#project-overview)
- [EDA Results Summary](#EDA-results-summary)
- [ML Results Summary](#ML-results-summary)
- [Policy Recommendations](#policy-recommendations)
- [Collected Datasets](#collected-datasets)
- [Project Progress](#project-progress)
- [License](#license)
- [Folder Structure](#folder-structure)

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