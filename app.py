import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear encabezado
st.header('Cuadro de Mandos de Vehículos en Venta')

# Opción 1: Usando botones
hist_button = st.button('Construir Histograma')
scatter_button = st.button('Construir Gráfico de Dispersión')

if hist_button:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión para Precio vs. Año de fabricación')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Opción 2: Usando casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para Precio vs. Año de fabricación')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
