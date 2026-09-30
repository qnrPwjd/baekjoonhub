row, column = map(int, input().split())
field = [list(input()) for _ in range(row)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
visited = set()

def backtracking(y, x, count):
    global visited, row, column, field, dy, dx
    max_count = count
    visited.add(field[y][x])
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < row and 0 <= nx < column and field[ny][nx] not in visited:
            visited.add(field[ny][nx])
            max_count = max(max_count, backtracking(ny, nx, count + 1))
            visited.remove(field[ny][nx])
    return max_count

print(backtracking(0, 0, 1))