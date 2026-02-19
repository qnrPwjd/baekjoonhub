def diffusion(): #확산
    move = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(column):
            if dust[i][j] >= 5:
                d = dust[i][j] // 5
                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < row and 0 <= nj < column and dust[ni][nj] != -1:
                        move[ni][nj] += d
                        dust[i][j] -= d
    for i in range(row):
        for j in range(column):
            dust[i][j] += move[i][j]

def air_clean():
    # 공기 청정기 위쪽(시계 방향)
    start = cleaner[0]
    # 1. 위로
    for i in range(start - 1, 0, -1):
        dust[i][0]= dust[i - 1][0]
    # 2. 오른쪽으로
    for j in range(0, column - 1):
        dust[0][j] = dust[0][j + 1]
    # 3. 아래로
    for i in range(0, start):
        dust[i][column - 1] = dust[i + 1][column - 1]
    # 4. 왼쪽으로
    for j in range(column - 1, 1, -1):
        dust[start][j] = dust[start][j - 1]
    dust[start][1] = 0
    
    # 공기 청정기 아래쪽(반시계 방향)
    start = cleaner[1]
    # 1. 오른쪽으로
    for i in range(start + 1, row - 1):
        dust[i][0] = dust[i + 1][0]
    # 2. 아래로
    for j in range(0, column - 1):
        dust[row - 1][j] = dust[row - 1][j + 1]
    # 3. 왼쪽으로
    for i in range(row - 1, start, -1):
        dust[i][column - 1] = dust[i - 1][column - 1]
    # 4. 위로
    for j in range(column - 1, 1, -1):
        dust[start][j] = dust[start][j - 1]
    dust[start][1] = 0

row, column, time = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(row)] # 방 정보
cleaner = [] # 공기청정기

for i in range(row):
    if dust[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i + 1)
        break

for _ in range(time):
    diffusion()
    air_clean()

dust[cleaner[0]][0], dust[cleaner[1]][0] = 0, 0
print(sum(map(sum, dust)))