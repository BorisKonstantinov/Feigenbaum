# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:24:32 2020

@author: 967869@swansea.ac.uk
"""

import numpy as np
from matplotlib import pyplot

# Define constants ------------------------------------------------------------

X = []
Y = []


def Law(rate):
    population = 0.2
    list = []

    for i in range(2000000):
        population = rate * population * (1 - population)

    for i in range(50000):
        population = rate * population * (1 - population)
        rounded = round(population, 5)
        if rounded not in list:
            list.append(rounded)

    return len(list)


X.append(0.5)
Y.append(Law(0.5))

X.append(1)
Y.append(Law(1))

X.append(1.5)
Y.append(Law(1.5))

X.append(2)
Y.append(Law(2))

X.append(2.5)
Y.append(Law(2.5))

for i in range(30):
    X.append(2.98 + (i / 60))
    Y.append(Law(2.98 + (i / 60)))

for j in range(1000):
    X.append(3.49 + (j / 2000))
    Y.append(Law(3.49 + (j / 2000)))

pyplot.bar(X, Y, edgecolor="green", width=0.0001)
pyplot.show()
