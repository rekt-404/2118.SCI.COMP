import numpy as np


A = np.array([
    [0., 1., 1., 1., 1.],
    [1., 0., 0., 0., 1.],
    [1., 0., 0., 1., 0.],
    [1., 0., 1., 0., 0.],
    [1., 1., 0., 0., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))

centrality = dominant_vector / dominant_vector.sum()

airports = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Malindi"]

print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")

for airport, score in zip(airports, centrality):
    print(f"{airport}: {score:.4f}")

v = np.real(eigenvectors[:, index])
print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))
