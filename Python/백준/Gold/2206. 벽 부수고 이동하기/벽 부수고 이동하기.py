from collections import deque

n, m = map(int, input().split())
field = [list(map(int, list(input()))) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append((0, 0, 1, 0)) # y, x, dist, wall_broken
    # visited에 벽을 부쉈는지 여부까지 같이 기록한다
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    # 시작점이니까 방문 처리
    visited[0][0][0] = True

    while queue:
        # 좌표, 이동 거리, 벽을 부쉈는지 여부
        y, x, dist, wall_broken = queue.popleft()

        # 목적지인 끝 점에 도달했다면 이동 거리 return
        if y == n - 1 and x == m - 1:
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # field 내에서
            if 0 <= ny < n and 0 <= nx < m:
                # 벽이 아니고, 방문한 적이 없다면
                if field[ny][nx] == 0 and not visited[ny][nx][wall_broken]:
                    visited[ny][nx][wall_broken] = True
                    queue.append((ny, nx, dist + 1, wall_broken))
                # 벽이면서, 벽을 부순적이 없고, 방문한 적이 없다면
                elif field[ny][nx] == 1 and wall_broken == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, dist + 1, 1))

    # 여기까지 왔으면 끝 점에는 도달 못하고 큐가 비었다는 말. 즉, -1 return
    return -1

print(bfs())