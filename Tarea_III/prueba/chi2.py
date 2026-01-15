import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

nam=['Java [0, 1[', 'Erlang [0, 1[', 'Python [0, 1[',
     'Python [1, 6]', 'C [1, 4]', 'C [1, 8]', 'Racket [1, 20]',
     'C++ [1, 10]']
ar =[13.44188, 13.67413, 17.16914,
     4.5997, 0.41294, 22.2786, 85.8501, 22.09294]
base=[10, 10, 10, 6, 4, 8, 20, 10]
# ---- Parámetros de la prueba ----
pos=7
df = (base[pos]//2)**2-1          # grados de libertad
alpha = 0.05    # significancia
chi_obs = ar[pos]  # estadístico observado
name=nam[pos]

# ---- Valores críticos (dos colas) ----
chi_left = chi2.ppf(alpha, df)
chi_right = chi2.ppf(1 - alpha, df)

# ---- Eje x para graficar (ajústalo si chi_obs es grande) ----
x_max = max(chi2.ppf(0.999, df), chi_obs) * 1.05
x = np.linspace(0, x_max, 1200)
y = chi2.pdf(x, df)

# ---- Gráfica ----
plt.plot(x, y, label=fr'$\chi^2$ (df={df})')

# Colas críticas
#plt.fill_between(x, y, where=(x <= chi_left), alpha=0.3, label='Región crítica (izq)')
plt.fill_between(x, y, where=(x >= chi_right), alpha=0.3, label='Región crítica (der)')

# Líneas críticas y observado
#plt.axvline(chi_left, linestyle='--')
plt.axvline(chi_right, linestyle='--')
plt.axvline(chi_obs, linewidth=2, label=fr'$\chi^2_{{obs}}={chi_obs}$')

# Etiquetas (valores)
#plt.text(chi_left, 0, f'{chi_left:.3f}', ha='center', va='top')
plt.text(chi_right, 0, f'{chi_right:.3f}', ha='center', va='top')
plt.text(chi_obs, 0, f'{chi_obs:.3f}', ha='center', va='bottom')

plt.title(name)
plt.xlabel(r'$\chi^2$')
plt.ylabel('Densidad')
plt.grid(True)
plt.legend()
plt.show()

