from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement
print('*****************순열************************')
print('서로 다른 n 개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것')
print('{"A","B","C"} 에서 두개를 선택하여 나열하는 경우: "ABC","ACB","BAC","BCA","CAB","CBA"')
print('****************************************************')
print('***********기본 사용 방법*************')
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)
print('----------------------------------------------')
print('***********조합*************')
print('서로 다른 n 개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것')
result = list(combinations(data, 2))
print(result)

print('----------------------------------------------')
print('***********중복 순열*************')
result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기(중복허용)
print(result)

print('----------------------------------------------')
print('***********중복 조합*************')
result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기(중복허용)
print(result)

print('----------------------------------------------')

print('****************************************************')
