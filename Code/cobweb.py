# -*- coding: utf-8 -*-
"""
bla

Found in Chapter 

This code has been modified in 2024 for the purposes of improving
readability and functionality.
Original version can be found in the appendix.
"""

import numpy as np
from matplotlib import pyplot


class CobwebSimulator:
    """Simulates the population growth using the cobweb plot method"""

    def __init__(
        self,
        rate=4,
        initial_population=0.2,
        cobweb_size=320
    ):
        self.rate = rate
        self.population = initial_population
        self.array_length = int(cobweb_size)
        self.X = np.zeros(self.array_length)
        self.Y = np.zeros(self.array_length)

    def Map(self, population, µ):
        """The map x = µx(1 - x)"""
        return µ * population * (1 - population)

    def Cycle(self):
        """Generates the cobweb plot data"""
        population = self.population
        self.Y[0] = 0
        for rate in np.arange(0, 4, 0.001):
            # Initial iterations to stabilize the population
            for _ in range(1500):
                population = self.Map(population, µ=self.rate)
            
            # Generate cobweb plot data
            for i in range(2, self.array_length, 2):
                self.X[i - 2] = population
                self.X[i - 1] = population
                population = self.Map(population, µ=self.rate)
                self.Y[i - 1] = population
                self.Y[i] = population
        self.X[-2] = population

    def plot(self):
        """Plots the cobweb plot"""
        pyplot.figure(dpi=480)
        pyplot.plot(self.X, self.Y, "-", linewidth=0.1, color="black")
        pyplot.xlabel("Population")
        pyplot.ylabel("Next Population")
        pyplot.title("Cobweb Plot")
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        """Runs the simulation"""
        self.Cycle()
        self.plot()


simulator = CobwebSimulator()
simulator.run()