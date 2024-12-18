# Educational Data Analysis Project

## Navigation

- [Project Overview](#project-overview)
- [Collected Datasets](#collected-datasets)
- [How to Use](#how-to-use)
- [Project Purpose](#project-purpose)
- [License](#license)
- [Folder Structure](#folder-structure)
- [Streamlit App](#streamlit-app)

---

## Project Overview

This project involves analyzing educational data collected from the United Nations Data (UNDATA). The data covers various aspects of education, including gender ratios, public expenditure, access to computers, and teaching staff in different regions and countries. The datasets provided are from the *Statistical Yearbook* and are crucial for understanding trends and disparities in global education systems.

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
1. Changing column names
2. Dropping rows with index 0 (which contained all the column names)
3. Looking for null values
4. Describing data by Region Code and Value
5. Getting all unique values
6. Filling null values with mode in the "Footnotes" column
7. Gathering further data
8. Changing and normalizing format
9. Filtering dataset for the regions needed
10. Grouping only for the years with the largest amount of data for the biggest number of countries kept
11. Repeating step 10 for the regions
12. Renaming the files
13. Loading files into a jupyter notebook, Running a correlation matrix for each variable, making sure all Nan values are filled with 0
14. Running several figures for the various variables by year, bar plots and violin plots mostly (disregarding 0 values using seaborn and plotly)

### MySQL Progress:
- Database creation in Python connector attempted but unsuccessful
- Proceeded to create database in mysql workbench directly
- Proceeding with each .csv file
- Creating a table for countries and for years separately, to relate all tables to each other
- Aggregate data from existing tables into a full table with only the chosen list of countries
- Creating a table for area 1 - total values

## License

This project is based on publicly available data from UNDATA. Please refer to the [UN Data Usage Policy](https://data.un.org/Usage.aspx) for licensing and attribution information.

## Folder Structure

The project is organized into the following folders:

- **`working_notebooks`**: Notebooks that contain work in progress and are not organized.
  - **`unused_notebooks`**
- **`usable_notebooks`**: Organized notebooks that present findings in an organized manner.
- **`data`**: Collects the data used for the project in three separate folders:
  - **`raw`**:
    - `unused_data`
      - `enrollment_data`
      - `government_expenditure`
    - `literacy_rates`
  - **`cleaned`**
  - **`merged`**
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

This app allows users to explore different aspects of the education data, run machine learning models, and analyze trends in global education. Navigation buttons within the app enable users to seamlessly switch between sections.