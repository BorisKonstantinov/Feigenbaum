# -*- coding: utf-8 -*-
"""
description: Population simulator
"""
import numpy as np
from matplotlib import pyplot


class PopulationSimulator:
    def __init__(
        self,
        resolution_mu = 0.1,
        resolution_x = 0.01
    ):
        self.resolution_mu = resolution_mu
        self.resolution_x = resolution_x
        array_length = int((4 / resolution_mu) * (1 / resolution_x))
        self.X = self.Y = np.zeros(array_length)

    def Map(self, µ, x):
        return µ * x * (1 - x)

    def Cycle(self):
        index = 0
        for µ in np.arange(0, 4, self.resolution_mu):
            for x in np.arange(0, 1, self.resolution_x):
                self.X[index] = x
                self.Y[index] = self.Map(µ, x)
                index += 1

    def plot(self):
        pyplot.figure(dpi=480)
        pyplot.plot(self.X, self.Y, ".", markersize=1)
        pyplot.xlabel("x")
        pyplot.ylabel("f(x)")
        pyplot.title("Density in X")
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        self.Cycle()
        self.plot()


simulator = PopulationSimulator()
simulator.run()
