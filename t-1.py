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

# Складання двох матриць
A = np.array([ [2, 1, -1], [0, 1, -4] ])
B = np.array([ [-2, 1, 0], [-3, 2, 2] ])

print("A+B", A+B)

# Task 1
A = np.array([ [4, 1, -1], [5, 1, -4] ])
B = np.array([ [-2, 3, 0], [2, 2, 2] ])
print("test1 A+B", A+B)

# Task 2
A = np.array([ [4, 1, -1], [-1, 6, 5], [5, 1, -4] ])
B = np.array([ [-2, 3, 0], [8, 1, 7], [2, 2, 2] ])
print("test2 A+B", A+B)

# Множення матриці на число
A = np.array([ [2, 1, -1], [0, 1, -4] ])

print("3A",3*A)

# Task 1
A = np.array([ [2, 1, -1], [0, 1, -4] ])
print("test1 5A", 5*A)

# Task 2
B = np.array([ [7, 1, -1], [2, 3, -4] ])
print("test2 2B", 2*B)

# Task 3
C = np.array([ [1, 5, -1], [7, 1, -1], [5, 3, 1] ])
print("test3 5C", 5*C)

# Множення матриць
a = np.array([ [1,1], [1,1]])
b = np.array([ [1,1], [1,1]])
total1 = a.dot(b)

print("total1", total1)

a = np.array([ [1, 2], [3, 4]])
b = np.array([ [5, 6], [7, 8] ])
total2 = a.dot(b)

print("total2", total2)

a = np.array([ [1, 2], [3, 4], [5,6]])
b = np.array([ [7,8,9], [10, 11, 12] ])
total3 = a.dot(b)
print("total3", total3)

a = np.array([ [1, 1], [2, 2], [3, 3], [4, 4], [5,5] ])
b = np.array([ [1,1,1], [2,2,2] ])

total4 = a.dot(b)
print("total4", total4)

a = np.array([ [1, 2], [2, 2], [3, 2], [4, 2], [5, 2] ])
b = np.array([ [1,1,1] ])

try:
    total5 = a.dot(b)
except ValueError:
    print("Error here - ValueError: shapes (5,2) and (1,3) not aligned: 2 (dim 1) != 1 (dim 0)")

