import math
import pandas as pd

g = 9.81
rho = 1000

def simular_vaciado(altura_inicial_m, diametro_orificio_m, area_tanque_m2, dt=0.2):
    """
    Simula el vaciado de un tanque usando Torricelli:
    v = sqrt(2gh)
    Q = A_orificio * v
    dh/dt = -Q / A_tanque
    """

    radio_orificio = diametro_orificio_m / 2
    area_orificio = math.pi * radio_orificio ** 2

    tiempo = 0
    altura = altura_inicial_m

    datos = []

    while altura > 0:
        velocidad = math.sqrt(2 * g * altura)
        presion = rho * g * altura
        caudal = area_orificio * velocidad
        volumen_restante = area_tanque_m2 * altura

        datos.append({
            "Tiempo (s)": tiempo,
            "Altura (m)": altura,
            "Velocidad (m/s)": velocidad,
            "Presión (Pa)": presion,
            "Caudal (L/s)": caudal * 1000,
            "Volumen restante (L)": volumen_restante * 1000
        })

        altura = altura - (caudal / area_tanque_m2) * dt
        tiempo = tiempo + dt

        if tiempo > 1000:
            break

    return pd.DataFrame(datos)
