import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

cars = pd.read_csv('vehicles_us.csv')

st.header('Factores que afectan a la rapidez con que se venden los vehículos')
st.write('Aquí podrás observar diferentes estadísticas de los coches que se encuetran en venta en la plataforma')


hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Mensaje a desplegar
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches según el tipo de vehículo')
    fig = go.Figure(data=[go.Histogram(x=cars['type'])])
    fig.update_layout(title_text='Distribución según el tipo de vehículo')
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir un scatter plot')

if scatter_button:
    # Mensaje a desplegar
    st.write('Explorar la relación entre el año del vahículo, el precio, la condición y el número de días posteado el anuncio')
    fig = px.scatter(cars, 
                     x="model_year", 
                     y="days_listed",
                     size="price", 
                     color="condition",
                     hover_name="price", 
                     log_x=True, 
                     size_max=60)
    fig.update_layout(title_text='Factores que afectan a la duración del anuncio')

    st.plotly_chart(fig, use_container_width=True)



