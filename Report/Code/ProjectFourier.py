# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:11:24 2020

@author: 967869@swansea.ac.uk
"""

# Imports ---------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# Define constants ------------------------------------------------------------

History = []


# Define variables ------------------------------------------------------------

rate = 2


population = 0.5

# Law of the land -------------------------------------------------------------


def Law():
    global population
    population = rate * population * (1 - population)
    return population


# Define functions ------------------------------------------------------------


def Series():
    for i in range(10000):
        Law()

    for i in range(1000):
        History.append(population)
        Law()


# cobweb ----------------------------------------------------------------------

array = np.array(range(1000))

Series()


complexfourier = fft(History)
fourier = complexfourier.real

gradient = np.gradient(np.gradient(fourier))
plt.plot(array[2::], fourier[2::], label="Fourier")


plt.plot(array[2::], History[2::], label="Series")

# plt.plot(array[2::],gradient[2::],label="Gradient")
plt.legend()
plt.show()


def countpeaks():
    n = 1
    for i in range(2, 1000):
        if abs(gradient[i]) >= 0.01:
            print(n)
            n += 1
