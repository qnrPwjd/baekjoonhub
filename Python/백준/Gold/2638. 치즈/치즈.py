from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
time = 0

def bfs_air():
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == 0:
                    if cheese[ny][nx] == 0:
                        visited[ny][nx] = 1
                        queue.append([ny, nx])
                    elif cheese[ny][nx] == 1:
                        visited[ny][nx] += 1
                else:
                    if cheese[ny][nx] == 1:
                        visited[ny][nx] += 1

while True:
    visited = [[0] * m for _ in range(n)]

    bfs_air()
    time += 1

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1 and visited[i][j] >= 2:
                cheese[i][j] = 0
    
    if sum(map(sum, cheese)) == 0:
        break

print(time)