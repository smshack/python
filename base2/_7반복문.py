# 반복문을 사용하는 예제
숫자형 = 3
실수형 = 2.1345
문자열 = 'hihi'
논리형 = True
리스트형 = [1, 2, 3, 4, 5]
집합형 = {1, 1, 2, 3, 4, 5, 6}
사전형 = dict()
사전형['사과'] = 'Apple'
사전형['바나나'] = 'Banana'
사전형['코코넛'] = 'Coconut'
튜플형 = (1, 2, 3, 4)

리스트1 = [숫자형, 실수형, 문자열, 논리형, 리스트형, 집합형, 사전형, 튜플형]

for x in 리스트1:
    print(x, type(x))

for i in range(6):
    print(i, " 번째 인덱스 ", 리스트1[i])

count = 0
for i in range(0, 10):
    count += i
    print(i, "번째", count)
