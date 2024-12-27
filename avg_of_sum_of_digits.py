## Python program to display all integers within the range 100-200 whose sum of digits is an even number

def sum_of_digits(num1,num2):
    l=[]
    for i in range(num1,num2+1):
        temp = i
        sum = 0
        while temp>0:
            digit = temp%10
            sum = sum + digit
            temp = temp//10
        if sum % 2 == 0:
            l.append(i)
    return l


print(sum_of_digits(100,200))