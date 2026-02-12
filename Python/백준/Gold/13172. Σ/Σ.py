# (x ^ pow - 2) mod 1000000007 계산
def dcq(x, pow):
  res = 1
  piv = x
  while(pow >= 1):
    if (pow % 2 == 1):
      res = (res * piv) % mod
    pow //= 2
    piv = (piv * piv) % mod
  return res

mod = 10 ** 9 + 7
ans = 0
m = int(input())
for i in range(m):
  p, q = map(int, input().split())
  ans = (ans + (q * dcq(p, mod-2))) % mod
print(ans % mod)