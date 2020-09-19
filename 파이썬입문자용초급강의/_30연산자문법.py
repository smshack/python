# 증감 연산자: 기존에 사용하던 증가/감소 기능을 짧게 이용
# 관계 연산자: 두개의 값을 비교하여 관계
# A == B: A와 B 가 같은지 판별 => True, False
# A != B: A가 B와 다른지 판별 => True, False
# A > B
# A < B
# 논리연산자: 여러 개의 수식을 논리적으로 연산
# A and B : A와 B 모두 참인지 판별
# A or B : A 혹은 B가 참인지 판별
# not A : A가 거짓인지 판별

a = 10
a += 10
print(a)

a = 3
b = 7
print(a == b)  # False
print(a != b)  # False
print(a >= b)  # False

a = "ABC"
b = "DEF"

print(a == b)
print(a < b)

a = True
b = False

print(a and b)
print(a or b)
print(not a)

if 3 > 5 or 7 < 10:
    print("야호!!")
