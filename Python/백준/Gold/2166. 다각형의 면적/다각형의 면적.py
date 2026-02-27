def solution():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]

    total = 0
    for i in range(n):
        if i != n - 1:
            total += (points[i][0] * points[i + 1][1])
            total -= (points[i][1] * points[i + 1][0])
        else:
            total += (points[n - 1][0] * points[0][1])
            total -= (points[n - 1][1] * points[0][0])

    print(abs(total) / 2)
solution()