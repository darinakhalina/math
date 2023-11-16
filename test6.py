import matplotlib.pyplot as plt
import networkx as nx

# Створення пустого графу
G = nx.DiGraph()

# Додавання вершин до графу
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Додавання зв'язків між вершинами
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'E'), ('C', 'E'), ('D', 'E')])

# Розміщення вершин графу
pos = nx.spring_layout(G)

# Відображення графу
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', arrows=True)
plt.title('Граф зв\'язків')
plt.show()