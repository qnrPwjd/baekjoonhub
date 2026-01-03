# 18870 좌표 압축
n = int(input())
array = list(map(int, input().strip().split()))
# 중복 제거, 정렬
sorted_set_array = sorted(list(set(array)))
# 좌표와 인덱스를 뒤집어서 딕셔너리로 접어 넣는다. 이를 통해 좌표가 압축된다
coord_dict = {value : idx for idx, value in enumerate(sorted_set_array)}
# 원본 배열을 순회하면서 해당하는 좌표 압축값(인덱스)를 산출
result = [str(coord_dict[num]) for num in array]
# 출력
print(' '.join(result))