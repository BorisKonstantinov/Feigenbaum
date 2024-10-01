"""
--- The Direct Method ---
Based on Briggs K., 1991: https://keithbriggs.info/documents/how-to-calc.pdf
Reference value at https://oeis.org/A006890/constant

The functions below obtain Feigenbaums constant.
One makes use of the double type variable and is constrained by its
accuracy.
The other uses the decimal library to increase its precision, with the
cost of computation time.
This is also implemented in Fortran90 in the_direct_method.f90.
"""

from decimal import Decimal, getcontext


def feigenbaum(range_i=10, range_j=100, f=3.2, mu=None):
    """
    This function is limited by the precision of the double type
    variable in Python.
    """
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


def feigenbaum_decimal(range_i=10, range_j=100, f=Decimal(3.2), mu=None, decimals=60):
    """
    This method has improved precision through increasing the available
    decimal places of variables with the decimal Python library.
    This comes at a cost of increased computation time.

    decimal places        | time (s)
    ---------------------------------
    15-17 (float default) |  1.9
    30                    | 16.0
    60                    | 19.4
    """
    getcontext().prec = decimals

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


def feigenbaum_table(function, accuracy):
    print(f"{'range_i':<10}{'f':>20}")
    print("-" * 30)
    for i in range(1, accuracy + 1):
        f_value = function(range_i=i)
        print(f"{i:<10}{f_value:>20.12f}")


feigenbaum_table(feigenbaum, 15)
