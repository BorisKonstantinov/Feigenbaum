import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

def Law(µ, x):
    return µ * x * (1 - x)

def Cycle():
    for µ in np.arange(0, 4, 0.1):
        for x in np.arange(0, 1, 0.01):
            X.append(x)
            Y.append(Law(µ, x))
            

Cycle()
plt.figure(dpi=480)
plt.plot(X, Y, '.', markersize=1)
plt.grid(True)
plt.show()