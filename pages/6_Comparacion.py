import math
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Comparación teórica y experimental",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Comparación: teoría, software y experimento")

st.write(
    """
    En esta sección se ingresan los mismos datos utilizados en los cálculos
    manuales. El sistema calcula los resultados teóricos y permite compararlos
    con cinco mediciones experimentales realizadas bajo las mismas condiciones.
    """
)

st.info(
    """
    Para la parte experimental se debe utilizar un solo orificio. El recipiente
    debe llenarse hasta la misma altura antes de cada prueba y se deben registrar
    cinco mediciones del alcance horizontal del chorro.
    """
)

# ---------------------------------------------------------
# 1. DATOS DE ENTRADA
# ---------------------------------------------------------

st.header("1. Datos utilizados")

col1, col2 = st.columns(2)

with col1:
    altura_agua_cm = st.number_input(
        "Altura total del agua (cm)",
        min_value=1.0,
        value=50.0,
        step=1.0
    )

    altura_orificio_cm = st.number_input(
        "Altura del orificio medida desde la base (cm)",
        min_value=0.1,
        value=20.0,
        step=1.0
    )

    diametro_orificio_mm = st.number_input(
        "Diámetro del orificio (mm)",
        min_value=0.1,
        value=5.0,
        step=0.1
    )

with col2:
    altura_suelo_cm = st.number_input(
        "Altura del orificio respecto al suelo (cm)",
        min_value=0.1,
        value=30.0,
        step=1.0
    )

    gravedad = st.number_input(
        "Aceleración de la gravedad (m/s²)",
        min_value=1.0,
        value=9.81,
        step=0.01
    )

# Conversión a metros
altura_agua = altura_agua_cm / 100
altura_orificio = altura_orificio_cm / 100
altura_suelo = altura_suelo_cm / 100
diametro_orificio = diametro_orificio_mm / 1000

altura_presion = altura_agua - altura_orificio

if altura_presion <= 0:
    st.error(
        "La altura total del agua debe ser mayor que la altura del orificio."
    )
    st.stop()

# ---------------------------------------------------------
# 2. CÁLCULOS TEÓRICOS
# ---------------------------------------------------------

velocidad_teorica = math.sqrt(2 * gravedad * altura_presion)
tiempo_caida = math.sqrt((2 * altura_suelo) / gravedad)
alcance_teorico = velocidad_teorica * tiempo_caida

radio = diametro_orificio / 2
area_orificio = math.pi * radio**2
caudal = area_orificio * velocidad_teorica

st.header("2. Resultados calculados ")

m1, m2, m3 = st.columns(3)

m1.metric(
    "Altura de presión",
    f"{altura_presion:.4f} m"
)

m2.metric(
    "Velocidad teórica",
    f"{velocidad_teorica:.4f} m/s"
)

m3.metric(
    "Tiempo de caída",
    f"{tiempo_caida:.4f} s"
)

m4, m5, m6 = st.columns(3)

m4.metric(
    "Alcance horizontal teórico",
    f"{alcance_teorico:.4f} m"
)

m5.metric(
    "Área del orificio",
    f"{area_orificio:.8f} m²"
)

m6.metric(
    "Caudal teórico",
    f"{caudal:.8f} m³/s"
)

# ---------------------------------------------------------
# 3. DESARROLLO DE LAS FÓRMULAS
# ---------------------------------------------------------

with st.expander("Ver desarrollo de los cálculos"):
    st.subheader("Altura de presión")

    st.latex(r"h = H - y")

    st.write(
        f"""
        h = {altura_agua:.4f} - {altura_orificio:.4f}
        = {altura_presion:.4f} m
        """
    )

    st.subheader("Velocidad de salida")

    st.latex(r"v = \sqrt{2gh}")

    st.write(
        f"""
        v = √(2 × {gravedad:.2f} × {altura_presion:.4f})
        = {velocidad_teorica:.4f} m/s
        """
    )

    st.subheader("Tiempo de caída")

    st.latex(r"t = \sqrt{\frac{2y}{g}}")

    st.write(
        f"""
        t = √((2 × {altura_suelo:.4f}) / {gravedad:.2f})
        = {tiempo_caida:.4f} s
        """
    )

    st.subheader("Alcance horizontal")

    st.latex(r"x = vt")

    st.write(
        f"""
        x = {velocidad_teorica:.4f} × {tiempo_caida:.4f}
        = {alcance_teorico:.4f} m
        """
    )

    st.subheader("Caudal")

    st.latex(r"Q = Av")

    st.write(
        f"""
        Q = {area_orificio:.8f} × {velocidad_teorica:.4f}
        = {caudal:.8f} m³/s
        """
    )

