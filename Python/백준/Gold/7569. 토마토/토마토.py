import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

day = 0
count = 0
ripped = 0
q = deque()
size = m * n * h

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                q.append([k, i, j])
                count += 1
            elif box[k][i][j] == -1:
                size -= 1

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while q:
    if count == 0:
        day += 1
        count = ripped
        ripped = 0
    
    z, y, x = q.pop()
    count -= 1
    size -= 1

    tmp_count = 0
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1
            tmp_count += 1
            q.appendleft([nz, ny, nx])
    
    ripped += tmp_count

if size == 0:
    print(day)
else:
    print(-1)