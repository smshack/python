n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

list1 = []
list2 = []
for i in range(0, 4):
    list1.append(i)

print(list1)

for j in range(0, 3):
    list2.append(list1)

print(list2)

for i in range(n):
    for j in range(m):
        print('(', i, ', ', j, ')', end=" ")
    print()

# 동 , 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2
print(x, y)
for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    print(nx, ny)