# ---------------------------------------------------------
# 4. DATOS EXPERIMENTALES
# ---------------------------------------------------------

st.header("3. Cinco mediciones experimentales")

st.write(
    """
    Ingresa las cinco distancias medidas desde el recipiente hasta el punto
    donde cayó el chorro de agua. Todas las mediciones deben realizarse con el
    mismo orificio y con la misma altura inicial de agua.
    """
)

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    medida_1_cm = st.number_input(
        "Medición 1 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with c2:
    medida_2_cm = st.number_input(
        "Medición 2 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with c3:
    medida_3_cm = st.number_input(
        "Medición 3 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with c4:
    medida_4_cm = st.number_input(
        "Medición 4 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

with c5:
    medida_5_cm = st.number_input(
        "Medición 5 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1
    )

medidas_cm = [
    medida_1_cm,
    medida_2_cm,
    medida_3_cm,
    medida_4_cm,
    medida_5_cm
]

tabla_mediciones = pd.DataFrame({
    "Medición": [1, 2, 3, 4, 5],
    "Alcance experimental (cm)": medidas_cm
})

st.dataframe(
    tabla_mediciones,
    use_container_width=True,
    hide_index=True
)

# ---------------------------------------------------------
# 5. COMPARACIÓN
# ---------------------------------------------------------

st.header("4. Comparación de resultados")

if all(medida > 0 for medida in medidas_cm):

    promedio_cm = sum(medidas_cm) / len(medidas_cm)
    promedio_m = promedio_cm / 100

    diferencia_m = abs(alcance_teorico - promedio_m)

    error_porcentual = (
        diferencia_m / alcance_teorico
    ) * 100

    resultado1, resultado2, resultado3 = st.columns(3)

    resultado1.metric(
        "Alcance teórico",
        f"{alcance_teorico:.4f} m",
        f"{alcance_teorico * 100:.2f} cm"
    )

    resultado2.metric(
        "Promedio experimental",
        f"{promedio_m:.4f} m",
        f"{promedio_cm:.2f} cm"
    )

    resultado3.metric(
        "Error porcentual",
        f"{error_porcentual:.2f}%"
    )

    tabla_comparacion = pd.DataFrame({
        "Tipo de resultado": [
            "Teórico",
            "Experimental promedio"
        ],
        "Alcance (m)": [
            alcance_teorico,
            promedio_m
        ],
        "Alcance (cm)": [
            alcance_teorico * 100,
            promedio_cm
        ]
    })

    st.subheader("Tabla comparativa")

    st.dataframe(
        tabla_comparacion,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Cálculo del error porcentual")

    st.latex(
        r"\%Error = "
        r"\frac{|Valor\ experimental - Valor\ teórico|}"
        r"{Valor\ teórico} \times 100"
    )

    st.write(
        f"""
        Error = |{promedio_m:.4f} − {alcance_teorico:.4f}|
        / {alcance_teorico:.4f} × 100
        """
    )

    st.write(f"**Error porcentual = {error_porcentual:.2f}%**")

    if error_porcentual <= 5:
        st.success(
            """
            Los resultados experimentales presentan una diferencia pequeña
            respecto al modelo teórico. Esto indica una buena aproximación a
            la ecuación de Torricelli.
            """
        )

    elif error_porcentual <= 10:
        st.warning(
            """
            Los resultados son cercanos al valor teórico, aunque existe una
            diferencia que puede estar relacionada con errores de medición,
            pérdida de energía o variación en la altura del agua.
            """
        )

    else:
        st.error(
            """
            La diferencia es considerable. Se recomienda revisar las medidas,
            mantener constante la altura del agua y verificar la posición del
            recipiente y del instrumento de medición.
            """
        )

else:
    st.warning(
        """
        Completa las cinco mediciones experimentales con valores mayores que
        cero para generar la comparación y calcular el error porcentual.
        """
    )

# ---------------------------------------------------------
# 6. VALIDACIÓN DEL SOFTWARE
# ---------------------------------------------------------

st.header("5. Validación del software")

st.write(
    """
    La aplicación funciona como una herramienta de comprobación de los
    cálculos desarrollados manualmente. Al ingresar los mismos datos usados
    en las operaciones teóricas, el software debe producir los mismos
    resultados, debido a que utiliza las mismas ecuaciones físicas.
    """
)

st.success(
    """
    Para la evidencia del informe, toma una captura donde se observen los
    datos ingresados y otra donde aparezcan los resultados teóricos,
    experimentales y el porcentaje de error.
    """
)

st.caption(
    "Proyecto basado en la ecuación de Torricelli y el movimiento parabólico."
)
