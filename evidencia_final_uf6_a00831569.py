# -*- coding: utf-8 -*-
"""Evidencia Final UF6_A00831569.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_4oF5ITdZw4_T4rs3gFYTi7lXTDJE0zn
"""
import streamlit as st
#import numpy as np
import pandas as pd
#import plotly as px
#import plotly.figure_factury as ff
#from brokeh.plotting import figure
#import matplotlib.pyplot as plt

st.title('Police Incidents Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv('https://drive.google.com/file/d/1WQ5QFkP9S1FfpAxCTxQpzWKEP5lD67uL/view?usp=drive_link')
st.dataframe(df)
st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')

mapa['Date']= df['Incident Date']
mapa['Day']= df['Incident Day of Week']
mapa['Police District']= df['Police District']
mapa['Neighborhood']= df['Analysis Neighborhood']
mapa['Incident Category']= df['Incidents Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa=pd.DataFrame(df['Latitude'], df['Longitude'])
mapa=mapa.dropna()
st.map(mapa.astype(int))



