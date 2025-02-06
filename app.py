import streamlit as st
import pathlib
from bs4 import BeautifulSoup
import logging
import shutil
def inject_ga():
    GA_ID = 'G-SGLY9K9D0H'

    GA_JS = """
     <script async scr="https://www.googletagmanager.com/gtag/js?id=G-SGLY9K9D0H"></script>     
     <script>
           window.datalayer = window.datalayer || [];
           function gtag(){dataLayer.push(arguments);}
           gtag('js', new Date());
           gtag('config', 'G-SGLY9K9D0H');
     </script>          
    """


    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f'editing {index_path}')
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    if not soup.find(id=GA_ID): # if id not found within html file
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  # backup recovery
        else:
            shutil.copy(index_path, bck_index)  # save backup
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS) 
        index_path.write_text(new_html) # insert analytics tag at top of head


st.header("STREAMLIT GOOGLE ANALYTICS TRIAL")        