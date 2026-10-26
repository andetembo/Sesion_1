import streamlit as st

st.title("Cálculo de la gravedad específica del petróleo")
st.sidebar.title("Parámetros")

ge = st.number_input("Ingrese el valor de la gravedad específica: ", min_value = 0.1, max_value = 2.0, value = 0.85)
API = (141.5/ge)-131.5
st.write("El resultado de la garvedad API es: ", API)

