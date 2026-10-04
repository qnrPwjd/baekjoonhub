def solution(players, m, k):
    # m은 서버 증설 기준
    # k는 증설한 서버를 운영하는 시간
    # players는 index시에 게임을 플레이중인 사람 수
    # players를 순회하면서 player를 얻어오면
    # player // m - (증설된 서버) 만큼 서버를 증설하고, 증설한 시간도 같이 기록
    # 증설한 시간이 지나면 증설한 서버는 반환
    # 24시간동안 이를 반복
    server_cur = 0
    server_need = 0
    server_added = [0 for _ in range(24)]

    # 24시간동안
    for time, player in enumerate(players):
        # 반환해야 하는 서버가 있다면 반환
        if time - k >= 0:
            server_cur -= server_added[time - k]
        # 지금 당장 필요한 서버 수를 계산
        server_need = player // m
        # 필요한 서버 수가 지금보다 많다면
        if server_need >= server_cur:
            # 필요한 만큼 서버 증설
            server_added[time] = server_need - server_cur
            server_cur = server_need
    
    print(server_added)
    answer = sum(server_added)
    return answer