import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to keep track of nodes with the smallest tentative distance
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Check if this path is already longer than the known shortest path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    0: [(1, 2), (4, 8)],
    1: [(0, 2), (2, 3), (4, 2)],
    2: [(1, 3), (3, 1)],
    3: [(2, 1), (4, 1)],
    4: [(0, 8), (1, 2), (3, 1)]
}

if __name__=="__main__":
    print("hello")
    start_node = 0
    distances = dijkstra(graph, start_node)

    print(distances)
