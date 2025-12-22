n, k = map(int, input().split())

queue = list(range(1, n + 1))

print('<', end = '')
while len(queue) >= 1:
    if len(queue) == 1:
        print(queue.pop(0), end = '')
        break
    for _ in range(k - 1):
        queue.append(queue.pop(0))
    print(queue.pop(0), end = ', ')
print('>')