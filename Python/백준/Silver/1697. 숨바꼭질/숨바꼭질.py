n, k = map(int, input().strip().split())
visited = [0 for _ in range(100001)]
queue = [(n, 0)]
visited[n] = 1

while queue:
    cur, time = queue.pop(0)

    if cur == k:
        print(time)
        break

    for next_pos in (cur - 1, cur + 1, cur * 2):
        if 0 <= next_pos <= 100000 and visited[next_pos] == 0:
            visited[next_pos] = 1
            queue.append((next_pos, time + 1))