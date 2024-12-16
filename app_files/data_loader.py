# data_loader.py

import pandas as pd
import streamlit as st

def load_data():
    """
    Load and return the data from the three CSV files:
    - Education Statistics
    - Ratio of Girls to Boys in Education
    - Teaching Staff in Education
    
    The function also calculates derived columns like 'completion' and 'age_group' if needed.
    """
    try:
        # File paths for the three datasets
        education_stats_url = 'https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/data/filtered/filtered_areas_totals_SYB67_309_202411.csv'
        girls_boys_ratio_url = 'https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/data/filtered/filtered_areas_totals_SYB67_319_202411.csv'
        teaching_staff_url = 'https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/data/filtered/filtered_areas_totals_SYB67_323_202411.csv'
        
        # Load the datasets from the provided URLs
        education_stats_df = pd.read_csv(education_stats_url)
        girls_boys_ratio_df = pd.read_csv(girls_boys_ratio_url)
        teaching_staff_df = pd.read_csv(teaching_staff_url)
        
        # Returning the dataframes as a dictionary
        return {
            'education_stats': education_stats_df,
            'girls_boys_ratio': girls_boys_ratio_df,
            'teaching_staff': teaching_staff_df
        }
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None