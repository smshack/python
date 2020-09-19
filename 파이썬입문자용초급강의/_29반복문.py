# 반복문: 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현: range(시작, 끝+1)
# continue: 만났을 때 더이상 명령어를 실행하지 않고 다음 반복을 진행
# 반복 한번 건너 뛰기
# break: 만났을 때 반복문을 벗어남
# while 특정 조건이 참일 때만 반복 거짓이 되면 빠져나감
sum = 0
for i in range(1, 11):
    print(i)
    sum = sum+i
print("합계: ", sum)


count = 0

for i in "Hello World":
    if i == 'o':
        count = count+1
print("o의 개수는", count, "개입니다")

sum = 0
list = [1, 2, 3, 4, 5]
for i in list:
    sum = sum+i
print("리스트의 원소들의 총 합은:", sum)

sum = 0
for i in list:
    if i % 2 == 1:  # 홀수이면 넘어간다
        continue
    print(i)
    sum = sum+i
print("리스트의 짝수원소들의 총 합은:", sum)

sum = 0
for i in list:
    if i == 4:  # 홀수이면 넘어간다
        break
    print(i)

i = 0
sum = 0
while i <= 5:
    i = i+1
    if i % 2 == 1:
        continue
    sum = sum+i
print("합계:", sum)
