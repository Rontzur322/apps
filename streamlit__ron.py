import streamlit as st
import cv2

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Get the path to the uploaded file
    file_path = uploaded_file.get_path()

    # Debug the file path
    print(file_path)

    # Read the image file
    image = cv2.imread(file_path)

    # Check if the image was successfully read
    if image is not None:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply the Canny edge detector to the grayscale image
        edges = cv2.Canny(gray, 50, 100)

        # Display only the edge-detected image
        st.image(edges, caption="Edge-detected Image")
    else:
        # Display an error message if the image could not be read
        st.error("Could not read image file")


        
