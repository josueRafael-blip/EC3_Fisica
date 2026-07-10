import math

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Comparación teórica y experimental",
    page_icon="📊",
    layout="wide",
)


# =========================================================
# ENCABEZADO
# =========================================================

st.title("📊 Comparación teórica, experimental y validación del software")

st.write(
    """
    En esta sección se ingresan los mismos datos utilizados en los cálculos
    manuales del informe. El sistema calcula los resultados teóricos y permite
    compararlos con las mediciones experimentales realizadas con un solo
    orificio.
    """
)

st.info(
    """
    Para obtener una comparación válida, el experimento debe repetirse bajo
    las mismas condiciones: mismo orificio, misma altura inicial del agua y
    misma ubicación del recipiente.
    """
)


# =========================================================
# 1. DATOS UTILIZADOS
# =========================================================

st.header("1. Datos utilizados")

col1, col2 = st.columns(2)

with col1:
    altura_total_agua_cm = st.number_input(
        "Altura total del agua (cm)",
        min_value=1.0,
        value=50.0,
        step=1.0,
    )

    altura_orificio_base_cm = st.number_input(
        "Altura del orificio medida desde la base (cm)",
        min_value=0.1,
        value=20.0,
        step=1.0,
    )

    diametro_orificio_mm = st.number_input(
        "Diámetro del orificio (mm)",
        min_value=0.1,
        value=4.0,
        step=0.1,
    )

with col2:
    altura_orificio_suelo_cm = st.number_input(
        "Altura del orificio respecto al suelo (cm)",
        min_value=0.1,
        value=110.0,
        step=1.0,
    )

    gravedad = st.number_input(
        "Aceleración de la gravedad (m/s²)",
        min_value=1.0,
        value=9.81,
        step=0.01,
    )


# Conversión de unidades

altura_total_agua_m = altura_total_agua_cm / 100
altura_orificio_base_m = altura_orificio_base_cm / 100
altura_orificio_suelo_m = altura_orificio_suelo_cm / 100
diametro_orificio_m = diametro_orificio_mm / 1000

altura_presion_m = altura_total_agua_m - altura_orificio_base_m

if altura_presion_m <= 0:
    st.error(
        "La altura total del agua debe ser mayor que la altura del orificio."
    )
    st.stop()


# =========================================================
# 2. RESULTADOS CALCULADOS POR EL SOFTWARE
# =========================================================

velocidad_teorica = math.sqrt(
    2 * gravedad * altura_presion_m
)

tiempo_caida = math.sqrt(
    (2 * altura_orificio_suelo_m) / gravedad
)

alcance_teorico_m = velocidad_teorica * tiempo_caida

radio_orificio_m = diametro_orificio_m / 2

area_orificio_m2 = math.pi * radio_orificio_m**2

caudal_m3_s = area_orificio_m2 * velocidad_teorica

caudal_l_s = caudal_m3_s * 1000

caudal_ml_s = caudal_m3_s * 1_000_000


st.header("2. Resultados calculados por el software")

r1, r2, r3 = st.columns(3)

r1.metric(
    "Altura de presión",
    f"{altura_presion_m:.4f} m",
)

r2.metric(
    "Velocidad teórica",
    f"{velocidad_teorica:.4f} m/s",
)

r3.metric(
    "Tiempo de caída",
    f"{tiempo_caida:.4f} s",
)

r4, r5, r6 = st.columns(3)

r4.metric(
    "Alcance horizontal teórico",
    f"{alcance_teorico_m:.4f} m",
)

r5.metric(
    "Área del orificio",
    f"{area_orificio_m2:.8f} m²",
)

r6.metric(
    "Caudal teórico",
    f"{caudal_m3_s:.8f} m³/s",
)

st.caption(
    f"Equivalencia del caudal: {caudal_l_s:.5f} L/s "
    f"o {caudal_ml_s:.2f} mL/s."
)


# =========================================================
# 3. DESARROLLO DE LOS CÁLCULOS
# =========================================================

