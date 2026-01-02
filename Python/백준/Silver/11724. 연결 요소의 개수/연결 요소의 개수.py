import sys
input = sys.stdin.readline
count = 0

def bfs(graph, start, visited = None):
    if visited == None:
        visited = set()

    queue = []
    queue.append(start)
    visited.add(start)
    global count
    count += 1

    if start not in graph.keys():
        return

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

n, m = map(int, input().strip().split())
graph = {}

for _ in range(m):
    s, e = map(int, input().strip().split())
    if s not in graph.keys():
        graph[s] = [e]
    else:
        graph[s].append(e)

    if e not in graph.keys():
        graph[e] = [s]
    else:
        graph[e].append(s)

for key, value in graph.items():
    graph[key] = sorted(value)

visited = set()
for node in range(1 , n + 1):
    if node not in visited:
        bfs(graph, node, visited)

print(count)