import heapq # 우선순위 큐를 위한 heapq 모듈

def dijkstra(graph, start, pre):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start)) # 시작 node와 거리를 우선순위 큐에 추가
    distances = {start: 0} # 시작 node에서 시작 node까지의 거리는 0
    visited = set() # 방문한 node를 추적하기 위한 집합

    while priority_queue: # 우선순위 큐에 내용물이 남아있는 동안
        current_distance, current_node = heapq.heappop(priority_queue) # 가장 거리가 짧은 node 추출
        
        if current_node in visited: # 이미 방문한 node라면 무시하지만
            continue
        visited.add(current_node) # 아니라면 현재 node를 방문 처리

        for neighbor, weight in graph[current_node]: # 현재 node의 인접 node들에 대해
            distance = current_distance + weight # 인접노드들의 거리 측정
            # 거리가 측정된 적이 없거나 새로 측정한 거리가 더 짧다면
            if neighbor not in distances or distance < distances[neighbor]: 
                distances[neighbor] = distance # 최단 거리 갱신
                pre[neighbor] = current_node # 경로 추적을 위해 이전 node 갱신
                heapq.heappush(priority_queue, (distance, neighbor)) # 우선순위 큐에 인접 node와 갱신된 거리 추가
    return distances

n = int(input()) # node 수 
m = int(input()) # edge 수

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    # 시작 node, 도착 node, 가중치를 여기서 입력받음
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

pre = {i: None for i in range(1, n + 1)} # 경로 추적을 위한 dictionary
start, end = map(int, input().split())
distances = dijkstra(graph, start, pre) # start node에서 시작하는 Daijkstra 알고리즘
print(distances[end])