n = int(input())

# 최소값, 최대값
min_board = [0, 0, 0]
max_board = [0, 0, 0]

for _ in range(n):
    line = list(map(int, input().split()))
    min_board = [min(min_board[:2]) + line[0], min(min_board) + line[1], min(min_board[1:]) + line[2]]
    max_board = [max(max_board[:2]) + line[0], max(max_board) + line[1], max(max_board[1:]) + line[2]]

print(f"{max(max_board)} {min(min_board)}")