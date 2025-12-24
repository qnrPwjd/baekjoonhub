import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pw_table = {}
for _ in range(n):
    site, pw = input().split()
    pw_table[site] = pw

for _ in range(m):
    site = input().strip()
    print(pw_table[site])