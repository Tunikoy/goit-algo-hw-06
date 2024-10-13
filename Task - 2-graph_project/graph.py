import networkx as nx

def create_graph():
    # Створення графа
    G = nx.Graph()

    # Додавання вершин і ребер
    G.add_edge("A", "B")
    G.add_edge("B", "C")
    G.add_edge("C", "D")
    G.add_edge("D", "A")
    G.add_edge("A", "C")

    return G