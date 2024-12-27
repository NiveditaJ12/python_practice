# Simple calculator

import time

def addition(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    try:
        return num1//num2
    except ZeroDivisionError:
        print("You are dividing by zero.")


num1 = float(input('Enter first number: '))
num2 = float(input("Enter second number: "))
while True:
    op = int(input("Choose the operation to be performed: \n 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division\n 5 to quit\n" ))
    if op == 1:
        print(f'{num1} + {num2} = {addition(num1,num2)}')
        time.sleep(3)
        continue
    elif op == 2:
        print(f'{num1} - {num2} = {subtract(num1,num2)}')
        time.sleep(3)
        continue
    elif op == 3:
        print(f'{num1} * {num2} = {multiply(num1,num2)}')
        time.sleep(3)
        continue
    elif op == 4:
        print(f'{num1} / {num2} = {divide(num1,num2)}')
        time.sleep(3)
        continue
    else:
        break