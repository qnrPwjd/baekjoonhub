n = int(input())
m = int(input())

INF = 100000000
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    s, e, cost = map(int, input().strip().split())
    graph[s][e] = min(graph[s][e], cost)

for l in range(1, n + 1):
    graph[l][l] = 0

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 경유할 때가 더 짧다면 갱신
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n + 1):
    print(' '.join(map(str, graph[i][1 : ])))