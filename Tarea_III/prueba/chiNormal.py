import numpy as np
from scipy.stats import norm, chi2
import matplotlib.pyplot as plt

df = 999_999
alpha = 0.05
chi_obs = 1000233.2889
name='C++ [1, 10]'

# Se tolera la hipotesis de varianza 🥳:  997229.0885291945 999531.1955061518 1002772.7000820216
# muestra_c_8.txt
# Se tolera la hipotesis de varianza 🥳:  997229.0885291945 1002772.4840664578 1002772.7000820216
# muestra_python_int.txt
# Se tolera la hipotesis de varianza 🥳:  997229.0885291945 999577.7238146316 1002772.7000820216
# muestra_racket_int.txt
# Se tolera la hipotesis de varianza 🥳:  997229.0885291945 999150.0486731323 1002772.7000820216
# muestra_c++_int.txt
# Se tolera la hipotesis de varianza 🥳:  997229.0885291945 1000233.2889295955 1002772.7000820216

# aproximación normal
mu = df
sigma = np.sqrt(2*df)

z = norm.ppf(1 - alpha/2)

chi_left = mu - z*sigma
chi_right = mu + z*sigma


x = np.linspace(mu - 5*sigma, mu + 5*sigma, 2000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, label='Aprox. normal a χ²')

plt.fill_between(x, y, where=(x <= chi_left), alpha=0.3)
plt.fill_between(x, y, where=(x >= chi_right), alpha=0.3)

plt.axvline(chi_left, linestyle='--', label='Crítico izq')
plt.axvline(chi_right, linestyle='--', label='Crítico der')
plt.axvline(chi_obs, linewidth=2, label=r'$\chi^2_{obs}$')

plt.xlabel(r'$\chi^2$')
plt.ylabel('Densidad')
plt.title(name)
plt.legend()
plt.grid(True)
plt.show()