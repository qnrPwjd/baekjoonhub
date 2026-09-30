import sys
input = sys.stdin.readline
n = int(input())

trees = {}
while True:
    try:
        s, e = map(int, input().split())
        if s not in trees.keys():
            trees[s] = [e]
        else:
            trees[s].append(e)
            
        if e not in trees.keys():
            trees[e] = [s]
        else:
            trees[e].append(s)
    except:
        break

parent_nodes = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

def dfs(start):
    global parent_nodes, visited
    if visited[start] == 1:
        return
    
    stack = [start]
    while stack:
        node = stack.pop()
        visited[node] = 1
        if node not in trees.keys():
            return

        children = trees[node]
        for child in children:
            if visited[child] == 1:
                continue
            parent_nodes[child] = node
            stack.append(child)

for i in range(1, n + 1):
    dfs(i)

for j in range(2, n + 1):
    print(parent_nodes[j])