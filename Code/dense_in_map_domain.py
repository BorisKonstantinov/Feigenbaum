# -*- coding: utf-8 -*-
"""
Shows that the map x = µx(1 - x) is dense in X - the domain of the map.
µ is the rate of growth of the population, and x is the population.
x is a value between 0 and 1 because it represents the proportion
of the population.

Found in Chapter 2.2 Proof of chaotic behaviour: Dense in X

This code has been modified in 2024 for the purposes of improving
readability and functionality.
Original version can be found in the appendix.
"""
import numpy as np
from matplotlib import pyplot


class PopulationSimulator:
    """ Simulates the population growth using the map x = µx(1 - x)"""
    def __init__(self, resolution_mu=0.1, resolution_x=0.01):
        self.resolution_mu = resolution_mu
        self.resolution_x = resolution_x
        array_length = int((4 / resolution_mu) * (1 / resolution_x))
        self.X = np.zeros(array_length)
        self.Y = np.zeros(array_length)

    def Map(self, µ, x):
        """ The map x = µx(1 - x)"""
        return µ * x * (1 - x)

    def Cycle(self):
        """ Cycles through the map for µ ∈ [0, 4] and x ∈ [0, 1],
        and stores the values in X and Y"""
        index = 0
        for µ in np.arange(0, 4, self.resolution_mu):
            for x in np.arange(0, 1, self.resolution_x):
                self.X[index] = x
                self.Y[index] = self.Map(µ, x)
                index += 1

    def plot(self):
        """ Plots the values of X and Y"""
        pyplot.figure(dpi=480)
        pyplot.plot(self.X, self.Y, ".", markersize=1)
        pyplot.xlabel("x")
        pyplot.ylabel("f(x)")
        pyplot.title("Density in X")
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        """ Runs the simulation"""
        self.Cycle()
        self.plot()


simulator = PopulationSimulator()
simulator.run()
