# index(원소): 리스트 내 특정한 원소의 인덱스를 찾기
# reverse(): 리스트의 원소를 뒤집기
# sum(리스트 자료형): 리스트의 모든 원소의 합
# range(시작, 끝): 특정 범위를 지정
# list(특정 범위): 특정 범위의 원소를 가지는 리스트를 반환
# all():  리스트의 모든 원소가 참인지 판별/
# any():하나라도 참인지 판별
# enumerate(): 리스트에서 인덱스와 원소를 함께 추출
#               튜플 형태로 인덱스 와 값이 들어감
# sort(): 리스트의 원소를 정려
# count() :특정한 원소의 개수를 추출
# del : 리스트의 특정 원소를 제거 1개
# insert(삽입인덱스위치, 값): 리스트에 특정 원소를 삽입
# append(): 리스트의 가장 마지막 원소로서 원소를 삽입

lists = ['서명석', '원빈', '소녀시대', '나동빈', '이태일', '이상욱', '이태일']
print(lists)
for i in range(len(lists)):
    print(i, "번째 인덱스", lists[i])
print()
print("소녀시대의 인덱스 번호는?")
print(lists.index('소녀시대'))

print()
print("리스트 뒤집기")

print(lists[::-1])
lists.reverse()
for i in range(len(lists)):
    print(i, "번째 인덱스", lists[i])
print()
print("리스트 원소의 모든 합")
list_num = [1, 4, 5, 7, 8]
print(sum(list_num))

print()
print('특정 범위 지정하기 range')
my_range = range(5, 10)
print(my_range)
rangelist = list(my_range)
print(rangelist)
print()

tf = [True, False, True]
print(all(tf))
print(any(tf))
print()

result = enumerate(lists)
for i, k in result:
    print("인덱스: ", i, '\t원소:', k)
result = enumerate(lists)
print(result)
print(list(result))
lists.sort()
print(lists)
print(lists.count('이태일'))
del lists[1:3]
print(lists)
lists.insert(-1, '삽입1')
print(lists)
lists.insert(2, '삽입2')
print(lists)
lists.append("마지막 원소 삽입")
print(lists)
