import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**2 - 3

# Secant Method
def secant_method(x0, x1, tol=1e-6, max_iter=100):
    estimates = [x0, x1]
    
    print(f"{'Iter':>4} | {'x_n':>14} | {'f(x_n)':>12}")
    print("-"*40)
    
    for i in range(2, max_iter + 2):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            raise ZeroDivisionError("Division by zero in secant formula.")

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        estimates.append(x2)

        print(f"{i-1:>4} | {x2:>14.6f} | {f(x2):>12.6f}")

        if abs(f(x2)) < tol:
            return x2, estimates

        x0, x1 = x1, x2

    print("Warning: Max iterations reached.")
    return x2, estimates

root, estimate_points = secant_method(1, 2)
print(f"\nEstimated root: {root:.6f}")

# Plotting
x_vals = np.linspace(1, 2, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - 3$", color='blue')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Root ≈ {root:.6f}")
plt.scatter(root, f(root), color='red')

# Draw secant lines
for i in range(len(estimate_points)-2):
    x0 = estimate_points[i]
    x1 = estimate_points[i+1]
    y0 = f(x0)
    y1 = f(x1)
    plt.plot([x0, x1], [y0, y1], 'orange', linestyle='--', alpha=0.5)
    plt.scatter([x0, x1], [y0, y1], color='green', s=30)

plt.title("Secant Method: Root of $f(x) = x^2 - 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
