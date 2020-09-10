'''
======================================================================
문제: 가장 큰수
https://programmers.co.kr/learn/courses/30/lessons/42746
=====================================================================
** 문제 설명
--------------------------------------------------------------------
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 
solution 함수를 작성해주세요.




---------------------------------------------------------------------
제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


---------------------------------------------------------------------
입출력 예
numbers	return
[6, 10, 2]	6210
[3, 30, 34, 5, 9]	9534330


======================================================================

'''


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


'''
다른풀이 1
-----------------------------------------------------------------------
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

------------------------------------------------------------------------
'''

'''
다른풀이 2
-----------------------------------------------------------------------
from io import StringIO


def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def comparator(x, y):
    x = str(x)
    y = str(y)
    x_y = int(x + y)
    y_x = int(y + x)

    if x_y < y_x:
        return -1
    elif y_x < x_y:
        return 1
    else:
        return 0


def solution(numbers):

    numbers = sorted(numbers, key=cmp_to_key(comparator), reverse=True)

    string_buffer = StringIO()
    for number in numbers:
        string_buffer.write(str(number))

    answer = int(string_buffer.getvalue())
    return str(answer)


------------------------------------------------------------------------
'''
