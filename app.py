import streamlit as st

st.set_page_config(
    page_title="Laboratorio Virtual de Torricelli",
    page_icon="💧",
    layout="wide"
)

st.title("💧 Laboratorio Virtual del Principio de Torricelli")

st.markdown("""
### Proyecto de Física

Esta aplicación complementa el experimento físico realizado con bidones, permitiendo simular y analizar el comportamiento del agua según el Principio de Torricelli.

El sistema permite:

✅ Comprender la teoría de Torricelli  
✅ Calcular velocidad, presión y caudal  
✅ Simular el vaciado dinámico del bidón  
✅ Observar cómo disminuye la presión con el tiempo  
✅ Comparar teoría vs experimento  
✅ Aplicar el modelo a un caso práctico  

---
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧪 Parte experimental")
    st.write("""
    Se utilizarán bidones físicos para observar cómo cambia la salida del agua según la altura,
    el diámetro del orificio y el tiempo de vaciado.
    """)

with col2:
    st.subheader("💻 Parte digital")
    st.write("""
    La aplicación en Streamlit permite visualizar el fenómeno, realizar cálculos automáticos
    y complementar los resultados obtenidos experimentalmente.
    """)

st.success("Selecciona una sección desde el menú lateral para iniciar.")
