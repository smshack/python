a = "HELLO WORLD HI"
print("문자열 a:", a)
# 문자열 인덱스 확인
for i in range(len(a)):
    print(i, ' 번째 인덱스:', a[i])
print()
# 문자열 대체 함수
b = a.replace("HELLO", "HI")

print('문자열 대체하기 b:', b)
print()
# 특정 문자열 세기
print('문자열 L의 개수 ', 'count', a.count('L'))
print()

# 특정 문자열의 인덱스 위치
print('문자열 WOR의 인덱스 위치', 'find', a.find("WOR"))
print()

# 전체 문자열을 대/소문자로 바꾸기
lowa = a.lower()
print('전체 문자열 소문자로:', lowa)
upa = lowa.upper()
print('전체 문자를 대문자로:', upa)
print()
# 특정 문자열 지우기
stripa = a.strip("WORLD")
print("특정 문자열 지우기:", stripa)
print()

# 특정 문자열 기준으로 나누기
# 나눠진 형태를 배열 형태로 반환
splita = a.split(" ")
print("특정 문자기준으로 나누기:", splita)
print()

# 자리수 만큼 0으로 채움
# 금액등의 자릿수/단위 수를 나눌때 사용
zfilla = a.zfill(20)
print("출력 형식 제한하기", zfilla)
print()
# 문자열을 숫자로 바꾸기
c = "1234"
d = int(c)
print(d+1000)
