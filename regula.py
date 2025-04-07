import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**2 - 3

# Regula-Falsi Method with plot points captured
def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    estimates = []

    print(f"{'Iter':>4} | {'a':>10} | {'b':>10} | {'x (est)':>14} | {'f(x)':>12}")
    print("-"*60)

    for i in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        estimates.append((a, b, x))

        print(f"{i:>4} | {a:>10.6f} | {b:>10.6f} | {x:>14.6f} | {fx:>12.6f}")

        if abs(fx) < tol:
            break

        if fa * fx < 0:
            b = x
        else:
            a = x

    return x, estimates

# Run the method and collect points
a, b = 1, 2
root, estimate_points = regula_falsi(a, b)

# Plotting
x_vals = np.linspace(a, b, 400)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r"$f(x) = x^2 - 3$", color='blue')
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(root, color='red', linestyle='--', label=f"Estimated Root ≈ {root:.6f}")
plt.scatter(root, f(root), color='red')

# Plot secant lines from each iteration
for i, (a_i, b_i, x_i) in enumerate(estimate_points):
    plt.plot([a_i, b_i], [f(a_i), f(b_i)], color='orange', linestyle='--', alpha=0.5)
    plt.scatter(x_i, f(x_i), color='green', s=30, label="Estimates" if i == 0 else "")

plt.title("Regula-Falsi Method: Root of $f(x) = x^2 - 3$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
