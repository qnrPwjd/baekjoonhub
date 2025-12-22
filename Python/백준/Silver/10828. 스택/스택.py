import sys
input = sys.stdin.readline
n = int(input())

stack = []
stack_pointer = -1

for _ in range(n):
    string = list(input().split())

    if string[0] == 'push':
        stack.append(string[1])
        stack_pointer += 1
    elif string[0] == 'pop':
        if stack_pointer == -1:
            print(-1)
        else:
            print(stack.pop())
            stack_pointer -= 1
    elif string[0] == 'size':
        print(stack_pointer + 1)
    elif string[0] == 'empty':
        if stack_pointer == -1:
            print(1)
        else:
            print(0)
    elif string[0] == 'top':
        if stack_pointer == -1:
            print(-1)
        else:
            print(stack[stack_pointer])
