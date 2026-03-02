# 2467 용액(gold 5)
# 투 포인터 or "이분 탐색"
def solution():
    n = int(input())
    vals = list(map(int, input().split()))

    left, right = 0, n - 1
    diff = float('inf') # 절대값이 가장 큰 경우보다 더 큰 값을 가져야 한다

    for i in range(n - 1): # 첫번째부터 n - 1번째까지 모든 자료들을 돌아보면서 
        cur = vals[i] # i번째 값을 기준으로
        start, end = i + 1, n - 1 # i번째부터 그 뒤의 나머지 모든 자료들에 대해

        while start <= end: # 이분 탐색
            mid = (start + end) // 2
            temp = cur + vals[mid] # temp값은 위에서 설정한 범위의 중간값 + i번째의 값

            if abs(temp) < diff: # 이전까지 합의 절대값의 기록보다 현재 합의 절대값이 더 작다면
                diff = abs(temp) # diff에 해당 절대값을 기록
                left = i # 왼쪽 위치
                right = mid # 오른쪽 위치 기록
                if temp == 0: # 아예 0이 되어버린다면 더 탐색할 필요가 없음(그걸 그대로 출력하면 되니까)
                    break
            
            if temp < 0: # 왼쪽의 절대값이 더 크다면 
                start = mid + 1 # start를 mid다음으로(이분 탐색)
            else: # 오른쪽의 절대값이 더 크다면
                end = mid - 1 # end를 mid 왼쪽으로(이분 탐색) 

    print(vals[left], vals[right]) # 결과 출력

solution()