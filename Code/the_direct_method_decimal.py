""" --- The Direct Method ---
Based on Briggs K., 1991: https://www.jstor.org/stable/2938684
Reference value at https://oeis.org/A006890/constant

This method has improved precision through increasing the available
decimal places of variables with the decimal Python library.
This comes at a cost of increased computation time.

decimal places        | time (s)
---------------------------------
15-17 (float default) |  1.9
30                    | 16.0
60                    | 19.4
"""

from decimal import Decimal, getcontext


def feigenbaum(range_i=10, range_j=100, f=Decimal(3.2), mu=None):
    if mu is None:
        mu = [Decimal(0), Decimal(1), Decimal(0)]

    for i in range(2, range_i + 1):
        mu[2] = mu[1] + (mu[1] - mu[0]) / f

        for _ in range(range_j):
            p = Decimal(0)
            dp = Decimal(0)
            for __ in range(2**i):
                dp = Decimal(1) - Decimal(2) * dp * p
                p = mu[2] - p**2
            mu[2] -= p / dp

        f = (mu[1] - mu[0]) / (mu[2] - mu[1])
        mu[0], mu[1] = mu[1], mu[2]
    return f


# Set precision
getcontext().prec = 60


def feigenbaum_table():
    print(f"{'range_i':<10}{'f':>20}")
    print("-" * 65)
    for i in range(1, 16):
        f_value = feigenbaum(range_i=i)
        print(f"{i:<10}{f_value:>20}")


feigenbaum_table()
