# utils/display.py

import streamlit as st
import requests

def load_markdown_from_url(url):
    """
    Function to load the content of a Markdown file from a URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading markdown content: {e}")
        return None

def display_dataframe(df):
    """
    Display the dataframe with the option to show only the top rows.
    """
    if df is not None:
        st.write("### Data Overview")
        st.dataframe(df.head())  # Display only the top rows of the dataframe
    else:
        st.error("No data to display.")