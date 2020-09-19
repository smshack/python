# 문자열 자료형 뒤집기
# len(): 문자열의 길이를 출력
# isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum()특정한 문자열이 문자와 숫자로만 이루어져있는지 확인
# join(리스트): 여러 개의 문자열을 구분자와 함께 함치는 함수
# sorted(문자열): 각 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
# find(서브 문자열): 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(), lower() : 문자열을 대문자로 혹은 소문자로 변환해주는 함수
# strip(): 좌우로 특정한 문자열을 제거하는 함수
# eval() : 문자열 수식을 계산해주는 함수

str = "Hello World"
num = "1234"
strnum = "1234abcd"
print(str[::-1])
print(len(str))
print(str.upper())
print(str.lower())
print()

print(str.isalpha())
print(num.isdigit())
print(strnum.isalnum())
print()

list = ['Hello', 'World', "서명석"]
print('-'.join(list))
print(sorted(str))
print(''.join(list))
list = sorted(str, reverse=True)
print(''.join(list))
print()

str = 'I wanna Watch a movie'
list = str.split(' ')
print(list)
print()

str = "I like  you like"
for i in range(len(str)):
    print(i, "번째 인덱스", str[i])
print(str.find('like'))
print(str.find('like', 5))
print(str.find('love'))
print()

str = " Hello World "
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print()

str = "ttHello Worldtt"
print(str.strip('t'))

exp = "(203+87)*3-(30/6)"
print(eval(exp))
