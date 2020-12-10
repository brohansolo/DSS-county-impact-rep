import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from sklearn import preprocessing
from urllib.request import urlopen
import json

def app():



    merged_data = pd.read_csv("merged_data.csv")
    def fill_missing(series, limit):
        series = series.astype('str')
        series = ['0' + i if len(i) < limit else i for i in series]
        return series
    merged_data['fips'] = fill_missing(merged_data['fips'], 5)

    columns = list(merged_data.columns)
    my_dict = {k: v for v, k in enumerate(columns)}

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)


    user_merged = merged_data.copy()
    def plot_severity(features, target):
        metrics = merged_data.iloc[:,features]
        matrix = metrics.corr(method = "spearman")
        f, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(matrix, mask=np.zeros_like(matrix, dtype=np.bool), cmap = "flare_r", square=True, ax=ax);
        weights = list(matrix[target].values)
        weights.remove(1)
        n2 = list(normalize([weights], norm="l1")[0])
        
        features = metrics.drop(columns = [target], axis = 1)
        scalars = features * n2
        user_merged['severity_index'] = (scalars.astype(float).sum(1)) 

        m =  user_merged['severity_index']
        user_merged['severity_index'] = np.log(m, where=(m>0))
        user_merged['severity_index'] = (user_merged['severity_index'] - np.min(user_merged['severity_index'])) / (np.max(user_merged['severity_index']) - np.min(user_merged['severity_index']))

        fig = px.choropleth_mapbox(user_merged, geojson=counties, locations='fips', color= 'severity_index',
                                color_continuous_scale="speed",
                                hover_name = 'county',
                                hover_data = {'fips':False, 'severity_index':True},
                                labels = {'severity_index':'Severity Index', 'county':'County'},
                                mapbox_style="carto-positron",
                                zoom=2.8, center = {"lat": 37.0902, "lon": -95.7129},
                                title = "Overlay Of Factors Considered (Severity Index)",
                                opacity=0.5
                                )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #     fig.update(layout_coloraxis_showscale=False)
        # st.write('This is plt.show')
        # st.write(plt.show())
        # st.write('This is f')
        # st.write(f)
        # st.write('This is f.show')
        # st.write(f.show())
        # st.write(fig)

        return fig
    #     return n2

    columns.remove('COVID Cases per Capita') 
    columns.remove('COVID Deaths per Capita') 
    columns.remove('Total COVID Cases') 
    columns.remove('Total COVID Deaths')
    # to remove
    columns.remove('fips')
    columns.remove('date')
    columns.remove('county')
    columns.remove('state')
    columns.remove('Month')

    user_input2 = st.selectbox('Select Basis of Severity', ('COVID Cases per Capita', 'COVID Deaths per Capita', 'Total COVID Cases', 'Total COVID Deaths')) 
    user_input1 = st.multiselect('Select Variable(s) to use in Severity Index', columns) 
    user_input1 = [my_dict[x] for x in user_input1] 
    # user_input1 += my_dict[target]
    user_input1.append(my_dict[user_input2]) 
 
    if st.button('Submit', key = '1'): 
        st.write(plot_severity(user_input1, user_input2), use_column_width = True) 

#    user_input2 = target


    # st.write("## Severity Index")

    # st.write('''
    #     This map is an overlay of all the factors correlating to the death rate and scaled by the respective value of the county.
    #     ''')

    # st.subheader('Overlay Of all Factors Considered (Severity Index)')
    # severity_index = open("severity_index.html", 'r', encoding='utf-8')
    # severity_index_code = severity_index.read()
    # components.html(severity_index_code, height=550)
    
    # st.subheader("Correlation of Various Factors Considered in Severity Index")
    # st.image('correlationIndex.png', use_column_width = True)
 
    # # counties = open("top20_severity.html")
    # # counties_code = counties.read()
    # # components.html(counties_code, height=600)

    combined = pd.read_csv('combined_df.csv')


    st.subheader('The Counties which Need the Most Help')

    # globalvar = globalvar.copy() 
    # globalvar.county = globalvar.county.str.replace(' County','') 

    # def n_most_severe(n): 
    #     result_series = globalvar.nlargest(n, 'severity_index').county + ", " + globalvar.nlargest(n, 'severity_index').state 
    #     final_df = result_series.to_frame() 
    #     final_df.rename({0:'Counties of Interest'}, axis = 1, inplace = True) 
    #     final_df.reset_index(inplace = True, drop = True) 
    #     return final_df 

    def get_top(n): 
        result_series = combined.nlargest(n, 'severity_index').county + ", " + combined.nlargest(n, 'severity_index').state
        final_df = result_series.to_frame() 
        final_df.rename({0:'Severity Ranking'}, axis = 1, inplace = True) 
        final_df.reset_index(inplace = True, drop = True) 
        return final_df
    
    choice = st.selectbox('Select Number of Counties', ('5','10','20','50', '100')) 
    if st.button('Submit', key = '2'):
        st.write(get_top(int(choice)))
    # choice = st.slider('Select Number of Counties', 0,100 ) 
    # if st.button('Submit', key = '2'):
    #     #  st.write(get_top(int(choice)))
    #     st.write(n_most_severe(int(choice)))
    #     st.balloons()
