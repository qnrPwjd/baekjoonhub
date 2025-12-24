import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = {input().strip() for _ in range(n)}
not_seen = {input().strip() for _ in range(m)}

not_heard_and_seen = sorted(list(not_heard & not_seen))
print(len(not_heard_and_seen))
for person in not_heard_and_seen:
    print(person)