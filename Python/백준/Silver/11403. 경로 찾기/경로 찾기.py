n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
INF = 1000000

# 최소 거리와 해당하는 유저를 저장할 변수
min_dist = INF
min_user = 0

# 플로이드-워셜 알고리즘
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if (graph[i][k] != 0 and graph[i][k] != INF) and \
                (graph[k][j] != 0 and graph[k][j] != INF):
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 or graph[i][j] != INF:
            print(graph[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print()