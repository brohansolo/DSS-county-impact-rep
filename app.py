import streamlit as st

st.title("County Impact for Covid-19")
st.subheader("Made for DSS Datathon")


PAGES = {
        "County Stats through Maps": maps.py,
        "Methodology and Findings": findings.py,
        }

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()));
page = PAGES[selection];
page.app();
