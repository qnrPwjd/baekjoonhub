# 이게 뭐지... 유한상태 오토마타 알고리즘(feat. 이산수학)
from collections import deque
N = int(input())
l = int(input())
check = deque(input().strip())
a = ''
ans = 0
# 큐에 내용물이 있고, 입력 문자열이 남아있는 동안
while check and l > 1:
    temp = a 
    cnt = 0

    # 결국 얘는 큐(입력 string)에서 첫 I를 찾는 코드가 된다
    while temp != 'I' and l > 1: # temp가 비어있거나 I가 아니라면(O라면)
        temp = check.popleft() # 큐에서 내용물을 꺼내와 temp에 넣어준다
        l -= 1 # 그 후 l을 1 줄임 
    
    # 첫 I를 찾았다면
    # 우리는 오직 OI를 찾는다.
    # OI를 세다가 II, OO, IO를 보는 경우 cnt를 올리는 것을 중단
    # IO일 경우는 다시 ...IIOIOI... 형태를 기대해 볼 수 있다.
    while check and l > 1:
        a, b = check.popleft(), check.popleft() # 큐에서 첫 두글자를 꺼내오고
        l -= 2 # 문자열 길이를 감소
        if a == 'O' and b == 'I': # 꺼내온 두 글자가 OI라면 
            cnt += 1  # 카운트를 올림
        elif a == 'I' and b == 'O': # 꺼내온 두 글자가 IO라면
            # O는 다시 큐 앞부분에 넣어주고(이때, 이미 앞의 문자는 I다. 즉, temp를 바꿀 이유가 없다.)
            check.appendleft(b) 
            l += 1 # 넣어줬으니 큐의 길이는 다시 늘려준다
            break # 굳이 여기서 cnt를 초기화 해 줄 필요 없이 break를 통해 위에서 초기화
        else: # II인 경우, OO인 경우는 볼 필요가 없다
            break
    # 첫 I를 찾고 나서부터는 OI의 반복 횟수 - N + 1이 해당 구간의 s_n의 수
    # n = 2에 IOIIO일 경우 cnt = 1, n = 2이므로 ans에는 0과 0을 비교해 0이 더해진다
    # n = 1에 IOIIO일 경우 cnt = 1, n = 1이므로 ans에는 1과 0을 비교해 1이 더해진다
    ans += max(cnt - N + 1, 0) 

print(ans)