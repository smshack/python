'''
return이란?
리턴이라고 읽는다. 돌려준다 반환한다 등으로 번역되었다.

함수를 실행한 결과를 함수를 호출한 곳으로 보내준다.
왜 쓰냐면 연산한 결과를 다른곳에 사용하기 위함
처음에 console만 보면 동일해서 헷갈림.
'''


def plus(val1, val2):
    return val1 + val2


result = plus(10, 20)

print(result)
'''
plus()를 호출한 곳으로 값을 돌려준다.

return을 이용하면 함수 실행 결과를 변수에 저장 할 수 있다.

변수에 저장한 값을 다른데 사용할 수 있다.
'''

'''
return을 썼을때와 안썼을 때의 차이
'''


def print_hello(p1, p2):
    print(p1 + p2)


result = plus(10, 20)
print(result)
result = print_hello(10, 20)
print(result)


def minus(val1, val2):
    return val1-val2


def multiple(val1, val2):
    return val1*val2


def divide(val1, val2):
    return val1/val2


def quotient(val1, val2):
    return val1//val2


def remainder(val1, val2):
    return val1 % val2


def squared(val1, val2):
    return val1**val2


print("더하기:", plus(10, 3))
print("빼기:", minus(10, 3))
print("곱하기:", multiple(10, 3))
print("나누기", divide(10, 3))
print("몫", quotient(10, 3))
print("나머지", remainder(10, 3))
print("제곱", squared(10, 3))
