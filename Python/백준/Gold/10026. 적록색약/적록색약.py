n = int(input())

pic_normal = []
pic_cw = []
for i in range(n):
    line = input().strip()
    pic_normal.append(list(line))
    pic_cw.append(list(line.replace('G','R')))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0 for _ in range(n)] for _ in range(n)]
answer_normal = 0
answer_cw = 0

def bfs(x, y, area_count, mode = 'normal'):
    global n, pic_normal, pic_cw, visited

    if visited[y][x] == 1:
        return area_count

    if mode == 'cw':
        pic = pic_cw
    else:
        pic = pic_normal

    queue = [[y, x]]
    visited[y][x] = 1
    color_cur = pic[y][x]

    while queue:
        y, x = queue.pop(0)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                if pic[ny][nx] == color_cur:
                    visited[ny][nx] = 1
                    queue.append([ny, nx])

    return area_count + 1

for i in range(n):
    for j in range(n):
        answer_normal = bfs(i, j, answer_normal)

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        answer_cw = bfs(i, j, answer_cw, 'cw')

print(f"{answer_normal} {answer_cw}")