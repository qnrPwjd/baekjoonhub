from collections import deque

n, k = map(int, input().strip().split())
visited = [-1 for _ in range(100001)]
queue = deque()
queue.append(n)
visited[n] = 0

while queue:
    cur = queue.popleft()

    if cur == k:
        print(visited[cur])
        break

    for idx, next_pos in enumerate((cur * 2, cur - 1, cur + 1)):
        if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
            if idx == 0:
                visited[next_pos] = visited[cur]
                queue.appendleft(next_pos)
            else:
                visited[next_pos] = visited[cur] + 1
                queue.append(next_pos)