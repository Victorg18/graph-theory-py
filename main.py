import json
from bfs import bfs
from dfs import dfs
from compare_orders import compare_orders
from dijkstra import dijkstra
from visualize import visualize_graph

# Load graph from JSON
with open("graph.json", "r") as f:
    graph = json.load(f)
with open("weighted_graph.json", "r") as f:
    weighted_graph = json.load(f)

def main():
    # Run Dijkstra on weighted graph
    distances = dijkstra(weighted_graph, "A")
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    print("Shortest distances from A (sorted):")
    for node, dist in sorted_distances:
        print(f"{node}: {dist}")

    # Visualize any graph
    print("\nVisualizing weighted graph...")
    visualize_graph(weighted_graph)

if __name__ == "__main__":
    main()
