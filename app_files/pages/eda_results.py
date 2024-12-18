# pages/eda_results.py

import streamlit as st
import pandas as pd
from data_loader import load_data, load_countries

def show(data=None):
    # Title for the page
    st.title("Exploratory Data Analysis (EDA) Results")

    # Load the countries data
    countries_df = load_countries()

    # Show country data
    st.write("### Countries List")
    st.write(f"Data contains {countries_df.shape[0]} rows and {countries_df.shape[1]} columns.")
    
    # Show the country list as a table
    st.dataframe(countries_df)

    # Display the data (if passed)
    if data is not None:
        st.write("### Data Overview")
        # Display basic data stats
        st.write(f"Data contains {data.shape[0]} rows and {data.shape[1]} columns.")
        
        # Provide an option to show a subset of the columns (e.g., first 10 columns)
        st.write("#### Data (Top 10 Rows)")
        st.dataframe(data.head(10))  # Show top 10 rows of the dataset by default

        # Display the summary statistics table using describe()
        st.write("#### Summary Statistics")
        st.dataframe(data.describe())  # Show the summary statistics table
        
        # Show column selection for users to filter out which columns to view
        columns = data.columns.tolist()
        selected_columns = st.multiselect("Select columns to display", columns, default=columns[:5])  # default to the first 5 columns
        st.dataframe(data[selected_columns])

    # Insert Analysis Text
    st.markdown("""
    ## Analysis Considering the Country Information:

    ### 1. Year
    The dataset spans from 2005 to 2022, with a concentration of data points around the early 2010s (average year: 2012.96). Given the countries involved (mostly high-income countries), it is likely that most data points come from stable educational systems, reflecting steady trends in education policy over this time period.
    The spread of years indicates that the dataset captures education-related trends during a relatively dynamic period, possibly influenced by events like the global financial crisis, which may have affected education budgets and policies.

    ### 2. Region/Country/Area
    - **High-Income Countries:** Many of the countries in this dataset are high-income countries in Europe (e.g., Germany, France, Sweden, United Kingdom, United States) and advanced economies in Asia (e.g., Japan, Republic of Korea).
    - **Data Gaps:** Several regions (such as Albania, Gibraltar, Montenegro, and Republic of Moldova) have fewer data points. This could indicate reporting challenges or differences in educational reporting standards in these countries.
    - **High Reporting Frequency:** Countries like China (mainland and Hong Kong SAR), Russia, India, and United States appear more frequently, possibly reflecting a broader availability of data or more comprehensive educational statistics reporting.

    ### 3. All Staff Compensation as % of Total Expenditure in Public Institutions (%)
    - **High Proportion in High-Income Countries:** The average percentage of staff compensation (50.77%) is likely to be high in more developed economies, where staff salaries are a substantial part of the education budget. Countries such as United States, United Kingdom, and Germany would likely have higher allocations toward staff compensation.
    - **Wide Variation:** The minimum value of 0% suggests some countries or regions with very low educational staff compensation relative to total expenditure, possibly reflecting developing or conflict-affected areas (e.g., Albania, Republic of Moldova).

    ### 4. Basic Access to Computers by Level of Education
    - **Access Gap:** The statistics for computer access (mean access at lower secondary is 33.3%, primary 44.6%, and upper secondary 34.1%) highlight an issue of digital inequality. High-income countries like United States, Germany, and Australia likely have near-complete access to computers, whereas other countries like Albania, Moldova, or Gibraltar may lag behind.
    - **Full Access vs. No Access:** The 25th percentile showing 0% access and the 75th percentile showing 100% access suggests a stark divide, with some regions offering complete access while others lack it entirely.

    ### 5. Capital Expenditure as % of Total Expenditure in Public Institutions (%)
    - **Mean Capital Expenditure (6.09%):** This is relatively low, and suggests many countries are focusing more on current expenditure (e.g., staff salaries) than on long-term investments in infrastructure.
    - **Developed Economies with Higher Capital Expenditure:** Countries like Germany, France, and United States may allocate more towards capital expenditure due to greater investment in educational infrastructure, whereas smaller or lower-income regions like Moldova or Albania may have lower capital expenditure allocations.

    ### 6. Current Expenditure Other Than Staff Compensation
    - **Operational Costs:** With a mean of 17.08%, this represents a moderate share of expenditure going toward educational operations outside staff salaries. Developed economies like United States, Germany, and United Kingdom likely have higher operational costs, while regions with smaller or developing economies may allocate less toward this category.

    ### 7. Gross Enrollment Ratios (GER) by Education Level
    - **High GERs in Primary and Secondary Education:** Countries like United States, United Kingdom, Germany, and France have near-universal enrollment, with GERs above 100% indicating education systems that accommodate students outside the typical age range.
    - **Slight Gender Differences:** Although there is a slight gender imbalance in enrollment at lower secondary and primary levels (favoring boys), the upper secondary level exhibits near-gender parity or a slight advantage for girls, which is consistent with trends seen in many developed nations.

    ### 8. Ratio of Girls to Boys in Education
    - **Gender Parity:** The ratio of girls to boys is close to 1 across all education levels. At upper secondary, there is a slight shift toward more girls being enrolled, which could be attributed to improved access and opportunities for girls in many developed countries, like Sweden, Finland, and Norway.
    - **Gender Imbalance in Some Regions:** Some countries with lower educational attainment or gender disparities may have ratios less favorable toward girls, particularly at lower secondary and primary levels.

    ### 9. Teachers by Education Level
    - **Disparities in Teacher Availability:** The large variation in teacher numbers, especially at lower and upper secondary levels, shows considerable disparities across regions. High-income countries like United States, Germany, and United Kingdom have more teachers in both primary and secondary education, while regions such as Albania, Moldova, or San Marino may have very low teacher counts or difficulty in data reporting.
    - **Teacher Shortages:** The mean number of teachers at the lower secondary level (6.63) and upper secondary level (1.16) is low, with many countries having zero data points, suggesting teacher shortages or underreporting in specific regions.

    ### 10. Teachers with Minimum Required Qualifications
    - **Qualified Teacher Proportion:** The data indicates that only a small fraction of teachers in certain countries meet the minimum qualification standards, particularly in lower secondary and upper secondary education. This may point to issues in teacher training, especially in developing or under-resourced countries like Albania, Republic of Moldova, and Montenegro.
    - **High Qualification Standards in Developed Countries:** Countries like Germany, United States, and Sweden are likely to have a higher percentage of teachers meeting qualification requirements, though even in these countries, some gaps may exist.

    ### Summary of Key Trends:
    - **Digital Divide:** There is a significant gap in access to computers, especially at the lower secondary and upper secondary levels, highlighting a digital divide between high-income and low-income countries.
    - **Investment in Education:** There is an apparent focus on current expenditures (e.g., staff salaries) rather than capital investments (e.g., infrastructure), with wide variations in spending priorities across regions.
    - **Teacher Availability and Qualification:** Teacher shortages and qualification gaps are evident, particularly at the secondary education levels, reflecting systemic issues in teacher training and recruitment, especially in lower-income regions.
    - **Gender Parity:** Generally, there is good gender parity in enrollment, though some countries show disparities, particularly at lower secondary and primary levels.
    - **Geographical Inequality:** The dataset highlights stark disparities between countries, with developed countries like those in Europe, United States, and Japan consistently showing higher levels of investment, qualified teachers, and enrollment rates.

    This detailed analysis suggests that education systems vary significantly across countries in terms of access to technology, teacher qualifications, expenditure priorities, and gender parity. High-income countries tend to have more stable educational systems, while low-income or smaller countries may face challenges in providing equal access to resources and qualified teachers.
    """)