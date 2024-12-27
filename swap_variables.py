# Swap two variables of python

def swap_num(num1,num2):
    num1,num2 = num2,num1
    return num1,num2

num1,num2 = map(int,input("Enter 2 numbers: ").split(' '))

print(swap_num(num1,num2))