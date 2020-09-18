'''
미로 탈출 문제
NxM 크기의 직사각형 형태의 미로에 갇혔음
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 함

처음 위치는 (1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있음
이 때 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시되어 있음
미로는 반드시 탈출할 수 있는 형태로 제시됨
이 때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오
칸을 셀때는 시작칸과 마지막 칸을 모두 포함해서 계산
------------------------------------------------------------------------------
문제 해결 아이디어
BFS 는 시작 지점에서 가까운 노드 부터 차례대로 그래프의 모든 노드를 탐색
상 하 좌 우 로 연결된 모든 노드로의 거리가 1로 동일함
따라서 (1,1) 지점 부터 BFS를 수행하여 모든 노드의 최단 거리값을 기록하면 해결할 수 있음

'''

from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현


def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
