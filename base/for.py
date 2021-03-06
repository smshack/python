print('*****************반복문************************')
print('특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법')
print('파이썬에서는 while문과 for 문이 있는데, 어떤ㄱ것을 사용해도 좋음')
print('코딩 테스트에서의 실제 사용예시의 경우 for문이 더 간결한 경우가 많음')
print('')
print('****************************************************')
print('***********while로 1~9까지 각 정수의 합 구하기*************')
print('----------------------------------------------')
i = 1
result = 0

while i <= 9:
    result += i
    i += 1
print(result)

print('----------------------------------------------')
print('***********while로 1~9까지 각 홀수의 합 구하기*************')
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print(result)

print('----------------------------------------------')
print('***********반복문 :for문*************')
print('반복문으로 for문을 이용 가능')
print('for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 in 뒤에 오는 자료형(리스트. 튜플 등) 포함되어 잇는 원소를 첫번째 인덱스 부터 차례대로 하나씩 방문')
print('for 변수 in 리스트:')
print('     실행할 소스코드')
print('for문에서 수를 차례대로 나열 할 때는 range()를 주로 사용함')
print('이 때 range(시작값, 끝값,(증감식)) 형태로 사용')
print('인자를 하나만 넣으면 자동으로 시작값은 0')
print('')
print('----------------------------------------------')
print('80점 이상인 학생들은 모두 합격이라고 표시')

score = [90, 85, 77, 65, 97]
for i in range(5):
    if score[i] >= 80:
        print(i+1, '번 학생은 합격입니다')
print('----------------------------------------------')
print('학생들의 합격 여부 판단 예시 특정 번호의 학생은 제외하기')
cheating_student_list = {2, 4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if score[i] >= 80:
        print(i+1, '번 학생은 합격입니다')
print('----------------------------------------------')
print('중첩된 반복문: 구구단 예시')
for i in range(2, 10):
    for j in range(1, 10):
        print(i, " X ", j, " = ", i*j)
    print()
print('----------------------------------------------')
print('반복문 list 이용')
list = ['one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine', 'ten']

for num in list:
    print(num)

setdata = {1, 2, 3, 4, 4, 5, 5, 6}
print(setdata)

for num in setdata:
    print(num)
print('----------------------------------------------')
for i in score:
    print(i)
print('***********************************************************')
