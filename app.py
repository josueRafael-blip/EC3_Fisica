import streamlit as st

st.set_page_config(
    page_title="Laboratorio Virtual de Torricelli",
    page_icon="💧",
    layout="wide"
)

st.title("🏠 Home - Laboratorio Virtual de Torricelli")

st.markdown("""
## 💧 Principio de Torricelli

Este proyecto combina un **experimento físico con 5 bidones** y una **aplicación web en Streamlit** para analizar cómo sale el agua por un orificio.

La aplicación permite observar cómo cambian:

- La altura del agua
- La presión
- La velocidad de salida
- El caudal
- El tiempo de vaciado

---
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧪 Experimento físico")
    st.write("""
    Se utilizarán 5 bidones para realizar mediciones reales y comprobar el Principio de Torricelli.
    """)

with col2:
    st.subheader("💻 Simulador digital")
    st.write("""
    El simulador permite calcular y visualizar el comportamiento del agua durante el vaciado.
    """)

st.markdown("---")

st.subheader("📌 Secciones de la aplicación")

st.write("""
1. 📖 Teoría  
2. 🧪 Simulador  
3. 📉 Simulación dinámica  
4. 🏦 Caso práctico  
5. 📊 Comparación  
6. ℹ️ Acerca del proyecto  
""")

st.success("Usa el menú lateral para navegar por las secciones.")
