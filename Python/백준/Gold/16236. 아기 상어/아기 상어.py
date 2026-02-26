import sys
from collections import deque
input = sys.stdin.readline

# bfs로 가장 가까운 먹을 수 있는 물고기를 찾는다
def bfs(shark_y, shark_x, baby_size):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[shark_y][shark_x] = True
    dist = 0

    Q = deque()
    Q.append([shark_y, shark_x, dist])
    direction = [(-1, 0),(0, -1),(0, 1),(1, 0)]
    result = []

    while Q:
        y, x, dist = Q.popleft()
        if space[y][x] != 0 and space[y][x] < baby_size:
        # Q. 이거 왜 x, y, dist순서 아님?
        # A. 정렬 기준이 dist라서 가장 깔끔한 코드를 만드려면 이 순서가 맞음
            result.append([dist, y, x])
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n:
                if space[ny][nx] <= baby_size and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    Q.append([ny, nx, dist + 1])
    if len(result) == 0:
        return -1
    else:
        # 굳이 x, y, dist순서로 쓰고 싶다면 여기를 sort(key = lambda x : x[2])로 만들어 주면 됨
        # 근데 이건 조금 더럽잖아?
        result.sort()
        return result[0]

# bfs에서 얻은 가장 가까운 먹을 수 있는 물고기의 위치로 이동하고 경험치(exp)로 반영
# 더이상 먹을 수 있는 물고기가 없다면 지금까지의 시간을 반환
def move_baby_shark(shark_y, shark_x):
    global space
    time = 0
    baby_size = 2
    exp = 0
    while True:
        result = bfs(shark_y, shark_x, baby_size)
        if result == -1:
            return time
                
        min_distance, near_y, near_x = result

        time += min_distance
        exp += 1
        space[near_y][near_x] = 9
        space[shark_y][shark_x] = 0
        shark_y, shark_x = near_y, near_x
        if exp == baby_size:
            baby_size += 1
            exp = 0

n = int(input())
space = []
can_eat = []
for _ in range(n):
    row = list(map(int, input().split()))
    space.append(row)

baby_y, baby_x = 0, 0
for y in range(n):
    for x in range(n):
        if space[y][x] == 9:
            baby_y = y
            baby_x = x
            break

sec = move_baby_shark(baby_y, baby_x)
print(sec)