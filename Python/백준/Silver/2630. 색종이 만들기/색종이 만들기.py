n = int(input())

colored_paper = [list(map(int, input().strip().split())) for _ in range(n)]
w = 0
b = 0

def check(x, y, size):
    global w, b
    start = colored_paper[y][x]
        
    if size == 1:
        if start == 0:
            w += 1
        else:
            b += 1
        return 

    for i in range(x, x + size):
        for j in range(y, y + size):
            if colored_paper[j][i] != start:
                check(x, y, size // 2)
                check(x + size // 2, y, size // 2)
                check(x, y + size // 2, size // 2)
                check(x + size // 2, y + size // 2, size // 2)
                return
    
    if start == 0:
        w += 1
    else:
        b += 1

check(0, 0, n)

print(w)
print(b)