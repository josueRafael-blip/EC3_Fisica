import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt

# 1. Configuración de la interfaz en modo ancho
st.set_page_config(
    page_title="Comparación: Teoría vs Experimento", 
    page_icon="📊", 
    layout="wide"
)

# Estilo CSS inyectado para las tarjetas de métricas
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

# --- CUERPO PRINCIPAL ---
st.title("📊 Comparación: Teoría vs Experimento")
st.markdown("""
En esta sección se contrastan los resultados teóricos puros obtenidos mediante el **Principio de Torricelli** frente a los datos empíricos medidos en el experimento real con los bidones.
""")

g = 9.81

# Layout dividido: Panel de ingreso a la izquierda, Gráficos y Resultados a la derecha
col_ingreso, col_resultados = st.columns([1, 1.2], gap="large")

with col_ingreso:
    st.subheader("⚙️ Configuración del Experimento")
    
    # Control global de la cantidad de muestras
    num_pruebas = st.slider("Número de pruebas o bidones registrados", 1, 10, 4)
    st.caption("Modifica el slider para añadir o quitar puntos de control.")
    st.markdown("<br>", unsafe_allow_html=True)

    datos = []

    # Iteración dinámica estilizada mediante expanders
    for i in range(num_pruebas):
        with st.expander(f"📦 Datos del Bidón / Prueba N° {i+1}", expanded=(i==0)):
            col1, col2, col3 = st.columns(3)

            with col1:
                altura_cm = st.number_input(
                    "Altura ($h$) (cm)",
                    min_value=1.0,
                    max_value=200.0,
                    value=30.0,
                    key=f"altura_{i}"
                )

            with col2:
                velocidad_exp = st.number_input(
                    "Vel. Exp. ($m/s$)",
                    min_value=0.0,
                    max_value=20.0,
                    value=2.30 - (i * 0.15), # Valores por defecto ligeramente variables para simular realismo
                    key=f"vel_exp_{i}"
                )

            with col3:
                alcance_exp = st.number_input(
                    "Alcance Exp. ($m$)",
                    min_value=0.0,
                    max_value=10.0,
                    value=1.00 - (i * 0.08),
                    key=f"alc_exp_{i}"
                )

            altura_m = altura_cm / 100
            velocidad_teorica = math.sqrt(2 * g * altura_m)

            if velocidad_teorica != 0:
                error_velocidad = abs((velocidad_teorica - velocidad_exp) / velocidad_teorica) * 100
            else:
                error_velocidad = 0

            datos.append({
                "Prueba": f"P{i+1}",
                "Altura (cm)": altura_cm,
                "Velocidad teórica (m/s)": velocidad_teorica,
                "Velocidad experimental (m/s)": velocidad_exp,
                "Error velocidad (%)": error_velocidad,
                "Alcance experimental (m)": alcance_exp
            })

df = pd.DataFrame(datos)

with col_resultados:
    st.subheader("📌 Métricas de Validación")
    
    # Cálculo de agregados analíticos
    promedio_error = df["Error velocidad (%)"].mean()
    max_v_teorica = df['Velocidad teórica (m/s)'].max()
    min_v_teorica = df['Velocidad teórica (m/s)'].min()

    # Fila horizontal de KPIs principales
    colA, colB, colC = st.columns(3)
    colA.metric("📉 Promedio de Error", f"{promedio_error:.2f} %")
    colB.metric("🚀 Max Vel. Teórica", f"{max_v_teorica:.2f} m/s")
    colC.metric("🐢 Min Vel. Teórica", f"{min_v_teorica:.2f} m/s")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- PROCESAMIENTO GRÁFICO EN PESTAÑAS (CORRECCIÓN TEMA OSCURO) ---
    plt.style.use('dark_background')
    
    tab_curva, tab_barras = st.tabs(["📈 Curva de Velocidades", "📊 Análisis de Error Porcentual"])
    
    grid_style = dict(color='#444444', linestyle='--', linewidth=0.5)
    text_color = '#FFFFFF'

    with tab_curva:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        fig.patch.set_alpha(0.0)
        
        ax.plot(df["Prueba"], df["Velocidad teórica (m/s)"], marker="o", color="#54C3FE", linewidth=2.5, label="Teórica (Torricelli)")
        ax.plot(df["Prueba"], df["Velocidad experimental (m/s)"], marker="s", color="#FF4B4B", linewidth=2, linestyle="--", label="Experimental")
        
        ax.set_title("Contraste de Velocidades (m/s)", fontsize=11, color=text_color, fontweight='bold')
        ax.set_xlabel("Muestras / Pruebas", fontsize=9, color=text_color)
        ax.set_ylabel("Velocidad (m/s)", fontsize=9, color=text_color)
        ax.tick_params(axis='both', colors=text_color, labelsize=9)
        ax.grid(**grid_style)
        ax.legend(facecolor='black', edgecolor='#444444', fontsize=9)
        
        st.pyplot(fig, clear_figure=True)

    with tab_barras:
        fig2, ax2 = plt.subplots(figsize=(6, 3.5))
        fig2.patch.set_alpha(0.0)
        
        # Gráfico de barras estilizado con color personalizado
        ax2.bar(df["Prueba"], df["Error velocidad (%)"], color="#22DD22", alpha=0.8, edgecolor="white", width=0.5)
        
        ax2.set_title("Error Porcentual por Unidad de Muestra", fontsize=11, color=text_color, fontweight='bold')
        ax2.set_xlabel("Muestras / Pruebas", fontsize=9, color=text_color)
        ax2.set_ylabel("Error (%)", fontsize=9, color=text_color)
        ax2.tick_params(axis='both', colors=text_color, labelsize=9)
        ax2.grid(**grid_style)
        
        st.pyplot(fig2, clear_figure=True)
        
    plt.style.use('default') # Resetear estilo

st.markdown("---")

# --- SECCIÓN DE DATOS CRUDOS Y CONCLUSIÓN GLOBAL ---
col_tabla, col_conclusion = st.columns([1.2, 1], gap="large")

with col_tabla:
    st.subheader("📋 Matriz Completa de Datos")
    # Mostramos el DataFrame ocupando el contenedor completo de la columna de manera ordenada
    st.dataframe(df, use_container_width=True, height=200)

with col_conclusion:
    st.subheader("💡 Conclusión Científica")
    st.success("""
    Este procedimiento permite validar estadísticamente si las variaciones geométricas del fluido en el laboratorio coinciden con el modelo ideal matemático. Un error general bajo indica que factores como la fricción hidráulica en el orificio y la viscosidad del agua tienen un impacto menor sobre el sistema en condiciones estándar.
    """)
