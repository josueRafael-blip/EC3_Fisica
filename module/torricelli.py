import math

g = 9.81
rho = 1000

def velocidad(altura_m):
    return math.sqrt(2 * g * altura_m)

def area_orificio(diametro_m):
    radio = diametro_m / 2
    return math.pi * radio ** 2

def caudal(altura_m, diametro_m):
    return area_orificio(diametro_m) * velocidad(altura_m)

def presion(altura_m):
    return rho * g * altura_m

def tiempo_caida(altura_suelo_m):
    return math.sqrt((2 * altura_suelo_m) / g)

def alcance_horizontal(altura_agua_m, altura_suelo_m):
    return velocidad(altura_agua_m) * tiempo_caida(altura_suelo_m)

def litros_por_segundo(caudal_m3_s):
    return caudal_m3_s * 1000
