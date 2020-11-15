from pathlib import Path
import streamlit as st

def app():
    st.write("# METHODOLOGY AND FINDINGS")

    def read_markdown_file(markdown_file):
            return Path(markdown_file).read_text()
    methodology = read_markdown_file("README.md")
    st.markdown(methodology, unsafe_allow_html=True)

    st.write('''
        We used data from the New York Times, from the US Census and various other verified sources to build an understanding of which factors most strongly correlated to the death rate.
        ''')

