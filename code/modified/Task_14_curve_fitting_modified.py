import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

hours = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
count = np.array([100, 150, 220, 330, 490, 740, 1100], dtype=float)


def model(t, a, b):
    return a * np.exp(b * t)


parameters, covariance = curve_fit(model, hours, count, p0=[100, 0.4])
a, b = parameters

predicted = model(hours, a, b)
rmse = np.sqrt(np.mean((count - predicted)**2))

print(f"Fitted model: y = {a:.2f} * exp({b:.4f} t)")
print(f"RMSE: {rmse:.2f}")
print(f"Predicted count at 8 hours: {model(8, a, b):.0f}")

t_plot = np.linspace(0, 8, 300)

plt.scatter(hours, count, label="Measurements")
plt.plot(t_plot, model(t_plot, a, b), label="Fitted curve")
plt.xlabel("Time (hours)")
plt.ylabel("Bacteria count")
plt.title("Bacteria growth curve fitting")
plt.legend()
plt.grid(True)
plt.show()
