import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

array = [0] + list(map(int, input().strip().split()))

prefix_sum = [0] * (n + 1)
prefix_sum[1] = array[1]
for i in range(1, n + 1):
    prefix_sum[i] = array[i] + prefix_sum[i - 1]

for _ in range(m):
    s, e = map(int, input().strip().split())
    subset_sum = prefix_sum[e] - prefix_sum[s - 1]
    print(subset_sum)