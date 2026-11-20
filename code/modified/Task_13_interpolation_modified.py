import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

voltage = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5])
pressure_kpa = np.array([10.0, 28.0, 52.0, 80.0, 110.0, 138.0, 160.0])

linear = interp1d(voltage, pressure_kpa, kind="linear")
cubic = CubicSpline(voltage, pressure_kpa)

fine_voltage = np.linspace(0.5, 3.5, 200)

target_voltage = 1.75

print(f"Linear estimate at 1.75 V: {float(linear(target_voltage)):.2f} kPa")
print(f"Cubic estimate at 1.75 V: {float(cubic(target_voltage)):.2f} kPa")

plt.scatter(voltage, pressure_kpa, label="Calibration points")
plt.plot(fine_voltage, linear(fine_voltage), label="Linear")
plt.plot(fine_voltage, cubic(fine_voltage), label="Cubic spline")
plt.xlabel("Sensor voltage (V)")
plt.ylabel("Pressure (kPa)")
plt.title("Pressure sensor calibration")
plt.legend()
plt.grid(True)
plt.show()
