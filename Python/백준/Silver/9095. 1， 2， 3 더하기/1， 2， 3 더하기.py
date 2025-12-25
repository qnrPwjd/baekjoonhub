n = int(input())
nums = [int(input()) for _ in range(n)]

for num in nums:
    dp = [0] * (num + 1)
    dp[0] = 1
    for i in range(1, num + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]

    print(dp[num])