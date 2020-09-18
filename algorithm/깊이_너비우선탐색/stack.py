# 스택 구현 예제

stack = []

# 삽입 (5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
print(stack)
stack.append(2)
print(stack)

stack.append(3)
print(stack)

stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.append(1)
print(stack)

stack.append(4)
print(stack)

stack.pop()
print(stack)    # 최상단 원소부터 출력
print(stack[::-1])  # 최하단 부터 출력
