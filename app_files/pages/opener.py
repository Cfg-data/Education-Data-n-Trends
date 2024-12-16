# pages/opener.py

import streamlit as st

def show(data):
    st.title("Welcome to the Education Project")
    st.write("### Data Loading Confirmation")
    
    if data is not None:
        st.success("Data has been successfully loaded!")
        
        # Display some basic information about each dataset
        st.write("### Collected Datasets")
        st.write("The following datasets have been collected from UNDATA:")

        st.markdown("""
        1. **[Ratio of Girls to Boys in Education](https://data.un.org/_Docs/SYB/CSV/SYB67_319_202411_Ratio%20of%20girls%20to%20boys%20in%20education.csv)**
           - Dataset ID: SYB67_319_202411
           - Description: This dataset provides the ratio of girls to boys in education across different countries and regions.

        2. **[Public Expenditure on Education and Access to Computers](https://data.un.org/_Docs/SYB/CSV/SYB67_245_202411_Public%20expenditure%20on%20education%20and%20access%20to%20computers.csv)**
           - Dataset ID: SYB67_245_202411
           - Description: This dataset presents the public expenditure on education, along with data on the availability of computers in educational institutions.

        3. **[Teaching Staff in Education](https://data.un.org/_Docs/SYB/CSV/SYB67_323_202411_Teaching%20Staff%20in%20education.csv)**
           - Dataset ID: SYB67_323_202411
           - Description: This dataset outlines the number of teaching staff in the education sector across various countries and regions.

        4. **[Education Statistics](https://data.un.org/_Docs/SYB/CSV/SYB67_309_202411_Education.csv)**
           - Dataset ID: SYB67_309_202411
           - Description: This dataset provides a comprehensive overview of various education-related statistics, such as enrollment rates, graduation rates, and literacy rates.
        """)

        st.write("### Additional Datasets")

        st.markdown("""
        - **[Youth Literacy Rate, Population 15-24 Years (%)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24)**  
          Identified as UNdata_Export_20241213_140703208 in the files.

        - **[Youth Literacy Rate, Population 15-24 Years, Gender Parity Index (GPI)](https://data.un.org/Data.aspx?d=UNESCO&f=series%3aLR_AG15T24_GPI)**  
          Identified as UNdata_Export_20241213_140708283 in the files.
        """)

        # Display dataset information (DataFrame dimensions) for loaded datasets
        for dataset_name, df in data.items():
            st.write(f"### {dataset_name.replace('_', ' ').title()}")
            st.write(f"Data contains {len(df)} rows and {len(df.columns)} columns.")

    else:
        st.error("There was an issue loading the data.")

    # License Information
    st.write("### License")
    st.write("This project is based on publicly available data from UNDATA. Please refer to the [UN Data Usage Policy](https://data.un.org/Usage.aspx) for licensing and attribution information.")