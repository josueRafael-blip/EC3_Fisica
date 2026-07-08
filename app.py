import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Laboratorio Virtual de Torricelli",
    page_icon="💧",
    layout="wide"
)

# Estilos CSS personalizados para mejorar la estética
st.markdown("""
    <style>
    .main-title {
        font-size: 42px !important;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px !important;
        color: #4B5563;
        margin-bottom: 30px;
    }
    .feature-box {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        height: 100%;
    }
    .section-card {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #E5E7EB;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<p class="main-title">🏠 Home - Laboratorio Virtual de Torricelli</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Una plataforma interactiva para el análisis de la hidrodinámica</p>', unsafe_allow_html=True)

# Contenedor Principal: Principio de Torricelli
with st.container():
    st.markdown("""
    ### 💧 El Principio de Torricelli
    Este proyecto integra un **experimento físico con 5 bidones** y esta **aplicación interactiva** para analizar el comportamiento del flujo de un líquido a través de un orificio bajo la influencia de la gravedad.
    """)
    
    # Usamos métricas o una lista visual para las variables
    st.markdown("**Variables de análisis clave:**")
    v_col1, v_col2, v_col3, v_col4, v_col5 = st.columns(5)
    v_col1.metric(label="Altura", value="h")
    v_col2.metric(label="Presión", value="P")
    v_col3.metric(label="Velocidad", value="v")
    v_col4.metric(label="Caudal", value="Q")
    v_col5.metric(label="Tiempo", value="t")

st.markdown("---")

# Sección de los dos pilares del proyecto (Físico vs Digital)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-box">
        <h4 style='color: #1E3A8A; margin-top:0;'>🧪 Experimento Físico</h4>
        <p>Monitoreo y recolección de datos reales utilizando <b>5 bidones configurados en paralelo</b> para validar de forma práctica las ecuaciones de la hidrodinámica y comprobar el Teorema de Torricelli.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box" style="border-left-color: #10B981;">
        <h4 style='color: #065F46; margin-top:0;'>💻 Simulador Digital</h4>
        <p>Herramienta algorítmica interactiva que permite calcular, predecir y visualizar dinámicamente el comportamiento del agua y las tasas de vaciado en tiempo real.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Secciones de la app organizadas en un Grid visual
st.subheader("📌 Secciones de la aplicación")

# Crear una cuadrícula de 3 columnas para mostrar las 6 secciones de forma moderna
s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    st.markdown('<div class="section-card"><b>📖 1. Teoría</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-card"><b>🏦 4. Caso Práctico</b></div>', unsafe_allow_html=True)

with s_col2:
    st.markdown('<div class="section-card"><b>🧪 2. Simulador</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-card"><b>📊 5. Comparación</b></div>', unsafe_allow_html=True)

with s_col3:
    st.markdown('<div class="section-card"><b>📉 3. Simulación Dinámica</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-card"><b>ℹ️ 6. Acerca del Proyecto</b></div>', unsafe_allow_html=True)

st.write("")
st.success("💡 Usa el menú lateral en la izquierda para navegar libremente por las secciones.")
