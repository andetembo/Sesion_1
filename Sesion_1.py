import streamlit as st


st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("selecciona un modulo", ["variables", "listas", "arreglos", "funciones"])

if modulos == "variables":
  st.title("Cálculo de la gravedad específica del petróleo")
  ge = st.number_input("Ingrese el valor de la gravedad específica: ", min_value = 0.1, max_value = 2.0, value = 0.85)
  API = (141.5/ge)-131.5
  st.write("El resultado de la garvedad API es: ", API)
elif modulos == "listas":
  st.write("Usted está en el modulo de listas")
elif modulos == "arreglos":
  st.write("Usted está en el modulo de arreglos")
else:
  st.write("Usted está en el modulo de funciones")
