lA = int(input())
arrA = list(map(int, input().split()))
lB = int(input())
arrB = list(map(int, input().split()))

# dictational longest common subsequence
def dlcs(arrA : list, arrB : list) -> list:
    if len(arrA) == 0 or len(arrB) == 0:
        return []
    
    tmp1, tmp2 = max(arrA), max(arrB)
    idx1, idx2 = arrA.index(tmp1), arrB.index(tmp2)

    if tmp1 == tmp2:
        return [tmp1] + dlcs(arrA[idx1 + 1 : ], arrB[idx2 + 1 : ])
    elif tmp1 > tmp2:
        arrA.pop(idx1)
        return dlcs(arrA, arrB)
    else:
        arrB.pop(idx2)
        return dlcs(arrA, arrB)
    
answer = dlcs(arrA, arrB)
print(len(answer))
print(*answer)