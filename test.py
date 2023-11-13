import numpy as np

a = np.array([[-1, 1, 2],
                         [0, -1, -3],
                         [4, -3, 2]])

b = np.array([[1],
                      [-4],
                      [7]])

# Знайдіть і виведіть визначник матриці A + add round round(np.linalg.det(A))
determinant_a = np.linalg.det(a)
print("Визначник матриці A:")
print(determinant_a)

# Знайдіть і виведіть матрицю відповідей x
solution_x = np.linalg.solve(a, b)
print("Матриця відповідей x:")
print(solution_x)

# Знайдіть і виведіть зворотню матрицю A
inverse_a = np.linalg.inv(a)
print("Зворотня матриця A:")
print(inverse_a)

print("test", np.linalg.solve(a, b))