import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


leer= pd.read_csv("/Users/antoniojaenarias/Desktop/DATA SCIENCE/GitHub mio/streamlit/prueba de julio/sevicidist.csv")
st.title("**Sevici Visualization App**")
st.write("\n")
st.write("\n")
st.write("\n")



imagen=Image.open("imagen.jpg")
imagen1=st.image(imagen)
st.write("\n")
st.write("\n")
st.write("\n")



home = st.sidebar.selectbox("Home", ["Home","Problema de Negocio", "Datos","Visualización","Filtrado","BONUS"])

if home == "Home":
    st.write("Bienvenidos a Sevici Visualization App")
    st.write("Esta pagina está dedicada a informar acerca del servicio de bicis 'Sevici'")
elif home == "Datos":
    st.write("\n")
    st.write ("Numero total de bicis Sevici en Sevilla")
    st.write("\n")
    st.write(leer["CAPACITY"].sum())
    st.write("Como podemos se puede observar que se ha aumentando la cantidad de bicis en un 20%, principalmente por al incremento de la demanda, a consecuencia del encarecimiento de los precios de los combustibles.")
    st.write("\n")
    st.write("A continuación les mostramos la cantidad de bicis que hay por calle, las cuales se han modificado tras realizar un anáilisis de aquellas zonas donde la demanda era mayor.")
    st.write(leer.loc[:,["CALLE","CAPACITY"]])


elif home == "Problema de Negocio":
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("**HIPOTÉTICO PROBLEMA DE NEGOCIO DONDE POSICIONAR BICIS ELÉCTRICAS EN SEVILLA**")
    imagen2=Image.open("imagen1.jpg")  
    imagen22=st.image(imagen2)  
    imagen3=Image.open("imagen2.jpg")  
    imagen33=st.image(imagen3)     
    st.write("Una empresa de bicis electricas nos contrata como Data Scientists y el primer proyecto en el que vamos a trabajar consiste en crear un pequeño dashboard de visualizacion para obtener informacion geográfica sobre las estaciones Sevici en Sevilla.") 

elif home == "Filtrado":
    filtrado=st.selectbox("Filtrado",["Calle","Capacidad y Distrito"])
    if filtrado == "Calle":
        calle=st.selectbox("Calle", [leer.loc[:,["CALLE"]]])
    if filtrado == "Capacidad y Distrito":
        capacidad=st.selectobox(leer.loc["CALLE"])

elif home == "Visualización":
    st.write("A continuación les mostraremos un mapa donde se muestran las localizaciones de las bicis")
    st.map(leer)
