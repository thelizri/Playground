import numpy as np

# Define the faces for each Platonic solid
tetrahedron = np.array([1 / 4 for i in range(4)])  # 4 faces
cube = np.array([1 / 6 for i in range(6)])  # 6 faces
octahedron = np.array([1 / 8 for i in range(8)])  # 8 faces
dodecahedron = np.array([1 / 12 for i in range(12)])  # 12 faces
icosahedron = np.array([1 / 20 for i in range(20)])  # 20 faces

probability_distribution = tetrahedron
for die in [cube, octahedron, dodecahedron, icosahedron]:
    probability_distribution = np.convolve(probability_distribution, die)

probability_of_winning = 0
for i in range(len(probability_distribution)):
    if i <= 5 or i >= 40:
        probability_of_winning += probability_distribution[i]

print(f"{probability_of_winning * 100}%")
print(probability_of_winning)
