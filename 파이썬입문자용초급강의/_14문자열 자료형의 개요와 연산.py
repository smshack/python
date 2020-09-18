print('안녕 파이썬')
print('"안녕"', "파이썬!!")
print('안녕 \t', "파이썬\n !!!")

a = "안녕"
b = "파이썬"

print((a+b+"\n")*5)

a = "HELLO WORLD"

for i in range(11):
    print(i, "번째 인덱스: ", a[i])

for char in a:
    print(char)

# 슬라이싱
print(a[3])
print(a[2:9])
# 시작 인덱스는 그대로
# 끝 인덱스는 +1로 해줘야 함

print(a[2:])
print(a[:-2])

print(a[0:7:2])
