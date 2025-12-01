import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, node = heapq.heappop(pq)

        if current_dist > distances[node]:
            continue

        for edge in graph[node]:
            neighbor = edge["node"]
            weight = edge["weight"]

            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances