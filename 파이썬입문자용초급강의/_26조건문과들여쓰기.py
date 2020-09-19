# 첫 명령어는 들여쓰기 없이 시작해야 함
# 조건문, 반복문 등의 문법을 사용할 때는 콜론(:) 으로 명령어의 끝을 알림
# 콜론(:)의 다음 줄 부터는 들여쓰기의 간격이 모두 일정해야 함

score = 65
if score >= 80:
    print("Good")
    print("점수가 80점을 넘었습니다")
elif score >= 70:
    print("Not Bad")
    print("점수가 70점 이상입니다")
else:
    print("Bad")
    print("공부좀 해라")

print("어떤 내용")


grade = 85
if grade < 90 and grade >= 80:
    print("grade good")


list = [1, 2, 3]
if 2 in list:
    print("2가 리스트에 포함되어 있습니다")
