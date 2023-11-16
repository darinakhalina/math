from criticalpath import Node

# Створення вузлів та їх зв'язків
p = Node('project')
a = p.add(Node('0-1', duration=3))
b = p.add(Node('0-2', duration=4))
c = p.add(Node('1-3', duration=1))
d = p.add(Node('3-4', duration=3))
e = p.add(Node('1-4', duration=3))
f = p.add(Node('2-4', duration=3))

# Встановлення зв'язків між вузлами
p.link(a, c)
p.link(b, f)
p.link(c, e)
p.link(d, e)
p.link(a, e)

# Оновлення графу
p.update_all()

# Отримання критичного шляху
critical_path = p.get_critical_path()
print("Критичний шлях:", [node.name for node in critical_path])

# Отримання загальної тривалості проекту
print("Загальна тривалість проекту:", p.duration)