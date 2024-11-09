"""
The map x = µx(1 - x) can be seen to be stable between
one or many population sizes up to a certain point close to 3.57,
where the population size becomes chaotic. The graph produced
by this code shows this behaviour.

Found in Chapter 3 Towards an understanding of chaos

This code has been modified in 2024 for the purposes of improving
readability and functionality.
Original version can be found in the appendix.
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
        """ The map x = µx(1 - x)"""
        return µ * population * (1 - population)

    def Cycle(self):
        """ After a number of initial itterations the system begins
        its oscillation between stable values (where aplicable), those values are then recorded."""
        index = 0
        for µ in np.arange(0, 4, self.resolution_mu):
            # self.X[int(µ * (1 / self.resolution_mu)) : int(µ * (1 / self.resolution_mu) + self.member_count)] = µ
            population = self.population
            for _ in range(5000):
                """ Itterate to approach equilibrium.""" 
                population = self.Map(µ, population)
            for _ in range(self.member_count):
                population = self.Map(µ, population)
                self.X[index] = µ
                self.Y[index] = population
                index += 1


    def plot(self):
        """ Plots the values of X and Y"""
        pyplot.figure(dpi=480)
        pyplot.plot(self.X, self.Y, ".", markersize=0.01)
        pyplot.xlabel("Growth rate - µ")
        pyplot.ylabel("Population")
        pyplot.title("Population supported at different growth rates")
        pyplot.grid()
        pyplot.tight_layout()
        pyplot.show()

    def run(self):
        """ Runs the simulation"""
        self.Cycle()
        self.plot()


simulator = PopulationSimulator()
simulator.run()


