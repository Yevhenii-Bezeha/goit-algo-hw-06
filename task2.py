from collections import deque


def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            if new_path:
                return new_path

    return None


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == goal:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'C'

dfs_path = dfs(graph, start_node, goal_node)
bfs_path = bfs(graph, start_node, goal_node)

print(f"DFS Path: {dfs_path}")
print(f"BFS Path: {bfs_path}")

