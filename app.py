import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Laboratorio Virtual de Torricelli",
    page_icon="💧",
    layout="wide"
)

# Estilos CSS adaptables (Dark/Light Mode friendly)
st.markdown("""
    <style>
    /* Usamos variables del sistema para que el texto siempre contraste con el fondo */
    .main-title {
        font-size: 40px !important;
        font-weight: 800;
        color: var(--text-color);
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px !important;
        color: #34D399; /* Un tono verde agua que resalta en ambos fondos */
        margin-bottom: 30px;
    }
    /* Cajas con fondo semitransparente que se adaptan a oscuro y claro */
    .custom-card {
        background-color: rgba(128, 128, 128, 0.1);
        padding: 22px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        height: 100%;
        color: var(--text-color);
    }
    .section-badge {
        background-color: rgba(59, 130, 246, 0.15);
        padding: 12px;
        border-radius: 8px;
        border: 1px solid rgba(59, 130, 246, 0.3);
        text-align: center;
        margin-bottom: 15px;
        font-weight: 600;
        color: var(--text-color);
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<p class="main-title">🏠 Home - Laboratorio Virtual de Torricelli</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Plataforma interactiva para el análisis de la hidrodinámica</p>', unsafe_allow_html=True)

# Contenedor Principal: Principio de Torricelli
st.markdown("""
### 💧 El Principio de Torricelli
Este proyecto combina un **experimento físico con 5 bidones** y una **aplicación web en Streamlit** para analizar de forma interactiva cómo se vacía un líquido a través de un orificio bajo la influencia de la gravedad.
""")

# Usamos st.container con borde nativo de Streamlit (se adapta perfecto al fondo)
with st.container(border=True):
    st.markdown("**Variables clave a monitorear en el flujo:**")
    v_col1, v_col2, v_col3, v_col4, v_col5 = st.columns(5)
    v_col1.metric(label="Altura del agua", value="h")
    v_col2.metric(label="Presión", value="P")
    v_col3.metric(label="Velocidad", value="v")
    v_col4.metric(label="Caudal de salida", value="Q")
    v_col5.metric(label="Tiempo vaciado", value="t")

st.markdown("---")

# Columnas del Experimento vs Simulador (Con diseño adaptativo)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="custom-card" style="border-left: 5px solid #3B82F6;">
        <h4 style="color: #3B82F6; margin-top:0;">🧪 Experimento Físico</h4>
        <p>Uso de <b>5 bidones</b> para recolectar mediciones reales y tiempos de vaciado, permitiendo contrastar la práctica directa con los modelos matemáticos teóricos.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="custom-card" style="border-left: 5px solid #10B981;">
        <h4 style="color: #10B981; margin-top:0;">💻 Simulador Digital</h4>
        <p>Modelado matemático algorítmico automatizado en Python para simular, predecir gráficos dinámicos y calcular instantáneamente los flujos de descarga.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Secciones de la aplicación organizada en una cuadrícula limpia
st.subheader("📌 Secciones del Laboratorio")

s_col1, s_col2 = st.columns(2)

with s_col1:
    st.markdown('<div class="section-badge">📖 1. Teoría</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-badge">🧪 2. Simulador</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-badge">📉 3. Simulación Dinámica</div>', unsafe_allow_html=True)

with s_col2:
    st.markdown('<div class="section-badge">🏦 4. Caso Práctico</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-badge">📊 5. Comparación</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-badge">ℹ️ 6. Acerca del Proyecto</div>', unsafe_allow_html=True)

st.write("")
st.info("💡 Consejo: Utiliza el menú desplegable de la barra lateral izquierda para navegar por los módulos.")
