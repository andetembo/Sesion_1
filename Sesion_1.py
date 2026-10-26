import streamlit as st

st.title("Cálculo de la gravedad específica del petróleo")
st.sidebar.title("Parámetros")

ge = st.number_input("Ingrese el valor de la gravedad específica: ")
API = (141.5/ge)-131.5
st.write("El resultado de la garvedad API es: ", API)

