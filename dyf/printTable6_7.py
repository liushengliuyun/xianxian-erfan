def printTable(t):
    width = [0] * len(t)
    for i, in_table in enumerate(t):

        for str in in_table:
            width[i] = max(width[i], len(str))

    x, y = len(t[0]), len(t)
    for j in range(x):
        for i in range(y):
            print((t[i][j] + " ").rjust(width[i] + 1), end="")
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
