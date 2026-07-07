import streamlit as st

st.set_page_config(
    page_title="Laboratorio Virtual de Torricelli",
    page_icon="💧",
    layout="wide"
)

st.title("💧 Laboratorio Virtual del Principio de Torricelli")

st.markdown("---")

st.write("""
Bienvenido al Laboratorio Virtual del Principio de Torricelli.

Esta aplicación permite:

✅ Comprender la teoría de Torricelli

✅ Simular el comportamiento del agua

✅ Visualizar el cambio de presión durante el vaciado

✅ Comparar resultados teóricos y experimentales

✅ Aplicar el principio en un caso práctico
""")

# st.image("assets/bidon.png", width=450)

st.success("Seleccione una sección desde el menú lateral.")
