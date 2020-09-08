# 변수는 값에 붙이는 특별한 이름
# 변수를 사용하기 위해서는 정의(define) 되어야 함
# 변수에 값을 넣기 위해서는 대입(할당,assignment)
print('--------------------------------------------------')
person = input('값을 입력:')
print('값을 출력:'+person)

# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 0
a = 0
print(a)

print('--------------------------------------------------')

# 선언 : 내가 이 변수를 지금부터 사용할 생각이야
# 정의 : 이 변수의 내용은 ~~ 로 구성될 거야
# 초기화: 이변수의 최초값은 ~~야
string = 'abc'
print(string)


hello = 'hi'
person = 'Park Bo Young'

temp = hello
hello = person
person = temp
print('hello: '+hello)
print('person: '+person)
print('--------------------------------------------------')
# 변수의 종류
# 정수형    int     -5, 0, 10
# 실수형    float   -2.5 0.0 .....
# 문자열    str    문자가 하나든 여러개든 문자열로 취급함
# 논리형    bool    true/false

# 파이썬에서는 상수를 지원하지 않음
