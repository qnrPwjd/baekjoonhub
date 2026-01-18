a, b, c = map(int, input().split())
# 모듈러 연산의 성질 : a ≡ b (mod m) 이고 c ≡ d (mod m) 이면, ac ≡ bd (mod m)이다.
# 확장 -> a ≡ b (mod m) 이면 a ^ k ≡ c ^ k (mod m) 이다.
def PowMod(base, exp, mod):
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp //= 2
        base = (base * base) % mod
    return res
print(PowMod(a, b, c))