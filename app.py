import maps
import severityindex
import perCapitaNums
import findings
import streamlit as st

# st.title("County Impact for Covid-19")
# st.subheader("Made for DSS Datathon")


PAGES = {
        "Methodology and Findings": findings,
        "County Stats": maps,
        "County Stats per Capita": perCapitaNums,
        "Severity Index": severityindex
        }

st.sidebar.title('County Impact for Covid-19')
selection = st.sidebar.radio("Go to", list(PAGES.keys()));
page = PAGES[selection];
page.app();
