import sys
input = sys.stdin.readline

n = int(input())
points_by_step = [0] * (n + 1)
point_each_step = [0] + [int(input()) for _ in range(n)]
step_counter = 0

for i in range(1, n + 1):
    if i == 1:
        points_by_step[i] = point_each_step[i]
    elif i == 2:
        points_by_step[i] = point_each_step[i] + point_each_step[i - 1]
    else:
        points_by_step[i] = max(point_each_step[i] + points_by_step[i - 2], 
                                point_each_step[i] + point_each_step[i - 1] + points_by_step[i - 3])
        
print(points_by_step[n])