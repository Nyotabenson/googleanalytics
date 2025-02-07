import streamlit as st

# Include the Google Analytics (GA4) script in the app
st.markdown("""
    <!-- Google Analytics (GA4) Code -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-SGLY9K9D0H"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-SGLY9K9D0H');
    </script>
""", unsafe_allow_html=True)

# Custom HTML or other Streamlit content
st.markdown("<h1>Header from HTML</h1>", unsafe_allow_html=True)
