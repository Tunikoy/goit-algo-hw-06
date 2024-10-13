import networkx as nx

def create_weighted_graph():
    G = nx.Graph()

    # Додавання вершин та ребер з вагами
    G.add_edge("A", "B", weight=1)
    G.add_edge("B", "C", weight=2)
    G.add_edge("C", "D", weight=1)
    G.add_edge("D", "A", weight=4)
    G.add_edge("A", "C", weight=3)

    return G