n, m = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]

ladders, snakes = dict(), dict()

for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

queue = [[1, 0]]
visited = [0 for _ in range(101)]
visited[1] = 1

while queue:
    loc, count = queue.pop(0)

    if loc == 100:
        print(count)
        break

    for eye in dice:
        new_eye = loc + eye
        
        if new_eye > 100:
            continue

        if visited[new_eye] == 1:
            continue

        visited[new_eye] = 1

        if new_eye in ladders.keys():
            new_eye = ladders[new_eye]
        elif new_eye in snakes.keys():
            new_eye = snakes[new_eye]
        
        visited[new_eye] = 1
        queue.append([new_eye, count + 1])