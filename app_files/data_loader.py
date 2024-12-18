# data_loader.py

import pandas as pd
import streamlit as st

def load_data():
    """
    Load and return the dataset from the given URL.
    
    The function loads the full country data CSV from the specified URL.
    """
    try:
        # URL for the dataset
        data_url = 'https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/usable_notebooks/full_country_data.csv'
        
        # Load the dataset from the provided URL
        full_country_data_df = pd.read_csv(data_url)
        
        # Returning the dataframe
        return full_country_data_df
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None