n, m = map(int, input().split())
_, *know = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
knows = 0

def union(node1, node2):
    parent1 = find(node1)
    parent2 = find(node2)

    if parent1 < parent2:
        parent[parent2] = parent1   
    else:
        parent[parent1] = parent2

def find(child):
    if child != parent[child]:
        parent[child] = find(parent[child])

    return parent[child]

for i in know:
    union(knows, i)

parties = []

for _ in range(m):
    count, *party = list(map(int, input().split()))
    parties.append(party)

    for i in range(count - 1):
        union(party[i], party[i + 1])

cnt = 0
for party in parties:
    if find(party[0]) == knows:
        continue
    cnt += 1

print(cnt)