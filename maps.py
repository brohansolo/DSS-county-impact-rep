import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("## Maps and Data")

    st.write('''
        The data in these maps represents the factors affecting the severity of covid-19 in different counties in the united states.
        ''')

    st.subheader('Overlay Of all Factors Considered (Severity Index)')
    severity_index = open("severity_index.html", 'r', encoding='utf-8')
    severity_index_code = severity_index.read()
    components.html(severity_index_code, height=550)

    st.subheader('Number of Cases Per County')
    numCases = open("num_cases.html", 'r', encoding='utf-8')
    numCases_code = numCases.read()
    components.html(numCases_code, height=550)

    st.subheader('Rate of Change of Cases Per County')
    firstDeriv = open("firstDerivative.html", 'r', encoding='utf-8')
    firstDeriv_code = firstDeriv.read()
    components.html(firstDeriv_code, height=550)

    st.subheader('Rate of Change of Rate of Change of Cases Per County')
    secondDeriv = open("secondDerivative.html", 'r', encoding='utf-8')
    secondDeriv_code = secondDeriv.read()
    components.html(secondDeriv_code, height=550)

    st.subheader('Elderly People Per County')
    elderlyCount = open("ElderlyCount.html", 'r', encoding='utf-8')
    elderlyCount_code = elderlyCount.read()
    components.html(elderlyCount_code, height=550)

    # ICU Beds
    components.iframe("https://datawrapper.dwcdn.net/OvQv5/1/", height=550)

    # Proportion of Elderly People
    # components.iframe("https://datawrapper.dwcdn.net/yarxi/1/", height=550)

    # Covid Cases Per Capita
    # components.iframe("https://datawrapper.dwcdn.net/iWLyV/1/", height=550)

    # Deaths per Capita 
    # components.iframe("https://datawrapper.dwcdn.net/D0KIt/1/", height=550)

    # Chronic Condition Coverage
    components.iframe("https://datawrapper.dwcdn.net/WrEcE/1/", height=550)