import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def mostrar(chi_obs, df):
    alpha = 0.05
    # aproximación normal
    mu = df
    sigma = np.sqrt(2*df)

    z = norm.ppf(1 - alpha)
    chi_right = mu + z*sigma

    x = np.linspace(mu - 5*sigma, mu + 5*sigma, 2000)
    y = norm.pdf(x, mu, sigma)

    plt.plot(x, y, label='Aprox. normal a χ²')

    plt.fill_between(x, y, where=(x >= chi_right), alpha=0.3)

    plt.axvline(chi_right, linestyle='--', label='Crítico der')
    plt.axvline(chi_obs, linewidth=2, label=r'$\chi^2_{obs}$')

    plt.xlabel(r'$\chi^2$')
    plt.ylabel('Densidad')
    plt.title(r'$\chi^2$')
    plt.legend()
    plt.grid(True)
    plt.show()