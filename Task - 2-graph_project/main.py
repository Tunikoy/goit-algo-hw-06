import networkx as nx
from graph import create_graph
from algorithms import dfs, bfs

# Створення графа
G = create_graph()

# Перетворення графа на словник для алгоритмів
graph_dict = {node: list(neighbors.keys()) for node, neighbors in G.adjacency()}

# Виконання алгоритму DFS
print("DFS:")
dfs(graph_dict, 'A')

# Виконання алгоритму BFS
print("\nBFS:")
bfs(graph_dict, 'A')

# Візуалізація графа
nx.draw(G, with_labels=True)
