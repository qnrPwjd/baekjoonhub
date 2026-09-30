# 입력 자체는 이게 끝이라 굳이 빠른 입출력이 필요하지는 않을 듯
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = []
l = len(arr)
arr_idx = [0 for _ in range(l)]

# 백트래킹
def backTracking(end, m):
    # 정답을 담아 줄 answer 리스트를 끌어온다
    global answer, arr

    # 조건이 맞으면 출력
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return
    
    # dfs
    remember = 0 # backTracking을 호출할 때마다 remember를 초기화  
    for index, item in enumerate(arr):
        # 이미 들어가 있지 않거나 이전 backTracking 호출 때 한 번 같은 수를 넣은 적이 없어야 실행(중복 제거)
        if arr_idx[index] == 0 and remember != item:
            answer.append(item)
            arr_idx[index] = 1
            remember = item
            backTracking(end, m)
            answer.pop()
            arr_idx[index] = 0

backTracking(l, m)