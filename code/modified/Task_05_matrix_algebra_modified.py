import numpy as np

points = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 2.0],
    [0.0, 2.0]
])

angle = np.deg2rad(30)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

shear = np.array([
    [1.0, 0.5],
    [0.0, 1.0]
])

transformation = rotation @ shear

transformed_points = points @ transformation.T

print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))
