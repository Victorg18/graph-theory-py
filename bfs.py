from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    order = []
    while queue:
        node = queue.popleft() #FIFO

        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    queue.append(neighbour)

    return order