with st.expander("Ver desarrollo paso a paso de las fórmulas"):

    st.subheader("Altura de presión")

    st.latex(
        r"h = H - y"
    )

    st.write(
        f"""
        h = {altura_total_agua_m:.4f} - {altura_orificio_base_m:.4f}
        = {altura_presion_m:.4f} m
        """
    )

    st.subheader("Velocidad de salida")

    st.latex(
        r"v = \sqrt{2gh}"
    )

    st.write(
        f"""
        v = √(2 × {gravedad:.2f} × {altura_presion_m:.4f})
        = {velocidad_teorica:.4f} m/s
        """
    )

    st.subheader("Tiempo de caída")

    st.latex(
        r"t = \sqrt{\frac{2y}{g}}"
    )

    st.write(
        f"""
        t = √((2 × {altura_orificio_suelo_m:.4f}) / {gravedad:.2f})
        = {tiempo_caida:.4f} s
        """
    )

    st.subheader("Alcance horizontal")

    st.latex(
        r"x = vt"
    )

    st.write(
        f"""
        x = {velocidad_teorica:.4f} × {tiempo_caida:.4f}
        = {alcance_teorico_m:.4f} m
        """
    )

    st.subheader("Área del orificio")

    st.latex(
        r"A = \pi r^2"
    )

    st.write(
        f"""
        A = π × ({radio_orificio_m:.4f})²
        = {area_orificio_m2:.8f} m²
        """
    )

    st.subheader("Caudal")

    st.latex(
        r"Q = Av"
    )

    st.write(
        f"""
        Q = {area_orificio_m2:.8f} × {velocidad_teorica:.4f}
        = {caudal_m3_s:.8f} m³/s
        """
    )


# =========================================================
# 4. COMPARACIÓN DEL ALCANCE HORIZONTAL
# =========================================================

st.header("3. Cinco mediciones experimentales del alcance")

st.write(
    """
    Ingresa las cinco distancias medidas desde la salida del orificio hasta
    el punto donde cayó el chorro de agua. Las mediciones deben registrarse
    en centímetros.
    """
)

a1, a2, a3, a4, a5 = st.columns(5)

with a1:
    alcance_1_cm = st.number_input(
        "Medición 1 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="alcance_1",
    )

with a2:
    alcance_2_cm = st.number_input(
        "Medición 2 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="alcance_2",
    )

with a3:
    alcance_3_cm = st.number_input(
        "Medición 3 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="alcance_3",
    )

with a4:
    alcance_4_cm = st.number_input(
        "Medición 4 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="alcance_4",
    )

with a5:
    alcance_5_cm = st.number_input(
        "Medición 5 (cm)",
        min_value=0.0,
        value=0.0,
        step=0.1,
        key="alcance_5",
    )


alcances_cm = [
    alcance_1_cm,
    alcance_2_cm,
    alcance_3_cm,
    alcance_4_cm,
    alcance_5_cm,
]

tabla_alcances = pd.DataFrame(
    {
        "Medición": [1, 2, 3, 4, 5],
        "Alcance experimental (cm)": alcances_cm,
    }
)

st.dataframe(
    tabla_alcances,
    use_container_width=True,
    hide_index=True,
)


st.header("4. Comparación del alcance horizontal")

