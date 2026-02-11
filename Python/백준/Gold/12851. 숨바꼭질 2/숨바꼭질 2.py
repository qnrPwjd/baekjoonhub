from collections import deque

n, k = map(int, input().strip().split())
visited = [[-1, 0] for _ in range(100001)]

queue = deque()
queue.append(n)

visited[n][0] = 0
visited[n][1] = 1
counter = 0

while queue:
    cur = queue.popleft()
    
    for next in (cur - 1, cur + 1, cur * 2):
        if 0 <= next <= 100000:
            if visited[next][0] == -1:
                visited[next][0] = visited[cur][0] + 1
                visited[next][1] = visited[cur][1]
                queue.append(next)
                
            elif visited[next][0] == visited[cur][0] + 1:
                visited[next][1] += visited[cur][1]

print(visited[k][0])
print(visited[k][1])