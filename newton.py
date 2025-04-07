import matplotlib.pyplot as plt
import numpy as np

# Define the function and its derivative
def f(x):
    return x**2 - 3

def f_prime(x):
    return 2*x

# Newton-Raphson Method
def newton_method(x0, tol=1e-6, max_iter=100):
    estimates = []
    
    print(f"{'Iter':>4} | {'x_n':>14} | {'f(x_n)':>12}")
    print("-"*40)

    for i in range(1, max_iter + 1):
        fx = f(x0)
        fpx = f_prime(x0)
        if fpx == 0:
            raise ZeroDivisionError("Derivative became zero. Method fails.")
        
        x1 = x0 - fx / fpx
        estimates.append(x0)

        print(f"{i:>4} | {x0:>14.6f} | {fx:>12.6f}")

        if abs(f(x1)) < tol:
            estimates.append(x1)
            return x1, estimates

        x0 = x1

    print("Warning: Max iterations reached.")
    return x0, estimates

# Run Newton's method
x0 = 1.5  # Initial guess
root, estimate_points = newton_method(x0)

# Plotting
x_vals = np.linspace(1, 2, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - 3$", color='blue')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root:.6f}")
plt.scatter(root, f(root), color='red')

# Draw tangent lines at each estimate
for x_n in estimate_points[:-1]:  # skip the last one (already root)
    slope = f_prime(x_n)
    y_n = f(x_n)
    # Draw tangent line from x_n
    tangent_x = np.linspace(x_n - 0.3, x_n + 0.3, 10)
    tangent_y = slope * (tangent_x - x_n) + y_n
    plt.plot(tangent_x, tangent_y, 'orange', linestyle='--', alpha=0.5)
    plt.scatter(x_n, y_n, color='green', s=30, label='Estimates' if x_n == estimate_points[0] else '')

plt.title("Newton-Raphson Method: Root of $f(x) = x^2 - 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
