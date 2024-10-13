import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Додавання ребер
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "D")
G.add_edge("D", "A")
G.add_edge("A", "C")

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Аналіз основних характеристик
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print(f"Ступінь кожної вершини: {dict(G.degree())}")