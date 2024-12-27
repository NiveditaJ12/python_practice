# Find the fibbonacci sequence of a number

def fibo(num):
    a,b = 0,1
    sum = 0
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            sum = a+b
            a = b
            b=sum
            print(sum)

# Using recursion

def recur_fibo(num):
    if num<=1:
        return 1
    else:
        return (recur_fibo(num-1) + recur_fibo(num-2))
num = int(input("Enter the number: "))
if num < 0:
    print('Please enter positive number.')
else:
    for i in range(num):
        print(recur_fibo(i))
recur_fibo(num)
fibo(num)