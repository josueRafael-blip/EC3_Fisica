import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import time

from module.dinamica import simular_vaciado
from module.visual import dibujar_bidon

# 1. Configuración de la interfaz en modo ancho
st.set_page_config(
    page_title="Simulación Dinámica de Vaciado", 
    page_icon="📉", 
    layout="wide"
)

# Estilo CSS inyectado para mejorar las tarjetas de métricas en toda la app
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

# --- BARRA LATERAL (CONTROL DE PARÁMETROS) ---
with st.sidebar:
    st.header("⚙️ Configuración del Sistema")
    st.write("Ajusta los valores geométricos y temporales del tanque.")
    
    altura_cm = st.slider("Altura inicial del agua (cm)", 5, 100, 30)
    diametro_mm = st.slider("Diámetro del orificio (mm)", 1, 20, 4)
    area_tanque_cm2 = st.slider("Área interna del bidón (cm²)", 50, 1000, 300)
    dt = st.slider("Paso de tiempo de simulación (s)", 0.1, 1.0, 0.2)
    
    st.markdown("---")
    st.caption("A menor diámetro de orificio, mayor será la duración del vaciado.")

# --- CUERPO PRINCIPAL ---
st.title("📉 Simulación Dinámica del Vaciado")
st.markdown("""
Esta sección analiza matemáticamente el comportamiento transitorio del vaciado de un tanque. 
Observa cómo, a medida que la altura del agua disminuye, la presión hidrostática cae, reduciendo simultáneamente la velocidad y el caudal de salida.
""")

# Procesamiento de variables y simulación matemática de fondo
altura_m = altura_cm / 100
diametro_m = diametro_mm / 1000
area_tanque_m2 = area_tanque_cm2 / 10000

df = simular_vaciado(altura_m, diametro_m, area_tanque_m2, dt)

tiempo_total = df["Tiempo (s)"].iloc[-1]
velocidad_inicial = df["Velocidad (m/s)"].iloc[0]
caudal_inicial = df["Caudal (L/s)"].iloc[0]
presion_inicial = df["Presión (Pa)"].iloc[0]

# --- DISTRIBUCIÓN PRINCIPAL DE COLUMNAS ---
col_izq, col_der = st.columns([1, 1.3], gap="large")

with col_izq:
    st.subheader("📌 Condiciones Iniciales Calculadas")
    
    # Grid estético de resultados antes de iniciar
    c1, c2 = st.columns(2)
    c1.metric("⏱️ Tiempo Total Est.", f"{tiempo_total:.2f} s")
    c2.metric("⚙️ Presión Inicial", f"{presion_inicial:.1f} Pa")
    
    st.markdown("<div style='margin-top: 12px;'></div>", unsafe_allow_html=True)
    
    c3, c4 = st.columns(2)
    c3.metric("🚀 Vel. Inicial", f"{velocidad_inicial:.3f} m/s")
    c4.metric("🌊 Caudal Inicial", f"{caudal_inicial:.4f} L/s")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contenedor llamativo para el botón de acción
    with st.container(border=True):
        st.markdown("##### ¿Todo listo para la animación?")
        st.write("Presiona el botón inferior para observar el fenómeno dinámico en tiempo real.")
        iniciar = st.button("▶️ Iniciar Simulación del Vaciado", use_container_width=True, type="primary")

with col_der:
    st.subheader("💧 Animación en Tiempo Real")
    
    # Marcadores de posición estables para evitar parpadeos visuales
    espacio_bidon = st.empty()
    espacio_metricas = st.empty()

    if iniciar:
        salto = max(1, len(df) // 80)

        for i in range(0, len(df), salto):
            fila = df.iloc[i]
            porcentaje = (fila["Altura (m)"] / altura_m) * 100
            chorro = int(fila["Velocidad (m/s)"] * 60)

            # Actualización del componente dinámico HTML
            with espacio_bidon:
                components.html(dibujar_bidon(porcentaje, chorro), height=440)

            # Grid de métricas cambiando en tiempo real
            with espacio_metricas:
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("⏱️ Tiempo", f"{fila['Tiempo (s)']:.1f} s")
                m2.metric("🚀 Velocidad", f"{fila['Velocidad (m/s)']:.2f} m/s")
                m3.metric("🌊 Caudal", f"{fila['Caudal (L/s)']:.3f} L/s")
                m4.metric("⚙️ Presión", f"{fila['Presión (Pa)']:.0f} Pa")

            time.sleep(0.06)  # Animación fluida ligeramente optimizada
    else:
        # Estado de espera (Pre-renderizado estático)
        porcentaje = 100
        chorro = int(velocidad_inicial * 60)
        components.html(dibujar_bidon(porcentaje, chorro), height=440)

st.markdown("---")

# --- SECCIÓN ANALÍTICA (PESTAÑAS Y TABLAS) ---
col_graficos, col_tabla = st.columns([1.3, 1], gap="large")

with col_graficos:
    st.subheader("📊 Análisis Gráfico del Comportamiento")
    
    # Creamos pestañas para organizar las curvas limpiamente
    tab1, tab2, tab3 = st.tabs(["💧 Altura vs Tiempo", "🚀 Velocidad vs Tiempo", "🌊 Caudal vs Tiempo"])
    
    # Estilos comunes de gráficos
    color_linea = "#1c83e1"
    grid_style = dict(color='gainsboro', linestyle='--', linewidth=0.5)

    with tab1:
        fig1, ax1 = plt.subplots(figsize=(6, 3))
        fig1.patch.set_alpha(0.0)
        ax1.plot(df["Tiempo (s)"], df["Altura (m)"], color=color_linea, linewidth=2.5)
        ax1.set_xlabel("Tiempo (s)", fontsize=9)
        ax1.set_ylabel("Altura del agua (m)", fontsize=9)
        ax1.grid(**grid_style)
        st.pyplot(fig1, clear_figure=True)

    with tab2:
        fig2, ax2 = plt.subplots(figsize=(6, 3))
        fig2.patch.set_alpha(0.0)
        ax2.plot(df["Tiempo (s)"], df["Velocidad (m/s)"], color="#ff4b4b", linewidth=2.5)
        ax2.set_xlabel("Tiempo (s)", fontsize=9)
        ax2.set_ylabel("Velocidad de salida (m/s)", fontsize=9)
        ax2.grid(**grid_style)
        st.pyplot(fig2, clear_figure=True)

    with tab3:
        fig3, ax3 = plt.subplots(figsize=(6, 3))
        fig3.patch.set_alpha(0.0)
        ax3.plot(df["Tiempo (s)"], df["Caudal (L/s)"], color="#2ca02c", linewidth=2.5)
        ax3.set_xlabel("Tiempo (s)", fontsize=9)
        ax3.set_ylabel("Caudal (L/s)", fontsize=9)
        ax3.grid(**grid_style)
        st.pyplot(fig3, clear_figure=True)

with col_tabla:
    st.subheader("📋 Datos Generados (Muestra)")
    st.write("Primeras filas de la matriz computacional calculada:")
    # Desplegamos el dataframe estilizado adaptándose al ancho total
    st.dataframe(df.head(25), use_container_width=True, height=260)

# Conclusión pedagógica
st.success("💡 **Conclusión del Experimento:** Esta simulación física demuestra que el vaciado no es un proceso lineal. Debido a la disminución de la carga hidráulica (altura), el empuje disminuye gradualmente hasta llegar a cero.", icon="✅")
