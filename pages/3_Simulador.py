import streamlit as st
import matplotlib.pyplot as plt
from module.torricelli import *

st.title("🧪 Simulador visual de Torricelli")

st.write("""
En esta sección puedes modificar la altura del agua y el diámetro del orificio.
El sistema calculará automáticamente la velocidad, presión, caudal y alcance horizontal.
""")

col_izq, col_der = st.columns([1, 1])

with col_izq:
    st.subheader("⚙️ Parámetros")

    altura_cm = st.slider("Altura del agua sobre el orificio (cm)", 1, 100, 30)
    diametro_mm = st.slider("Diámetro del orificio (mm)", 1, 20, 4)
    altura_suelo_m = st.slider("Altura del orificio al suelo (m)", 0.10, 2.00, 1.00)

    altura_m = altura_cm / 100
    diametro_m = diametro_mm / 1000

    v = velocidad(altura_m)
    q = caudal(altura_m, diametro_m)
    p = presion(altura_m)
    t = tiempo_caida(altura_suelo_m)
    x = alcance_horizontal(altura_m, altura_suelo_m)
    q_litros = litros_por_segundo(q)

    st.markdown("### 📌 Resultados")

    c1, c2 = st.columns(2)
    c1.metric("🚀 Velocidad", f"{v:.3f} m/s")
    c2.metric("⚙️ Presión", f"{p:.2f} Pa")

    c3, c4 = st.columns(2)
    c3.metric("🌊 Caudal", f"{q_litros:.4f} L/s")
    c4.metric("📏 Alcance", f"{x:.3f} m")

    st.metric("⏱️ Tiempo de caída", f"{t:.3f} s")

with col_der:
    st.subheader("💧 Representación del bidón")

    fig, ax = plt.subplots(figsize=(4, 6))

    # Bidón
    ax.plot([0, 0], [0, 10], linewidth=3)
    ax.plot([4, 4], [0, 10], linewidth=3)
    ax.plot([0, 4], [0, 0], linewidth=3)
    ax.plot([0, 4], [10, 10], linewidth=3)

    # Nivel del agua
    nivel = altura_cm / 10
    ax.fill_between([0.1, 3.9], 0, nivel, alpha=0.5)

    # Orificio
    ax.plot(4, 0.8, "o", markersize=8)

    # Chorro
    ax.arrow(4, 0.8, min(x, 3), -1.2, head_width=0.15, length_includes_head=True)

    ax.text(0.2, nivel + 0.2, f"Nivel: {altura_cm} cm")
    ax.text(4.1, 0.8, "Orificio")

    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-2, 11)
    ax.axis("off")

    st.pyplot(fig)

st.info("Mientras mayor sea la altura del agua, mayor será la presión y la velocidad de salida.")
