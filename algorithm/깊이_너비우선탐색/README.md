# 그래프 탐색 알고리즘

- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말함
- 대표 적인 그래프 탐색 알고리즘으로는 DFS 와 BFS가 있음
- 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지

## 스택 자료구조(Stack)

- 먼저 들어 온 데이터가 나중에 나가는 형식(선입 후출)의 자료구조 => FILO (First In Last Out)
- 입구와 출구가 동일한 형태로 스택을 시각화

### 재귀 함수

- 자기 자신을 다시 호출하는 함수를 의미
- 재귀 함수를 문제 풀이에서 사용할 대는 재귀함수의 종료 조건을 반드시 명시해야함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출

## 큐 자료구조(Queue)

- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조 => FIFO (First In First Out)
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화

## DFS 깊이 우선 탐색

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작과정은 다음과 같음

  1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 함
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면  
     그 노드를 스택에 넣고 방문처리를 함  
     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

- 깊이 우선 탐색의 특징
  - 자기 자신을 호출하는 순환 알고리즘의 형태를 지님
  - 이 알고리즘을 구현할 때 가장 큰 차이점은 그래프 탐색의 경우 어떤 노드를 방몬 했었는지
    여부를 반드시 검사해야 한다는 것(이를 검사하지 않을 경우 무한 루프에 빠질 위험이 있음)

## BFS 너비 우선 탐색

- 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다

  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서  
     방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 함
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복함
