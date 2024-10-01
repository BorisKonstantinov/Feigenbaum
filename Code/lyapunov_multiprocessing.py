# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:01:04 2020

@author: 967869@swansea.ac.uk
"""

import multiprocessing as mp

from matplotlib import pyplot


def lyapunov(rate, dx, N):
    """Returns Lyapunov exponent for rate over N gen."""
    function = 0.2
    d_function = function + dx
    sigma = 0

    for _ in range(N):
        function = rate * function * (1 - function)
        d_function = rate * d_function * (1 - d_function)

        diff = abs(d_function - function)
        if diff == 0:
            break

        sigma += math.log(diff / dx)

    sigma = sigma / N  # (i + 2)
    return sigma


def loop(start, stop, x, y, resolution, dx, N):
    """Runs Lyapunov over a range of rates"""
    for i in range(start, stop):
        x[i - start] = i / resolution
        y[i - start] = lyapunov(i / resolution, dx, N)


def run(
    start_range=3000, end_range=4000, num_of_cpu=10, resolution=1000, dx=1e-8, N=1e4
):
    """Runs the lyapunov function"""
    x = mp.Array("d", resolution)
    y = mp.Array("d", resolution)

    processes = []

    step = (end_range - start_range) // num_of_cpu

    if (end_range - start_range) % num_of_cpu != 0:
        leftover = (end_range - start_range) % num_of_cpu
        p = mp.Process(
            target=loop, args=(start_range, step + leftover, x, y, resolution, dx, N)
        )
        processes.append(p)
        p.start()
        start_range += leftover + step

    for i in range(start_range, end_range, step):
        p = mp.Process(target=loop, args=(i, i + step, x, y))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    pyplot.axhline(y=0)
    pyplot.plot(x, y)
    pyplot.show()
