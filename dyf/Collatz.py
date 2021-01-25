from sys import stdin


def collatz(x):
    if x <= 1:
        return 1
    if x % 2 == 0:
        result = x // 2
    else:
        result = 3 * x + 1
    print(result)
    return result


# value = stdin.readline()
value = int(input("Enter a number :"))


# 只对大于1的正整数会最终输出1
def recurrence(f):
    collatzResult = f(value)
    while collatzResult != 1:
        collatzResult = f(collatzResult)
        pass


recurrence(collatz)
