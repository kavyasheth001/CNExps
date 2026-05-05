edges = [
    ('A','B',1),
    ('B','C',2),
    ('A','C',4)
]

dist = {'A':0, 'B':float('inf'), 'C':float('inf')}

for _ in range(len(dist)-1):
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

print(dist)