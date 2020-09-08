# 자주 사용되는 내장 함수
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)

print(min_result, max_result)
# eval()
result = eval("(3+5)*7")
print(result)


# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)
