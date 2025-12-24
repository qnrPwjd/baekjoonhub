fibo_count = {0 : [1, 0], 1 : [0, 1]}

def fibo(n : int):
    if n in fibo_count.keys():
        return fibo_count[n]
    else:
        fibo_count[n] = [fibo(n - 1)[0] + fibo(n - 2)[0], fibo(n - 1)[1] + fibo(n - 2)[1]]
        return fibo_count[n]
    
n = int(input())
for _ in range(n):
    result = fibo(int(input()))
    print(f"{result[0]} {result[1]}")