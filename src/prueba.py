import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from data.constants import RT, h, G, M


# 1. Desarrollo de Taylor alrededor de r0 hasta orden 1
# Definir variable simbólica
r = sp.Symbol('r')

# Definir la función f(r) = -GM / r^2
f = -G * M / r**2

r0 = RT
taylor_order1 = f.series(r, r0, 2).removeO()  
taylor_redondeado = taylor_order1.evalf(5)  # 5 cifras significativas aprox.


print("Parte 1: ", taylor_redondeado)


f_RT = -G * M / RT**2
f_RTh = -G * M / (RT + h)**2

# Redondeamos los resultados como en el informe
f_RT_rounded = round(f_RT, 3)
f_RTh_rounded = round(f_RTh, 4)

# Calculamos la diferencia relativa usando los valores redondeados
rel_diff = abs(f_RTh_rounded - f_RT_rounded) / abs(f_RT_rounded)
rel_diff_porcent = round(rel_diff * 100, 3)

# Mostramos los resultados
print(f"f(RT) = {RT + h} m/s²")
print(f"f(RT + h) = {f_RTh_rounded} m/s²")
print(f"Diferencia relativa: {rel_diff_porcent} %")