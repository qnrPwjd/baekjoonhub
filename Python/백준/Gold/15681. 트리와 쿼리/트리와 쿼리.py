def solution():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    n, r, q = map(int, input().split())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    visited = [False] * (n + 1)
    subtree_size = [0] * (n + 1)

    def dfs(node):
        visited[node] = True
        subtree_size[node] = 1  # 자신도 포함

        for neighbor in tree[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                subtree_size[node] += subtree_size[neighbor]
    
    dfs(r)
    queries = [int(input()) for _ in range(q)]
    for u in queries:
        print(subtree_size[u])

solution()