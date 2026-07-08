# 보드에서 빈칸을 먼저 찾고
# 빈칸에 맞는 조각 유무를 테이블에서 확인
# 조각의 회전을 판단 할 방법이...
# 행렬로 도형을 뽑아와서 회전시킨다, 혹은 시작 지점 하나 지정 후 상대 거리 이용(selected)
# dfs든 bfs든 해서 보드에서의 실제 좌표를 먼저 얻고
# 얻어낸 좌표를 정규화(조각(빈 칸)의 실제 좌표 - 조각(빈 칸)의 x, y의 각 최소값)한 후
# 이렇게 얻어낸 좌표를 비교적 간단히 회전해가면서 비교([(y, -x) for x, y in pts])
def get_blocks_or_places(data, check):
    visited = set()
    def dfs(x, y):
        if data[x][y] != check:
            return []
        visited.add((x, y))

        connected = [(x, y)]
        if x > 0 and (x - 1, y) not in visited:
            connected.extend(dfs(x - 1, y))
        if y > 0 and (x, y - 1) not in visited:
            connected.extend(dfs(x, y - 1))
        if x + 1 < len(data) and (x + 1, y) not in visited:
            connected.extend(dfs(x + 1, y))
        if y + 1 < len(data) and (x, y + 1) not in visited:
            connected.extend(dfs(x, y + 1))
        return connected

    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            if (i, j) not in visited:
                block_or_place = dfs(i, j)
                if block_or_place:
                    result.append(block_or_place)

    return result

def norm_and_sort(points):
    min_x = min(list(map(lambda x: x[0], points)))
    min_y = min(list(map(lambda x: x[1], points)))
    normalized = [(x - min_x, y - min_y) for x, y in points]
    return sorted(normalized, key = lambda x: (x[0], x[1]))

def rotate(pts):
    return [(y, -x) for x, y in pts]

def isFillIn(normed_place, block):
    if len(normed_place) != len(block):
        return False

    for _ in range(4):
        block = norm_and_sort(rotate(block))
        if normed_place == block:
            return True

    return False

def solution(game_board, table):
    places = get_blocks_or_places(game_board, 0)
    blocks = get_blocks_or_places(table, 1)

    used_places = set()
    used_blocks = set()
    for i, p in enumerate(places):
        normed_p = norm_and_sort(p)
        for j, b in enumerate(blocks):
            if i not in used_places and j not in used_blocks and isFillIn(normed_p, b):
                used_places.add(i)
                used_blocks.add(j)

    result = 0
    for i in used_blocks:
        result += len(blocks[i])

    return result