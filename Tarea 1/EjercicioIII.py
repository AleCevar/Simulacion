from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 3
p = 0.5

x = [i for i in range(n+1)]
y = binom.pmf(x, n,p)


plt.bar(x,y)
plt.show()
