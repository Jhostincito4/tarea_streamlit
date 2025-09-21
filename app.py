import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import base64

import streamlit as st

page_bg = """
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/Jhostincito4/tarea_streamlit/refs/heads/main/FONDOIMAGEN.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)



# --- Título de la app ---
st.title("Análisis Exploratorio de Cultivos 🌱")
st.write("Explora cómo las condiciones del suelo y clima afectan el tipo de cultivo recomendado.")

# --- Cargar dataset ---
df = pd.read_csv("datos.csv")

# --- Vista rápida ---
st.subheader("Vista rápida del dataset")
st.dataframe(df.head(10))  # muestra las 10 primeras filas

# --- Estadísticas ---
st.subheader("Estadísticas descriptivas")
st.write(df.describe())

# --- Histograma interactivo ---
st.sidebar.header("Opciones de visualización")
columna = st.sidebar.selectbox("Selecciona una variable", df.columns[:-1])  # excluye la última (label)

st.subheader(f"Histograma de {columna}")
fig, ax = plt.subplots()
sns.histplot(df[columna], kde=True, ax=ax)
st.pyplot(fig)

# --- Scatter plot interactivo ---
st.subheader("Relación entre dos variables")
x_var = st.sidebar.selectbox("Eje X", df.columns[:-1])
y_var = st.sidebar.selectbox("Eje Y", df.columns[:-1])

fig2, ax2 = plt.subplots()
sns.scatterplot(x=df[x_var], y=df[y_var], hue=df['label'], ax=ax2)
st.pyplot(fig2)

# --- Matriz de correlación ---
st.subheader("Matriz de correlación")
df_num = df.select_dtypes(include='number')
corr = df_num.corr()

fig3, ax3 = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="YlGnBu", ax=ax3, linewidths=0.5, vmin=-1, vmax=1)
ax3.set_title("Matriz de correlación de variables numéricas")
st.pyplot(fig3)








