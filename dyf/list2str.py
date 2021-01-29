"""def list2str(alist):
    result = ""
    for i, v in enumerate(alist):
        if i == len(alist) - 1:
            result = result + " and " + v
        else:
            result = result == "" and v or result+','+v
    return result


result = list2str(["i", "love", "you"])

print(result)"""

t = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

x, y = len(t[0]), len(t)
for j in range(x):
    for i in range(y):
        print(t[i][j], end=" ")
    print('')

"""def printNova(alist):
    r_list = []
    for i in range(len(alist)):
        r_list.append([])
    for i, list in enumerate(alist):
        for i, v in enumerate(list):
            r_list[i].append(v)
    return r_list


resultList = printNova(testList)

for v in resultList:
    r_str = ""
    for value in v:
        r_str = r_str + value
    print(r_str)"""
