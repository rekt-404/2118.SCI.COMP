import numpy as np



A = np.array([
    [10.0, -4.0],
    [-4.0, 12.0]
])

b = np.array([32.0, 8.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Loop 1 current: {solution[0]:.3f} A")
print(f"Loop 2 current: {solution[1]:.3f} A")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
