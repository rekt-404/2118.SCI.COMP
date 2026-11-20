import numpy as np
from scipy.optimize import root



def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 25,
        (x - 4)**2 + y**2 - 16
    ]


for guess in ([3.0, 4.0], [3.0, -4.0]):
    solution = root(equations, guess)

    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", np.round(equations(solution.x), 12))
    print("Converged:", solution.success)
    print()
