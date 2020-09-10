'''
======================================================================
문제: 이중 우선순위 큐
https://programmers.co.kr/learn/courses/30/lessons/42628
=====================================================================
** 문제 설명
--------------------------------------------------------------------
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 
하도록 solution 함수를 구현해주세요.




---------------------------------------------------------------------
제한 사항
operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.



---------------------------------------------------------------------
입출력 예
operations	return
[I 16,D 1]	[0,0]
[I 7,I 5,I -5,D -1]	[7,5]

16을 삽입 후 최댓값을 삭제합니다. 비어있으므로 [0,0]을 반환합니다.
7,5,-5를 삽입 후 최솟값을 삭제합니다. 최대값 7, 최소값 5를 반환합니다.
======================================================================

'''
import heapq


def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]


'''
다른풀이 1
-----------------------------------------------------------------------
from heapq import heappush, heappop

def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]


------------------------------------------------------------------------
'''


'''
다른풀이 2
-----------------------------------------------------------------------
def solution(arguments):
    answer = []

    while len(arguments) is not 0:
        operation = arguments.pop(0).split(' ')
        op = operation[0]
        op_num = int(operation[1])

        if op == 'I':
            answer.append(op_num)

        if len(answer) is not 0:
            if op == 'D' and op_num is 1:
                answer.remove(max(answer))

            elif op == 'D' and op_num is -1:
                answer.remove(min(answer))

        else:
            pass

    if len(answer) is 0:
        return [0, 0
               ]
    return [max(answer), min(answer)]

------------------------------------------------------------------------
'''

'''
다른풀이 3
-----------------------------------------------------------------------

def solution(arguments):
    queue = list()
    for operation in arguments :
        if operation[0] == 'I' :
            queue.append(int(operation[1 : ]))
        elif operation[0] == 'D' :

            if len(queue) == 0 :
                continue

            if int(operation[1 : ]) == 1 :
                queue.remove(max(queue))
            elif int(operation[1 : ]) == -1 :
                queue.remove(min(queue))

    if len(queue) == 0 :
        answer = [0, 0]
    else :
        answer = [max(queue), min(queue)]

    return answer

------------------------------------------------------------------------
'''
