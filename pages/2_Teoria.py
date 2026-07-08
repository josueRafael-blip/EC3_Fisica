import streamlit as st

# Configuración de la página (opcional, pero le da un buen toque)
st.set_page_config(page_title="Fundamento Teórico", page_icon="📖", layout="centered")

# Título principal con un subtítulo limpio
st.title("📖 Fundamento Teórico")
st.markdown("---")

# --- SECCIÓN 1: TORRICELLI ---
st.header("⚡ Principio de Torricelli")

# Usamos columnas para que la fórmula y la explicación queden lado a lado o mejor distribuidas
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<br>", unsafe_allow_html=True) # Un pequeño espacio térmico
    st.latex(r"v=\sqrt{2gh}")

with col2:
    st.markdown("""
    **Donde:**
    * $v$: Velocidad de salida del fluido.
    * $g$: Aceleración de la gravedad ($9.81 \, \text{m/s}^2$).
    * $h$: Altura de la carga hidráulica (columna de agua).
    """)

st.markdown("---")

# --- SECCIÓN 2: CAUDAL Y PRESIÓN ---
# Colocamos estas dos ecuaciones en paralelo para aprovechar el espacio horizontal
col_caudal, col_presion = st.columns(2)

with col_caudal:
    st.subheader("💧 Caudal (Q)")
    with st.container(border=True): # Crea un recuadro estético alrededor
        st.latex(r"Q = A \cdot v")
        st.markdown("""
        * $Q$: Caudal o gasto volumétrico.
        * $A$: Área de la sección transversal.
        * $v$: Velocidad del fluido.
        """)

with col_presion:
    st.subheader("⛰️ Presión Hidrostática")
    with st.container(border=True):
        st.latex(r"P = \rho \cdot g \cdot h")
        st.markdown("""
        * $P$: Presión en el punto.
        * $\rho$: Densidad del fluido.
        * $g$: Gravedad.
        * $h$: Profundidad.
        """)

st.markdown("<br>", unsafe_allow_html=True)

# --- NOTA FINAL ---
st.info("💡 **Nota:** Estas ecuaciones fundamentales serán la base matemática utilizada durante toda la simulación.", icon="ℹ️")
