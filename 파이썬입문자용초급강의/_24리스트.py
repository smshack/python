# 많은 양의 데이터를 담아야 할 경우 어떻게 처리해야 할까??
# 리스트 : 비슷한 성질을 가진 객체의 나열
# 인덱스 : 0    1   2   3   4   5
# 값    :  3.5  4.3 2.3 3.8 3.2 4.5
students = [3.5, 4.3, 2.3, 3.8, 3.2, 4.5]

print(students)

for student in students:
    print(student)

for i in range(len(students)):
    print(i, "번째 인덱스:", students[i])

sum = 0
for i in students:
    sum = sum+i

print("평균점수:", sum/len(students))

eng = [90, 95, 83, 40, 30, 20, 19, 48, 39, 59]
math = [48, 53, 64, 76, 58, 34, 55, 85, 96, 85]

score = [eng, math]
sum = 0
for engscore in score[0]:
    sum = engscore+sum

print('영어 점수의 평균은: ', sum/len(score[0]))
