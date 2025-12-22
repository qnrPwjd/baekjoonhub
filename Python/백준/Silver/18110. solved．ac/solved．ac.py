import sys
input = sys.stdin.readline
def half_up(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
    
n = int(input())
if n == 0:
    print(0)
else:
    levels = [int(input()) for _ in range(n)]
    levels.sort()
    cutline_high = half_up(n * 0.15)
    cutline_low = n - cutline_high

    avg_level = sum(levels[cutline_high:cutline_low]) / (n - 2 * cutline_high)
    print(half_up(avg_level))