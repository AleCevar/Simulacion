import numpy as np

muestra=np.random.poisson(lam=4, size=100000)

np.savetxt("poiMuestra.txt", muestra, fmt="%.0f")