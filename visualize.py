import matplotlib.pyplot as plt
import networkx as nx
import json

def load_graph(path="graph.json"):
    """Load graph from JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def visualize_graph(graph):
    """
    Visualize a graph.
    - Works with both weighted and unweighted adjacency lists.
    - Weighted format: {"A": [{"node": "B", "weight": 4}, ...]}
    - Unweighted format: {"A": ["B", "C", ...]}
    """
    G = nx.Graph()

    for node, neighbors in graph.items():
        for edge in neighbors:
            # Detect if neighbor is dict (weighted) or string (unweighted)
            if isinstance(edge, dict):
                nbr = edge["node"]
                weight = edge.get("weight", 1)  # default weight = 1
                G.add_edge(node, nbr, weight=weight)
            else:
                G.add_edge(node, edge)

    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes + labels
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos,
        with_labels=True,
        node_size=500,
        font_size=10,
        font_color="white",
        edge_color="gray"
    )

    # If weighted edges exist, draw labels
    if any("weight" in data for _, _, data in G.edges(data=True)):
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.title("Graph Visualization")
    plt.show()
