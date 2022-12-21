#import streamlit as st

# Ask the user to upload an image file
#uploaded_file = st.file_uploader("Choose an image file")

# Check if the user has uploaded a file
#if uploaded_file is not None:
    # Display the uploaded image
 #   st.image(uploaded_file)

# Allow the user to select a CSV file containing worker data
worker_data_file = st.file_uploader("Select a CSV file containing worker data")

# Load the worker data into a Pandas DataFrame
if worker_data_file is not None:
    worker_data = pd.read_csv(worker_data_file)
    worker_data.set_index("ID", inplace=True)

# Display the worker data in a table
if worker_data is not None:
    st.table(worker_data)

# Allow the user to select workers to add to a shift
selected_workers = st.multiselect("Select workers to add to shift:", worker_data.index)

# Display the selected workers in a table
if selected_workers:
    st.table(worker_data.loc[selected_workers])
