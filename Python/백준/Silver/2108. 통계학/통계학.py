import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
array.sort()

# 반올림
def half_up(n):
    if n > 0:
        if n - int(n) >= 0.5:
            return int(n) + 1
        else:
            return int(n)
    else:
        if abs(n - int(n)) >= 0.5:
            return int(n) - 1
        else:
            return int(n)

# 산술 평균
print(half_up(sum(array)/n))

# 중앙 값
print(array[n // 2])

# 최빈 값
mode_dict = {}
for num in array:
    if num in mode_dict:
        mode_dict[num] += 1
    else:
        mode_dict[num] = 1
max_mode = max(mode_dict.values())
mode_list = [key for key, value in mode_dict.items() if value == max_mode]
mode_list.sort()
if len(mode_list) >= 2:
    print(mode_list[1])
else:
    print(mode_list[0])

# 범위
print(array[-1] - array[0])