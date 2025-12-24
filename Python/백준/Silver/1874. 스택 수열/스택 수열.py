import sys
input = sys.stdin.readline # 별 의미는 없지만... 일단 넣자

n = int(input())
# 입력으로 받을 스택 수열 
stack_array = [int(input()) for _ in range(n)]

stack = [] # 스택 역할을 할 리스트
stack_pointer = -1 # 스택 포인터 역할을 할 변수
record = [] # +, - 기록할 리스트

def push(num):
    global stack_pointer
    stack.append(num)
    stack_pointer += 1
    record.append('+')

def pop():
    global stack_pointer
    stack_pointer -= 1
    record.append('-')
    return stack.pop()
    
possible = True # 스택 수열이 가능한지 여부
n = 1

while (possible):
    if len(stack) == 0:
        push(n)
        n += 1
    elif stack[stack_pointer] == stack_array[0]:
        pop()
        stack_array.pop(0)
        if len(stack_array) == 0:
            break
    elif stack[stack_pointer] < stack_array[0]:
        push(n)
        n += 1
    else:
        possible = False

if possible:
    for action in record:
        print(action)
else:
    print("NO")