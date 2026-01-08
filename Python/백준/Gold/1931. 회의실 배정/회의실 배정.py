import heapq
import sys

input = sys.stdin.readline

class Act:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __lt__(self, other):
        if self.e == other.e:
            return self.s < other.s
        return self.e < other.e

n = int(input())
activities_heap = []

for _ in range(n):
    s, e = map(int, input().split())
    act = Act(s, e)
    heapq.heappush(activities_heap, act)

count = 0   
last_end_time = 0

while activities_heap:
    act = heapq.heappop(activities_heap)
    s, e = act.s, act.e
    if s >= last_end_time:
        count += 1
        last_end_time = e

print(count)