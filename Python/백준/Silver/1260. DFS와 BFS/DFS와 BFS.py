def dfs(graph, start, visited = None):
    if start not in graph.keys():
        print(start, end = '')
        return 
    if visited == None:
        visited = set()

    stack = [start]
    while stack:
        current = stack.pop()
        
        if current in visited:
            continue

        visited.add(current)
        print(current, end = ' ')

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)


def bfs(graph, start, visited = None):
    if start not in graph.keys():
        print(start, end = '')
        return 
    if visited == None:
        visited = set()

    queue = []
    queue.append(start)
    visited.add(start)
    print(start, end = ' ')

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                print(neighbor, end = ' ')
                queue.append(neighbor)

n, m, v = map(int, input().strip().split())
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

dfs(graph, v, set())
print()
bfs(graph, v, set())