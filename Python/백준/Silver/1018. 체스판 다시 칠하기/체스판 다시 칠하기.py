n, m = map(int, input().split())

matrix = [list(input().strip()) for _ in range(n)]
ans_lst = []

ans1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

ans2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

def get_submatrice(m, n, matrix):
    submatrice=[]
    for i in range(m-7):
        for j in range(n-7):
            submatrix = [row[i:i+8] for row in matrix[j:j+8]]
            submatrice.append(submatrix)
    return submatrice

submatrices = get_submatrice(m, n, matrix)

for submatrix in submatrices:
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if submatrix[i][j] != ans1[i][j]:
                cnt1 += 1
            if submatrix[i][j] != ans2[i][j]:
                cnt2 += 1
    ans_lst.append(min(cnt1, cnt2))

print(min(ans_lst))