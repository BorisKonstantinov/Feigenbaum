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

    def max_value(self):
        X = np.zeros(self.resolution)
        Y = np.zeros(self.resolution)
        population = self.population
        for rate in np.arange(0, 4, 0.001):
            for _ in range(2000):
                population = self.Law(population, rate)
            for i in range(self.resolution):
                X[i] = population
                Y[i] = population = self.Law(population, rate)
        return X, Y

    def project(self):
        X = np.zeros(self.resolution)
        Y = np.zeros(self.resolution)
        population = self.population
        for rate in np.arange(0, 4, 0.001):
            for _ in range(2000):
                population = self.Law(population, rate)
            for i in range(self.resolution):
                X[i] = rate
                Y[i] = population = self.Law(population, rate)
        return X, Y

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

    def transitivity(self):
        


    def plot(self, X, Y, args, xlabel, ylabel, title):
        pyplot.plot(X, Y, args)
        pyplot.xlabel(xlabel)
        pyplot.ylabel(ylabel)
        pyplot.title(title)
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        self.max_value()
        self.plot()

simulator = PopulationSimulator()
simulator.run()


# -----------------------------------------------------------------------------
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
