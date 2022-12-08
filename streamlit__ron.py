# import libs
import streamlit as st
import cv2
import numpy as np
import skimage.io as io
#import matplotlib.pyplot as plt

# check versions
#np.__version__

# Function to apply K-means clustering to an image
def kmeans_segmentation(image, k):
  # Convert the image to a two-dimensional array of pixels
  pixels = image.reshape((image.shape[0] * image.shape[1], 3))

  # Apply K-means clustering to the pixels with the specified number of clusters
  kmeans = KMeans(n_clusters=k)
  kmeans.fit(pixels)

  # Use the cluster labels to replace the pixel values in the original image
  return kmeans.cluster_centers_[kmeans.labels_].reshape(image.shape)

# Set the maximum number of clusters that can be selected by the user
MAX_CLUSTERS = 5

# Create the main app
def main():
  # Allow the user to upload an image
  uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

  # Load the uploaded image and display it
  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original image", use_column_width=True)

    # Allow the user to specify the number of clusters to use for K-means clustering
    k = st.slider("Select the number of clusters:", 2, MAX_CLUSTERS, 2)

    # Apply K-means clustering to the image
    result = kmeans_segmentation(image, k)

    # Display the resulting segmented image
    st.image(result, caption="Segmented image", use_column_width=True)

# Run the main app
if __name__ == "__main__":
  main()
