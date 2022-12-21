import streamlit as st

# Ask the user to upload an image file
#uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
#if uploaded_file is not None:
    # Display the uploaded image
 #   st.image(uploaded_file)
import streamlit as st
import pandas as pd

# Allow the user to select an Excel file
excel_file = st.file_uploader("Select an Excel file")

# Load the Excel file into a Pandas DataFrame
if excel_file is not None:
    df = pd.read_excel(excel_file)

# Display the contents of the Excel file in a table
if df is not None:
    st.table(df)

