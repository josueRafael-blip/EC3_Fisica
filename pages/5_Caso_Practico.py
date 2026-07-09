import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Caso Práctico Banco",
    page_icon="🏦",
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
    st.header("⚙️ Configuración del Banco")
    clientes_iniciales = st.slider("Clientes iniciales en espera", 10, 500, 100)
    cajeros = st.slider("Número de cajeros disponibles", 1, 10, 3)
    capacidad_base = st.slider("Capacidad por cajero (clientes/min)", 1, 10, 4)

st.title("🏦 Caso Práctico: Sistema de Atención en un Banco")

st.write("""
Este apartado usa el concepto de flujo para representar un sistema de atención bancaria.
El objetivo es calcular cuánto tiempo tardan los cajeros en atender a todos los clientes.
""")

st.info("""
Aclaración: este caso no aplica directamente la ecuación de Torricelli.
Se usa como analogía de flujo: los clientes entran al sistema y salen cuando son atendidos.
""")

# Cálculos principales
capacidad_total = cajeros * capacidad_base
tiempo_total = clientes_iniciales / capacidad_total

minutos = int(tiempo_total)
segundos = (tiempo_total - minutos) * 60

# Simulación minuto a minuto
clientes_restantes = clientes_iniciales
datos = []
minuto = 0

while clientes_restantes > 0:
    datos.append({
        "Tiempo (min)": minuto,
        "Clientes restantes": max(clientes_restantes, 0),
        "Clientes atendidos por minuto": capacidad_total
    })

    clientes_restantes -= capacidad_total
    minuto += 1

datos.append({
    "Tiempo (min)": round(tiempo_total, 2),
    "Clientes restantes": 0,
    "Clientes atendidos por minuto": 0
})

df_banco = pd.DataFrame(datos)

col_izq, col_der = st.columns([1, 1.3], gap="large")

with col_izq:
    st.subheader("🔁 Relación de equivalencias")

    with st.container(border=True):
        st.markdown("""
        | 💧 Componente hidráulico | 🏦 Equivalencia bancaria |
        | :--- | :--- |
        | Bidón | Banco |
        | Agua almacenada | Clientes en espera |
        | Orificio de salida | Cajeros activos |
        | Caudal | Clientes atendidos por minuto |
        | Volumen restante | Clientes pendientes |
        """)

    st.subheader("🧮 Desarrollo de las operaciones")

    st.latex(r"\text{Capacidad total}=\text{Cajeros}\times\text{Capacidad por cajero}")
    st.latex(
        fr"\text{{Capacidad total}}={cajeros}\times{capacidad_base}={capacidad_total}\ \text{{clientes/min}}"
    )

    st.latex(r"\text{Tiempo total}=\frac{\text{Clientes iniciales}}{\text{Capacidad total}}")
    st.latex(
        fr"\text{{Tiempo total}}=\frac{{{clientes_iniciales}}}{{{capacidad_total}}}={tiempo_total:.2f}\ \text{{min}}"
    )

    st.latex(
        fr"{tiempo_total:.2f}\ \text{{min}}={minutos}\ \text{{min}}\ {segundos:.0f}\ \text{{s}}"
    )

with col_der:
    st.subheader("📊 Resultados de la simulación")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "⏱️ Tiempo total",
        f"{tiempo_total:.2f} min",
        help=f"Aproximadamente {minutos} min {segundos:.0f} s"
    )

    m2.metric("👥 Clientes iniciales", clientes_iniciales)
    m3.metric("🏧 Cajeros", cajeros)
    m4.metric("⚡ Capacidad total", f"{capacidad_total} clientes/min")

    plt.style.use("dark_background")

    tab1, tab2 = st.tabs(["📉 Clientes en cola", "⚡ Ritmo de atención"])

    grid_style = dict(color="#444444", linestyle="--", linewidth=0.5)
    text_color = "#FFFFFF"

    with tab1:
        fig1, ax1 = plt.subplots(figsize=(6, 3.2))
        fig1.patch.set_alpha(0.0)

        ax1.plot(
            df_banco["Tiempo (min)"],
            df_banco["Clientes restantes"],
            color="#54C3FE",
            linewidth=3
        )

        ax1.set_title("Clientes restantes en el banco", color=text_color, fontweight="bold")
        ax1.set_xlabel("Tiempo (min)", color=text_color)
        ax1.set_ylabel("Clientes", color=text_color)
        ax1.tick_params(axis="both", colors=text_color)
        ax1.grid(**grid_style)

        st.pyplot(fig1, clear_figure=True)

    with tab2:
        fig2, ax2 = plt.subplots(figsize=(6, 3.2))
        fig2.patch.set_alpha(0.0)

        ax2.plot(
            df_banco["Tiempo (min)"],
            df_banco["Clientes atendidos por minuto"],
            color="#FF4B4B",
            linewidth=3
        )

        ax2.set_title("Clientes atendidos por minuto", color=text_color, fontweight="bold")
        ax2.set_xlabel("Tiempo (min)", color=text_color)
        ax2.set_ylabel("Clientes/min", color=text_color)
        ax2.tick_params(axis="both", colors=text_color)
        ax2.grid(**grid_style)

        st.pyplot(fig2, clear_figure=True)

    plt.style.use("default")

st.markdown("---")

col_tabla, col_conclusion = st.columns([1, 1.3], gap="large")

with col_tabla:
    st.subheader("📋 Datos de la simulación")
    st.dataframe(df_banco, use_container_width=True, height=260)

with col_conclusion:
    st.subheader("💡 Interpretación")

    st.success(f"""
    Con {clientes_iniciales} clientes, {cajeros} cajeros y una capacidad de {capacidad_base} clientes por minuto por cajero,
    el banco puede atender {capacidad_total} clientes por minuto.

    Por ello, el tiempo total de atención es {tiempo_total:.2f} minutos,
    aproximadamente {minutos} minutos con {segundos:.0f} segundos.
    """)

    st.write("""
    En este modelo, el ritmo de atención se mantiene constante porque los cajeros conservan la misma capacidad durante todo el proceso.
    """)
