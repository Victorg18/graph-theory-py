def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node not in visited:
        visited.add(node)
        order.append(node)

        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited, order)

    return order

def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()  # LIFO
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add neighbors to stack (reverse for consistent order)
            stack.extend(reversed(graph.get(node, [])))

    return order