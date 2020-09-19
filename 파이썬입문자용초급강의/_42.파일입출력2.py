# with 구문은 파일 open close를 바로 할 수 있게 하는 구문

with open("D:\\bread.json", "r", encoding="UTF-8") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번재 줄: %s" % (i+1, data), end="")
