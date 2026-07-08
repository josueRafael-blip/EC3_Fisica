import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import time

from module.dinamica import simular_vaciado
from module.visual import dibujar_bidon


st.title("📉 Simulación dinámica del vaciado")

st.write("""
En esta sección se observa cómo el nivel del agua disminuye durante el vaciado.
Al bajar la altura del agua, también disminuyen la presión, la velocidad y el caudal.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Parámetros")

    altura_cm = st.slider("Altura inicial del agua (cm)", 5, 100, 30)
    diametro_mm = st.slider("Diámetro del orificio (mm)", 1, 20, 4)
    area_tanque_cm2 = st.slider("Área interna aproximada del bidón (cm²)", 50, 1000, 300)
    dt = st.slider("Paso de tiempo de simulación (s)", 0.1, 1.0, 0.2)

    altura_m = altura_cm / 100
    diametro_m = diametro_mm / 1000
    area_tanque_m2 = area_tanque_cm2 / 10000

    df = simular_vaciado(altura_m, diametro_m, area_tanque_m2, dt)

    tiempo_total = df["Tiempo (s)"].iloc[-1]
    velocidad_inicial = df["Velocidad (m/s)"].iloc[0]
    caudal_inicial = df["Caudal (L/s)"].iloc[0]
    presion_inicial = df["Presión (Pa)"].iloc[0]

    st.markdown("### 📌 Resultados iniciales")
    st.metric("⏱️ Tiempo total de vaciado", f"{tiempo_total:.2f} s")
    st.metric("🚀 Velocidad inicial", f"{velocidad_inicial:.3f} m/s")
    st.metric("🌊 Caudal inicial", f"{caudal_inicial:.4f} L/s")
    st.metric("⚙️ Presión inicial", f"{presion_inicial:.2f} Pa")

    iniciar = st.button("▶️ Iniciar simulación")


with col2:
    st.subheader("💧 Vista del bidón")

    espacio_bidon = st.empty()
    espacio_metricas = st.empty()

    if iniciar:
        salto = max(1, len(df) // 80)

        for i in range(0, len(df), salto):
            fila = df.iloc[i]

            porcentaje = (fila["Altura (m)"] / altura_m) * 100
            chorro = int(fila["Velocidad (m/s)"] * 60)

            with espacio_bidon:
                components.html(
                    dibujar_bidon(porcentaje, chorro),
                    height=480
                )

            with espacio_metricas:
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("⏱️ Tiempo", f"{fila['Tiempo (s)']:.1f} s")
                c2.metric("🚀 Velocidad", f"{fila['Velocidad (m/s)']:.3f} m/s")
                c3.metric("🌊 Caudal", f"{fila['Caudal (L/s)']:.4f} L/s")
                c4.metric("⚙️ Presión", f"{fila['Presión (Pa)']:.2f} Pa")

            time.sleep(0.08)

    else:
        porcentaje = 100
        chorro = int(velocidad_inicial * 60)

        components.html(
            dibujar_bidon(porcentaje, chorro),
            height=480
        )

    st.subheader("📊 Gráficas del comportamiento")

    fig1, ax1 = plt.subplots()
    ax1.plot(df["Tiempo (s)"], df["Altura (m)"])
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_ylabel("Altura del agua (m)")
    ax1.set_title("Disminución de la altura del agua")
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(df["Tiempo (s)"], df["Velocidad (m/s)"])
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Velocidad (m/s)")
    ax2.set_title("Cambio de la velocidad de salida")
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    ax3.plot(df["Tiempo (s)"], df["Caudal (L/s)"])
    ax3.set_xlabel("Tiempo (s)")
    ax3.set_ylabel("Caudal (L/s)")
    ax3.set_title("Cambio del caudal")
    st.pyplot(fig3)


st.markdown("### 📋 Datos generados por la simulación")
st.dataframe(df.head(20))

st.success("""
Esta simulación demuestra que el sistema no mantiene una presión constante:
a medida que baja el nivel del agua, disminuyen la altura, la presión, la velocidad y el caudal.
""")
