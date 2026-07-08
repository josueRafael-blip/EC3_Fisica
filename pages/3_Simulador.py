import streamlit as st
import math
import matplotlib.pyplot as plt
from module.torricelli import *

st.title("🧪 Simulador Visual de Torricelli")

st.write("""
En esta sección puedes cambiar los datos y ver automáticamente los resultados y el desarrollo de las operaciones.
""")

st.sidebar.subheader("⚙️ Parámetros de Control")

altura_cm = st.sidebar.slider("Altura del agua sobre el orificio (cm)", 1, 100, 30)
diametro_mm = st.sidebar.slider("Diámetro del orificio (mm)", 1, 20, 4)
altura_suelo_m = st.sidebar.slider("Altura del orificio al suelo (m)", 0.10, 2.00, 1.00)

# Conversión de unidades
h = altura_cm / 100
d = diametro_mm / 1000
r = d / 2
g = 9.81
rho = 1000

# Cálculos
v = math.sqrt(2 * g * h)
p = rho * g * h
area = math.pi * r**2
q_m3 = area * v
q_l = q_m3 * 1000
t = math.sqrt((2 * altura_suelo_m) / g)
x = v * t

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 Resultados del Sistema")

    c1, c2 = st.columns(2)
    c1.metric("🚀 Velocidad de salida", f"{v:.3f} m/s")
    c2.metric("💥 Presión hidrostática", f"{p:.1f} Pa")

    c3, c4 = st.columns(2)
    c3.metric("🌊 Caudal volumétrico", f"{q_l:.4f} L/s")
    c4.metric("📏 Alcance horizontal", f"{x:.3f} m")

    st.metric("⏱️ Tiempo de caída del fluido", f"{t:.3f} s")

    st.info("Mientras mayor sea la altura del agua, mayor será la presión, la velocidad y el alcance del chorro.")

st.markdown("---")
st.subheader("🧮 Desarrollo de las operaciones")

st.markdown("### 1. Conversión de unidades")
st.latex(fr"h = {altura_cm}\ cm = {h:.2f}\ m")
st.latex(fr"d = {diametro_mm}\ mm = {d:.4f}\ m")
st.latex(fr"r = \frac{{d}}{{2}} = \frac{{{d:.4f}}}{{2}} = {r:.4f}\ m")

st.markdown("### 2. Velocidad de salida")
st.latex(r"v=\sqrt{2gh}")
st.latex(fr"v=\sqrt{{2({g})({h:.2f})}}")
st.latex(fr"v={v:.3f}\ m/s")

st.markdown("### 3. Presión hidrostática")
st.latex(r"P=\rho gh")
st.latex(fr"P=({rho})({g})({h:.2f})")
st.latex(fr"P={p:.1f}\ Pa")

st.markdown("### 4. Área del orificio")
st.latex(r"A=\pi r^2")
st.latex(fr"A=\pi({r:.4f})^2")
st.latex(fr"A={area:.8f}\ m^2")

st.markdown("### 5. Caudal volumétrico")
st.latex(r"Q=A\cdot v")
st.latex(fr"Q=({area:.8f})({v:.3f})")
st.latex(fr"Q={q_m3:.8f}\ m^3/s")
st.latex(fr"Q={q_l:.4f}\ L/s")

st.markdown("### 6. Tiempo de caída")
st.latex(r"t=\sqrt{\frac{2y}{g}}")
st.latex(fr"t=\sqrt{{\frac{{2({altura_suelo_m:.2f})}}{{{g}}}}}")
st.latex(fr"t={t:.3f}\ s")

st.markdown("### 7. Alcance horizontal")
st.latex(r"x=v\cdot t")
st.latex(fr"x=({v:.3f})({t:.3f})")
st.latex(fr"x={x:.3f}\ m")

with col2:
    st.subheader("💧 Representación del Bidón")

    fig, ax = plt.subplots(figsize=(4, 6))

    ax.plot([0, 0], [0, 10], linewidth=3)
    ax.plot([4, 4], [0, 10], linewidth=3)
    ax.plot([0, 4], [0, 0], linewidth=3)
    ax.plot([0, 4], [10, 10], linewidth=3)

    nivel = altura_cm / 10
    ax.fill_between([0.1, 3.9], 0, nivel, alpha=0.5)

    ax.plot(4, 1, "o", markersize=8)
    ax.arrow(4, 1, min(x, 3), -1, head_width=0.15, length_includes_head=True)

    ax.text(0.4, nivel + 0.3, f"Nivel: {altura_cm} cm")
    ax.text(4.1, 1, "Orificio")

    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-2, 11)
    ax.axis("off")

    st.pyplot(fig)

