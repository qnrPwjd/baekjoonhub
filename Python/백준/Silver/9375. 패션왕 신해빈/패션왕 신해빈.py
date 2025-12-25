n = int(input())

for _ in range(n):
    m = int(input())
    table = {}
    for __ in range(m):
        name, sort = input().strip().split()
        if sort in table.keys():
            table[sort].append(name)
        else:
            table[sort] = [name]
    
    result = 1
    for key, value in table.items():
        result *= (len(value) + 1)
    
    print(result - 1)