import streamlit as st
import streamlit_analytics

# Replace with your Google Analytics tracking ID
GA_TRACKING_ID = "UA-XXXXXXXXX-X"

# Start tracking
streamlit_analytics.track(unsafe_password="your_password", ga_tracking_id=GA_TRACKING_ID)

# Your Streamlit app code
st.title("My Streamlit App")
st.write("Welcome to my app!")