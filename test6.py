import matplotlib.pyplot as plt
import networkx as nx

# Створення пустого графу
G = nx.DiGraph()

# Додавання вершин до графу
G.add_nodes_from(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# Додавання зв'язків між вершинами
G.add_edges_from([('0', '1'),
                  ('0', '2'), 
                  ('0', '3'), 
                  ('0', '4'), 
                  ('1', '5'), 
                  ('5', '6'), 
                  ('6', '10'),
                  ('2', '7'),
                  ('7', '8'),
                  ('8', '10'),
                  ('3', '9'),
                  ('3', '10'),
                  ('9', '10'),
                  ('4', '5'), 
                ])

# Розміщення вершин графу
pos = nx.spring_layout(G)

# Відображення графу
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold', arrows=True)
plt.title('Граф зв\'язків')
plt.show()