import numpy as np

# Детермінант 2х2 матриці
A = np.array(
 [[1, 2],
 [3, 4]]
 )
result = np.linalg.det(A)
result_round = round(result)
print("Детермінант 2х2 матриці result", result)
print("Детермінант 2х2 матриці result round", result_round)

# Детермінант 3х3 матриці
A = np.array(
 [[4, -5, 7],
 [1, -4, 9],
 [-4, 0, 5],
 ]
 )
print("Детермінант 3х3 матриці result round", round(np.linalg.det(A)))

# Властивості детермінантів
# Визначник не змінюється під час транспонування матриці
A = np.array(
 [[4, -5, 7],
 [1, -4, 9],
 [-4, 0, 5],
 ]
 )
At = np.transpose(A)
print("Базова матриця A:", A)
print(f"Визначник базової матриці А: {int(np.linalg.det(A))}")
print("Транспонована матриця At:", At)
print(f"Визначник транспонованої матриці At: {int(np.linalg.det(At))}")
