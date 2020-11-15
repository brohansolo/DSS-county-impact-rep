import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("## Maps and Data on Per Capita Basis")

    st.write('''
        The data in these maps represents the factors affecting the severity of covid-19 in different counties in the united states on a per person basis.
        ''')

    # Proportion of Elderly People
    components.iframe("https://datawrapper.dwcdn.net/yarxi/1/", height=550)

    # Covid Cases Per Capita
    components.iframe("https://datawrapper.dwcdn.net/iWLyV/1/", height=550)

    # Deaths per Capita 
    # components.iframe("https://datawrapper.dwcdn.net/D0KIt/1/", height=550)

