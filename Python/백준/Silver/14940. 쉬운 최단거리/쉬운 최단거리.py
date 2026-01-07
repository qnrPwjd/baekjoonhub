n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
queue = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x = i
            start_y = j

dist = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    global queue, grid, visited, dist, cnt
    sub_queue = []

    while True:
        cnt += 1
        while queue:
            y, x = queue.pop(0)
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    visited[ny][nx] = 1
                    dist[ny][nx] = cnt
                    sub_queue.append((ny, nx))

        if not sub_queue:
            break

        while sub_queue:
            queue.append(sub_queue.pop(0))

cnt = 0
visited[start_x][start_y] = 1
queue.append((start_x, start_y))
bfs()

for i in range(n):
    for j in range(m):
        if dist[i][j] == 0 and grid[i][j] == 1:
            dist[i][j] = -1

for row in dist:
    print(' '.join(map(str, row)))