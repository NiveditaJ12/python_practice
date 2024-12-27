# Find the factorial of number.
def fact(num):
    mul = 1
    for i in range(1,num+1):
        mul *= i
    return mul

num = int(input("Enter the number: "))
print(fact(num))