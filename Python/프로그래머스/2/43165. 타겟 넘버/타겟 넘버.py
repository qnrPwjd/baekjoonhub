def solution(numbers, target):
    stack = [[0, 0]]
    l = len(numbers)
    answer = 0

    while stack:
        cur, idx = stack.pop()

        if idx != l:
            stack.append([cur + numbers[idx], idx + 1])
            stack.append([cur - numbers[idx], idx + 1])
        else:
            if cur == target:
                answer += 1

    return answer