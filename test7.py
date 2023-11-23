from sympy import symbols, sqrt, diff

# Оголошення символьної змінної
x = symbols('x')

# Задання функції
f = sqrt(x**2 + 1)

# Знаходження похідної
derivative = diff(f, x)
print("Похідна функції:", derivative)

# Значення похідних у точках x=1 та x=-1/2
value_at_1 = derivative.subs(x, 1)
value_at_minus_half = derivative.subs(x, -1/2)

print("Значення похідної у точці x=1:", value_at_1)
print("Значення похідної у точці x=-1/2:", value_at_minus_half)

# https://app.screencast.com/8gzBHF36Okdna
# https://app.screencast.com/PzQxU8udidmdK

# hw4 - https://app.screencast.com/JflpVLQsRThi5
# https://app.screencast.com/hhSZbiQ4jxxFM
# 
#