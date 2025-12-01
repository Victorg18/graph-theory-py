from bfs import bfs
from dfs import dfs

def compare_orders(graph, start="A"):
    bfs_order = bfs(graph, start)
    dfs_order = dfs(graph, start)

    matches = []
    for i in range(1, min(len(bfs_order), len(dfs_order))):
        if bfs_order[i] == dfs_order[i]:
            matches.append(bfs_order[i])

    return matches