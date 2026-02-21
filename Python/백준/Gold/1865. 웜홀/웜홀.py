import sys
input = sys.stdin.readline

def bellman_ford(start):
    INF = 100000
    dists = [INF for _ in range(N + 1)]
    dists[start] = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for neighbor, time in edges[j]:
                if dists[neighbor] > dists[j] + time:
                    dists[neighbor] = dists[j] + time
                    if i == N:
                        return True
    return False

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = [[] for _ in range(N + 1)]

    for _ in range(M):
        start, end, time = map(int, input().split())
        edges[start].append([end, time])
        edges[end].append([start, time])

    for _ in range(W):
        start, end, time = map(int, input().split())
        edges[start].append([end, -time])

    print('YES' if bellman_ford(1) else 'NO')