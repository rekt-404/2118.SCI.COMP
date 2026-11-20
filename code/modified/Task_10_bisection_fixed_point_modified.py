import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt


def profit(q):
    return 50*q - (2000 + 20*q + 0.01*q**2)


solution = root_scalar(
    profit,
    bracket=[0, 200],
    method="bisect",
    xtol=1e-10
)


def g(q):
    return (2000 + 0.01*q**2) / 30


q = 100.0
history = [q]

for _ in range(200):
    q_new = g(q)
    history.append(q_new)

    if abs(q_new - q) < 1e-10:
        break

    q = q_new

print(f"Bisection break-even quantity: {solution.root:.6f} units")
print(f"Fixed-point break-even quantity: {history[-1]:.6f} units")
print("Fixed-point iterations:", len(history) - 1)

quantities = np.linspace(0, 200, 300)

plt.plot(quantities, profit(quantities))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Units produced")
plt.ylabel("Profit")
plt.title("Break-even quantity")
plt.grid(True)
plt.show()
