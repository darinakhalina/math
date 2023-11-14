import numpy as np
a = np.array([3,1])
b = np.array([0,2])

c = a + b
d = a - b

print (f'Sum of vectors: {c}')
print (f'Difference of vectors: {d}')

# Скалярний добуток векторів
import numpy as np
print("Скалярний добуток векторів", np.dot(a,b))

# Кут між векторами
import numpy as np
from numpy import linalg as LA
a = np.array([1, 3])
b = np.array([2, 0])
cos_angle = np.dot(a, b) / LA.norm(a) / LA.norm(b)
print(f"Косинус кута:{cos_angle}")
print(f"Значення кута (радіани) {np.arccos(cos_angle)}")