N, r, c = map(int, input().split())
size = 2 ** N

count = 0

while size >= 1:
    if r >= size // 2:
        if c >= size // 2:
            count += (size ** 2) * 3 // 4
            c -= size // 2
        else:
            count += (size ** 2) * 2 // 4
        r -= size // 2
    else:
        if c >= size // 2:
            count += (size ** 2) * 1 // 4
            c -= size // 2
    size //= 2

print(count)