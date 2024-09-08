	# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:01:04 2020

@author: 967869@swansea.ac.uk
"""
#Imports ---------------------------------------------------------------------
import decimal as d
import multiprocessing as mp
import time
import matplotlib.pyplot as plt
import numpy as np

#Define constants ------------------------------------------------------------
START_TIME = time.time()
N = 10000
DX = 0.00000001
RESOLUTION = 1000

#   f(x) ---------------------------------------------------------------------
def lyapunov(rate):
    """Returns Lyapunov exponent for rate over N gen."""
    function = 0.2
    d_function = function+DX
    sigma = 0

    for i in range(N):
        function = rate * function * (1 - function)
        d_function = rate * d_function * (1-d_function)

        if d_function-function == 0:
            break

        sigma += d.Decimal(abs(d_function - function) / DX).ln()

    sigma = sigma / N #(i + 2)
    return sigma

#Thread  functions-------------------------------------------------------------
def loop(start, stop, X, Y):
    """Runs Lyapunov over a range of rates"""
    for i in range(start, stop):
        X[i-(3*RESOLUTION)] = i / RESOLUTION
        Y[i-(3*RESOLUTION)] = lyapunov(i / RESOLUTION)


if __name__ == '__main__':

    X = mp.Array('d', 1000)
    Y = mp.Array('d', 1000)

    CPU1 = mp.Process(target=loop, args=(3000, 3100, X, Y))
    CPU2 = mp.Process(target=loop, args=(3100, 3200, X, Y))
    CPU3 = mp.Process(target=loop, args=(3200, 3300, X, Y))
    CPU4 = mp.Process(target=loop, args=(3300, 3400, X, Y))
    CPU5 = mp.Process(target=loop, args=(3400, 3500, X, Y))
    CPU6 = mp.Process(target=loop, args=(3500, 3600, X, Y))
    CPU7 = mp.Process(target=loop, args=(3600, 3700, X, Y))
    CPU8 = mp.Process(target=loop, args=(3700, 3800, X, Y))
    CPU9 = mp.Process(target=loop, args=(3800, 3900, X, Y))
    CPU10 = mp.Process(target=loop, args=(3900, 4000, X, Y))

    CPU1.start()
    CPU2.start()
    CPU3.start()
    CPU4.start()
    CPU5.start()
    CPU6.start()
    CPU7.start()
    CPU8.start()
    CPU9.start()
    CPU10.start()

    CPU1.join()
    CPU2.join()
    CPU3.join()
    CPU4.join()
    CPU5.join()
    CPU6.join()
    CPU7.join()
    CPU8.join()
    CPU9.join()
    CPU10.join()

    ZERO = np.array(range(len(X))) * 0

    plt.plot(X, ZERO)
    plt.plot(X, Y)
    plt.show()
    print(time.time() - START_TIME)