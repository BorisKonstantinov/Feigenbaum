import numpy as np
from matplotlib import pyplot


class PopulationSimulator:
    def __init__(
        self,
        resolution=100,
        population=0.3,
    ):
        self.resolution = resolution
        self.population = population

    def Law(self, population, rate):
        return rate * population * (1 - population)

    def cobweb(self):
        X = np.zeros(self.resolution)
        Y = np.zeros(self.resolution)
        population = self.population
        Y[0] = 0
        for rate in np.arange(0, 4, 0.001):
            for _ in range(2000):
                population = self.Law(population, rate)
            for i in range(2, self.resolution, 2):
                X[i - 2] = population
                X[i - 1] = population
                population = self.Law(population, rate)
                Y[i - 1] = population
                Y[i] = population
        X[-2] = population
        return X, Y

    def plot(self, X, Y, args, xlabel, ylabel, title):
        pyplot.plot(X, Y, args)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.title(title)
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        X, Y = self.project()
        self.plot(X, Y, ".", "x", "f(x)", "max_value experiments.py")


simulator = PopulationSimulator()
simulator.run()
