# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:01:04 2020

@author: 967869@swansea.ac.uk
"""

import decimal as d
import multiprocessing as mp

import numpy as np
from matplotlib import pyplot


def lyapunov(rate):
    """Returns Lyapunov exponent for rate over N gen."""
    function = 0.2
    d_function = function + DX
    sigma = 0

    for _ in range(N):
        function = rate * function * (1 - function)
        d_function = rate * d_function * (1 - d_function)

        diff = abs(d_function - function)
        if diff < epsilon:
            break

        sigma += math.log(diff / DX)

    sigma = sigma / N  # (i + 2)
    return sigma


def loop(start, stop, X, Y):
    """Runs Lyapunov over a range of rates"""
    for i in range(start, stop):
        X[i - start] = i / RESOLUTION
        Y[i - start] = lyapunov(i / RESOLUTION)


def run(
    start_range=3000, end_range=4000, num_of_cpu=10, RESOLUTION=1000, DX=1e-8, N=1e4
):
    """Runs the lyapunov function"""
    X = mp.Array("d", RESOLUTION)
    Y = mp.Array("d", RESOLUTION)

    processes = []

    step = (end_range - start_range) // num_of_cpu

    if (end_range - start_range) % num_of_cpu != 0:
        leftover = (end_range - start_range) % num_of_cpu
        p = mp.Process(target=loop, args=(start_range, step + leftover, X, Y))
        processes.append(p)
        p.start()
        start_range += leftover + step

    for i in range(start_range, end_range, step):
        p = mp.Process(target=loop, args=(i, i + step, X, Y))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    ZERO = np.zeros(RESOLUTION)

    pyplot.axhline(y=0)
    pyplot.plot(X, Y)
    pyplot.show()
