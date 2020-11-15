import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("## Maps and Data")

    st.write('''
        The data in these maps represents the factors affecting the severity of covid-19 in different counties in the united states.
        ''')

    numCases = open("num_cases.html", 'r', encoding='utf-8')
    numCases_code = numCases.read()
    components.html(numCases_code)

    # ICU Beds
    components.iframe("https://datawrapper.dwcdn.net/OvQv5/1/", height=550)

    # Proportion of Elderly People
    components.iframe("https://datawrapper.dwcdn.net/yarxi/1/", height=550)

    # Covid Cases Per Capita
    components.iframe("https://datawrapper.dwcdn.net/iWLyV/1/", height=550)

    # Deaths per Capita 
    components.iframe("https://datawrapper.dwcdn.net/D0KIt/1/", height=550)

    # Chronic Condition Coverage
    components.iframe("https://datawrapper.dwcdn.net/WrEcE/1/", height=550)