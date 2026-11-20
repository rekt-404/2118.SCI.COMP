import numpy as np
from scipy.integrate import simpson

time_s = np.array([0, 10, 20, 30, 40, 50, 60], dtype=float)
flow_lps = np.array([0.0, 2.5, 4.0, 5.0, 4.5, 3.0, 1.0])

volume_trapezoid = np.trapezoid(flow_lps, time_s)
volume_simpson = simpson(flow_lps, x=time_s)

print(f"Volume using trapezoidal rule: {volume_trapezoid:.3f} L")
print(f"Volume using Simpson's rule: {volume_simpson:.3f} L")
print(f"Difference between estimates: {abs(volume_simpson-volume_trapezoid):.3f} L")
