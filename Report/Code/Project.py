# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:11:24 2020

@author: 967869@swansea.ac.uk
"""

from matplotlib import pyplot

# Define constants ------------------------------------------------------------

X = []
Y = []

# Define variables ------------------------------------------------------------

rate = 0
population = 0.2

# Law of the land -------------------------------------------------------------


def Law(r):
    global population
    population = r * population * (1 - population)
    # population = r - population**2
    return population


# Define functions ------------------------------------------------------------


def Cycle(r):
    global population
    for i in range(20000):
        Law(r)
    for i in range(20000, 21000):
        X.append(rate)
        Y.append(Law(r))
    population = 0.2


def Scenario():
    global rate
    for i in range(1, 2000):
        Cycle(rate)
        rate = i / 1000


Scenario()

# Create the plot
pyplot.plot(X, Y, ".")

# Show the plot
pyplot.show()
