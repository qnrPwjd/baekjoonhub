n = int(input())

array = [0] + list(map(int, input().split()))
length = [0 for _ in range(n + 1)]

length[1] = 1
for i in range(2, n + 1):
    length[i] = 1
    for j in range(1, i):
        if array[i] > array[i-j]:
            length[i] = max(length[i], 1 + length[i-j])
print(str(max(length)))