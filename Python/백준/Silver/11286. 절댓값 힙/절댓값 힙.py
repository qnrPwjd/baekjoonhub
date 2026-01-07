import heapq as hq
import sys

input = sys.stdin.readline

class Node:
    def __init__(self, abs_val, sign):
        self.abs_val = abs_val
        self.sign = sign

    def __lt__(self, other):
        if self.abs_val == other.abs_val:
            return self.abs_val * self.sign < other.abs_val * other.sign
        else:
            return self.abs_val < other.abs_val
    
n = int(input())

heap = []

for _ in range(n):
    num = int(input())
    if num != 0:
        if num < 0:
            sign = -1
            unsigned_val = abs(num)
            hq.heappush(heap, Node(unsigned_val, sign))
        elif num > 0:
            sign = 1
            unsigned_val = abs(num)
            hq.heappush(heap, Node(unsigned_val, sign))
    else:
        if len(heap) == 0:
            print(0)
        else:
            node = hq.heappop(heap)
            pop_val, sign = node.abs_val, node.sign
            print(pop_val * sign)