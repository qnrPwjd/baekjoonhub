import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)

# 무향 그래프 입력
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 필수로 지나가야 하는 노드들
node1, node2 = map(int, input().split())

# 다익스트라
def dijkstra(start, end):
    global graph

    priority_queue = []
    heapq.heappush(priority_queue, (0, start)) # 시작 node와 거리를 우선순위 큐에 추가
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0

    while priority_queue: # 우선순위 큐에 내용물이 남아있는 동안
        current_distance, current_node = heapq.heappop(priority_queue) # 가장 거리가 짧은 node 추출
        
        for neighbor, weight in graph[current_node]: # 현재 node의 인접 node들에 대해
            distance = current_distance + weight # 인접노드들의 거리 측정
            
            if distance < distances[neighbor]: # 거리가 측정된 적이 없거나 새로 측정한 거리가 더 짧다면
                distances[neighbor] = distance # 최단 거리 갱신
                heapq.heappush(priority_queue, (distance, neighbor)) # 우선순위 큐에 인접 node와 갱신된 거리 추가

    return distances[end]

# 1번 -> 필수 1 -> 필수 2 -> 끝 노드
dist1 = dijkstra(1, node1) + dijkstra(node1, node2) + dijkstra(node2, n)
# 1번 -> 필수 2 -> 필수 1 -> 끝 노드
dist2 = dijkstra(1, node2) + dijkstra(node2, node1) + dijkstra(node1, n)
# 둘 중 최소 거리를 고른다
dist = min(dist1, dist2)

if dist >= INF : print(-1)
else : print(dist)