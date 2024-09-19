# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:54:29 2020

@author: 967869@swansea.ac.uk (Inspired by Rosetta Code)
"""


def feigenbaum():

    return 0


max_it = 25  # For easier control over cycle length
max_it_k = 100  #
mu1 = 1  # This is Growth rate mu^(i-1)
mu2 = 0.0  # mu^(i-2)
f = 4.92  # Best approx. of Feigenbaums constant

print(" i       f         mu")
print("{0:2d}    {1:.8f}      {2:.5f}".format(1, f, mu1))

for i in range(2, max_it + 1):
    mu = mu1 + (mu1 - mu2) / f  # mu is mu^(i)
    for k in range(1, max_it_k + 1):
        p = 0.0
        dp = 0.0
        for n in range(1, (1 << i) + 1):
            dp = 1.0 - 2.0 * dp * p
            p = mu - p**2
        mu = mu - p / dp
    f = (mu1 - mu2) / (mu - mu1)

    print("{0:2d}    {1:.8f}      {2:.5f}".format(i, f, mu))
    mu2 = mu1
    mu1 = mu
