from collections import deque

def bfs(graph, start):
    """Breadth-First Search menggunakan queue"""
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def dfs(graph, start, visited=None):
    """Depth-First Search menggunakan recursion"""
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Test
print("\n=== BFS & DFS ===")
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print(f"BFS dari 0: {bfs(graph, 0)}")
print(f"DFS dari 0: {dfs(graph, 0)}")
