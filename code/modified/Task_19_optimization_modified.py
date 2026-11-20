import numpy as np
from scipy.optimize import minimize



def cost(z):
    x, y = z
    return 10*x + 14*y


constraints = [
    {"type": "ineq", "fun": lambda z: 5*z[0] + 8*z[1] - 60},
    {"type": "ineq", "fun": lambda z: 300*z[0] + 200*z[1] - 2400}
]

bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[10, 10],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization success:", solution.success)
print(f"Type A units: {x:.3f}")
print(f"Type B units: {y:.3f}")
print(f"Total capacity: {5*x + 8*y:.2f} TB")
print(f"Total throughput: {300*x + 200*y:.2f} MB/s")
print(f"Minimum cost: {solution.fun:.2f}")

best_integer = None

for a in range(0, 30):
    for b in range(0, 30):
        capacity = 5*a + 8*b
        throughput = 300*a + 200*b

        if capacity >= 60 and throughput >= 2400:
            total_cost = 10*a + 14*b

            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity, throughput)

print("Best integer solution (cost, A, B, capacity, throughput):", best_integer)
