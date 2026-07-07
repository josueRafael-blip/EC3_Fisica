import streamlit as st

st.title("📖 Fundamento Teórico")

st.header("Principio de Torricelli")

st.latex(r"v=\sqrt{2gh}")

st.write("""
Donde:

- v = velocidad de salida
- g = gravedad (9.81 m/s²)
- h = altura del agua
""")

st.header("Caudal")

st.latex(r"Q=A\cdot v")

st.header("Presión Hidrostática")

st.latex(r"P=\rho gh")

st.info("Estas ecuaciones serán utilizadas durante toda la simulación.")
