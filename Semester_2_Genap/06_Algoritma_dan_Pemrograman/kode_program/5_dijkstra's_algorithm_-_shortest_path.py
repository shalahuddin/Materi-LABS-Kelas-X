import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm untuk shortest path.
    Kompleksitas: O((V+E) log V)
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        # Skip jika sudah processed
        if current_dist > distances[current]:
            continue
        
        for neighbor, weight in graph[current].items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Test
print("\n=== DIJKSTRA'S SHORTEST PATH ===")
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = dijkstra(graph, 'A')
print(f"Shortest distances dari A: {distances}")
print(f"A->A: {distances['A']}, A->B: {distances['B']}, A->C: {distances['C']}, A->D: {distances['D']}")
