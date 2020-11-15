import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("## Severity Index")

    st.write('''
        This map is an overlay of all the factors correlating to the death rate and scaled by the respective value of the county.
        ''')

    st.subheader('Overlay Of all Factors Considered (Severity Index)')
    severity_index = open("severity_index.html", 'r', encoding='utf-8')
    severity_index_code = severity_index.read()
    components.html(severity_index_code, height=550)
    
    st.subheader("Correlation of Various Factors Considered in Severity Index")
    st.image('correlationIndex.png', use_column_width = True)

    st.subheader('The Counties which Need the Most Help')
    counties = open("top20_severity.html")
    counties_code = counties.read()
    components.html(counties_code, height=600)
