# 사전 (Dictionary): 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
dict = {}
dict['안녕'] = "Hello"
dict['기적'] = "Miracle"
dict['노력'] = "effort"

dict['안녕'] = "Hi"

del dict['기적']
print(dict)

for i, k in enumerate(dict):
    print("[인덱스:", i, "] 한글: ", k, '\t영어: ', dict[k])

keys = dict.keys()
values = dict.values()
print(keys)
print(values)

key_list = list(keys)
value_list = list(values)

print(key_list)
print(value_list)

if '노력' in dict:
    print("노력이 존재 합니다")

print(sorted(dict))  # 키로 정렬하기 오름차순
print(sorted(dict, reverse=True))  # 키로 정렬하기 내림차순
print(sorted(dict.values()))  # 값으로 정렬하기 오름차순


print(len(dict))
dict.clear()
print(dict)
print(len(dict))
