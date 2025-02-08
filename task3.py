import networkx as nx

G = nx.Graph()

stations = ["A", "B", "C", "D", "E", "F", "G", "H"]

edges_with_weights = [
    ("A", "B", 2), ("B", "C", 1), ("C", "D", 4), ("D", "E", 3),
    ("E", "F", 2), ("F", "G", 1), ("G", "H", 5), ("B", "E", 2),
    ("C", "F", 3)
]

G.add_weighted_edges_from(edges_with_weights)

def dijkstra(graph, start):
    shortest_paths = {}
    for target in graph.nodes():
        if target != start:
            path = nx.dijkstra_path(graph, source=start, target=target, weight='weight')
            shortest_paths[target] = path
    return shortest_paths

shortest_paths_from_A = dijkstra(G, "A")

print("Shortest paths from node A:")
for target, path in shortest_paths_from_A.items():
    print(f"Shortest path to {target}: {path}")
