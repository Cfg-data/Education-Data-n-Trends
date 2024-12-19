# app.py

import streamlit as st
from data_loader import load_data
from pages import opener, introduction, eda_results, ml_results, recommendations  # Import recommendations page

# Set the page title and layout
st.set_page_config(page_title="Education Project Overview", layout="wide")

# Load data for the entire app
data = load_data()

# Display a sidebar with navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Opener", "Introduction", "EDA Results", "ML Results", "Recommendations"])  # Add Recommendations here

# Display selected page content
if page == "Opener":
    opener.show(data)
elif page == "Introduction":
    introduction.show(data)
elif page == "EDA Results":
    eda_results.show(data)
elif page == "ML Results":
    ml_results.show(data)
elif page == "Recommendations":  # Show Recommendations page
    recommendations.show(data)