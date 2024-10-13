import heapq

def dijkstra(graph, start):
    # Ініціалізація найкоротших шляхів
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, attributes in graph[current_node].items():
            distance = attributes['weight']
            new_distance = current_distance + distance

            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return shortest_paths