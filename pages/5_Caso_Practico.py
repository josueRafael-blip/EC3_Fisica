import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuración de la interfaz en modo ancho
st.set_page_config(
    page_title="Analogía Bancaria - Torricelli", 
    page_icon="🏦", 
    layout="wide"
)

# Estilo CSS inyectado para mejorar las tarjetas de métricas en modo oscuro
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

# --- BARRA LATERAL (PARÁMETROS DEL BANCO) ---
with st.sidebar:
    st.header("⚙️ Configuración del Banco")
    st.write("Ajusta las variables de atención para simular el comportamiento de la cola.")
    
    clientes_iniciales = st.slider("Clientes iniciales en espera", 10, 500, 100)
    cajeros = st.slider("Número de cajeros disponibles", 1, 10, 3)
    capacidad_base = st.slider("Capacidad base (clientes/min)", 1, 10, 4)
    
    st.markdown("---")
    st.caption("Nota: La velocidad de atención decrece con la raíz cuadrada de la proporción de clientes restantes (simulando la pérdida de presión).")

# --- CUERPO PRINCIPAL ---
st.title("🏦 Caso Práctico: Analogía con un Banco")

st.write("""
Este apartado utiliza una analogía muy intuitiva para relacionar el **Principio de Torricelli** con un sistema de atención en una sucursal bancaria. 
""")

st.info("💡 **Aclaración pedagógica:** Esta comparación no significa que un banco funcione físicamente bajo leyes hidráulicas, sino que nos ayuda a visualizar cómo un flujo dinámico de salida disminuye de manera no lineal conforme se reduce la cantidad disponible dentro de un sistema.", icon="ℹ️")

# --- CÓMPUTO LÓGICO DE LA SIMULACIÓN ---
clientes_restantes = clientes_iniciales
tiempo = 0
datos = []

while clientes_restantes > 0:
    proporcion = clientes_restantes / clientes_iniciales
    
    # Modelo matemático basado en Torricelli (v = sqrt(2gh)) -> proporcional a sqrt(h)
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

# --- DISTRIBUCIÓN DE COLUMNAS PRINCIPALES ---
col_izq, col_der = st.columns([1, 1.3], gap="large")

with col_izq:
    st.subheader("🔁 Relación de Equivalencias")
    st.write("¿Cómo se conecta la física de fluidos con el modelo de atención?")
    
    # Creamos un contenedor limpio con bordes para mostrar la tabla comparativa
    with st.container(border=True):
        st.markdown("""
        | 💧 Componente Hidráulico | 🏦 Equivalencia Bancaria |
        | :--- | :--- |
        | **El Bidón (Tanque)** | La Entidad Financiera |
        | **El Agua Almacenada** | Clientes en cola de espera |
        | **El Orificio de Salida** | Cantidad de Cajeros activos |
        | **El Caudal ($Q$)** | Clientes atendidos por minuto |
        | **Volumen Restante ($V$)** | Clientes pendientes en fila |
        """)

with col_der:
    st.subheader("📊 Simulación del Flujo de Atención")
    
    # Fila horizontal de métricas resumidas
    m1, m2, m3 = st.columns(3)
    m1.metric("⏱️ Tiempo Total", f"{tiempo} min")
    m2.metric("👥 Clientes Iniciales", f"{clientes_iniciales}")
    m3.metric("🏧 Cajeros Activos", f"{cajeros}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- GRÁFICOS CORRECTAMENTE OPTIMIZADOS PARA MODO OSCURO ---
    plt.style.use('dark_background')
    tab1, tab2 = st.tabs(["📉 Clientes en Cola", "⚡ Ritmo de Atención"])
    
    grid_style = dict(color='#444444', linestyle='--', linewidth=0.5)
    text_color = '#FFFFFF'

    with tab1:
        fig1, ax1 = plt.subplots(figsize=(6, 3.2))
        fig1.patch.set_alpha(0.0) # Transparencia de fondo
        
        ax1.plot(df_banco["Tiempo (min)"], df_banco["Clientes restantes"], color="#54C3FE", linewidth=3)
        ax1.set_title("Clientes Restantes en el Banco", fontsize=11, color=text_color, fontweight='bold')
        ax1.set_xlabel("Tiempo (min)", fontsize=9, color=text_color)
        ax1.set_ylabel("Clientes", fontsize=9, color=text_color)
        ax1.tick_params(axis='both', colors=text_color, labelsize=9)
        ax1.grid(**grid_style)
        
        st.pyplot(fig1, clear_figure=True)

    with tab2:
        fig2, ax2 = plt.subplots(figsize=(6, 3.2))
        fig2.patch.set_alpha(0.0)
        
        ax2.plot(df_banco["Tiempo (min)"], df_banco["Clientes atendidos por minuto"], color="#FF4B4B", linewidth=3)
        ax2.set_title("Flujo de Atención (Clientes / min)", fontsize=11, color=text_color, fontweight='bold')
        ax2.set_xlabel("Tiempo (min)", fontsize=9, color=text_color)
        ax2.set_ylabel("Velocidad (clientes/min)", fontsize=9, color=text_color)
        ax2.tick_params(axis='both', colors=text_color, labelsize=9)
        ax2.grid(**grid_style)
        
        st.pyplot(fig2, clear_figure=True)
        
    plt.style.use('default') # Restauración de estilo

st.markdown("---")

# --- SECCIÓN INFERIOR DE DATOS Y CONCLUSIONES ---
col_tabla, col_conclusion = st.columns([1, 1.3], gap="large")

with col_tabla:
    st.subheader("📋 Datos Históricos")
    st.dataframe(df_banco.head(20), use_container_width=True, height=220)

with col_conclusion:
    st.subheader("💡 Conclusión Analítica")
    st.success("""
    Este caso práctico nos demuestra de forma analógica que, de la misma manera en que el caudal de agua está condicionado por la presión hidrostática reinante, en un proceso de colas y servicios el flujo de salida puede modelarse matemáticamente como una variable transitoria que se auto-ajusta dinámicamente según el inventario restante del sistema.
    """)
