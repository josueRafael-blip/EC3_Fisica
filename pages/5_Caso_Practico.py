import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🏦 Caso práctico: analogía con un banco")

st.write("""
Este apartado utiliza una analogía para relacionar el Principio de Torricelli con un sistema de atención en un banco.

El agua representa a los clientes, el bidón representa la entidad financiera y el orificio representa los cajeros que atienden.
""")

st.info("""
Esta comparación no significa que un banco funcione físicamente como un bidón, sino que permite visualizar cómo un flujo de salida puede disminuir conforme se reduce la cantidad disponible en el sistema.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Parámetros del banco")

    clientes_iniciales = st.slider("Clientes iniciales en espera", 10, 500, 100)
    cajeros = st.slider("Número de cajeros disponibles", 1, 10, 3)
    capacidad_base = st.slider("Capacidad de atención por cajero (clientes/min)", 1, 10, 4)

    st.markdown("### 🔁 Relación con Torricelli")

    st.write(f"""
    - Bidón → Banco
    - Agua → Clientes en espera
    - Orificio → Cajeros disponibles
    - Caudal → Clientes atendidos por minuto
    - Volumen restante → Clientes pendientes
    """)

clientes_restantes = clientes_iniciales
tiempo = 0
datos = []

while clientes_restantes > 0:
    proporcion = clientes_restantes / clientes_iniciales

    flujo_atencion = cajeros * capacidad_base * (proporcion ** 0.5)

    clientes_atendidos = min(flujo_atencion, clientes_restantes)

    datos.append({
        "Tiempo (min)": tiempo,
        "Clientes restantes": clientes_restantes,
        "Clientes atendidos por minuto": flujo_atencion
    })

    clientes_restantes -= clientes_atendidos
    tiempo += 1

df_banco = pd.DataFrame(datos)

with col2:
    st.subheader("📊 Simulación del flujo de atención")

    st.metric("⏱️ Tiempo total estimado", f"{tiempo} min")
    st.metric("👥 Clientes iniciales", clientes_iniciales)
    st.metric("🏧 Cajeros disponibles", cajeros)

    fig1, ax1 = plt.subplots()
    ax1.plot(df_banco["Tiempo (min)"], df_banco["Clientes restantes"])
    ax1.set_title("Clientes restantes en el banco")
    ax1.set_xlabel("Tiempo (min)")
    ax1.set_ylabel("Clientes restantes")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(df_banco["Tiempo (min)"], df_banco["Clientes atendidos por minuto"])
    ax2.set_title("Flujo de atención")
    ax2.set_xlabel("Tiempo (min)")
    ax2.set_ylabel("Clientes/min")
    st.pyplot(fig2)

st.markdown("### 📋 Datos de la simulación")
st.dataframe(df_banco.head(20))

st.success("""
El caso práctico permite entender que, así como el caudal del agua depende de la presión y la altura,
en un sistema de atención el flujo de salida puede analizarse como una cantidad que cambia con el tiempo.
""")
