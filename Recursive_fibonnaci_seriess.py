#0 1 1 2 3 5 8 13 21 34.....

# print('Fibonacci series of 7 terms')
# print("0 1 1 2 3 5 8")

# f1=0,f2=1
# f3=f1+f2
# f4=f3+f2
# f5=f4+f3
# f6=f5+f4
# f7=f6+f5

def fibonacci(n,f1=1,f0=0):
    if n==0:
        return f0
    elif n==1:
        return f1
    else:
        return fibonacci(n-1,f1+f0,f1)
n=int(input("Enter till where you want to calculate the series "))
print(f'Fibonacci series of {n} terms:')
for i in range(n):
    f=fibonacci(i)
    print(f)
