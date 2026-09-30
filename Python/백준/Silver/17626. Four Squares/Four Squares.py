N = int(input())
squares = [n ** 2 for n in range(int(N ** (1 / 2)) + 1)]
total = 0
nums = [N]
# N보다 작은 모든 제곱수들을 N에서 다 빼가면서 0이 나올때까지 반복. BFS
while len(nums) > 0: # 무한 루프를 구현하기 위함. 사실 while True여도 상관 없을 듯
    total += 1 # 이 녀석이 출력을 할 결과물. count up.
    temp = set() # 얘를 통해 브루트 포스 (squares의 모든 원소들을 하나씩 여기에 있는 애들로 부터 빼준다)
    for num in nums: # nums의 원소들에서 
        for n in squares: # 제곱수들을 
            if n <= num: # 빼서 양수만 된다면 
                temp.add(num - n) # set인 temp에 집어 넣음
    
    if 0 in temp: # 0이 나오면 걔가 최소임
        break # 그러니 반복문 파괴
    nums = list(temp) # 아니면 빼 본 결과들을 가지고 다시 루프
print(total)