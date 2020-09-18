# 1이 될때 까지
'''
어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택 가능
    1. N에서 1을 뺀다
    2. N을 K로 나눈다
예를 들어 N이 17, K가 4라고 가정 이때 1번의 과정을 한번 수행하면 
N은 16 두번째는 K로 나눌수 있음

N 과 K가 주어질 때 최소횟수를 구하는 프로그램

주어진 N에 대하여 최대한 많이 나누는게 최소로 만드는데에 최선
'''
# 공백을 기준으로 구분하여 입력
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때가만 1씩 빼기
    target = (n//k)*k
    print(n, target, result)
    result += (n-target)
    n = target
    print(n, target, result)

    # N이 K 보다 작을 때(더이상 나눌수 없을 때) 반복문 탁출
    if n < k:
        print('반복끝')
        break
    result += 1
    n //= k
    print(n, target, result)
    print('----------------')

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
