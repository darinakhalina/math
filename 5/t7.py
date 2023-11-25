from sympy import symbols, diff
import matplotlib.pyplot as plt
import numpy as np

# Оголошуємо символи 'a', 'b' та 'x'
a, b, x = symbols('a b x')

# Задана функція
f = 2*a*x + 3*b

# Знаходимо похідну функції за змінною 'x'
derivative = diff(f, x)
print(derivative)

# Значення a та b
a_value = 2
b_value = 5

# Задана функція
def f(x):
    return 2 * a_value * x + 3 * b_value

# Генерація значень x
x_values = np.linspace(-10, 10, 100)  # Генеруємо 100 значень x в діапазоні від -10 до 10

# Обчислення значень y (2ax + 3b) для кожного x
y_values = f(x_values)

# Побудова графіка
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='2ax + 3b')

# Позначення осей та заголовок графіка
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції 2ax + 3b')

# Додавання легенди
plt.legend()

# Показ графіка
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()