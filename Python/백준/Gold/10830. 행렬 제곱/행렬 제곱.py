n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def matrix_mult(mat1, mat2):
    size = len(mat1)
    result = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000

    return result

def matrix_pow(matrix, exp):
    if exp == 1:
        return [[item % 1000 for item in row] for row in matrix]
    
    half = matrix_pow(matrix, exp // 2)
    squared = matrix_mult(half, half)

    if exp % 2 == 1:
        squared = matrix_mult(squared, matrix)

    return squared

result = matrix_pow(matrix, b)
for line in result:
    print(' '.join(map(str, line)))