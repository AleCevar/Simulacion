import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# ----- Datos -----
ar=[0.289032, -0.056645, 1.125373,
    -0.57734, 0.06708, 0.684331, 0.162843, -1.272855]
nam=['Java [0, 1[', 'Erlang [0, 1[', 'Python [0, 1[',
     'Python [1, 6]', 'C [1, 4]', 'C [1, 8]', 'Racket [1, 20]',
     'C++ [1, 10]']
z_obs = ar[7]
alpha = 0.05
name= nam[7]

z_crit = norm.ppf(1 - alpha/2)

x = np.linspace(-4, 4, 2000)
y = norm.pdf(x)

plt.plot(x, y, label='Normal estándar')

# Regiones críticas
plt.fill_between(x, y, where=(x <= -z_crit), alpha=0.3, label='Región crítica')
plt.fill_between(x, y, where=(x >= z_crit), alpha=0.3)

# Líneas
plt.axvline(-z_crit, linestyle='--')
plt.axvline(z_crit, linestyle='--')
plt.axvline(z_obs, linewidth=2, label=r'$z_{obs}$')

# Etiquetas abajo
plt.text(-z_crit, 0, f'{-z_crit:.2f}', ha='center', va='top')
plt.text(z_crit, 0, f'{z_crit:.2f}', ha='center', va='top')
plt.text(z_obs, 0, f'{z_obs:.2f}', ha='center', va='bottom')

plt.xlabel('z')
plt.ylabel('Densidad')
plt.title(name)
plt.legend()
plt.grid(True)
plt.show()