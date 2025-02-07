import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open('index.html', 'r') as f:
    html_content = f.read()

# Embed the HTML in Streamlit app
components.html(html_content, height=600)
