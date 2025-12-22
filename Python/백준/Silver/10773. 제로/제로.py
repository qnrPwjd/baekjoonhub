k = int(input())

stack = []
stack_pointer = -1

for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
        stack_pointer -= 1
    else:
        stack.append(num)
        stack_pointer += 1
print(sum(stack))