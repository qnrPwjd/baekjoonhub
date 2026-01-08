import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    funcs = input()
    size = int(input())
    str_array = input().strip()

    start_index = 0
    end_index = size - 1
    reverse = False
    error_checker = False

    str_array = str_array.lstrip('[')
    str_array = str_array.rstrip(']')
    if len(str_array) != 0:
        input_array = list(map(int, str_array.split(',')))
    else:
        input_array = []

    for func in funcs:
        if func == 'R':
            start_index, end_index = end_index, start_index
            if reverse:
                reverse = False
            else:
                reverse = True
        elif func == 'D':
            if reverse:
                if start_index < end_index:
                    print('error')
                    error_checker = True
                    break
                start_index -= 1
            else:
                if start_index > end_index:
                    print('error')
                    error_checker = True
                    break
                start_index += 1
    
    if error_checker:
        continue

    print('[', end = '')
    if reverse:
        for index in range(start_index, end_index - 1, -1):
            print(input_array[index], end = ',' if index > end_index else '')
    else:
        for index in range(start_index, end_index + 1, 1):
            print(input_array[index], end = ',' if index < end_index else '')
    print(']')