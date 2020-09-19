with open("D:\\bread.json", "r") as f:
    dict = {}
    data = f.read()
    print(data)
    for i in data:
        if i in dict:
            dict[i] += 1
            print(i, '\t', dict[i])
        else:
            dict[i] = 1
            print(i, '\t', dict[i])
    print(dict)