if all(valor > 0 for valor in alcances_cm):

    promedio_alcance_cm = sum(alcances_cm) / len(alcances_cm)

    promedio_alcance_m = promedio_alcance_cm / 100

    diferencia_alcance_m = abs(
        alcance_teorico_m - promedio_alcance_m
    )

    error_alcance = (
        diferencia_alcance_m / alcance_teorico_m
    ) * 100

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Alcance teórico",
        f"{alcance_teorico_m:.4f} m",
        f"{alcance_teorico_m * 100:.2f} cm",
    )

    c2.metric(
        "Promedio experimental",
        f"{promedio_alcance_m:.4f} m",
        f"{promedio_alcance_cm:.2f} cm",
    )

    c3.metric(
        "Error porcentual",
        f"{error_alcance:.2f}%",
    )

    tabla_comparacion_alcance = pd.DataFrame(
        {
            "Resultado": [
                "Teórico",
                "Experimental promedio",
            ],
            "Alcance (m)": [
                alcance_teorico_m,
                promedio_alcance_m,
            ],
            "Alcance (cm)": [
                alcance_teorico_m * 100,
                promedio_alcance_cm,
            ],
        }
    )

    st.subheader("Tabla comparativa del alcance")

    st.dataframe(
        tabla_comparacion_alcance,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Cálculo del error porcentual")

    st.latex(
        r"\%Error = "
        r"\frac{|Valor\ experimental - Valor\ teórico|}"
        r"{Valor\ teórico} \times 100"
    )

    st.write(
        f"""
        Error = |{promedio_alcance_m:.4f} − {alcance_teorico_m:.4f}|
        / {alcance_teorico_m:.4f} × 100
        """
    )

    st.write(
        f"**Error porcentual del alcance: {error_alcance:.2f}%**"
    )

    if error_alcance <= 5:
        st.success(
            """
            El resultado experimental presenta una diferencia pequeña respecto
            al resultado teórico. Esto indica una buena aproximación al modelo
            de Torricelli.
            """
        )

    elif error_alcance <= 10:
        st.warning(
            """
            El resultado experimental es cercano al teórico, aunque existe una
            diferencia que puede deberse a errores de medición, resistencia del
            aire, pérdidas de energía o cambios en la altura del agua.
            """
        )

    else:
        st.error(
            """
            La diferencia es considerable. Se recomienda revisar las medidas,
            mantener constante la altura del agua y comprobar la posición del
            recipiente.
            """
        )

else:
    st.info(
        """
        Completa las cinco mediciones del alcance para calcular el promedio
        experimental y el porcentaje de error.
        """
    )


# =========================================================
# 5. COMPARACIÓN DEL TIEMPO DE VACIADO
# =========================================================

st.header("5. Comparación del tiempo de vaciado")

st.write(
    """
    Esta sección se basa en los datos del punto 6.3 del informe:
    altura del agua sobre el orificio de 20 cm, diámetro del orificio
    de 4 mm y volumen de agua de 250 mL.
    """
)

altura_vaciado_m = 0.20
diametro_vaciado_m = 0.004
volumen_vaciado_m3 = 250 / 1_000_000

radio_vaciado_m = diametro_vaciado_m / 2

area_vaciado_m2 = math.pi * radio_vaciado_m**2

velocidad_vaciado = math.sqrt(
    2 * gravedad * altura_vaciado_m
)

caudal_vaciado_m3_s = (
    area_vaciado_m2 * velocidad_vaciado
)

tiempo_teorico_vaciado = (
    volumen_vaciado_m3 / caudal_vaciado_m3_s
)

vt1, vt2, vt3 = st.columns(3)

vt1.metric(
    "Volumen utilizado",
    "250 mL",
)

vt2.metric(
    "Caudal teórico",
    f"{caudal_vaciado_m3_s * 1_000_000:.2f} mL/s",
)

vt3.metric(
    "Tiempo teórico de vaciado",
    f"{tiempo_teorico_vaciado:.2f} s",
)


st.subheader("Cinco tiempos experimentales")

st.write(
    """
    Registra los cinco tiempos medidos para vaciar 250 mL de agua utilizando
    el mismo orificio de 4 mm.
    """
)

t1, t2, t3, t4, t5 = st.columns(5)

with t1:
    tiempo_1 = st.number_input(
        "Tiempo 1 (s)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="tiempo_1",
    )

with t2:
    tiempo_2 = st.number_input(
        "Tiempo 2 (s)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="tiempo_2",
    )

with t3:
    tiempo_3 = st.number_input(
        "Tiempo 3 (s)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="tiempo_3",
    )

with t4:
    tiempo_4 = st.number_input(
        "Tiempo 4 (s)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="tiempo_4",
    )

with t5:
    tiempo_5 = st.number_input(
        "Tiempo 5 (s)",
        min_value=0.0,
        value=0.0,
        step=0.01,
        key="tiempo_5",
    )


tiempos_experimentales = [
    tiempo_1,
    tiempo_2,
    tiempo_3,
    tiempo_4,
    tiempo_5,
]

tabla_tiempos = pd.DataFrame(
    {
        "Prueba": [1, 2, 3, 4, 5],
        "Tiempo experimental (s)": tiempos_experimentales,
    }
)

st.dataframe(
    tabla_tiempos,
    use_container_width=True,
    hide_index=True,
)


if all(valor > 0 for valor in tiempos_experimentales):

    promedio_tiempo = (
        sum(tiempos_experimentales)
        / len(tiempos_experimentales)
    )

    diferencia_tiempo = abs(
        promedio_tiempo - tiempo_teorico_vaciado
    )

    error_tiempo = (
        diferencia_tiempo / tiempo_teorico_vaciado
    ) * 100

    tc1, tc2, tc3 = st.columns(3)

    tc1.metric(
        "Tiempo teórico",
        f"{tiempo_teorico_vaciado:.2f} s",
    )

    tc2.metric(
        "Promedio experimental",
        f"{promedio_tiempo:.2f} s",
    )

    tc3.metric(
        "Error porcentual",
        f"{error_tiempo:.2f}%",
    )

    tabla_comparacion_tiempo = pd.DataFrame(
        {
            "Resultado": [
                "Teórico",
                "Experimental promedio",
            ],
            "Tiempo (s)": [
                tiempo_teorico_vaciado,
                promedio_tiempo,
            ],
        }
    )

    st.subheader("Tabla comparativa del tiempo")

    st.dataframe(
        tabla_comparacion_tiempo,
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Cálculo del error del tiempo")

    st.latex(
        r"\%Error = "
        r"\frac{|t_{experimental}-t_{teórico}|}"
        r"{t_{teórico}}\times100"
    )

    st.write(
        f"""
        Error = |{promedio_tiempo:.2f} − {tiempo_teorico_vaciado:.2f}|
        / {tiempo_teorico_vaciado:.2f} × 100
        """
    )

    st.write(
        f"**Error porcentual del tiempo: {error_tiempo:.2f}%**"
    )

    if error_tiempo <= 5:
        st.success(
            """
            El tiempo experimental es muy cercano al tiempo teórico calculado.
            """
        )

    elif error_tiempo <= 10:
        st.warning(
            """
            Existe una diferencia moderada entre el tiempo experimental y el
            teórico. Puede deberse a pérdidas de energía o errores al medir.
            """
        )

    else:
        st.error(
            """
            La diferencia es alta. Revisa que el volumen sea exactamente
            250 mL y que el diámetro del orificio sea de 4 mm.
            """
        )

else:
    st.info(
        """
        Ingresa los cinco tiempos experimentales para calcular el promedio
        y el error porcentual.
        """
    )


# =========================================================
# 6. COMPARACIÓN CON ORIFICIO DE 8 MM
# =========================================================

st.header("6. Efecto de duplicar el diámetro del orificio")

diametro_doble_m = 0.008

radio_doble_m = diametro_doble_m / 2

area_doble_m2 = math.pi * radio_doble_m**2

caudal_doble_m3_s = (
    area_doble_m2 * velocidad_vaciado
)

tiempo_doble = (
    volumen_vaciado_m3 / caudal_doble_m3_s
)

d1, d2, d3 = st.columns(3)

d1.metric(
    "Diámetro original",
    "4 mm",
)

d2.metric(
    "Tiempo con 4 mm",
    f"{tiempo_teorico_vaciado:.2f} s",
)

d3.metric(
    "Tiempo con 8 mm",
    f"{tiempo_doble:.2f} s",
)

st.write(
    """
    Al duplicar el diámetro del orificio, el área aumenta cuatro veces.
    Como consecuencia, el caudal aumenta y el tiempo de vaciado disminuye
    aproximadamente a la cuarta parte.
    """
)


# =========================================================
# 7. VALIDACIÓN DEL SOFTWARE
# =========================================================

st.header("7. Validación del software")

st.write(
    """
    El programa utiliza las mismas ecuaciones empleadas en los cálculos
    manuales del informe. Por ello, al ingresar los mismos datos, los
    resultados obtenidos por el software deben coincidir con los resultados
    teóricos, considerando únicamente pequeñas diferencias por redondeo.
    """
)

st.success(
    """
    Para el informe, toma una captura de los datos ingresados, otra de los
    resultados teóricos y otra de la comparación con las cinco mediciones
    experimentales.
    """
)

st.caption(
    "Proyecto basado en la ecuación de Torricelli, el caudal y el movimiento parabólico."
)
