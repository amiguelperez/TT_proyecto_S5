import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de anuncios de venta de vehículos")
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón

if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehículos')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para la columna fuel')

    fig = px.scatter(car_data, y="price", x="type",
                     color="fuel", symbol="fuel")
    fig.update_traces(marker_size=10)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
