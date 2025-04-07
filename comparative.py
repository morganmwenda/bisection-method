import numpy as np
import matplotlib.pyplot as plt

# Define the function and derivative
def f(x):
    return x**2 - 3

def f_prime(x):
    return 2 * x

# 1. Bisection Method
def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    estimates = []
    for _ in range(max_iter):
        c = (a + b) / 2
        estimates.append(c)
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return estimates

# 2. Regula-Falsi Method
def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    estimates = []
    for _ in range(max_iter):
        fa, fb = f(a), f(b)
        c = (a * fb - b * fa) / (fb - fa)
        estimates.append(c)
        if abs(f(c)) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return estimates

# 3. Newton-Raphson Method
def newton(x0, tol=1e-6, max_iter=100):
    estimates = [x0]
    for _ in range(max_iter):
        fx = f(x0)
        fpx = f_prime(x0)
        if fpx == 0:
            break
        x1 = x0 - fx / fpx
        estimates.append(x1)
        if abs(f(x1)) < tol:
            break
        x0 = x1
    return estimates

# 4. Secant Method
def secant(x0, x1, tol=1e-6, max_iter=100):
    estimates = [x0, x1]
    for _ in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        estimates.append(x2)
        if abs(f(x2)) < tol:
            break
        x0, x1 = x1, x2
    return estimates

# Run all methods
bisection_points = bisection(1, 2)
regula_points = regula_falsi(1, 2)
newton_points = newton(1.5)
secant_points = secant(1, 2)

# True root
true_root = np.sqrt(3)

# Plotting
plt.figure(figsize=(12, 7))
x_vals = np.linspace(1, 2, 400)
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - 3$", color='black')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(true_root, color='blue', linestyle=':', label=f"True root ≈ {true_root:.6f}")

# Plot estimates
plt.plot(bisection_points, [f(x) for x in bisection_points], 'o-', label='Bisection', color='purple')
plt.plot(regula_points, [f(x) for x in regula_points], 's-', label='Regula-Falsi', color='orange')
plt.plot(newton_points, [f(x) for x in newton_points], '^-', label='Newton-Raphson', color='green')
plt.plot(secant_points, [f(x) for x in secant_points], 'd-', label='Secant', color='red')

plt.title("Comparison of Root-Finding Methods on $f(x) = x^2 - 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
