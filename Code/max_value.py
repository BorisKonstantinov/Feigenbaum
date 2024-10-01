# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:07:10 2020

@author: 967869@swansea.ac.uk
"""
import numpy as np
from matplotlib import pyplot


class PopulationSimulator:
    def __init__(
        self,
        resolution=100,
        population=0.2,
    ):
        self.resolution = resolution
        self.population = population
        self.X = np.zeros(resolution)
        self.Y = np.zeros(resolution)

    def Law(self, population, rate):
        return rate * population * (1 - population)

    def Cycle(self, rate):
        population = self.population
        for _ in range(2000):
            population = self.Law(population, rate)
        for i in range(self.resolution):
            self.X[i] = population
            self.Y[i] = self.Law(population, rate)
            population = self.Y[i]

    def Scenario(self):
        for rate in np.arange(0, 4, 0.001):
            self.Cycle(rate)

    def plot(self):
        pyplot.plot(self.X, self.Y, ".")
        pyplot.show()

    def run(self):
        self.Scenario()
        self.plot()


simulator = PopulationSimulator()
simulator.run()
