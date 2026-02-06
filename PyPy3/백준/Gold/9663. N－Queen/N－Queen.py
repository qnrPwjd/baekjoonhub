n = int(input())

def promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queen(x):
    global answer
    if x == n:
        answer += 1
        return 
    else:
        for i in range(n):
            row[x] = i
            if promising(x):
                n_queen(x + 1)

answer = 0
row = [0 for _ in range(n)]
n_queen(0)
print(answer)