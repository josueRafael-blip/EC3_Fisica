import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt

st.title("📊 Comparación: teoría vs experimento")

st.write("""
En esta sección se comparan los resultados teóricos obtenidos con el Principio de Torricelli
frente a los resultados medidos en el experimento físico con los bidones.
""")

g = 9.81

st.subheader("⚙️ Datos del experimento")

num_pruebas = st.slider("Número de pruebas o bidones", 1, 10, 5)

datos = []

for i in range(num_pruebas):
    st.markdown(f"### Bidón / Prueba {i+1}")

    col1, col2, col3 = st.columns(3)

    with col1:
        altura_cm = st.number_input(
            f"Altura del agua sobre el orificio (cm) - Prueba {i+1}",
            min_value=1.0,
            max_value=200.0,
            value=30.0,
            key=f"altura_{i}"
        )

    with col2:
        velocidad_exp = st.number_input(
            f"Velocidad experimental (m/s) - Prueba {i+1}",
            min_value=0.0,
            max_value=20.0,
            value=2.30,
            key=f"vel_exp_{i}"
        )

    with col3:
        alcance_exp = st.number_input(
            f"Alcance experimental (m) - Prueba {i+1}",
            min_value=0.0,
            max_value=10.0,
            value=1.00,
            key=f"alc_exp_{i}"
        )

    altura_m = altura_cm / 100
    velocidad_teorica = math.sqrt(2 * g * altura_m)

    if velocidad_teorica != 0:
        error_velocidad = abs((velocidad_teorica - velocidad_exp) / velocidad_teorica) * 100
    else:
        error_velocidad = 0

    datos.append({
        "Prueba": i + 1,
        "Altura (cm)": altura_cm,
        "Velocidad teórica (m/s)": velocidad_teorica,
        "Velocidad experimental (m/s)": velocidad_exp,
        "Error velocidad (%)": error_velocidad,
        "Alcance experimental (m)": alcance_exp
    })

df = pd.DataFrame(datos)

st.markdown("---")
st.subheader("📋 Tabla comparativa")

st.dataframe(df)

st.subheader("📌 Resultados principales")

promedio_error = df["Error velocidad (%)"].mean()

colA, colB, colC = st.columns(3)

colA.metric("Promedio de error", f"{promedio_error:.2f} %")
colB.metric("Mayor velocidad teórica", f"{df['Velocidad teórica (m/s)'].max():.3f} m/s")
colC.metric("Menor velocidad teórica", f"{df['Velocidad teórica (m/s)'].min():.3f} m/s")

st.subheader("📈 Gráfica comparativa de velocidades")

fig, ax = plt.subplots()

ax.plot(df["Prueba"], df["Velocidad teórica (m/s)"], marker="o", label="Velocidad teórica")
ax.plot(df["Prueba"], df["Velocidad experimental (m/s)"], marker="o", label="Velocidad experimental")

ax.set_xlabel("Prueba / Bidón")
ax.set_ylabel("Velocidad (m/s)")
ax.set_title("Comparación entre velocidad teórica y experimental")
ax.legend()

st.pyplot(fig)

st.subheader("📉 Error porcentual por prueba")

fig2, ax2 = plt.subplots()

ax2.bar(df["Prueba"], df["Error velocidad (%)"])
ax2.set_xlabel("Prueba / Bidón")
ax2.set_ylabel("Error (%)")
ax2.set_title("Error porcentual entre teoría y experimento")

st.pyplot(fig2)

st.success("""
Esta comparación permite validar si el comportamiento observado en los bidones coincide con lo predicho
por el Principio de Torricelli. Si el error porcentual es bajo, significa que el modelo teórico representa
adecuadamente el fenómeno físico.
""")
