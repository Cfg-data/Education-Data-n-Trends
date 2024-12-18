# pages/eda_results.py

import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from data_loader import load_data
from data_loader import load_countries  # Correctly import the function

def show(data=None):
    # Title for the page
    st.title("Exploratory Data Analysis (EDA) Results")

    # Load the countries data
    countries_df = load_countries()  # Use the imported function

    # Show country data
    st.write("### Countries List")
    st.write(f"Data contains {countries_df.shape[0]} rows and {countries_df.shape[1]} columns.")
    
    # Show the country list as a table
    st.dataframe(countries_df)

    # Show country data
    st.write("### Countries List")
    st.write(f"Data contains {countries_df.shape[0]} rows and {countries_df.shape[1]} columns.")
    
    # Show the country list as a table
    st.dataframe(countries_df)

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

    # Plots and interpretations section
    st.markdown("## Plots and Interpretations")

    # Create Plotly plots for each category
    trace1 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Primary (female)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Primary (female)'].mean(),
                        mode='lines+markers', name='Primary (Female)')
    trace2 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Primary (male)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Primary (male)'].mean(),
                        mode='lines+markers', name='Primary (Male)')
    trace3 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Lower secondary level (female)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Lower secondary level (female)'].mean(),
                        mode='lines+markers', name='Lower Secondary (Female)')
    trace4 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Lower secondary level (male)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Lower secondary level (male)'].mean(),
                        mode='lines+markers', name='Lower Secondary (Male)')
    trace5 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Upper secondary level (female)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Upper secondary level (female)'].mean(),
                        mode='lines+markers', name='Upper Secondary (Female)')
    trace6 = go.Scatter(x=data.groupby('Year')['Gross enrollment ratio - Upper secondary level (male)'].mean().index,
                        y=data.groupby('Year')['Gross enrollment ratio - Upper secondary level (male)'].mean(),
                        mode='lines+markers', name='Upper Secondary (Male)')

    # Combine all traces into a data list
    data_traces = [trace1, trace2, trace3, trace4, trace5, trace6]

    # Define layout for the plot
    layout = go.Layout(
        title='Trend of Gross Enrollment Ratios (Female & Male) Over Time',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Gross Enrollment Ratio'),
        template="plotly_white"
    )

    # Create a Figure and render it in the Streamlit app
    fig = go.Figure(data=data_traces, layout=layout)
    st.plotly_chart(fig)

    # Grouping the data by year and calculating the mean for each category
    trend_data = pd.DataFrame({
        'Year': data['Year'].unique(),  # Unique years in the dataset
        'Primary (Female)': data.groupby('Year')['Gross enrollment ratio - Primary (female)'].mean(),
        'Primary (Male)': data.groupby('Year')['Gross enrollment ratio - Primary (male)'].mean(),
        'Lower Secondary (Female)': data.groupby('Year')['Gross enrollment ratio - Lower secondary level (female)'].mean(),
        'Lower Secondary (Male)': data.groupby('Year')['Gross enrollment ratio - Lower secondary level (male)'].mean(),
        'Upper Secondary (Female)': data.groupby('Year')['Gross enrollment ratio - Upper secondary level (female)'].mean(),
        'Upper Secondary (Male)': data.groupby('Year')['Gross enrollment ratio - Upper secondary level (male)'].mean()
    })

    # Display the trend table
    st.write("### Enrollment Ratio Trends Table")
    st.dataframe(trend_data)

    # Insert the analysis for Enrollment Ratio Trends
    st.markdown("""
    ## Enrollment Ratio Trends Analysis

    ### Primary Education (Female and Male)
    - **Trend**: Both primary female and male enrollment ratios have remained stable over the years, with a slight decline between 2005 and 2022.
      - **Female**: From 102.66% in 2005 to 97.88% in 2022.
      - **Male**: From 104% in 2005 to 98.36% in 2022.
    - **Interpretation**: This indicates good access to primary education for both genders, with near-universal enrollment. The slight decline could reflect demographic or economic shifts.

    ### Lower Secondary Education (Female and Male)
    - **Trend**: Enrollment in lower secondary education shows a slight decrease over time, particularly for females.
      - **Female**: From 105.93% in 2005 to 88.23% in 2022.
      - **Male**: From 105.51% in 2005 to 90.43% in 2022.
    - **Interpretation**: The decline in enrollment may reflect challenges such as economic instability, educational policies, or shifts in enrollment priorities. Some countries might face difficulties due to infrastructure or economic conditions.

    ### Upper Secondary Education (Female and Male)
    - **Trend**: Enrollment in upper secondary education shows significant variation.
      - **Female**: From 98.26% in 2005 to a peak of 110% in 2015, followed by a drop to 92.07% in 2022.
      - **Male**: From 93.61% in 2005 to 108.24% in 2015, followed by a decline to 93.64% in 2022.
    - **Interpretation**: The sharp increase followed by a drop in upper secondary enrollment, especially for females, suggests possible shifts in access or economic factors influencing educational policies.

    ## Gender Parity Trends
    - **Primary Education**: Both male and female students exhibit near-equal enrollment rates, with only slight declines over time.
    - **Secondary Education**: 
      - **Lower Secondary**: Both genders saw similar declines, but **female enrollment** experienced a slightly sharper drop than **male enrollment**.
      - **Upper Secondary**: **Females** initially had higher GER but saw a decline after 2015, with **males** having slightly higher GER in 2022.

    ## Geographical Insights
    - **High-Income Countries**: Countries like the **United States**, **Canada**, **Germany**, **France**, and the **United Kingdom** likely maintained strong enrollment rates across all levels.
    - **Challenges in Lower-Income or Smaller Regions**: Countries such as **Albania**, **Republic of Moldova**, and **Montenegro** may experience challenges related to enrollment, particularly in secondary and upper-secondary education due to limited resources or political instability.
    - **Global Trends**: The global trend from 2005 to 2022 indicates significant progress in primary education, but challenges persist at the secondary and upper-secondary levels.

    ## Conclusion
    - The data suggests near-universal primary education enrollment globally, but significant challenges remain in maintaining high enrollment at the secondary and upper-secondary levels.
    - **Gender Parity**: While gender parity exists in primary and lower secondary education, females experienced a slight decline in upper secondary enrollment compared to males by 2022.
    - **Regional Variations**: Developed countries show consistent high enrollment, while regions with lower resources or political challenges face difficulties in maintaining enrollment rates at the secondary education levels.
    """)

        # Group by 'Region/Country/Area Name' and calculate the mean for the required columns
    expenditure_comparison = data.groupby('Region/Country/Area')[[
        'All staff compensation as % of total expenditure in public institutions (%)',
        'Capital expenditure as % of total expenditure in public institutions (%)',
        'Current expenditure other than staff compensation as % of total expenditure in public institutions (%)'
    ]].mean()

    # Sort the values for better readability
    expenditure_comparison = expenditure_comparison.sort_values(
        'All staff compensation as % of total expenditure in public institutions (%)', ascending=False)

    # Display the comparison table
    st.write("### Expenditure Comparison Table")
    st.dataframe(expenditure_comparison)

    # Plotting the expenditure comparison using Plotly
    bar_width = 0.25
    index = np.arange(len(expenditure_comparison))
    
    # Creating traces for each expenditure category
    trace1 = go.Bar(
        y=expenditure_comparison.index,
        x=expenditure_comparison['All staff compensation as % of total expenditure in public institutions (%)'],
        orientation='h',
        name='Staff Compensation',
        marker=dict(color='skyblue'),
        width=bar_width
    )
    trace2 = go.Bar(
        y=expenditure_comparison.index,
        x=expenditure_comparison['Capital expenditure as % of total expenditure in public institutions (%)'],
        orientation='h',
        name='Capital Expenditure',
        marker=dict(color='lightgreen'),
        width=bar_width
    )
    trace3 = go.Bar(
        y=expenditure_comparison.index,
        x=expenditure_comparison['Current expenditure other than staff compensation as % of total expenditure in public institutions (%)'],
        orientation='h',
        name='Current Expenditure (Other than Staff)',
        marker=dict(color='salmon'),
        width=bar_width
    )
    
    # Create layout for the bar chart
    layout = go.Layout(
        title='Comparison of Expenditures as % of Total Expenditure in Public Institutions',
        xaxis=dict(title='Percentage of Total Expenditure'),
        yaxis=dict(title='Region/Country/Area'),
        barmode='group',
        bargap=0.2,
        template='plotly_white'
    )
    
    # Combine traces into a figure and plot using Streamlit
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
    st.plotly_chart(fig)
    
    # Public Expenditure Comparison Across Regions/Countries
    st.markdown("## Public Expenditure Comparison Across Regions/Countries")
    
    # Displaying the analysis before the table
    st.markdown("""
    ### Observations & Comparison
    
    #### **Staff Compensation**:
    - **Mexico** (85.5%) and **Belgium** (83.6%) allocate the highest percentages to staff compensation, indicating a significant portion of the public sector budget goes towards salaries and benefits.
    - Several countries, including **China**, **Estonia**, and **Hong Kong**, report 0% allocation, which may imply alternative expenditure classifications or lack of available data.

    #### **Capital Expenditure**:
    - **Japan** (13%) and **Norway** (12.3%) have the highest capital expenditure percentages, suggesting substantial investments in infrastructure and long-term projects.
    - **San Marino** reports 0% in this category, possibly reflecting its small size or unique expenditure policies.

    #### **Current Expenditure (Other than Staff Compensation)**:
    - **Finland** (32.85%) and **Sweden** (29.77%) dedicate the largest shares of their budgets to current expenditure other than staff compensation, highlighting robust spending on public services and operational costs.
    - **Andorra** stands out with a high percentage (50.87%) in current expenditure, which might reflect specific priorities or high operational costs.

    ### Conclusion:
    - **Mexico**, **Belgium**, and **Norway** exhibit high allocations for staff compensation, suggesting a greater focus on personnel costs in public institutions.
    - **Japan**, **Norway**, and **Latvia** emphasize capital expenditures, indicating a long-term investment in infrastructure and public assets.
    - **Finland** and **Romania** allocate substantial amounts to other current expenditure, signaling broad operational funding beyond staffing needs.
    
    This comparison provides valuable insights into the expenditure priorities and trends of these countries.
    """)
    # Title for the page
    st.title("Teacher Data Analysis (2005-2022)")

    # Group by 'Year' and calculate the mean of the number of teachers at each level
    teachers_primary = data.groupby('Year')['Teachers at primary level'].mean()
    teachers_lower_secondary = data.groupby('Year')['Teachers at lower secondary level'].mean()
    teachers_upper_secondary = data.groupby('Year')['Teachers at upper secondary level'].mean()

    # Create a Plotly plot for the number of teachers at different levels over the years
    trace1 = go.Scatter(x=teachers_primary.index, y=teachers_primary, mode='lines+markers', name='Primary Level', line=dict(color='skyblue'))
    trace2 = go.Scatter(x=teachers_lower_secondary.index, y=teachers_lower_secondary, mode='lines+markers', name='Lower Secondary Level', line=dict(color='lightgreen'))
    trace3 = go.Scatter(x=teachers_upper_secondary.index, y=teachers_upper_secondary, mode='lines+markers', name='Upper Secondary Level', line=dict(color='salmon'))

    # Create the layout for the plot
    layout = go.Layout(
        title='Number of Teachers at Different Education Levels Over Time',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Number of Teachers'),
        template='plotly_white'
    )

    # Plot the figure
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)
    st.plotly_chart(fig)

    # Group by 'Year' and calculate the mean for teachers with minimum qualifications at each level
    teachers_min_qualified_primary = data.groupby('Year')['Teachers with minimum required qualifications at primary level'].mean()
    teachers_min_qualified_lower_secondary = data.groupby('Year')['Teachers with minimum required qualifications at lower secondary level'].mean()
    teachers_min_qualified_upper_secondary = data.groupby('Year')['Teachers with minimum required qualifications at upper secondary level'].mean()

    # Create a Plotly plot for teachers with minimum qualifications over the years
    trace4 = go.Scatter(x=teachers_min_qualified_primary.index, y=teachers_min_qualified_primary, mode='lines+markers', name='Primary Level (Qualified)', line=dict(color='skyblue'))
    trace5 = go.Scatter(x=teachers_min_qualified_lower_secondary.index, y=teachers_min_qualified_lower_secondary, mode='lines+markers', name='Lower Secondary Level (Qualified)', line=dict(color='lightgreen'))
    trace6 = go.Scatter(x=teachers_min_qualified_upper_secondary.index, y=teachers_min_qualified_upper_secondary, mode='lines+markers', name='Upper Secondary Level (Qualified)', line=dict(color='salmon'))

    # Create the layout for the second plot
    layout_qualified = go.Layout(
        title='Number of Teachers with Minimum Qualifications at Different Education Levels Over Time',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Number of Teachers with Minimum Qualifications'),
        template='plotly_white'
    )

    # Plot the second figure
    fig_qualified = go.Figure(data=[trace4, trace5, trace6], layout=layout_qualified)
    st.plotly_chart(fig_qualified)

    # Group by 'Year' and calculate the mean for relevant columns
    teachers_data = data.groupby('Year')[[
        'Teachers at primary level', 
        'Teachers at lower secondary level', 
        'Teachers at upper secondary level',
        'Teachers with minimum required qualifications at primary level', 
        'Teachers with minimum required qualifications at lower secondary level',
        'Teachers with minimum required qualifications at upper secondary level'
    ]].mean()

    # Reset index to make 'Year' a column and display the table
    teachers_data = teachers_data.reset_index()
    st.write("### Teachers Data Table")
    st.dataframe(teachers_data)

    # Insert the analysis
    st.markdown("""
    ### Interpretation of the Results

    - **Primary Level Teachers**:
      - In **2005**, there were no teachers reported at the primary level.
      - By **2010**, the number of primary-level teachers sharply increased to **48.38**.
      - **2015** saw a reduction in primary-level teachers to **11.64**, with a subsequent rise to **55.42** in **2022**.
    
    - **Lower Secondary Level Teachers**:
      - Similar to the primary level, there were no teachers at the lower secondary level in **2005**.
      - The number of teachers increased by **2010** to **18.06**, but **2015** saw a dramatic drop to **0**.
      - There was some recovery in **2022**, with **13.17** teachers reported at the lower secondary level.
    
    - **Upper Secondary Level Teachers**:
      - The trend for upper secondary teachers mirrored that of primary and lower secondary, with **no teachers** in **2005** and **2010**.
      - **2022** marked the highest number of upper secondary teachers at **10.75**.
    
    - **Teachers with Minimum Required Qualifications**:
      - The percentage of teachers with minimum required qualifications was generally high across all levels, but showed variability.
      - **Primary Level**: Saw a fluctuation in qualifications from **18.80%** in **2005** to **52.17%** in **2022**.
      - **Lower Secondary Level**: The percentage of teachers meeting the qualification standard ranged from **8.96%** in **2005** to **24.20%** in **2022**, reflecting a steady improvement.
      - **Upper Secondary Level**: The qualification rate increased over time, from **9.10%** in **2005** to **32.92%** in **2022**, indicating improved teacher qualification.
    
    ---
    
    ### Key Observations:
    1. **Sharp Increase in Teacher Numbers**: There was a sharp increase in teacher numbers in **2010** for primary and lower secondary levels, followed by a drop in **2015** and a recovery in **2022**.
    2. **Teacher Qualification Improvement**: Over time, the percentage of teachers with minimum required qualifications increased across all education levels, especially at the primary and upper secondary levels.
    3. **Fluctuating Trends**: The data suggests fluctuating trends, possibly due to changes in educational policies, economic factors, or disruptions affecting education systems during the interim years (2010-2021).
    4. **Lack of Teachers in 2005 and 2010**: The lack of reported teachers in **2005** and **2010** at primary and lower secondary levels raises questions about either data reporting issues or temporary educational setbacks.
    
    This data highlights both progress in teacher qualifications and the instability in the number of teachers across various education levels over the years.
    """)

    # Optionally, you can also display the link to the image mentioned in the analysis:
    st.image("https://github.com/Cfg-data/final-project/blob/master/usable_notebooks/full_analysis/scatter_capital_vs_enrollment_combined.png", caption="Capital Expenditure vs Gross Enrollment Ratios at Different Levels")