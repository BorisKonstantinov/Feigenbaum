import timeit


def solve(x):
    return x + 1


def test1(func, x, rangex):
    for _ in range(rangex):
        x = func(x)


def test2(x, rangex):
    for _ in range(rangex):
        x = solve(x)


# Parameters
x = 0
rangex = 1000000

# Timing test1
time_test1 = timeit.timeit(lambda: test1(solve, x, rangex), number=1000)
print(f"test1 time: {time_test1:.6f} seconds")

# Timing test2
time_test2 = timeit.timeit(lambda: test2(x, rangex), number=1000)
print(f"test2 time: {time_test2:.6f} seconds")
