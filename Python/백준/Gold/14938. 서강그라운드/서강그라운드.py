# 입력 처리
nodes, max_len, edges = map(int, input().split())
items = [0] + list(map(int, input().split()))

INF = float('inf')
graph = [[INF for _ in range(nodes + 1)] for _ in range(nodes + 1)]
for _ in range(edges):
    start, end, dist = map(int, input().split())
    if dist <= max_len:
        graph[start][end], graph[end][start] = dist, dist

for i in range(1, nodes + 1):
    graph[i][i] = 0

# 플로이드-워셜 알고리즘(길이 제약)
for k in range(1, nodes + 1):
    for i in range(1, nodes + 1):
        for j in range(1, nodes + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, nodes + 1):
    tmp = 0
    for j in range(1, nodes + 1):
        if graph[i][j] <= max_len:
            tmp += items[j]
    answer = max(answer,tmp)
  
print(answer)