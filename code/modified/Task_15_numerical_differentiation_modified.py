import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
velocity = np.array([0.0, 2.1, 4.5, 7.4, 10.8, 14.5, 18.0])

acceleration = np.zeros_like(velocity)

acceleration[0] = (velocity[1] - velocity[0]) / (time[1] - time[0])

for i in range(1, len(time) - 1):
    acceleration[i] = (
        velocity[i + 1] - velocity[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

acceleration[-1] = (
    velocity[-1] - velocity[-2]
) / (
    time[-1] - time[-2]
)

for t, v, a in zip(time, velocity, acceleration):
    print(f"t={t:.0f}s, velocity={v:.1f}m/s, estimated acceleration={a:.2f}m/s^2")

plt.plot(time, acceleration, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated acceleration (m/s^2)")
plt.title("Acceleration estimated from train velocity data")
plt.grid(True)
plt.show()
