# 시퀀스(Sequence): 문자열 , 리스트, 튜플 등의 인덱스(Index)를 가지는 자료형

string = "Hello World"
list = ['H', 'e', 'l', 'l', 'o',
        ' ', 'W', 'o', 'r', 'l', 'd']
tuple = ('H', 'e', 'l', 'l', 'o',
         ' ', 'W', 'o', 'r', 'l', 'd')
print(string)
print(list)
print(tuple)
print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in string:
    print(i)

for i in list:
    print(i)

for i in tuple:
    print(i)

string2 = ", Python"

print(string+string2)
print(len(string+string2))

print('H' in list)
print('H' in string)
print('H' in string2)
print('H' in tuple)
