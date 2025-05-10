import streamlit as st
import pandas as pd
import random

# Function to make random predictions between 0 and 10
def make_predictions(features):
    prediction = round(random.uniform(0, 10), 2)
    return prediction

# Streamlit UI
def main():
    st.title("Citi Bike Trip Duration Prediction (Mock)")

    st.markdown("Enter the details of the bike trip:")

    # User inputs for prediction (example: pickup and drop-off data)
    start_station = st.selectbox("Start Station", ["Station 1", "Station 2", "Station 3"])  # Add real stations
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])
    trip_duration = st.number_input("Trip Duration (Minutes)", min_value=0)

    # When the user clicks the "Predict" button
    if st.button("Predict"):
        # Example feature vector (not used here, but kept for structure)
        features = [start_station, rideable_type, trip_duration]
        
        prediction = make_predictions(features)
        st.success(f"Predicted Trip Duration: {prediction} minutes")

if __name__ == "__main__":
    main()
