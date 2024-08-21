import pandas as pd 
import plotly.express as px
import streamlit as st

print("ya se instalan las librerias del proyecto")

car_data = pd.read_csv('vehicles_us.csv')
print(car_data)

hist_button =st.button('Construir Histograma')


if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos')
    
    fig = px.histogram(car_data,x='odometer',nbins=20)
    
    st.plotly_chart(fig,use_container_width = True)
    