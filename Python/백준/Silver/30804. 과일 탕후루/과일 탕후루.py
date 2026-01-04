from collections import defaultdict 

n = int(input())
fruits = list(map(int, input().strip().split()))

left, right, count = 0, 0, 0 # 포인터, 과일 종류 수
fruit_dict = defaultdict(int) # 과일 종류별 개수를 세어줄 dict
answer = 0 # 답

while right < n: # 이론적으로 O(n)에 끝낼 수 있겠네 
    if fruit_dict[fruits[right]] == 0: # 새로운 과일을 찾으면
        count += 1 # 종류 수를 1 늘려주고
    fruit_dict[fruits[right]] += 1 # 해당 과일이 새 과일인지 여부에 관계없이 해당 과일 개수 +1 

    while count > 2: # 종류가 너무 많다면
        fruit_dict[fruits[left]] -= 1 # 왼쪽에서 하나를 뺀다
        if fruit_dict[fruits[left]] == 0: # 해당 과일이 더 없다면
            count -= 1 # 종류를 1 줄인다
        left += 1 # 왼쪽 포인터를 이동한다

    answer = max(answer, right - left + 1) # 답 갱신
    right += 1 # 오른쪽 포인터 이동

print(answer)