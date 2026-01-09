import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

day = 0
count = 0
ripped = 0
q = deque()
size = m * n

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])
            count += 1
        elif box[i][j] == -1:
            size -= 1

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while q:
    if count == 0:
        day += 1
        count = ripped
        ripped = 0
    
    y, x = q.pop()
    count -= 1
    size -= 1

    tmp_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
            box[ny][nx] = 1
            tmp_count += 1
            q.appendleft([ny, nx])
    
    ripped += tmp_count

if size == 0:
    print(day)
else:
    print(-1)