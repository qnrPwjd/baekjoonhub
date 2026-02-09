input_str = input().strip()
bomb_str = input().strip()

stack = []
bomb_len = len(bomb_str)

for char in input_str:
    stack.append(char)
    if ''.join(stack[-bomb_len:]) == bomb_str:
        del stack[-bomb_len:]

print("".join(stack) if stack else "FRULA")