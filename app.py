import streamlit as st

def inject_ga():
    GA_JS = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-SGLY9K9D0H"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-SGLY9K9D0H');
    </script>
    """
    
    # Inject GA JS directly into the Streamlit app
    st.markdown(GA_JS, unsafe_allow_html=True)
    
    # Display header for Streamlit app
    st.header("STREAMLIT GOOGLE ANALYTICS TRIAL")

# Run the function to inject GA code
inject_ga()