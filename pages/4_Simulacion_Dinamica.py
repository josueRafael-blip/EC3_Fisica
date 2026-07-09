import streamlit as st
import matplotlib.pyplot as plt

from module.dinamica import simular_vaciado

st.set_page_config(
    page_title="Simulación Dinámica de Vaciado", 
    page_icon="📉", 
    layout="wide"
)

st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: rgba(28, 131, 225, 0.08);
        padding: 12px 18px;
        border-radius: 8px;
        border: 1px solid rgba(28, 131, 225, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Configuración del Sistema")
    st.write("Ajusta los valores geométricos y temporales del tanque.")
    
    altura_cm = st.slider("Altura inicial del agua (cm)", 5, 100, 30)
    diametro_mm = st.slider("Diámetro del orificio (mm)", 1, 20, 4)
    area_tanque_cm2 = st.slider("Área interna del bidón (cm²)", 50, 1000, 300)
    dt = st.slider("Paso de tiempo de simulación (s)", 0.1, 1.0, 0.2)
    
    st.markdown("---")
    st.caption("A menor diámetro de orificio, mayor será la duración del vaciado.")

st.title("📉 Simulación Dinámica del Vaciado")

st.markdown("""
Esta sección analiza matemáticamente el comportamiento transitorio del vaciado de un tanque. 
A medida que la altura del agua disminuye, la presión hidrostática cae, reduciendo también la velocidad y el caudal de salida.
""")

altura_m = altura_cm / 100
diametro_m = diametro_mm / 1000
area_tanque_m2 = area_tanque_cm2 / 10000

df = simular_vaciado(altura_m, diametro_m, area_tanque_m2, dt)

tiempo_total = df["Tiempo (s)"].iloc[-1]
velocidad_inicial = df["Velocidad (m/s)"].iloc[0]
caudal_inicial = df["Caudal (L/s)"].iloc[0]
presion_inicial = df["Presión (Pa)"].iloc[0]

st.subheader("📌 Condiciones Iniciales Calculadas")

c1, c2, c3, c4 = st.columns(4)
c1.metric("⏱️ Tiempo total estimado", f"{tiempo_total:.2f} s")
c2.metric("⚙️ Presión inicial", f"{presion_inicial:.1f} Pa")
c3.metric("🚀 Velocidad inicial", f"{velocidad_inicial:.3f} m/s")
c4.metric("🌊 Caudal inicial", f"{caudal_inicial:.4f} L/s")

st.markdown("---")

st.subheader("📊 Análisis gráfico del comportamiento")

plt.style.use("dark_background")

tab1, tab2, tab3, tab4 = st.tabs([
    "💧 Altura vs Tiempo",
    "⚙️ Presión vs Tiempo",
    "🚀 Velocidad vs Tiempo",
    "🌊 Caudal vs Tiempo"
])

grid_style = dict(color="#444444", linestyle="--", linewidth=0.5)
text_color = "#FFFFFF"

with tab1:
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    fig1.patch.set_alpha(0.0)
    ax1.plot(df["Tiempo (s)"], df["Altura (m)"], color="#54C3FE", linewidth=3)
    ax1.set_title("Evolución de la altura del agua", color=text_color, fontweight="bold")
    ax1.set_xlabel("Tiempo (s)", color=text_color)
    ax1.set_ylabel("Altura (m)", color=text_color)
    ax1.tick_params(axis="both", colors=text_color)
    ax1.grid(**grid_style)
    st.pyplot(fig1, clear_figure=True)

with tab2:
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    fig2.patch.set_alpha(0.0)
    ax2.plot(df["Tiempo (s)"], df["Presión (Pa)"], color="#FACC15", linewidth=3)
    ax2.set_title("Evolución de la presión hidrostática", color=text_color, fontweight="bold")
    ax2.set_xlabel("Tiempo (s)", color=text_color)
    ax2.set_ylabel("Presión (Pa)", color=text_color)
    ax2.tick_params(axis="both", colors=text_color)
    ax2.grid(**grid_style)
    st.pyplot(fig2, clear_figure=True)

with tab3:
    fig3, ax3 = plt.subplots(figsize=(7, 4))
    fig3.patch.set_alpha(0.0)
    ax3.plot(df["Tiempo (s)"], df["Velocidad (m/s)"], color="#FF4B4B", linewidth=3)
    ax3.set_title("Evolución de la velocidad de salida", color=text_color, fontweight="bold")
    ax3.set_xlabel("Tiempo (s)", color=text_color)
    ax3.set_ylabel("Velocidad (m/s)", color=text_color)
    ax3.tick_params(axis="both", colors=text_color)
    ax3.grid(**grid_style)
    st.pyplot(fig3, clear_figure=True)

with tab4:
    fig4, ax4 = plt.subplots(figsize=(7, 4))
    fig4.patch.set_alpha(0.0)
    ax4.plot(df["Tiempo (s)"], df["Caudal (L/s)"], color="#22DD22", linewidth=3)
    ax4.set_title("Evolución del caudal", color=text_color, fontweight="bold")
    ax4.set_xlabel("Tiempo (s)", color=text_color)
    ax4.set_ylabel("Caudal (L/s)", color=text_color)
    ax4.tick_params(axis="both", colors=text_color)
    ax4.grid(**grid_style)
    st.pyplot(fig4, clear_figure=True)

plt.style.use("default")

st.markdown("---")

col_tabla, col_exp = st.columns([1.3, 1])

with col_tabla:
    st.subheader("📋 Datos generados por la simulación")
    st.dataframe(df.head(30), use_container_width=True)

with col_exp:
    st.subheader("🧠 Interpretación")
    st.write("""
    Esta simulación demuestra que el vaciado no ocurre con caudal constante.
    
    Al inicio, el nivel del agua es mayor, por eso la presión, la velocidad y el caudal son más altos.
    
    Conforme el agua baja, la presión disminuye y el fluido sale cada vez con menor velocidad.
    """)

st.success("""
Conclusión: la simulación confirma que la presión, la velocidad y el caudal dependen directamente de la altura del agua.
""")
