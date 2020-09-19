# open(): 파일을 특정한 모드로 여는 함수입니다
# 읽기모드 r  쓰기모드 w
# seek(): 읽는 시작 위치를 바이트 단위로 설정
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로 부터 한줄씩 문자열을 읽는 함수
# readlines(): 전체 내용을 한번에 리스에 담는 함수


f = open("D:\\bread.json", "r", encoding="UTF-8")
f.seek(15)
count = 0
while count < 5:
    data = f.readline()
    count = count+1
    print("%d번째줄: %s" % (count, data), end='')

obj = f.readlines()
print()
print('리스트의 원소를 출력')
for i, data in enumerate(obj):
    print("%d리스트번째 줄: %s" % (i+1, data), end='')

print()
data = f.read()
print(data)
f.close()
