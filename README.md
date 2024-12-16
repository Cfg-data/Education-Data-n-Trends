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
  Identified as UNdata_Export_20241213_133629943 in the files.
- **[Primary Education (ISCED 1) Enrolment](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_1)**  
  Identified as UNdata_Export_20241213_133635513 in the files.
- **[Lower Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_2)**  
  Identified as UNdata_Export_20241213_133640358 in the files.
- **[Upper Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_3)**  
  Identified as UNdata_Export_20241213_133644616 in the files.
- **[Total Secondary Education Enrolment in All Programmes](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_23)**  
  Identified as UNdata_Export_20241213_133648447 in the files.
- **[Post-Secondary Non-Tertiary Education Enrolment](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_4)**  
  Identified as UNdata_Export_20241213_133652500 in the files.
- **[Enrolment in Tertiary Education (ISCED 5, 6, 7, and 8)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aE_56)**  
  Identified as UNdata_Export_20241213_133700618 in the files.
- **[Percentage of Enrolment in Pre-Primary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_0)**  
  Identified as UNdata_Export_20241213_133705713 in the files.
- **[Private Enrolment as Percentage of Total Enrolment in Primary Education](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_1)**  
  Identified as UNdata_Export_20241213_133710489 in the files.
- **[Percentage of Enrolment in Secondary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_23)**  
  Identified as UNdata_Export_20241213_133715390 in the files.
- **[Percentage of Enrolment in Tertiary Education in Private Institutions](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aPRP_56)**  
  Identified as UNdata_Export_20241213_133719900 in the files.

### Public Expenditure Data:
- **[Government Expenditure on Education as % of GDP](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXGDP_FSGOV)**  
  Identified as UNdata_Export_20241213_135417902 in the files.
- **[Government Expenditure on Education as % of Total Government Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXGOVEXP)**  
  Identified as UNdata_Export_20241213_135423189 in the files.
- **[Current Educational Expenditure in Pre-primary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC0TO)**  
  Identified as UNdata_Export_20241213_135427611 in the files.
- **[Current Educational Expenditure in Lower Secondary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC2TO)**  
  Identified as UNdata_Export_20241213_135432370 in the files.
- **[Current Educational Expenditure in Upper Secondary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC3TO)**  
  Identified as UNdata_Export_20241213_135440652 in the files.
- **[Current Educational Expenditure in Post Secondary Non-Tertiary as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_EC4TO)**  
  Identified as UNdata_Export_20241213_135445396 in the files.
- **[Current Educational Expenditure in Not Allocated by Level as % of Total Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aED_ECNTO)**  
  Identified as UNdata_Export_20241213_135449826 in the files.
- **[Public Current Educational Expenditure in Primary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_1_FSGOV_FNCUR_FFD)**  
  Identified as UNdata_Export_20241213_135453818 in the files.
- **[Public Current Educational Expenditure in Secondary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_23_FSGOV_FNCUR_FFD)**  
  Identified as UNdata_Export_20241213_135458315 in the files.
- **[Public Current Educational Expenditure in Tertiary as % of Public Current Educational Expenditure](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXLEVEL_56_FSGOV_FNCUR_FFD)**  
  Identified as UNdata_Export_20241213_135502548 in the files.
- **[Government expenditure per primary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_1_FSGOV)**  
  Identified as UNdata_Export_20241213_140220131 in the files.
- **[Government expenditure per secondary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_23_FSGOV)**  
  Identified as UNdata_Export_20241213_140228086 in the files.
- **[Government expenditure per tertiary student as % of GDP per capita (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aXUNIT_GDPCAP_56_FSGOV)**  
  Identified as UNdata_Export_20241213_140233366 in the files.

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