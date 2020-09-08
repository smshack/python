print('*****************튜플 자료형************************')
print('사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형')
print('앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과 대비')
print('사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 변경(Immutable)자료형을 키로 사용할 수 있음')
print('파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 검색 및 수정에 있어 O(1)의 시간에 처리 가능')

print('****************************************************')
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다")

print(list(data.keys()))
print(list(data.values()))

print('----------------------------------------------')
print('-- 키 데이터만 담은 리스트/값 데이터만 담은 리스트')
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)
print('')

print('-- 각 키에 따른 값을 하나씩 출력')
for key in key_list:
    print(data[key])
