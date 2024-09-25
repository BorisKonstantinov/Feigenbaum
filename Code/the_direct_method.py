""" --- The Direct Method ---
Based on Briggs K., 1991: https://www.jstor.org/stable/2938684
Reference value at https://oeis.org/A006890/constant

This method is limited by the precision of the regular double type variable
in Python. For higher precision see the_direct_method_decimal.py
"""


def feigenbaum(range_i=10, range_j=100, f=3.2, mu=None):
    if mu is None:
        mu = [0, 1, 0]

    for i in range(2, range_i + 1):
        mu[2] = mu[1] + (mu[1] - mu[0]) / f

        for _ in range(range_j):
            p = 0
            dp = 0
            for __ in range(2**i):
                dp = 1 - 2 * dp * p
                p = mu[2] - p**2
            mu[2] -= p / dp

        f = (mu[1] - mu[0]) / (mu[2] - mu[1])
        mu[0], mu[1] = mu[1], mu[2]
    return f


def feigenbaum_table():
    print(f"{'range_i':<10}{'f':>20}")
    print(f"{'ref. value':<10}{'4.669201609102':>20}")
    print("-" * 30)
    for i in range(1, 16):
        f_value = feigenbaum(range_i=i)
        print(f"{i:<10}{f_value:>20.12f}")


feigenbaum_table()
