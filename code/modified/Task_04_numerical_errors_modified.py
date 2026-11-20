import numpy as np

total = 0.0
for _ in range(1_000_000):
    total += 0.1

expected = 100000.0

absolute_error = abs(total - expected)
relative_error = absolute_error / abs(expected)

print(f"Accumulated total: {total:.10f}")
print("Exact comparison:", total == expected)
print("Tolerance-based comparison:", np.isclose(total, expected))
print(f"Absolute error: {absolute_error:.10f}")
print(f"Relative error: {relative_error:.10%}")
