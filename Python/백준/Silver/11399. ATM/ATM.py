n = int(input())
times = sorted(list(map(int, input().split())))
total = 0
for idx, time in enumerate(times):
    total += time * (n - idx)
print(total)