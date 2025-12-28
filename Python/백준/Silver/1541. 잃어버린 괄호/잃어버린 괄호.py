digit = 0
parsed = []
pre_parsed = input().strip()

# 문자열 파싱(숫자는 숫자대로, 문자는 문자대로, 소수점 입력은 없다.)
for idx, char in enumerate(pre_parsed):
    if char.isdigit():
        digit = digit * 10 + int(char)
    else:
        parsed.append(digit)
        digit = 0
        parsed.append(char)
    
    if idx == len(pre_parsed) - 1:
        parsed.append(digit)

result = 0
tmp = 0
minus_checker = False

# 파싱된 문자열을 순회할거임
for val in parsed:
    # 만약 '-'가 등장한다면
    if val == '-':
        # 그 뒤로는 '+'도 전부 '-'취급해도 상관 없잖아?
        # '-'가 나오면 당연히 '-'취급할 거고
        minus_checker = True
        continue
    
    if minus_checker:
        if val == '+':
            continue
        else:
            val *= -1
    
    if val == '+':
        continue
    result += val
print(result)