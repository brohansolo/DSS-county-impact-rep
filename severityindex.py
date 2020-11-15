import pandas as pd
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
 
    # counties = open("top20_severity.html")
    # counties_code = counties.read()
    # components.html(counties_code, height=600)

    combined = pd.read_csv('combined_df.csv')

    st.subheader('The Counties which Need the Most Help')
    def get_top(n): 
        result_series = combined.nlargest(n, 'severity_index').county + ", " + combined.nlargest(n, 'severity_index').state
        final_df = result_series.to_frame() 
        final_df.rename({0:'Severity Ranking (Top 20)'}, axis = 1, inplace = True) 
        final_df.reset_index(inplace = True, drop = True) 
        return final_df
    
    choice = st.selectbox('Select Number of Counties', ('5','10','20','50', '100')) 
    if st.button('Show Counties', key = '1'):
        st.write(get_top(int(choice)))
