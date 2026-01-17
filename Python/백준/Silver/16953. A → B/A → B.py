a, b = map(int, input().split())

two_times = lambda x : x * 2
shift_plus_one = lambda x : x * 10 + 1
queue = [[a, 0]]
flag = False

while queue:
    cur, time = queue.pop()

    if cur == b:
        print(time + 1)
        flag = True
        break

    two_time = two_times(cur)
    shift = shift_plus_one(cur)
    if two_time <= b:
        queue.append([two_time, time + 1])
    if shift <= b:
        queue.append([shift, time + 1])

if not flag:
    print(-1)