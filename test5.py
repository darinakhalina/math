import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph() # створити неорієнтований граф
G.add_node('1') # додати вузол
G.add_node('2') # додати вузол
G.add_node('3') # додати вузол
G.add_node('4') # додати вузол
G.add_node('5') # додати вузол
G.add_node('6') # додати вузол
G.add_node('7') # додати вузол
G.add_node('8') # додати вузол
G.add_node('9') # додати вузол
G.add_node('10') # додати вузол
# G.add_edge('a','b')
# G.add_edge('a','c')
# G.add_edge('b','c')
# G.add_edge('c','d')
# G.add_nodes_from([2,3,4]) # додати вузли
# G.add_edge(1,2) # додати ребро
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
                ]) # додати ребра

print (G.number_of_nodes(), G.number_of_edges()) # кількість вузлів і ребер
print ('nodes', G.nodes) # вузли
print ('edges', G.edges) # ребра
print ('adj', G.adj) # сусіди вершин
print ('degree', G.degree) # степені вершин (кількість ребер вершин)

nx.draw(G, with_labels = True) # рисувати граф за допомогою matplotlib

plt.show();

