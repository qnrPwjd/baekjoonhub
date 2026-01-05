n, m = map(int, input().strip().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = [(0, 0, 1)]
visited[0][0] = 1

while queue:
    y, x, count = queue.pop(0)

    if x == m - 1 and y == n - 1:
        print(count)
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        
        if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
        if visited[ny][nx] == 1: continue
        if maze[ny][nx] == 0: continue

        queue.append((ny, nx, count + 1))
        visited[ny][nx] = 1