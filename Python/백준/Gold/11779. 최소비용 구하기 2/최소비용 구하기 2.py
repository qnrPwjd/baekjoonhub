import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

start, end = map(int, input().split())
pre = [0 for _ in range(n + 1)]
INF = int(1e9)

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, [0, start])
    dists = [INF for _ in range(n + 1)]
    dists[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if dists[node] < dist:
            continue

        for neighbor, time in graph[node]:
            cost = dist + time
            if cost < dists[neighbor]:
                dists[neighbor] = cost
                pre[neighbor] = node
                heapq.heappush(queue, [cost, neighbor])

    return dists[end]

answer = dijkstra(start, end)
print(answer)

path = []
cur = end
while cur != 0:
    path.append(cur)
    cur = pre[cur]

print(len(path))
print(*path[ : : -1])