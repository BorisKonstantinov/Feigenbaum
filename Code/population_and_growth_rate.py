"""
instructions

"""
import numpy as np
from matplotlib import pyplot


class PopulationSimulator:
    def __init__(
        self,
        population_members_per_growth_rate=100,
        resolution_mu=0.001,
        initial_population=0.3,
    ):
        self.member_count = population_members_per_growth_rate
        self.resolution_mu = resolution_mu
        self.population = initial_population
        array_length = int((4 / resolution_mu) * population_members_per_growth_rate)
        self.X = np.zeros(array_length)
        self.Y = np.zeros(array_length)

    def Map(self, µ, population):
        return µ * population * (1 - population)

    def Cycle(self):
        for µ in np.arange(0, 4, self.resolution_mu):
            self.X[int(µ * (1 / self.resolution_mu)) : int(µ * (1 / self.resolution_mu) + self.member_count)] = µ
            population = self.population
            for _ in range(5000):
                """ Itterate to approach equilibrium.""" 
                population = self.Map(µ, population)
            for i in range(self.member_count):
                population = self.Map(µ, population)
                self.Y[i] = population


    def plot(self):
        """ Plots the values of X and Y"""
        pyplot.figure(dpi=480)
        pyplot.plot(self.X, self.Y, ".", markersize=0.1)
        pyplot.xlabel("Growth rate - µ")
        pyplot.ylabel("Population")
        pyplot.title("Population supported at different growth rates")
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        self.Cycle()
        self.plot()


simulator = PopulationSimulator()
simulator.run()


