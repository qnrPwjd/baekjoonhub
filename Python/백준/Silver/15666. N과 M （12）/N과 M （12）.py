# 입력 자체는 이게 끝이라 굳이 빠른 입출력이 필요하지는 않을 듯
n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

answer = []
l = len(arr)
answer_top = 0

# 백트래킹
def backTracking():
    # 정답을 담아 줄 answer 리스트를 끌어온다
    global answer, arr, m

    # 조건이 맞으면 출력
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    # dfs 
    for item in arr:
        if len(answer) == 0:
            answer.append(item)
            backTracking()
            answer.pop()
        else:
            if item < answer[-1]:
                continue
            else:
                answer.append(item)
                backTracking()
                answer.pop()

backTracking()