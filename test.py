import numpy as np
import matplotlib.pyplot as plt

# Вектор швидкості кулі до удару в борт
v_before = np.array([3, 2])

# Вектор швидкості удару
v_impact = np.array([0, -4])

# Знаходження швидкості кулі після удару (сума векторів)
v_after = v_before + v_impact
print("Швидкість кулі після удару:", v_after)

# Обчислення скалярного добутку
dot_product = np.dot(v_before, v_impact)

# Обчислення довжин векторів
magnitude_before = np.linalg.norm(v_before)
magnitude_impact = np.linalg.norm(v_impact)

# Обчислення кута в радіанах
cos_theta = dot_product / (magnitude_before * magnitude_impact)
print("V1", cos_theta)
v2 = dot_product / magnitude_before / magnitude_impact
print("V2", v2)
angle_rad = np.arccos(cos_theta)

# Переведення кута в градуси
angle_deg = np.degrees(angle_rad)
print("Кут удару (в градусах):", angle_deg)

# Побудова графіку
plt.figure()
plt.plot([0, v_before[0]], [0, v_before[1]], label='До удару')
plt.plot([0, v_impact[0]], [0, v_impact[1]], label='Удар')
plt.plot([0, v_after[0]], [0, v_after[1]], label='Після удару')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()