import maps
import severityindex
import perCapitaNums
import findings
import streamlit as st

st.title("County Impact for Covid-19")
st.subheader("Made for DSS Datathon")


PAGES = {
        "Severity Index": severityindex,
        "County Stats": maps,
        "County Stats per Capita": perCapitaNums,
        "Methodology and Findings": findings
        }

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()));
page = PAGES[selection];
page.app();
