import streamlit as st

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file)
