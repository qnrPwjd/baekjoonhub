n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))

stack = []
def dfs(nums):
    global stack
    if len(stack) == m:
        print(' '.join(map(str,stack)))
        return
    
    for i in range(n):
        if nums[i] not in stack:
            stack.append(nums[i])
        else:
            continue
        dfs(nums)
        stack.pop()

dfs(nums)