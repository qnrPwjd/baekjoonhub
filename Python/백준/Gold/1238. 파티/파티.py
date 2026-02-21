import heapq

N, M, X = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, [0, start])
    dists = [INF for _ in range(N + 1)]
    dists[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if dists[node] < dist:
            continue

        for neighbor, time in graph[node]:
            cost = dist + time
            if cost < dists[neighbor]:
                dists[neighbor] = cost
                heapq.heappush(queue, [cost, neighbor])

    return dists[end]

answer = 0
for i in range(1, N + 1):
    if i == X:
        continue
    answer = max(answer, dijkstra(i, X) + dijkstra(X, i))
print(answer)