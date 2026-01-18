n = int(input())

costs = [list(map(int, input().split())) for _ in range(n)]
total_costs = [[0 for _ in range(3)] for _ in range(n)]
total_costs[0] = costs[0]

for i in range(1, n):
    total_costs[i][0] = min(total_costs[i - 1][1], total_costs[i - 1][2]) + costs[i][0]
    total_costs[i][1] = min(total_costs[i - 1][0], total_costs[i - 1][2]) + costs[i][1]
    total_costs[i][2] = min(total_costs[i - 1][0], total_costs[i - 1][1]) + costs[i][2]

print(min(total_costs[n - 1]))