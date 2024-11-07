# -*- coding: utf-8 -*-
"""
The Lyapunov exponent is a measure of divergence between two systems, f(x) and f(x + ∆x), 
evolving from slightly different initial conditions.

Found in Chapter 2.3 Sensitivity to initial conditions: The Lyapunov exponent

This code has been modified in 2024 for the purposes of improving
readability and functionality.
Original version can be found in the appendix.
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

    def lyapunov(self, µ):
        """Returns Lyapunov exponent for rate µ over N gen."""
        x = 0.2
        dx = x + self.dx
        Σ = 0

        for _ in range(self.N):
            x = µ * x * (1 - x)
            dx = µ * dx * (1 - dx)

            diff = abs(dx - x)
            if diff == 0:
                break

            Σ += math.log(diff / self.dx)

        Σ = Σ / self.N
        return Σ

    def loop(self, start, stop):
        """Runs Lyapunov over a range of µs"""
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

        """Plot the results"""
        pyplot.figure(dpi=480)
        pyplot.xlabel("Growth rate µ")
        pyplot.ylabel("Lyapunov exponent λ")
        pyplot.title("Lyapunov exponent for the logistic map")
        pyplot.grid()
        pyplot.axhline(y=1)
        pyplot.plot(self.x, self.y, linewidth=0.1, color="black")
        pyplot.show()


calculator = LyapunovCalculator()
calculator.run()
