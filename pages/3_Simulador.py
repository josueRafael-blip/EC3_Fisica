import streamlit as st

from module.torricelli import *

st.title("🧪 Simulador de Torricelli")

altura = st.slider(
    "Altura del agua (cm)",
    1,
    100,
    30
)

diametro = st.slider(
    "Diámetro del orificio (mm)",
    1,
    20,
    4
)

altura = altura / 100
diametro = diametro / 1000

if st.button("Calcular"):

    v = velocidad(altura)

    q = caudal(altura, diametro)

    p = presion(altura)

    c1,c2,c3 = st.columns(3)

    c1.metric("🚀 Velocidad",f"{v:.3f} m/s")

    c2.metric("🌊 Caudal",f"{q:.8f} m³/s")

    c3.metric("⚙ Presión",f"{p:.2f} Pa")
