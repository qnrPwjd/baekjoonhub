import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))

def find_start_end_idx(target, cards):
    start_idx = 0
    end_idx = len(cards) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if cards[mid_idx] < target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    first_idx = start_idx

    start_idx = 0
    end_idx = len(cards) - 1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if cards[mid_idx] <= target:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    last_idx = end_idx

    return first_idx, last_idx

for target in targets:
    first_idx, last_idx = find_start_end_idx(target, cards)
    print(last_idx - first_idx + 1, end = ' ')