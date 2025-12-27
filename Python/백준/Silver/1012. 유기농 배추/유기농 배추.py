import sys
input = sys.stdin.readline

T = int(input())

def find():
    m, n, k = map(int, input().split())

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = []

    counter = 0
    for i in range(m):
        for j in range(n):
            if visited[j][i] == 1 or field[j][i] == 0:
                continue

            queue.append((j, i))
            visited[j][i] = 1
            counter += 1

            while queue:
                curY, curX = queue.pop(0)
                for k in range(4):
                    ny = curY + dy[k]
                    nx = curX + dx[k]

                    if ny >= n or ny < 0 or nx >= m or nx < 0: continue
                    if visited[ny][nx] == 1: continue

                    if field[ny][nx] == 1:
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    print(counter)

for _ in range(T):
    find()