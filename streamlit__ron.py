import streamlit as st
import cv2

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Get the path to the uploaded file
    file_path = uploaded_file.name

    # Read the image file
    image = cv2.imread(file_path)

    # Check if the image was successfully read
    if image is not None:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR
