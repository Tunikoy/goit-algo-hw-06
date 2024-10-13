import networkx as nx
from graph import create_weighted_graph
from algorithms import dijkstra

# Створюємо граф з вагами
G = create_weighted_graph()

# Перетворення графу для алгоритму
graph_dict = {node: dict(neighbors) for node, neighbors in G.adjacency()}

# Виконуємо алгоритм Дейкстри
start_node = "A"
shortest_paths = dijkstra(graph_dict, start_node)

# Виводимо результати
print(f"Найкоротші шляхи від вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"До {node}: {distance}")

# Візуалізація графу
nx.draw(G, with_labels=True)