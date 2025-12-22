import sys
input = sys.stdin.readline
n = int(input())

queue = []

for _ in range(n):
    string = list(input().split())
    if string[0] == 'push':
        queue.append(string[1])
    if string[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    if string[0] == 'size':
        print(len(queue))
    if string[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if string[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if string[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])