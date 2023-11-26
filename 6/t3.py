from sympy import symbols, diff
import matplotlib.pyplot as plt
import numpy as np
from sympy import solve

# Оголошення символів та функції
x = symbols('x')
y = -3*x**2 + 30*x

# Обчислення похідної
dy_dx = diff(y, x)
print("Похідна функції y по x:", dy_dx)

# Значення x для графіків
x_vals = np.linspace(-5, 15, 400)

# Значення функції y та її похідної
y_vals = -3 * x_vals ** 2 + 30 * x_vals
dy_dx_vals = -6 * x_vals + 30

# Побудова графіків
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Функція y = -3x^2 + 30x')
plt.plot(x_vals, dy_dx_vals, label="Похідна функції")
plt.title('Графік функції та її похідної')
plt.xlabel('x')
plt.ylabel('y та y\'')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

critical_points = solve(dy_dx, x)
print("Критичні точки:", critical_points)

# Знайдемо значення y для кожної критичної точки
max_y = max([-3 * x_val ** 2 + 30 * x_val for x_val in critical_points])
print("Значення максимуму функції:", max_y)