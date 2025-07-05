import numpy as np
import matplotlib.pyplot as plt
from data.constants import g_val, gammas
from src.utils import y_with_friction, y_without_friction, y_taylor

# Condiciones iniciales a evaluar
initial_conditions = [
    (1, 0),
    (1000, 0),
    (1, -100),
    (1000, -100),
    (0, 0.1),
    (0, 100)
]

# Tiempo de simulación
t_vals = np.linspace(0, 20, 400)

# Dividir en 3 partes (2 condiciones por parte)
condiciones_divididas = [
    initial_conditions[0:2],
    initial_conditions[2:4],
    initial_conditions[4:6]
]

# Graficar cada parte con leyenda única
for k, condiciones in enumerate(condiciones_divididas):
    fig, axs = plt.subplots(len(condiciones), len(gammas), figsize=(18, 7), sharex=True, sharey=True)
    fig.suptitle(f"Comparación de modelos de caída libre - Parte {k+1}", fontsize=16)

    for i, (y0, v0) in enumerate(condiciones):
        for j, (label, gamma_val) in enumerate(gammas.items()):
            y_real = y_with_friction(t_vals, y0, v0, g_val, gamma_val)
            y_free = y_without_friction(t_vals, y0, v0, g_val)
            y_tayl = y_taylor(t_vals, y0, v0, g_val, gamma_val)

            ax = axs[i, j]
            ax.plot(t_vals, y_real, label="Rozamiento" if (i == 0 and j == 0) else "", color="tab:blue")
            ax.plot(t_vals, y_free, "--", label="Sin rozamiento" if (i == 0 and j == 0) else "", color="tab:orange")
            ax.plot(t_vals, y_tayl, ":", label="Taylor 2° orden" if (i == 0 and j == 0) else "", color="tab:green")
            ax.set_title(f"{label}\n$y_0$={y0}, $v_0$={v0}")
            ax.grid(True)
            if i == len(condiciones) - 1:
                ax.set_xlabel("Tiempo (s)")
            if j == 0:
                ax.set_ylabel("Altura (m)")

    # Leyenda única por figura
    handles, labels = axs[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.01))
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    plt.show()



