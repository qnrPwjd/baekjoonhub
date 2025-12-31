import sys
input = sys.stdin.readline # 1만개면 빠른 입출력이 필요할 수도?

k, n = map(int, input().split())
# 정렬해봐야 연산 횟수가 14만번을 못넘음. 충분히 빠를 것
lines_len = sorted([int(input()) for _ in range(k)], reverse = True)
# 가지고 있는 랜선의 최대 길이 
max_len = lines_len[0]
# 1cm
start = 1

# 이분 탐색
while start <= max_len:
    mid = (start + max_len) // 2

    lines = 0
    for line_len in lines_len:
        lines += (line_len // mid)

    if lines < n:
        max_len = mid - 1
    else:
        start = mid + 1

print(max_len)