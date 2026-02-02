import heapq

def dijkstra(start):
    q = []
    
    heapq.heappush(q, [0, start])
    distances[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distances[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

n, e = map(int, input().split())
start = int(input())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
visited = [0 for _ in range(n + 1)]
distances = [INF for _ in range(n + 1)]
dijkstra(start)

for distance in distances[1:]:
    print('INF' if distance == INF else distance) 