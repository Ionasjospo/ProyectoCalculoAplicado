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

# 5. Altura necesaria para que g sea un 1 % menor que en la superficie

r_target_1pct = RT / np.sqrt(0.99)

height_1pct_drop = r_target_1pct - RT


# 6 Polinomios de Taylor de orden 2 y 3 alrededor de r0_small = 0.01 m
r0_small = 0.01

# Taylor orden 2 y 3
taylor2_small = f.series(r, r0_small, 3).removeO()

taylor3_small = f.series(r, r0_small, 4).removeO()

taylor2_small_func = sp.lambdify(r, taylor2_small.subs({G: G, M: M}), 'numpy')
taylor3_small_func = sp.lambdify(r, taylor3_small.subs({G: G, M: M}), 'numpy')

# Elegimos r_eval = 2 * r0_small para comparar valores
r_eval = 2 * r0_small

# Evaluamos la f exacta y las aproximaciones
f_exact_small   = f_lambdified(r_eval)         
f_taylor2_small = taylor2_small_func(r_eval)   
f_taylor3_small = taylor3_small_func(r_eval)   

# Errores relativos (fracción)
error_rel_t2 = abs(f_exact_small - f_taylor2_small) / abs(f_exact_small)
error_rel_t3 = abs(f_exact_small - f_taylor3_small) / abs(f_exact_small)

# 7. Gráfica de f(r) y sus Taylors de orden 2 y 3 cerca de r0_small 
radii_small = np.linspace(r0_small*0.5, r0_small*1.5, 500)
plt.figure(figsize=(8,5))


plt.plot(radii_small, f_lambdified(radii_small),         label='f(r) exacta')
# Taylor de orden 2 y 3
plt.plot(radii_small, taylor2_small_func(radii_small), '--', label='Taylor orden 2')
plt.plot(radii_small, taylor3_small_func(radii_small),  ':', label='Taylor orden 3')

plt.axvline(r0_small, color='gray', linestyle=':')  
plt.xlabel('r (m)')
plt.ylabel('Aceleración (m/s**2)')
plt.title('Aproximación de Taylor cerca de r = 0.01 m')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



print("Parte 1: ", taylor_redondeado)

print("\nParte 2: ", rel_diff_porcent_round)

print("\nParte 3: ", rel_diff_porcent_round)
print("Taylor de orden 2:", taylor_order2_simplified)
print("taylor_val_at_RTh: ", taylor_val_at_RTh)
print("error_order2: ", error_order2)

print(f"\nParte 5: Altura para 1% de caída de g: {height_1pct_drop/1e3:.2f} km")

print(f"\nParte 6: Error Taylor de orden 2 en r={r_eval} m: {error_rel_t2*100:.1f} %")
print(f"\nParte 6: Error Taylor de orden 3 en r={r_eval} m: {error_rel_t3*100:.1f} %")
