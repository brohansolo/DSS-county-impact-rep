import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("## Maps and Data")

    st.write('''
        The data in these maps represents the factors affecting the severity of covid-19 in different counties in the united states.
        ''')

    components.iframe("https://datawrapper.dwcdn.net/OvQv5/1/", height=483)