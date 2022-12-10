import streamlit as st
import cv2

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Read the image file
    image = cv2.imread(uploaded_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detector to the grayscale image
    edges = cv2.Canny(gray, 50, 100)

    # Display the original image and the edge-detected image
    st.image([image, edges], caption=["Original Image", "Edge-detected Image"])
