# Addition of natural numbers

def add_natural_num(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

# Using while loop
def add_natural_num1(num):
    sum = 0
    while num > 0:
        sum += num
        num-=1
    return sum

# Using Recursion
def recurse_natural_sum(num):
    if num<=1:
        return num
    else:
        return num + recurse_natural_sum(num-1)
     
num = int(input("Enter the number: "))
print(add_natural_num1(num))
print(recurse_natural_sum(num))