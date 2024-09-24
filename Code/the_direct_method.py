""" --- The Direct Method ---
Created on Tue Apr 21 15:54:29 2020

Based on Briggs, 1991: https://www.jstor.org/stable/2938684
"""


def feigenbaum(range_i=10, range_j=100, f=3.2, mu=None):
    if mu is None:
        mu = [0, 1, 0]

    for i in range(2, range_i + 1):
        mu[2] = mu[1] + (mu[1] - mu[0]) / f

        for j in range(range_j):
            p = 0
            dp = 0
            for k in range(2**i):
                dp = 1 - 2 * dp * p
                p = mu[2] - p**2
            mu[2] -= p / dp

        f = (mu[1] - mu[0]) / (mu[2] - mu[1])
        mu[0], mu[1] = mu[1], mu[2]
    return f


print(feigenbaum())
