def ceil(num):
    return int(num) if num % 1 == 0 else int(num) + 1

def solution(progresses, speeds):
    queue = []
    answer = []

    for progress, speed in zip(progresses, speeds):
        remain_progress = 100 - progress
        available_date = ceil(remain_progress / speed)
        queue.append(available_date)

    while queue:
        available = queue.pop(0)
        available_cnt = 1
        while len(queue) != 0 and queue[0] <= available:
            queue.pop(0)
            available_cnt += 1
        answer.append(available_cnt)
    return answer