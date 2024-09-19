# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:11:24 2020

@author: 967869@swansea.ac.uk
"""

import numpy as np
from matplotlib import pyplot

# Define constants ------------------------------------------------------------

X = []
Y = [0]

# Define variables ------------------------------------------------------------

rate = 4
population = 0.2

# Law of the land -------------------------------------------------------------


def Law():
    global population
    population = rate * population * (1 - population)
    return population


# Define functions ------------------------------------------------------------


def Cobweb():

    for i in range(1500):
        Law()

    for i in range(320):
        X.append(population)
        X.append(population)
        Law()
        Y.append(population)
        Y.append(population)


# cobweb ----------------------------------------------------------------------

m = np.array(range(1001))
n = rate * (m / 1000) * (1 - (m / 1000))
o = m / 1000

Cobweb()
X.append(population)

pyplot.plot(m / 1000, n)
pyplot.plot(m / 1000, o)
pyplot.plot(X, Y)
pyplot.show()
