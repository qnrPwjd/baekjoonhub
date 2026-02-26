infix = list(input().strip())

def infix_to_postfix(infix : str):
    postfix = ''
    stack = []
    instack_priority = {'(' : 0, '+' : 1, '-': 1, '*': 2, '/': 2}
    outstack_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

    for item in infix:
        if item.isalpha():
            postfix += item
        else:
            if stack == []:
                stack.append(item)
            else:
                if item == ')':
                    while stack[-1] != '(':
                        postfix += stack.pop()
                    stack.pop()
                else:
                    while stack:
                        if instack_priority[stack[-1]] < outstack_priority[item]:
                            stack.append(item)
                            break
                        else:
                            postfix += stack.pop()
                    if stack == []:
                        stack.append(item)
    while stack:
        postfix += stack.pop()

    return postfix

print(infix_to_postfix(infix))