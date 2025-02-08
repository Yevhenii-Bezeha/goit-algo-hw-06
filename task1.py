import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(stations)

edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"),
         ("E", "F"), ("F", "G"), ("G", "H"), ("B", "E"), ("C", "F")]
G.add_edges_from(edges)

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)
plt.title("City Transport Network")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
avg_degree = sum(degrees.values()) / num_nodes

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Node degrees:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
print(f"Average node degree: {avg_degree:.2f}")
