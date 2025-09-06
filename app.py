import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title("Análisis de vehículos usados 🚗")

# Cargar dataset
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # asegúrate de que se llame así en tu carpeta

df = load_data()

# Mostrar primeras filas
st.subheader("Vista previa de los datos")
st.write(df.head())

# Botón para construir histograma
if st.button("Mostrar histograma de precios"):
    st.subheader("Distribución de precios de vehículos")
    fig_hist = px.histogram(df, x="price", nbins=50, title="Histograma de precios")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    st.subheader("Relación entre precio y odómetro")
    fig_scatter = px.scatter(df, x="odometer", y="price",
                             title="Precio vs Kilometraje",
                             opacity=0.6)
    st.plotly_chart(fig_scatter, use_container_width=True)