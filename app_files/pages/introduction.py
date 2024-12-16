# pages/introduction.py
import streamlit as st

def show(data):
    st.title("Project Introduction")
    st.write("""
        Education serves as a cornerstone for societal progress, yet the global landscape reveals significant disparities in both access to education and educational outcomes. 
        These inequalities are particularly evident when examining key factors such as literacy rates, gender parity in education, teacher qualifications, and resource allocation. 
        This research project is designed to analyze and present educational data from the United Nations Database (UNDATA) with the goal of understanding the complex factors influencing educational disparities worldwide. 
        The project is divided into two primary parts: one focused on literacy disparities using machine learning models, and the other on a statistical analysis of educational metrics such as gender ratios, teacher qualifications, and access to resources.
    """)
    
    st.write("""
        The first part of the project will apply machine learning techniques—specifically Linear Regression and Random Forest models—to identify patterns and relationships in global literacy data. 
        By examining literacy rates across different regions and correlating them with socio-economic, demographic, and policy variables, this analysis will provide insights into the global disparities in literacy.
    """)
    
    st.write("""
        The second part of the project takes a deeper dive into the gender gap in education, the availability of qualified teachers, and the distribution of educational resources over time. 
        This will include a statistical analysis of the ratio of girls to boys at various levels of education, the number of teachers at each educational level, and the proportion of teachers with the required qualifications. 
        Additionally, the study will explore access to computers in education and analyze government expenditure on education as a percentage of total national expenditure, considering how these factors evolve year by year.
    """)

    st.write("""
        By integrating both machine learning models and statistical analysis, this project aims to offer a multifaceted view of the global educational landscape, revealing how gender, resources, and government investment influence educational outcomes. 
        Ultimately, the findings will contribute to a more nuanced understanding of the educational inequalities that persist across different regions and provide a foundation for policy recommendations to foster more equitable and effective education systems globally.
    """)