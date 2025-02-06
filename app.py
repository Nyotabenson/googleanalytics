# app.py
import streamlit as st
from components.ga4_component import ga4

GA_ID = "G-SGLY9K9D0H"  # Replace with your Measurement ID

ga4(GA_ID)  # Place this near the top of your app

st.title("My Streamlit App with GA4")
st.write("Welcome!")

# ... rest of your Streamlit app