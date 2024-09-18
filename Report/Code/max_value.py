# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:07:10 2020

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
    for i in range(2000):
        Law(r)
    for i in range(2000, 2100):
        X.append(population)
        Y.append(Law(r))
    population = 0.2


def Scenario():
    global rate
    for i in range(1, 4000):
        Cycle(rate)
        rate = i / 1000


# Run this bad boy ------------------------------------------------------------

Scenario()

# Create the plot
pyplot.plot(X, Y, ".")

# Show the plot
pyplot.show()
