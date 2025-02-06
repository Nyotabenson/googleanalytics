# components/ga4_component.py
import streamlit.components.v1 as components

def ga4(measurement_id):
    html = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={measurement_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '{measurement_id}');
    </script>
    """
    components.html(html, height=0, width=0)  # Ensure no visual footprint