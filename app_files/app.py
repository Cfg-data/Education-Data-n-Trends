#app.py

import streamlit as st
from data_loader import load_data
from pages import opener, introduction, ml_results

# Set the page title and layout
st.set_page_config(page_title="Education Project Overview", layout="wide")

# Load data for the entire app
data = load_data()

# Display a sidebar with navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Opener", "Introduction", "ML Results"])

# Display selected page content
if page == "Opener":
    opener.show(data)
elif page == "Introduction":
    introduction.show(data)
elif page == "ML Results":
    ml_results.show(data)