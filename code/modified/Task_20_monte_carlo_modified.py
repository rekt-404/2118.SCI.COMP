import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

means = np.array([10.0, 15.0, 8.0])
stds = np.array([2.0, 3.0, 1.5])
deadline = 36.0
N = 100_000

durations = rng.normal(means, stds, size=(N, 3))
total_days = durations.sum(axis=1)

late = total_days > deadline
late_probability = late.mean()

print(f"Mean project duration: {total_days.mean():.2f} days")
print(f"Estimated probability of missing the deadline: {late_probability:.4%}")
print(f"Number of late projects: {late.sum()} out of {N}")

running_probability = np.cumsum(late) / np.arange(1, N + 1)

indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)
plt.xlabel("Number of simulations")
plt.ylabel("Estimated probability of delay")
plt.title("Monte Carlo estimate of project delay risk")
plt.grid(True)
plt.show()
