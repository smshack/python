'''
상하 좌우: 문제 설명
여행가  A는 NxN 크기의 정사각형 공간 위에 서있음
이 공간은 1 x 1 크기의 정사각형으로 나누어져 있음
가장 왼쪽 위 좌표는 1 , 1 이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당함
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
시작 좌표는 항상 (1, 1)입니다
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있음

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여
L , R, U, D 중 하나의 문자가 반복적으로 적혀 있음
각 문자의 의미는 다음과 같음
L   왼쪽으로 한칸 이동
R   오른쪽으로 한칸 이동
U   위로 한칸 이동
D   아래로 한칸 이동

이때 여행가가 정사각형 공간을 벗어나는 움직임은 무시


이런 문제는 요구 사항대로 충실히 구현하면 되는 문제
일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션유형으로도 분류되며
구현이 중요한 대표적인 문제 유형

다만, 알고리즘 교재나 문제 풀이 사이트에 따라서 다르게 일컬을 수 있으므로,
코딩 테스트에서의 시뮬레이션 유형, 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다는 정도로만 기억

'''

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
