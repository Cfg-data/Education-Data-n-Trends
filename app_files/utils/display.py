# utils/display.py

import streamlit as st

def display_dataframe(df):
    """
    Display the dataframe with the option to show only the top rows.
    """
    if df is not None:
        st.write("### Data Overview")
        st.dataframe(df.head())
    else:
        st.error("No data to display.")