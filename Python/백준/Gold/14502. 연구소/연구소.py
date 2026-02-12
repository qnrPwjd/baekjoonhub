from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 이제 bfs에 더 설명은 필요 없을 것
def bfs(x, y, visited):
    queue = deque()
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([ny, nx])

def count_safe(visited):
    count = 0
    for line in visited:
        for item in line:
            if item == 0:
                count += 1
    return count

empty = []
virus = []

for i in range(n):
    for j in range(m):
        # 벽을 세울 수 있는 위치들을 기록
        if lab[i][j] == 0:
            empty.append([i, j])
        # 바이러스의 위치를 기록
        elif lab[i][j] == 2:
            virus.append([i, j])

result = 0
l = len(empty)
# 빈 공간들(empty)에서 벽을 세울 가능한 3개 위치 전부 선정(feat. 3중 for문)
for i in range(l):
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            count = 0
            # visited 초기화(벽인 부분, 바이러스가 있는 부분은 방문할 필요가 없으므로 방문 처리)
            visited = [[0 if lab[y][x] == 0 else 1 for x in range(m)] for y in range(n)]
            
            # 벽을 세운다
            visited[empty[i][0]][empty[i][1]] = 1
            visited[empty[j][0]][empty[j][1]] = 1
            visited[empty[k][0]][empty[k][1]] = 1

            # 벽을 세웠으니 바이러스를 퍼뜨려 보자
            for v in virus:
                bfs(v[1], v[0], visited)

            # 바이러스를 퍼뜨리고 안전한 구역의 넓이를 구한다(feat. 브루트 포스)
            count = count_safe(visited)
            # 먼저 구한 조합들 중 가장 넓이가 넓은 경우와 비교해 더 넓은 쪽을 채택한다.
            result = max(result, count)
print(result)