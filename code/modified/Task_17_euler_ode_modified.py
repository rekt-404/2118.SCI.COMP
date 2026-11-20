import numpy as np
import matplotlib.pyplot as plt


r = 0.4
K = 1000.0
P_initial = 100.0
h = 1.0  # days
end_time = 30.0


def growth_rate(P):
    return r * P * (1 - P / K)


time = np.arange(0, end_time + h, h)
population = np.zeros_like(time)
population[0] = P_initial

for i in range(len(time) - 1):
    population[i + 1] = (
        population[i] + h * growth_rate(population[i])
    )

exact = K / (1 + ((K - P_initial) / P_initial) * np.exp(-r * time))

print(f"Euler population after 30 days: {population[-1]:.2f}")
print(f"Exact population after 30 days: {exact[-1]:.2f}")
print(f"Maximum absolute error: {np.max(np.abs(population - exact)):.2f}")

plt.plot(time, population, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (days)")
plt.ylabel("Population")
plt.title("Logistic population growth")
plt.legend()
plt.grid(True)
plt.show()
