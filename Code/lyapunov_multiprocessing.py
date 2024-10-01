# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:01:04 2020

@author: 967869@swansea.ac.uk
"""

import math
import multiprocessing as mp

from matplotlib import pyplot


class LyapunovCalculator:
    def __init__(
        self,
        start_range=3000,
        end_range=4000,
        num_of_cpu=10,
        resolution=1000,
        dx=0.001,
        N=10000,
    ):
        self.start_range = start_range
        self.end_range = end_range
        self.num_of_cpu = num_of_cpu
        self.resolution = resolution
        self.dx = dx
        self.N = N
        self.x = mp.Array("d", resolution)
        self.y = mp.Array("d", resolution)

    def lyapunov(self, rate):
        """Returns Lyapunov exponent for rate over N gen."""
        function = 0.2
        d_function = function + self.dx
        sigma = 0

        for _ in range(self.N):
            function = rate * function * (1 - function)
            d_function = rate * d_function * (1 - d_function)

            diff = abs(d_function - function)
            if diff == 0:
                break

            sigma += math.log(diff / self.dx)

        sigma = sigma / self.N
        return sigma

    def loop(self, start, stop):
        """Runs Lyapunov over a range of rates"""
        for i in range(start, stop):
            self.x[i - self.start_range] = i / self.resolution
            self.y[i - self.start_range] = self.lyapunov(i / self.resolution)

    def run(self):
        """Runs the lyapunov function"""
        processes = []
        step = (self.end_range - self.start_range) // self.num_of_cpu
        if (self.end_range - self.start_range) % self.num_of_cpu != 0:
            leftover = (self.end_range - self.start_range) % self.num_of_cpu
            p = mp.Process(target=self.loop, args=(self.start_range, step + leftover))
            processes.append(p)
            p.start()
            self.start_range += leftover + step

        for i in range(self.start_range, self.end_range, step):
            p = mp.Process(target=self.loop, args=(i, i + step))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        pyplot.axhline(y=1)
        pyplot.plot(self.x, self.y, linewidth=0.1)
        pyplot.show()


calculator = LyapunovCalculator()
calculator.run()
