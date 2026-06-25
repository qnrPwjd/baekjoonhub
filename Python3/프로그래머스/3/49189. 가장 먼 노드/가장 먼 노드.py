from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    
    for start, end in vertex:
        graph[start].append(end)
        graph[end].append(start)
    
    dist = [-1] * (n + 1)
    dist[1] = 0
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    max_dist = max(dist)
    
    return dist.count(max_dist)