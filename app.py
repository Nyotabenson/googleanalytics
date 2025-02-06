import streamlit as st

# Add Google Analytics script to the page
google_analytics_tracking_id = "G-SGLY9K9D0H"  # Replace with your Google Analytics tracking ID

st.markdown(f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={google_analytics_tracking_id}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{google_analytics_tracking_id}');
    </script>
    """, unsafe_allow_html=True)

st.title("My Streamlit App")
st.write("Welcome to my Streamlit app with Google Analytics!")
