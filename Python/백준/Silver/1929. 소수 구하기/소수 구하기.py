m, n = map(int, input().split())
primes = [True for _ in range(n + 1)]
primes[0] = False
primes[1] = False

for i in range(2, int(n**0.5) + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

for k in range(m, n + 1):
    if primes[k]:
        print(k)