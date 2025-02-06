import streamlit as st
import pathlib

def load_html_page():
    # Path to your HTML file
    html_path = pathlib.Path('index.html')

    if html_path.exists():
        # Read the HTML content
        html_content = html_path.read_text()
        
        # Render HTML with GA script
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.error("HTML file not found!")

# Run the function to display the HTML content
load_html_page()
