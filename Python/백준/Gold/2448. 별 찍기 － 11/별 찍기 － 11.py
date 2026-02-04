n = int(input())
star = [[' ' for _ in range(2 * n - 1)] for _ in range(n)]

def draw_star(y, x, size):
    if size == 3:
        star[y][x] = '*'
        star[y + 1][x - 1] = '*'
        star[y + 1][x + 1] = '*'
        for i in range(-2, 3):
            star[y + 2][x + i] = '*'
        return
    half_size = size // 2
    draw_star(y, x, half_size)
    draw_star(y + half_size, x - half_size, half_size)
    draw_star(y + half_size, x + half_size, half_size)

draw_star(0, n - 1, n)
for line in star:
    print(''.join(line))