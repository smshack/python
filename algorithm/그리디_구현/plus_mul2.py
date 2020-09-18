'''
문제 : 곱하기 혹은 더하기 문제
- 각 자리가 숫자 0 ~9 로만 이루어진 문자열 S가 주어졌을 때
S :0~9
왼쪽 부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
곱하기 혹은 더하기 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요
단, + 보다 X를 먼저 계산하는 일반적인 방식과는 달리
모든 연산은 왼쪽에서 부터 순서대로 이루어 진다고 가정

'''
datastr = input()
data = []

for num in datastr:
    data.append(int(num))
print(data)
result = 0
for i in range(0, len(data)):
    if data[0] != 0 and data[0] != 1:
        result = 1
    if data[i] == 0 or data[i] == 1:
        result += data[i]
    else:
        result *= data[i]

print(result)
