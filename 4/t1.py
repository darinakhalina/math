# Задання множини з елементами-числами:
num_set = {1, 2, 3, 4, 5, 6}
print(num_set)

# Задання значення множини з елементами-рядками:
string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)

# Створення множини зі списку:
num_set = set([1, 2, 3, 4, 5, 6])
print(num_set)

# Створення множини зі списку назв місяців та перевірка приналежності множини до елемента:
months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Чи належить елемент "May" множині months
print("May" in months)

# Об'єднання множин
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])

all_months = months_a.union(months_b)
print(all_months)

# Приклад об'єднання трьох множин з елементами-числами:
x = {1, 2, 3}
y = {4, 3, 6}
z = {7, 4, 9}

print(x | y | z)

# Перетин множин
x = {1, 2, 3}
y = {4, 3, 6}

print(x & y)

# Різниця між множинами
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff_set = set_a.difference(set_b)
print(diff_set)

# Симетрична різниця між множинами
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)

