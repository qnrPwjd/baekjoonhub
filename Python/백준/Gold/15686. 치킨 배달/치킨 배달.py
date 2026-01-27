n, m = map(int, input().split())
home = []
chick = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            home+=[(i, j)]
        elif temp[j] == 2:
            chick+=[(i, j)]

save = []
answer = 1000000000
l = len(chick)
def backtracking(index, depth):
    global save, answer
    if depth == m:
        temp_ans = 0
        for i in home:
            dist = 1000000000
            for j in save:
                dist = min(dist, abs(i[0] - j[0]) + abs(i[1] - j[1]))
            temp_ans += dist
        answer = min(answer, temp_ans)
        return
        
    for i in range(index, l):
        save.append(chick[i])
        backtracking(i + 1, depth + 1)
        del save[-1]
        
backtracking(0,0)
print(answer)