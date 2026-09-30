def solution(n, results):
    fights = [[False for _ in range(n)] for _ in range(n)]
    
    for win, lose in results:
        fights[win - 1][lose - 1] = True

    # 플로이드-워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if fights[i][k] and fights[k][j]:
                    fights[i][j] = True

    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            elif fights[i][j] or fights[j][i]:
                count += 1
        if count == n - 1:
            answer += 1
    
    return answer