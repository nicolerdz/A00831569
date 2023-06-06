# -*- coding: utf-8 -*-
"""Evidencia Final UF6_A00831569.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_4oF5ITdZw4_T4rs3gFYTi7lXTDJE0zn
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title('Police Incidents Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv('https://drive.google.com/file/d/1WQ5QFkP9S1FfpAxCTxQpzWKEP5lD67uL/view?usp=drive_link')

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution.')
# Coordenadas geográficas de San Francisco
latitude = df['Latitude']
longitude = df['Longitude']

# Crear un DataFrame con las coordenadas de San Francisco
mapa = pd.DataFrame(
    np.array([[latitude, longitude]]),
    columns=['lat', 'lon']
)

mapa = mapa.dropna()
st.map(mapa.astype(float))

