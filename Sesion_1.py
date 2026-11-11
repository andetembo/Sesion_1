import streamlit as st
import numpy as np
import libreria_funciones as lf


st.sidebar.image("Python-Logo.png")
st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("selecciona un modulo", ["variables", "listas", "arreglos", "funciones"])

if modulos == "variables":
  st.title("Cálculo de la gravedad específica del petróleo")
  ge = st.number_input("Ingrese el valor de la gravedad específica: ", min_value = 0.1, max_value = 2.0, value = 0.85)
  API = (141.5/ge)-131.5
  st.write("El resultado de la garvedad API es: ", API)
elif modulos == "listas":
  st.write("Usted está en el modulo de listas")
  valor_inicial = st.number_input("Ingrese el valor incial de su lista", min_value = 0, max_value = 1000, value = 0)
  valor_final = st.number_input("Ingrese el valor final de su lista", min_value = 0, max_value = 10000, value = 10)
  step = st.slider("Ingrese step de su lista", min_value = 0, max_value = 10, value = 1)
  lista = list(range(valor_inicial, valor_final, step))
  st.write(lista)

elif modulos == "arreglos":
  st.write("Usted está en el modulo de arreglos")
  valor_inicial_arreglo = st.number_input("Ingrese el valor incial de su arreglo", min_value = 0, max_value = 1000, value = 0)
  valor_final_arreglo = st.number_input("Ingrese el valor final de su arreglo", min_value = 0, max_value = 10000, value = 10)
  step_arreglo = st.slider("Ingrese step de su areglo", min_value = 0, max_value = 10, value = 1)
  arreglo = np.arange(valor_inicial_arreglo, valor_final_arreglo, step_arreglo)
  st.write(arreglo)

else:
  st.write("Usted está en el modulo de funciones")
  produccion = st.number_input("Ingrese la produccion diaria en barriles: ", min_value = 0, max_value = 10000, value = 1000)
  BSW = st.number_input("Ingrese % de agua y sedimento BSW: ", min_value = 0.0, max_value = 1.0, value = 0.05)
  dias_produccion = st.slider("Ingrese los dias efectivos de produccion; ", min_value = 1, max_value = 365, value = 30)
  precio_barril = st.number_input("Ingrese precio del barril: ", min_value = 0.0, max_value = 150.0, value = 75.0 )
  ingreso = lf.produccion_neta_petroleo(produccion, BSW, dias_produccion, precio_barril)
  st.warning(ingreso)
