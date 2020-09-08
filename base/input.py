import sys

print('*****************튜플 자료형************************')
print('모든 프로그램은 적절한(약속된) 입출력 양식을 가지고 있음')
print('프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것')
print('')
print('****************************************************')
print('***********자주 사용되는 표준 입력 방법*************')
print('input() 함수는 한줄의 문자열을 입력 받는 함수')
print('Map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용')
print('공백을 기준으로 구분된 데이터를 입력 받을 때는 다음과 같이 사용')
print('list(map(int,input().split()))')
print('공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같이 사용')
print('a,b,c =map(int,input().split())')
print('')
print('----------------------------------------------')
# 입력 : 1 2 3 4 5
# input().split() : ['1','2','3','4','5']
# map(int, input().split()): map([1,2,3,4,5])
# a, b, c, d, e = map(int, input().split())
# print(a, b, c, d, e)
print('데이터의 개수 입력')
n = int(input())
print('각 데이터를 공백을 기준으로 구분하여 입력')
data = list(map(int, input().split()))
print(n)
print(data)

'''
3 * 4 형태의 리스트
0   0   0   0
0   0   0   0   
0   0   0   0
'''
print('행수 입력: ')
n = int(input())
print('열수 입력: ')
m = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

print(arr)
print('----------------------------------------------')
print('***********빠르게 입력 받기*************')
print('사용자로부터 입력을 최대한 빠르게 받아야 하는 경우')
print('파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용')
print('단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함게 사용해야함')
print('')
print('----------------------------------------------')
print('-- 문자열 입력 받기')
data = sys.stdin.readline().rstrip()
print(data)
print('***********************************************************')
