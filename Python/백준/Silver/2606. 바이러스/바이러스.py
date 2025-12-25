num_node = int(input())
num_edge = int(input())

graph = {}
for _ in range(num_edge):
    s, e = map(int, input().strip().split())
    if s in graph.keys():
        graph[s].append(e)
    else:
        graph[s] = [e]
    
    if e in graph.keys():
        graph[e].append(s)
    else:
        graph[e] = [s]
    
counter = 0
def dfs(graph, start, visited = None):
    if len(graph) == 0 or start not in graph.keys():
        return

    if visited == None:
        visited = set()
    
    global counter
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            counter += 1
            dfs(graph, neighbor, visited)

dfs(graph, 1, set())
print(counter)