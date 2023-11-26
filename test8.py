import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Функція для побудови матриці суміжності
def get_adjacency_matrix(data):
    # Визначаємо кількість вершин
    num_tasks = max([row[2] for row in data]) + 1
    # Ініціалізуємо матрицю нулями
    adjacency_matrix = np.zeros((num_tasks, num_tasks), dtype=int)
    # Записуємо вагу ребер у матрицю
    for (_, edge_start, edge_end, _, weight) in data:
        adjacency_matrix[edge_start][edge_end] = weight
    return adjacency_matrix

# Функція для пошуку всіх критичних шляхів
def get_critical_paths(graph, source, target):
    longest_paths = []
    longest_path_length = 0
    for path in nx.all_simple_paths(G, source=source, target=target):
        path_length = nx.classes.function.path_weight(graph, path, 'weight')
        if path_length > longest_path_length:
            longest_path_length = path_length
            longest_paths.clear()
            longest_paths.append(path)
        elif path_length == longest_path_length:
            longest_paths.append(path)
    return longest_paths, longest_path_length

# Список ребер з назвами та вагами
data = [
    # number, start node, end node, name, duration/weight
    [1, 0, 1, 'Робота дизайнера', 4],
    [2, 0, 2, 'Робота над текстами', 3],
    [3, 0, 3, 'Підготовка рекламної кампанії у пошуку', 3],
    [4, 0, 4, 'Анализ цін конкурентів', 1],
    [5, 1, 5, 'Оновлення дизайну сайту', 2],
    [6, 5, 6, 'Зміна цін на сайті', 1],
    [7, 6, 10, 'Перевірка всіх змін', 1],
    [8, 2, 7, 'Створення шаблону імейла', 2],
    [9, 7, 8, 'Додавання контента в імейл', 1],
    [10, 8, 10, 'Старт емейл компанії', 1],
    [11, 3, 9, 'Налаштування реклами в соцмережах', 2],
    [12, 3, 10, 'Старт рекламних компаній у пошуку', 1],
    [13, 9, 10, 'Оголосити про промо в соцмережах', 1],
    [14, 4, 5, 'Робота над цінами', 3],
]

# Побудова матриці суміжності
adjacency_matrix = get_adjacency_matrix(data)
print(adjacency_matrix)

# Створюємо граф
G = nx.DiGraph()

# Створюємо список ребер
edges = [
    (edge_start, edge_end, {'weight': weight})
    for (_, edge_start, edge_end, _, weight) in data
]
G.add_edges_from(edges)

# Рахуємо критичні шляхи та їх довжину
critical_paths, critical_path_length = get_critical_paths(G, 0, 10)

print(f'Критичні шляхи: {critical_paths}')
print(f'Довжина критичних шляхів: {critical_path_length}')

# Створюємо множину ребер, з яких складаються критичні шляхи
critical_edges = {(cp[i], cp[i + 1]) for cp in critical_paths for i in range(len(cp) - 1)}

# Задаємо координати вершин для відображення
pos = {
    0: ([0, 0]),
    1: ([4, -2]),
    2: ([4, 8]),
    3: ([4, 2]),
    4: ([4, -6]),
    5: ([10, -4]),
    6: ([16, -4]),
    7: ([10, 8]),
    8: ([16, 8]),
    9: ([16, 4]),
    10: ([20, 0]),
}
# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=500, arrows=True)

# Додаємо критичні ребра червоним кольором
nx.draw_networkx_edges(G, pos, edgelist=critical_edges, edge_color='red', width=3)

# Додаємо ваги ребер на граф
edge_labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
