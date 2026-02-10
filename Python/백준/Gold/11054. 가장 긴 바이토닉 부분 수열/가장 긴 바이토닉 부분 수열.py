# |가장 긴 증가하는 부분 수열| + |가장 긴 감소하는 부분 수열| - 1
n = int(input())
a = list(map(int,input().split()))
dp = [1 for _ in range(n)]
dp1 = [1 for _ in range(n)]
sum = []

# 가장 긴 증가하는 부분 수열
for i in range(1, n):
    count = 0
    for j in range(i):
        if(a[i] > a[j] and count < dp[j]):
            count = dp[j]
            dp[i] += 1

# 가장 긴 감소하는 부분 수열
for i in range(n - 2, -1, -1):
    count = 0
    for j in range(n - 1, i, -1):
        if(a[i] > a[j] and count < dp1[j]):
            count = dp1[j]
            dp1[i] += 1

for i in range(n):
    sum.append(dp[i] + dp1[i])

print(max(sum) - 1)