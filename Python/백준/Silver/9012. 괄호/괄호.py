stack = []
stack_pointer = -1
n = int(input())

for _ in range(n):
    string = input()
    for idx, char in enumerate(string):
        if char == '(':
            stack.append(char)
            stack_pointer += 1
        elif char == ')':
            if (stack_pointer == -1) or stack[stack_pointer] != '(':
                print("NO")
                break
            else:
                stack.pop()
                stack_pointer -= 1

        if idx == len(string) - 1:
            if stack_pointer == -1:
                print("YES")
            else:
                print("NO")

    stack = []
    stack_pointer = -1