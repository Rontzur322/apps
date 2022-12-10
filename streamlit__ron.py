import streamlit as st

# Create a sidebar
st.sidebar.title("Sidebar")

# Add some options to the sidebar
st.sidebar.checkbox("Option 1")
st.sidebar.checkbox("Option 2")
st.sidebar.checkbox("Option 3")

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file)
