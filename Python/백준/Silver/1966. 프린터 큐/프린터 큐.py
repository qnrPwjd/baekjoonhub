num = int(input())
for _ in range(num):
    # n = number of files, m = current location of the target file
    n , m = map(int, input().split())
    queue = [(i, int(x)) for i, x in enumerate(input().split())]
    target = queue[m][0]
    if n == 1:
        print(1)
        continue
    else:
        cnt = 0
        while True:
            front = queue.pop(0)
            if any(front[1] < other[1] for other in queue):
                queue.append(front)
            else:
                cnt += 1
                if front[0] == target:
                    print(cnt)
                    break