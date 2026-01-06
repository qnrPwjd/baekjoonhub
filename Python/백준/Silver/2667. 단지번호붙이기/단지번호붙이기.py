n = int(input())
town = [list(map(int, list(input()))) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = [[0 for _ in range(n)] for _ in range(n)]

def flood_fill(start) -> int:
    queue = [start]
    global visited
    visited[start[0]][start[1]] = 1
    counter = 0

    while queue:
        y, x = queue.pop(0)

        if town[y][x] == 1:
            counter += 1
        else:
            visited[y][x] = 1
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n: continue
            if visited[ny][nx] == 1: continue
            if town[ny][nx] == 0: visited[ny][nx] = 1; continue

            queue.append((ny, nx))
            visited[ny][nx] = 1
    
    return counter

result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            continue
        num = flood_fill((i, j))
        if num != 0:
            result.append(num)

print(len(result))
srt_result = sorted(result)
for val in srt_result:
    print(val)