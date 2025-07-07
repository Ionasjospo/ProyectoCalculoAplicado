import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from data.constants import g_val, gammas, y0, v0
from utils import y_with_friction, y_without_friction, y_taylor

#---------------------PARTE 2--------------------------
#Ejercicio 1
t = np.linspace(0, 2, 500)  # 0 → 2 s

plt.figure(figsize=(10, 6))
for nombre, gamma in gammas.items():
    y_tay = y_taylor(t, y0, v0, g_val, gamma)         
    plt.plot(t, y_tay, "--", label=f"Taylor 2ᵒ orden – {nombre}")

y_exact = y_without_friction(t, y0, v0, g_val)
plt.plot(t, y_exact, "-", color="black", label="Caída libre (sin rozamiento)")

plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")
plt.title("Comparación: Taylor 2ᵒ orden vs. caída libre")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#Ejercicio 2
# ---------------- CONDICIONES ----------------
initial_conditions = [
    (1,    0.0),     # y0=1 m,     v0=0
    (1000, 0.0),     # y0=1000 m,  v0=0
    (1,   -100.0),   # y0=1 m,     v0=-100 m/s
    (1000,-100.0),   # y0=1000 m,  v0=-100 m/s
    (0,     0.1),    # y0=0 m,     v0=0.1 m/s
    (0,   100.0)     # y0=0 m,     v0=100 m/s
]

# ---------------- TIEMPO ---------------------
t_vals = np.linspace(0, 20, 400)

# ---------------- GRAFICADO ------------------
for label, gamma_val in gammas.items():
    fig, axs = plt.subplots(2, 3, figsize=(16, 6), sharex=True, sharey=True)
    fig.suptitle(f"Modelo con γ = {gamma_val} s⁻¹  ({label})", fontsize=15)

    for idx, (y0, v0) in enumerate(initial_conditions):
        r, c = divmod(idx, 3)          # fila, columna
        ax = axs[r, c]

        y_real = y_with_friction(t_vals, y0, v0, g_val, gamma_val)
        y_free = y_without_friction(t_vals, y0, v0, g_val)
        y_tayl = y_taylor(t_vals, y0, v0, g_val, gamma_val)

        ax.plot(t_vals, y_real,  color="tab:blue",   label="Rozamiento"      if idx==0 else "")
        ax.plot(t_vals, y_free,  "--",  color="tab:orange", label="Sin rozam." if idx==0 else "")
        ax.plot(t_vals, y_tayl,  ":",   color="tab:green",  label="Taylor 2º"  if idx==0 else "")

        ax.set_title(f"$y_0$={y0}, $v_0$={v0} m/s", fontsize=9)
        ax.grid(True)
        if r == 1:
            ax.set_xlabel("t (s)")
        if c == 0:
            ax.set_ylabel("y (m)")

    handles, labels_ = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels_, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02))
    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    plt.show()
