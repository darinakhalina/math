import numpy as np
import matplotlib.pyplot as plt

# Вектор швидкості першої кулі до удару
v1_before = np.array([0, 5])

# Вектор швидкості першої кулі після удару
v1_after = np.array([1, 2])

# Вектор швидкості другої кулі після удару
v2_after = np.array([0, 0])  # Друга куля повністю зупинилась

v2_before = v1_after - v1_before
print("Швидкість другої кулі до удару:", v2_before)

# Створення фігури та підготовка графіку
fig, ax = plt.subplots()

# Додавання векторів на графік
ax.quiver(0, 0, v1_before[0], v1_before[1], angles='xy', scale_units='xy', scale=1, color='b', label='Вектор v1 до удару')
ax.quiver(0, 0, v1_after[0], v1_after[1], angles='xy', scale_units='xy', scale=1, color='r', label='Вектор v1 після удару')
ax.quiver(0, 0, v2_before[0], v2_before[1], angles='xy', scale_units='xy', scale=1, color='g', label='Вектор v2 до удару')
ax.quiver(0, 0, v2_after[0], v2_after[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Вектор v2 після удару')

# Налаштування параметрів графіку
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 10)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Відображення графіку
plt.show()