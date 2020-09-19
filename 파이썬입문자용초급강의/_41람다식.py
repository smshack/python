# 람다식
# 함수의 형태를 더욱 짧게 쓸수 있게 해준다
# map(): 다수의 원소에 대한 함수의 결과를 한번에 얻을 수 있도록 도와줌
def add(x, y): return x+y


print(add(1, 2))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
def my_function(a, b): return a+b


result = map(my_function, list1, list2)

print(result)
print(list(result))
