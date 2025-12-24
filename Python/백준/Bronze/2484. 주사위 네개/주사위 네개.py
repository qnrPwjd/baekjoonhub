import sys
input = sys.stdin.readline

n = int(input())
rewards = []
for _ in range(n):
    nums = list(map(int, input().split()))
    list_set_list = list(set(nums))
    # 4개 주사위가 전부 같은 눈
    if len(list_set_list) == 1:
        rewards.append(50000 + list_set_list[0] * 5000)

    # list_set_list의 길이가 2인 경우
    elif len(list_set_list) == 2:
        # 같은 눈 3개
        if nums.count(list_set_list[0]) == 3:
            rewards.append(10000 + list_set_list[0] * 1000)
        elif nums.count(list_set_list[1]) == 3:
            rewards.append(10000 + list_set_list[1] * 1000)
        # 같은 눈 2개씩
        elif nums.count(list_set_list[0]) == 2 and nums.count(list_set_list[1]) == 2:
            rewards.append(2000 + list_set_list[1] * 500 + list_set_list[0] * 500)
    # list_set_list의 길이가 3인 경우
    elif len(list_set_list) == 3:
        for item in list_set_list:
            if nums.count(item) == 2:
                rewards.append(1000 + item * 100)
                break
    # list_set_list의 길이가 4인 경우
    else:
        rewards.append(max(nums) * 100)
# 최대 보상 출력
print(max(rewards))