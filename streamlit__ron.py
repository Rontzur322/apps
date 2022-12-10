import streamlit as st

# Ask the user to upload an image file
uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
if uploaded_file is not None:
    # Read the image file
    image = cv2.imread(uploaded_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a sidebar
    st.sidebar.title("Canny Edge Detector")

    # Add a slider to the sidebar for controlling the edge detection threshold
    threshold = st.sidebar.slider("Threshold", 0, 255, 50)

    # Apply the Canny edge detector to the grayscale image
    edges = cv2.Canny(gray, threshold, threshold * 2)

    # Display the original image and the edge-detected image
    st.image([image, edges], caption=["Original Image", "Edge-detected Image"])
