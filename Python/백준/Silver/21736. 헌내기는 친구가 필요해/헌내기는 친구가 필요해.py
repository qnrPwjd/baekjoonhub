n, m = map(int, input().strip().split())

campus = [list(input()) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

people = 0
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = []

counter = 0

def find_I_loc(campus):
    for i in range(n):
        for j in range(m):
            if campus[i][j] == 'I':
                return (i, j)

I_loc = find_I_loc(campus)
queue.append(I_loc)
visited[I_loc[0]][I_loc[1]] = 1

while queue:
    curY, curX = queue.pop(0)
    for k in range(4):
        ny = curY + dy[k]
        nx = curX + dx[k]

        if ny >= n or ny < 0 or nx >= m or nx < 0: continue
        if visited[ny][nx] == 1: continue
        if campus[ny][nx] == 'X': visited[ny][nx] = 1; continue

        if campus[ny][nx] == 'P':
            visited[ny][nx] = 1
            counter += 1
        elif campus[ny][nx] == 'O':
            visited[ny][nx] = 1
        queue.append((ny, nx))

if counter == 0:
    print("TT")
else:
    print(counter)