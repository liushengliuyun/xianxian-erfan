def collatz(number):
    if int(number)%2==0:
        result=number/2
        return result
    else:
        return 3*number+1

ni=input('Input one integer:')
a=int(ni)
while a !=1:
    a=collatz(a)
    print(a)
print(a)
