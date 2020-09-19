# 튜플(Tuple): 리스트와 비슷한 자료형
# 변경 불가
# 튜플 자체는 바꿀수 없지만
# 튜플 안에 있는 리스트의 내용은 변경 가능
# 인덱싱, 슬라이싱 등의 문법도 그대로 사용이 가능

tuple = (1, 2, 3, 4, 5, 6)

for i in tuple:
    print(i)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

tuple2 = (list1, list2)

print(tuple2)

print(tuple[0:4]*3)
