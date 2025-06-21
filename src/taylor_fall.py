import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# 1. Desarrollo de Taylor alrededor de r0 hasta orden 1

# Definir las variables
RT = 6.378e6  # Radio de la Tierra en metros
h = 8849      # Altura del Monte Everest
G = 6.674e-11  # Constante de gravitación universal
M = 5.972e24     # Masa de la Tierra

# Definir variable simbólica
r = sp.Symbol('r')

# Definir la función f(r) = -GM / r^2
f = -G * M / r**2

r0 = RT
taylor_order1 = f.series(r, r0, 2).removeO()  #Preguntar si se puede utilizar esta funcion o hacer desarollo completo de taylor
taylor_redondeado = taylor_order1.evalf(5)  # 5 cifras significativas aprox.




# 2. Evaluar f(RT + h) y calcular diferencia relativa con f(RT)

f_lambdified = sp.lambdify(r, f.subs({G: G, M: M}), modules='numpy') #es lo mismo que f=-G * M / r**2
f_RT = f_lambdified(RT)
f_RTh = f_lambdified(RT + h)
rel_diff = abs(f_RTh - f_RT) / abs(f_RT)
print("Valor f_RT: ",  f_RT)
print("Valor f_RTh: ", f_RTh)


rel_diff_porcent = (rel_diff * 100)
rel_diff_porcent_round = round(rel_diff_porcent, 3 - int(np.floor(np.log10(abs(rel_diff_porcent)))) - 1) if rel_diff_porcent != 0 else 0


#REVISAR PARTE DE COMPARAR CON TAYOR GRADO 2
# 3. Polinomio de Taylor de orden 2
taylor_order2 = f.series(r, r0, 3).removeO()
taylor_order2_simplified = sp.simplify(taylor_order2)

taylor_order2_func = sp.lambdify(r, taylor_order2.subs({G: G, M: M}), modules='numpy')

#Comparar f(RT + h) con el taylor de orden 2
taylor_val_at_RTh = taylor_order2_func(RT + h)
error_order2 = abs(taylor_val_at_RTh - f_RTh) / abs(f_RTh)





# 4. Graficar f(r) y el polinomio de Taylor cerca de RT
r_vals = np.linspace(RT - 10000, RT + 10000, 500)
f_vals = f_lambdified(r_vals)
taylor_vals = taylor_order2_func(r_vals)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(r_vals, f_vals, label='f(r) = -GM/r^2')
plt.plot(r_vals, taylor_vals, '--', label='Polinomio de Taylor orden 2')
plt.axvline(RT, color='gray', linestyle=':')
plt.xlabel('r (m)')
plt.ylabel('Aceleración (m/s²)')
plt.title('Comparación entre f(r) y su Taylor de orden 2 cerca de RT')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

(taylor_order1, rel_diff, error_order2)





print("Parte 1: ", taylor_redondeado)

print("\nParte 2: ", rel_diff_porcent_round)

print("\nParte 3: ", rel_diff_porcent_round)
print("Taylor de orden 2:", taylor_order2_simplified)
print("taylor_val_at_RTh: ", taylor_val_at_RTh)
print("error_order2: ", error_order2)
