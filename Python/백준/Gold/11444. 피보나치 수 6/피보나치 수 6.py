# 도가뉴 항등식(d'Ocagne's identity)
# 피보나치 수열에 대해 다음의 항등식이 성립
# F_(n + m) = F_(m - 1) * F_n + F_m * F_(n + 1)
# m = n 이라면(피보나치 수열의 짝수 항에 대해)
# F_2n = F_n * (F_(n - 1) + F_(n + 1))
# m = n + 1 이라면(피보나치 수열의 홀수 항에 대해)
# F_(2n + 1) = F_n ** 2 + F_(n + 1) ** 2
import sys
sys.setrecursionlimit(10 ** 8)
memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 1

def dp(num):
    if num not in memo.keys():
        if num % 2 == 0:
            memo[num] = (dp(num // 2) * (dp(num // 2 - 1) + dp(num // 2 + 1))) % 1000000007
        else:
            memo[num] = (dp(num // 2) ** 2 + dp(num // 2 + 1) ** 2) % 1000000007
    return memo[num]

n = int(input())
print(dp(n))