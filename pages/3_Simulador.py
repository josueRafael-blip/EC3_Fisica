import streamlit as st
import matplotlib.pyplot as plt
from module.torricelli import *

# 1. Configuración de página con diseño expandido
st.set_page_config(
    page_title="Simulador de Torricelli", 
    page_icon="🧪", 
    layout="wide"
)

# Estilo CSS personalizado para mejorar las tarjetas de métricas
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(28, 131, 225, 0.1);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(28, 131, 225, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (CONFIGURACIÓN) ---
with st.sidebar:
    st.header("⚙️ Parámetros de Control")
    st.write("Modifica las variables para ver los cambios en tiempo real.")
    
    altura_cm = st.slider("Altura del agua sobre el orificio (cm)", 1, 100, 30)
    diametro_mm = st.slider("Diámetro del orificio (mm)", 1, 20, 4)
    altura_suelo_m = st.slider("Altura del orificio al suelo (m)", 0.10, 2.00, 1.00)
    
    st.markdown("---")
    st.caption("Desarrollado para la simulación física del Principio de Torricelli.")

# --- CUERPO PRINCIPAL ---
st.title("🧪 Simulador Visual de Torricelli")
st.markdown("""
En esta sección puedes simular el comportamiento de un fluido saliendo por un orificio lateral. 
El sistema calcula automáticamente la velocidad, presión, caudal y el alcance horizontal del chorro.
""")

# Cálculos matemáticos
altura_m = altura_cm / 100
diametro_m = diametro_mm / 1000

v = velocidad(altura_m)
q = caudal(altura_m, diametro_m)
p = presion(altura_m)
t = tiempo_caida(altura_suelo_m)
x = alcance_horizontal(altura_m, altura_suelo_m)
q_litros = litros_por_segundo(q)

# División en dos grandes columnas independientes (Resultados vs Gráfico)
col_izq, col_der = st.columns([1, 1.2], gap="large")

with col_izq:
    st.subheader("📌 Resultados del Sistema")
    
    # Grid de métricas en 2x2
    c1, c2 = st.columns(2)
    c1.metric(label="🚀 Velocidad de Salida", value=f"{v:.3f} m/s")
    c2.metric(label="💥 Presión Hidrostática", value=f"{p:.1f} Pa")
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True) # Espaciador
    
    c3, c4 = st.columns(2)
    c3.metric(label="🌊 Caudal Volumétrico", value=f"{q_litros:.4f} L/s")
    c4.metric(label="📏 Alcance Horizontal", value=f"{x:.3f} m")
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    
    # Métrica destacada individual
    st.metric(label="⏱️ Tiempo de Caída del Fluido", value=f"{t:.3f} s")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **Dinámica:** Mientras mayor sea la altura del agua, mayor será la presión hidrostática en el fondo y, por ende, la velocidad y el alcance del chorro.", icon="ℹ️")

with col_der:
    st.subheader("💧 Representación del Bidón")
    
    # Configuración estética de Matplotlib para que encaje con la interfaz
    fig, ax = plt.subplots(figsize=(5, 6.5))
    fig.patch.set_alpha(0.0)  # Fondo transparente de la figura
    ax.set_facecolor("none")  # Fondo transparente del gráfico
    
    # Dibujo de las paredes del Bidón (Color gris oscuro/azul, líneas más estéticas)
    color_paredes = "#2b3a42"
    ax.plot([0, 0], [0, 10], color=color_paredes, linewidth=4)
    ax.plot([4, 4], [0, 10], color=color_paredes, linewidth=4)
    ax.plot([0, 4], [0, 0], color=color_paredes, linewidth=4)
    ax.plot([0, 4], [10, 10], color=color_paredes, linewidth=2, linestyle="--") # Tapa abierta

    # Representación del Agua (Celeste moderno con transparencia)
    nivel = altura_cm / 10
    ax.fill_between([0.1, 3.9], 0, nivel, color="#1c83e1", alpha=0.6, label="Fluido")

    # Orificio (Un punto rojo o naranja para que resalte)
    ax.plot(4, 0.8, "o", markersize=10, color="#ff4b4b", markeredgecolor="white", markeredgewidth=1.5)

    # Trayectoria simulación del Chorro (Curva suavizada en vez de flecha recta)
    import numpy as np
    # Generamos una pequeña parábola ficticia para simular el chorro de agua de forma realista
    xs = np.linspace(4, min(4 + x*2, 7.5), 50)
    ys = 0.8 - 0.1 * (xs - 4)**2
    # Filtrar para que no caiga más abajo del "suelo" ficticio del gráfico gráfico
    xs = xs[ys > -1]
    ys = ys[ys > -1]
    ax.plot(xs, ys, color="#1c83e1", linewidth=3, linestyle="-")

    # Textos anotativos estilizados
    ax.text(0.3, nivel + 0.3, f"Nivel: {altura_cm} cm", color="#1c83e1", fontsize=11, fontweight='bold')
    ax.text(4.3, 1.2, "Orificio de salida", color="#ff4b4b", fontsize=10, fontweight='bold')

    # Ajustes finales de ejes
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-1.5, 11)
    ax.axis("off") # Ocultamos el recuadro negro feo por defecto de matplotlib

    # Renderizado del gráfico limpio
    st.pyplot(fig, clear_figure=True)
