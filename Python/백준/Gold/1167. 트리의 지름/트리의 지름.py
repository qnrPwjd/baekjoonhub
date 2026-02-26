n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    line = list(map(int, input().split()))
    start = line[0]
    end_idx, weight_idx = 1, 2

    while line[end_idx] != -1:
        tree[start].append([line[end_idx], line[weight_idx]])
        end_idx += 2
        weight_idx += 2

def dfs(start, dist):
    global visited
    stack = [[start, dist]]
    visited[start] = 0

    while stack:
        cur_node, cur_dist = stack.pop()

        for neighbor, weight in tree[cur_node]:
            if visited[neighbor] == -1:
                visited[neighbor] = cur_dist + weight
                stack.append([neighbor, cur_dist + weight])

visited = [-1 for _ in range(n + 1)]
dfs(1, 0)
max_dist = max(visited)
farthest_node = visited.index(max_dist)

visited = [-1 for _ in range(n + 1)]
dfs(farthest_node, 0)
max_dist = max(visited)
print(max_dist)