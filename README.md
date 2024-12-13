# Educational Data Analysis Project

## Navigation

- [Project Overview](#project-overview)
- [Collected Datasets](#collected-datasets)
- [How to Use](#how-to-use)
- [Project Purpose](#project-purpose)
- [License](#license)
- [Folder Structure](#folder-structure)

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

### Enrollment Data:
- **[Pre-Primary Education (ISCED 02) Enrolment](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_0)**
- **[Primary Education (ISCED 1) Enrolment](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_1)**
- **[Lower Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_2)**
- **[Upper Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_3)**
- **[Total Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_23)**
- **[Post-Secondary Non-Tertiary Education Enrolment](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_4)**
- **[Enrolment in Tertiary Education (ISCED 5, 6, 7, and 8)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_56)**
- **[Percentage of Enrolment in Pre-Primary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_0)**
- **[Private Enrolment as Percentage of Total Enrolment in Primary Education](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_1)**
- **[Percentage of Enrolment in Secondary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_23)**
- **[Percentage of Enrolment in Tertiary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_56)**

### Public Expenditure Data:
- **[Government Expenditure on Education as % of GDP](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXGDP_FSGOV)**
- **[Government Expenditure on Education as % of Total Government Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXGOVEXP)**
- **[Current Educational Expenditure in Pre-primary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC0TO)**
- **[Current Educational Expenditure in Lower Secondary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC2TO)**
- **[Current Educational Expenditure in Upper Secondary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC3TO)**
- **[Current Educational Expenditure in Post Secondary Non-Tertiary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC4TO)**
- **[Current Educational Expenditure in Not Allocated by Level as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_ECNTO)**
- **[Public Current Educational Expenditure in Primary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_1_FSGOV_FNCUR_FFD)**
- **[Public Current Educational Expenditure in Secondary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_23_FSGOV_FNCUR_FFD)**
- **[Public Current Educational Expenditure in Tertiary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_56_FSGOV_FNCUR_FFD)**
- **[Government expenditure per primary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_1_FSGOV)**
- **[Government expenditure per secondary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_23_FSGOV)**
- **[Government expenditure per tertiary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_56_FSGOV)**

### Literacy Rates:
- **[Youth Literacy Rate, Population 15-24 Years (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24)**
- **[Youth Literacy Rate, Population 15-24 Years, Gender Parity Index (GPI)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24_GPI)**

## Project Progress

### Handling Data:
1. Changing column names
2. Dropping rows with index 0 (which contained all the column names)
3. Looking for null values
4. Describing data by Region Code and Value
5. Getting all unique values
6. Filling null values with mode in the "Footnotes" column

### MySQL Progress:
- Database creation in Python connector
- Proceeding with each .csv file
- Creating a table for area 1 - total values

## License

This project is based on publicly available data from UNDATA. Please refer to the [UN Data Usage Policy](https://data.un.org/Usage.aspx) for licensing and attribution information.

## Folder Structure

The project is organized into the following folders:

- **`working_notebooks`**: Notebooks that contain work in progress and are not organized.
- **`usable_notebooks`**: Organized notebooks that present findings in an organized manner.
- **`data`**: Collects the data used for the project in three separate folders:
  - **`raw`**:
    - `enrollment_data`
    - `government_expenditure`
    - `literacy_rates`
  - **`cleaned`**
  - **`merged`**
- **`mysql_scripts`**: Collects MySQL scripts and tables created for the project directly in MySQL Workbench.
- **`app_files`**: Contains all the files that pertain to the Streamlit app written for the project.
- **`tableau`**: Tableau visualizations created for the project in PDF form for ease of reading.
- **`slides`**: Presentation PDF for ease of view.