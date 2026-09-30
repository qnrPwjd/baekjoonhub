def solution(n, computers):
    visited = set()
    answer = 0

    for i in range(n):
        if i in visited:
            continue

        answer += 1
        queue = [i]

        while queue:
            cur = queue.pop()
            visited.add(cur)
            for idx, linked in enumerate(computers[cur]):
                if idx in visited or idx == cur or linked == 0:
                    continue

                queue.append(idx)

    return answer