""" --- The Direct Method ---
Created on Tue Apr 21 15:54:29 2020

Based on Briggs, 1991: https://www.jstor.org/stable/2938684
"""


def feigenbaum(max_it=25, max_it_k=100, mu1=1, mu2=0, f=4.92, p=0, p_=0):

    for i in range(2, max_it + 1):

        mu = mu1 + (mu1 - mu2) / f
        for k in range(1, max_it_k + 1):
            for n in range(1, (1 << i) + 1):
                p_ = 1.0 - 2.0 * p_ * p
                p = mu - p**2
            mu = mu - p / p_

        f = (mu1 - mu2) / (mu - mu1)
        mu2, mu1 = mu1, mu

    return f

def feigenbaum(max_it=25, max_it_k=100, f=4.92, p=0, dp= 0, mu=None):
    if mu is None:
        mu = [0, 1, 0]

    mu[2] = mu[1] + (mu[1] - mu[0]) / f
    dp = 1 - 2 * p * dp
    for _ in range(100):
        mu[2] = mu[2] - p / dp
        p = mu[2] - p**2



    for i in range(2, max_it + 1):

        mu[2] = mu[1] + (mu[1] - mu[0]) / f
        for _ in range(1, max_it_k + 1):
            for __ in range(1, (1 << i) + 1):
                dp = 1.0 - 2.0 * dp * p
                p = mu - p**2
            mu[2] = mu[2] - p / dp

        f = (mu[1] - mu[0]) / (mu[2] - mu[1])
        mu[0], mu[1] = mu[1], mu[2]

    return f
