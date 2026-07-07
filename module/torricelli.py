import math

g = 9.81

rho = 1000

def velocidad(altura):
    return math.sqrt(2 * g * altura)

def area(diametro):
    radio = diametro / 2
    return math.pi * radio**2

def caudal(altura, diametro):
    return area(diametro) * velocidad(altura)

def presion(altura):
    return rho * g * altura
