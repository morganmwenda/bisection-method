import matplotlib.pyplot as plt
import numpy as np


# Define the function
def f(x):
    return x**2 - 3# Example function

# Bisection Method
def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iter':>4} | {'a':>10} | {'b':>10} | {'t (midpoint)':>14} | {'f(t)':>12}")
    print("-"*60)

    for i in range(1, max_iter+1):
        t = (a + b) / 2
        ft = f(t)

        print(f"{i:>4} | {a:>10.6f} | {b:>10.6f} | {t:>14.6f} | {ft:>12.6f}")

        if abs(ft) < tol:
            return t

        if f(a) * ft < 0:
            b = t
        else:
            a = t

    print("Warning: Max iterations reached.")
    return t

# Solve the equation on [1, 9]
a, b = 0, 2 # Initial interval
root = bisection_method(a, b)

# Plotting
x_vals = np.linspace(a, b, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - 3$")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root:.6f}")
plt.scatter(root, f(root), color='red')
plt.title("Bisection Method: Root of $f(x) = x^2 - 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""
Bisection Method Algorithm
Follow the below procedure to get the solution for the continuous function:

For any continuous function f(x),

Find two points, say a and b such that a < b and f(a)* f(b) < 0
Find the midpoint of a and b, say “t”
t is the root of the given function if f(t) = 0; else follow the next step
Divide the interval [a, b] – If f(t)*f(a) <0, there exist a root between t and a
– else if f(t) *f (b) < 0, there exist a root between t and b
Repeat above three steps until f(t) = 0.
The bisection method is an approximation method to find the roots of the given equation by repeatedly dividing the interval. This method will divide the interval until the resulting interval is found, which is extremely small.




"""