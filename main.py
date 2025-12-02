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
    # Visualize any graph
    print("\nVisualizing a graph graph...")
    visualize_graph(graph)

if __name__ == "__main__":
    main()
