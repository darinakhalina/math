import numpy as np

# https://colab.research.google.com/drive/1xvj-MnGX3LJNR39wwbw5R6S3cSehFoSn#scrollTo=vD1QR0H8Zq75

# Вектор-столбец
vector_column = np.array([[1],
                          [2],
                          [3],
                          [4]])
print("Вектор-столбец:", vector_column)

a = np.array([ 2,  1,  -1])
print("a", a)

# Вектор-рядок
vector_row = np.array([1, 2, 3, 4])
print("Вектор-рядок:", vector_row)

b = np.array([ [2], [1], [-1]])
print("b", b)

# Матриця
import numpy as np

A = np.array([ [2, 1, -1], [0, 1, -4] ])
print("матриця A:",A)

B = np.array([ [5, 5, 5], [5, 5, 5],[5, 5, 5] ])
print("матриця B", B)

# Task 1
t1 = np.array([1, 5, 3])
print("test 1", t1)

# Task 2
t2 = np.array([[1], [3], [4]])
print("test 2", t2)

# Task 3
t3 = np.array([[1, 2], [3, 4]])
print("test 3", t3)

# Одинична матриця
matrix1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print("matrix1", matrix1)

# Task 1
# 2x3
t1 = np.array([[1, 5, 3], [5, 1, 2]])
print("test 1", t1)

# Task 2
# квадратна 2х2
t2 = np.array([[1, 2], [3, 4]])
print("test 2", t2)

# Task 3
# 2x4
t3 = np.array([[1, 2, 2, 2], [3, 4, 4, 4]])
print("test 3", t3)

# Task 4
# квадратна 4х4
# діагональна
# трикутна - верхньотрикутна і нижньотрикутна
# заповнена головною діагоналлю
# pаповнена зворотною діагоналлю
t4 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print("test 4", t4)

# Task 5
# квадратна 4х4
# діагональна
# трикутна - верхньотрикутна і нижньотрикутна
t5 = np.array([[3, 1, 1, 1], [1, 3, 1, 1], [1, 1, 3, 1], [1, 1, 1, 3]])
print("test 5", t5)

# Task 6
# квадратна 4х4
t6 = np.array([[1, 1, 1, 5], [1, 1, 5, 1], [1, 5, 1, 1], [5, 1, 1, 1]])
print("test 6", t6)

# Task 7
# квадратна 4х4
# діагональна
# трикутна - верхньотрикутна
t7 = np.array([[4, 1, 1, 5], [0, 4, 5, 1], [0, 0, 4, 1], [0, 0, 0, 4]])
print("test 7", t7)

# Task 8
# квадратна 4х4
# трикутна - нижньотрикутна
t8 = np.array([[4, 0, 0, 0], [4, 4, 0, 0], [2, 7, 4, 0], [1, -3, 9, 4]])
print("test 8", t8)


# toDo: remove
# С = A / B, 
# np.divide
# А = np.array([[1], [2], [3], [4], [5], [6], [7], [8]]).
# 8й пункт із ДЗ 1 можна пропустити