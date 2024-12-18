# pages/eda_results.py

import streamlit as st
from utils.display import load_markdown_from_url

def show():
    # Title for the page
    st.title("Exploratory Data Analysis (EDA) Results")

    # Markdown URL for the EDA results
    markdown_url = "https://raw.githubusercontent.com/Cfg-data/final-project/refs/heads/master/EDA_results.md"

    # Load and display markdown content
    markdown_content = load_markdown_from_url(markdown_url)
    
    if markdown_content:
        st.markdown(markdown_content)