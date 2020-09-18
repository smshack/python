a = [10, 20, 30, 40, 50, 10, 10]
b = [70, 50, 40]
print(a)
for i in range(len(a)):
    print(i, "번째 인덱스 값 ", a[i])
# count(원소) : 리스트 내 특정 원소가 몇 개 포함되어 있는지 반환
print(a.count(10))
print()
# index(원소) : 리스트 내 특정 원소의 인덱스를 반환
print(a.index(50))
print()

# append(원소) : 리스트의 뒤쪽에 새로운 원소를 삽입
a.append(25)
print(a)
print()

# sort(): 리스트를 오름차순으로 정렬
a.sort()
print(a)
print()

# extend(리스트): 리스트의 뒤쪽에 다른 리스트를 삽입
a.extend(b)
print(a)
print()

# insert(인덱스, 원소): 특정한 위치에 원소를 삽입
a.insert(3, 1000)
print(a)
print()

# remove(원소) : 리스트 내의 특정 원소를 삭제 인덱스 처음에 나온 하나를 없앤다
a.remove(10)
print(a)
print()

# pop(인덱스) :리스트 내 특정 인덱스의 원소를 삭제
a.pop(2)
print(a)
print()

# reverse()리스트를 뒤집는 함수
a.reverse()
print(a)
