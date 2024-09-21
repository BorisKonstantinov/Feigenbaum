import mpmath as mp

# Set the precision to 1050 decimal places
mp.mp.dps = 1050  # Set to 1050 decimal places to exceed 1028

# Define the Feigenbaum functional equation for g(x)
def feigenbaum_g(x, alpha):
    return (1/alpha) * g(alpha * x) - g(g(x))

# Recursive function for g(x)
# We will approximate g(x) using a truncated Taylor series or polynomial.
def g(x):
    # Example: a simple quadratic approximation
    # In practice, this needs to be refined with more complex approximations
    return 1 - x**2

# Newton's method to solve for alpha (Feigenbaum constant)
def newtons_method(f, df, x0, tol=mp.mpf("1e-1028"), max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        x = x - fx / dfx
    raise ValueError("Newton's method did not converge")

# Derivative of feigenbaum_g for Newton's method
def d_feigenbaum_g(x, alpha):
    h = mp.mpf('1e-50')  # Small step for numerical derivative
    return (feigenbaum_g(x + h, alpha) - feigenbaum_g(x, alpha)) / h

# Define an initial guess for alpha
alpha_guess = mp.mpf("2.50290787509589")

# Solve for alpha using Newton's method
alpha = newtons_method(lambda alpha: feigenbaum_g(0, alpha),  # We solve g(0) = 1
                       lambda alpha: d_feigenbaum_g(0, alpha),  # Derivative
                       alpha_guess)

# Output the Feigenbaum constant alpha to high precision
print(f"Feigenbaum constant alpha: {alpha}")
