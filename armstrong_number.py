# Check whether the number is armstrong or not

def arm_num(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp%10
        sum += digit**order
        temp = temp // 10
    return 'Armstrong' if sum==num else 'No Armstrong'

# num = int(input("Enter the number: "))
# print(arm_num(num))

# list of amstrong numbers in an interval

def arm_num_list(n1,n2):
    lst = []
    for i in range(n1,n2+1):
        order = len(str(i))
        temp = i
        sum = 0
        while temp>0:
            digit = temp%10
            sum += digit**order
            temp = temp//10
        if sum == i:
            lst.append(i)
    return lst


n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
print(arm_num_list(n1,n2))