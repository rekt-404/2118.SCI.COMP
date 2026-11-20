import numpy as np

water_level_cm = np.array([
    120.0, 118.5, 117.0, 115.2, 114.0, 113.5,
    112.0, 108.5, 104.0, 99.5, 95.0, 92.0,
    90.5, 91.0, 94.0, 98.5, 104.0, 110.0,
    115.5, 119.0, 121.5, 123.0, 123.5, 124.0
])

mean_level = np.mean(water_level_cm)
min_level = np.min(water_level_cm)
max_level = np.max(water_level_cm)

water_level_in = water_level_cm / 2.54

print(f"Daily mean level: {mean_level:.2f} cm")
print(f"Minimum level: {min_level:.2f} cm")
print(f"Maximum level: {max_level:.2f} cm")
print("First six readings in inches:", np.round(water_level_in[:6], 2))
