import streamlit as st
import streamlit.components.v1 as components

# Path to your custom index.html file
index_html_path = 'index.html'

# Read the custom HTML file
with open(index_html_path, 'r') as file:
    custom_html = file.read()

# Inject the custom HTML into the Streamlit app using components.html
components.html(custom_html, height=0)  # height=0 means we don't need to render anything visually

# Now add Streamlit-specific content below the injected HTML
st.write("This is dynamic content injected by Streamlit!")

# You can continue adding Streamlit widgets, charts, etc.
st.button("Click Me")
