# 1389 케빈 베이컨의 6단계 법칙
# 입력은 그래프
# 유저 수 n (2 <= n <= 100), 친구 관계 수 m (1 <= m <= 5000)
# 최단 경로, 플로이드-워셜 알고리즘
# m은 기껏해야 5000정도, 빠른 입출력은 필요 없을 듯 (느리다 싶으면 넣어보자)
n, m = map(int, input().strip().split())

# 무한으로 초기화
INF = 100000000
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

# 입력값에 따라 그래프 초기화
for _ in range(m):
    s, e = map(int, input().strip().split())
    graph[s][e] = 1
    graph[e][s] = 1

# 자기 자신과의 거리는 0
for l in range(1, n + 1):
    graph[l][l] = 0

# 최소 거리와 해당하는 유저를 저장할 변수
min_dist = INF
min_user = 0

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 경유할 때가 더 짧다면 갱신
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 각 유저별 케빈 베이컨 수 계산
for i in range(1, n + 1):
    total_dist = sum(graph[i][j] for j in range(1, n + 1) if graph[i][j] != INF)
    if total_dist < min_dist:
        min_dist = total_dist
        min_user = i

print(min_user)