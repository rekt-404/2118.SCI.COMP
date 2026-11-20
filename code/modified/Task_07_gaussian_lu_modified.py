import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [5.0, -2.0, 0.0],
    [-2.0, 6.0, -3.0],
    [0.0, -3.0, 5.0]
])

scenarios = [
    np.array([10.0, 0.0, 5.0]),
    np.array([12.0, 3.0, 4.0]),
    np.array([8.0, 6.0, 9.0])
]

lu, piv = lu_factor(A)

for i, b in enumerate(scenarios, start=1):
    v = lu_solve((lu, piv), b)
    residual = b - A @ v

    print(f"Scenario {i}")
    print("Node voltages (V):", v)
    print("Residual norm:", np.linalg.norm(residual))
    print()
