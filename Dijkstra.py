import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

def dijkstra(start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cost, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return dist

print(dijkstra('A'))