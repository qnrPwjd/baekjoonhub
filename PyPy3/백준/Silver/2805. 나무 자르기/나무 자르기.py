import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
max_height = max(heights)

while start + 1 < max_height:
    mid = (start + max_height) // 2

    total = 0
    for height in heights:
        total += (height - mid) if height > mid else 0
    
    if total >= m:
        start = mid
    else:
        max_height = mid

print(start)