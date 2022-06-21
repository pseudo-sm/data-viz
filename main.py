import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

DATA_URL = ('sales_data_sample.csv')


def load_data():

    data = pd.read_csv(DATA_URL)
    return data

def groupby_data(data,dim,measure,filter_col,filter_val):

    temp = pd.DataFrame(covid_data[covid_data[filter_col].isin([filter_val])].groupby([dim]).sum(measure)[measure])
    temp.columns.name = None
    return temp


covid_data = load_data()
st.write("Here's our first attempt at using data to create a table:")



option = st.selectbox(
    'Which number do you like best?',
     covid_data['STATUS'].unique())

grouped_data = groupby_data(covid_data,"STATE","SALES","STATUS",option)
st.bar_chart(grouped_data)