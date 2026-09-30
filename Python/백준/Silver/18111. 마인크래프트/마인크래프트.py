# 18111 마인크래프트
import sys
input = sys.stdin.readline

n, m, b = map(int, input().strip().split())
ground = [list(map(int, input().strip().split())) for _ in range(n)]

min_time = 100000000
max_height = 257

for height in range(257):
    time = 0
    block = b
    for i in range(n):
        for j in range(m):
            diff = ground[i][j] - height
            if diff > 0:
                time += diff * 2
            elif diff < 0:
                time += -diff
            block += diff
    
    if block < 0: 
        # 남은 블럭 개수가 0보다 작아버리면 이것보다 높은 높이는 찾아보는 의미가 없겠지. 결국은 블럭을 더 써야 하니까
        break
    
    if time <= min_time:
        min_time = time
        max_height = height

print(min_time, max_height)