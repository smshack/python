# input(): 사용자로부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 변환
# float() :문자열, 정수 등의 자료형을 실수형으로 변환
# min(), max() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 회소값
# bin(), hex() : 10진수 -> 2진수  변환 , 10진수 -> 16진수 변환
# round() : 반올림을 수행
# type(): 자료형의 종류

user_input = input('정수를 입력하세요')
print("입력한 수", int(user_input))
print("입력한 수", float(user_input))

list = [10, 20, 30, 40, 50]

print(list)
print(min(list))
print(max(list))
print(bin(min(list)))
print(hex(min(list)))

print(round(1.2345, 3))

문자열 = "hihi"
숫자 = 3
리스트 = [1, 2, 3, 4, 5]
사전 = {'apple': '사과'}
튜플 = (1, 2, 3, 4, 5, 6)
print(type(문자열))
print(type(숫자))
print(type(리스트))
print(type(사전))
print(type(튜플))
