import streamlit as st

# Allow user to upload image
uploaded_file = st.file_uploader("Choose an image file:")

# Show the uploaded image
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
