import streamlit as st
import random

# Function to generate a random trip duration between 0 and 10 minutes
def predict_trip_duration(start_station, end_station, rideable_type):
    # You can later modify this logic to use actual ML models
    return round(random.uniform(0, 10), 2)

# Streamlit App
def main():
    st.title("Mock Citi Bike Trip Duration Predictor")

    st.markdown("### Enter the trip details:")

    start_station = st.selectbox("Start Station", ["Station A", "Station B", "Station C"])
    end_station = st.selectbox("End Station", ["Station A", "Station B", "Station C"])
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])

    if st.button("Predict Trip Duration"):
        if start_station == end_station:
            st.warning("Start and end stations cannot be the same.")
        else:
            predicted_duration = predict_trip_duration(start_station, end_station, rideable_type)
            st.success(f"Predicted Trip Duration: {predicted_duration} minutes")

if __name__ == "__main__":
    main()
